#!/bin/bash

. /cvmfs/lhcb.cern.ch/lib/lhcb/LBSCRIPTS/LBSCRIPTS_v9r2p7/InstallArea/scripts/LbLogin.sh -c x86_64-centos7-gcc7-opt
cp geometry_data.txt /home/nb_user/Gauss/Sim/LbDelphes/options/geometry_data.txt
cp LbDelphes.py /home/nb_user/Gauss/Sim/LbDelphes/options/LbDelphes.py
cp pi0mass_SimpleRes.C /home/nb_user/Gauss/Sim/LbDelphes/options/pi0mass_SimpleRes.C
for ((j=1; j<=10; j++))
do
	cd /home/nb_user/
	cp GJN_template.py GJN.py
	sed -i "/par1/c\nEvts = 10000" GJN.py
	sed -i "/par2/c\gaussGen.FirstEventNumber = $(((j-1)*10000 + 1))" GJN.py
	sed -i "/par3/c\gaussGen.RunNumber = $j" GJN.py
	cp GJN.py /home/nb_user/Gauss/Sim/LbDelphes/options/Gauss-Job-New.py
	cd /home/nb_user/Gauss/Sim/LbDelphes/options/
	lb-project-init
	../../../build.x86_64-centos7-gcc7-opt/run gaudirun.py Gauss-Job-New.py | tee log.txt
	mv GaussTuple_13142411.root $j.root
done

. /cvmfs/sft.cern.ch/lcg/releases/LCG_88/ROOT/6.08.06/x86_64-slc6-gcc62-opt/ROOT-env.sh
hadd GaussTuple_13142411.root 1.root 2.root 3.root 4.root 5.root 6.root 7.root 8.root 9.root 10.root
root -l -x -b -q 'pi0mass_SimpleRes.C("GaussTuple_13142411.root")'
cp output_E.txt /home/nb_user/output_E.txt

