#!/bin/bash
/usr/bin/cubied
python3.6 change_tcl.py
/cvmfs/lhcb.cern.ch/lib/lhcb/LBSCRIPTS/LBSCRIPTS_v9r2p4/InstallArea/scripts/LbLogin.sh -c x86_64-centos7-gcc62-opt
cd Gauss/Sim/LbDelphes/options && /home/nb_user/Gauss/build.x86_64-centos7-gcc62-opt/run gaudirun.py Gauss-Job.py
python3.6 get_std.py
