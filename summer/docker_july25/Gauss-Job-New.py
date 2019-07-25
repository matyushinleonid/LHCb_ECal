#
# Options specific for a given job
# ie. setting of random number seed and name of output files
#

from Gaudi.Configuration import *
from Configurables import Gauss, ApplicationMgr, UpdateManagerSvc
from Gauss.Configuration import *    

#add general configurations
#beam config
importOptions("$APPCONFIGOPTS/Gauss/Sim08-Beam4000GeV-mu100-2012-nu2.5.py")
#importOptions("$APPCONFIGOPTS/Gauss/Sim08-Beam4000GeV-md100-2012-fix1.py")

#tags
from Configurables import LHCbApp
LHCbApp().DDDBtag   = "dddb-20170721-3"
LHCbApp().CondDBtag = "sim-20170721-2-vc-mu100"
###choose event type
#eventType = '56000400'#photon particle gun
#eventType = '30000000'#min bias
#eventType = '13102201'#Bs-> phi gamma
#eventType = '56200001'#pi0 particle gun
#eventType = '12163401'#B+-> D0 K, D0 -> K pi pi0 (CF)
#eventType = '13102201'#Bs->phi gamma, phi->kk
#eventType = '11102421'#B0 -> KK pi0, pi0-> gamma gamma
#eventType="13112001"#Bs->MuMu
eventType = '13142411' #[B_s0 -> (J/psi(1S) -> mu+ mu- ) (pi0 -> gamma gamma) ]cc

#eventType="11102013"
#use PGun sim or pythia?
importOptions('$DECFILESOPTS/%s.py'%eventType)
#get PDG
pGun=True

if True==pGun:    
    importOptions("$LBPGUNSROOT/options/PGuns.py")
    from Configurables import ToolSvc
    from Configurables import EvtGenDecay
    from Configurables import ParticleGun

    #if the dec file already has a particle gun configuration, pass it here, else, configure a flat momentum spectrum
    if hasattr(ParticleGun(),'SignalPdgCode'):
        print 'has attribute!'
        #no configuration necessary
        pass
    elif hasattr(ParticleGun(),'MomentumRange'):
        if hasattr(ParticleGun().MomentumRange,"PdgCodes"):
            print 'got PDGCodes. Should be Configured'
            pass
        else:
            print 'problem with configuration!'
            import sys
            sys.exit()
    else:
        print 'using flat momentum spectrum!'
        from Configurables import MomentumRange
        ParticleGun().addTool( MomentumRange )
        from GaudiKernel import SystemOfUnits
        ParticleGun().MomentumRange.MomentumMin = 1.0*SystemOfUnits.GeV
        from GaudiKernel import SystemOfUnits
        ParticleGun().MomentumRange.MomentumMax = 100.*SystemOfUnits.GeV
        ParticleGun().EventType = eventType
                
        ParticleGun().ParticleGunTool = "MomentumRange"
        ParticleGun().NumberOfParticlesTool = "FlatNParticles"
        #figure this out
        from Configurables import Generation
        pid_list = []
        if hasattr(Generation(),'SignalRepeatedHadronization'):
            pid_list = Generation().SignalRepeatedHadronization.SignalPIDList
        elif hasattr(Generation(),"SignalPlain"):
            pid_list = Generation().SignalPlain.SignalPIDList
        else:
            print 'major configuration problem, please fix!'
            import sys
            sys.exit()
        print 'got signal PID list',pid_list
        ParticleGun().MomentumRange.PdgCodes = pid_list
        ParticleGun().SignalPdgCode = abs(pid_list[0])
        ParticleGun().DecayTool="EvtGenDecay"
    
else:
    importOptions('$DECFILESOPTS/%s.py'%eventType)
    importOptions("$LBPYTHIA8ROOT/options/Pythia8.py")

    


importOptions("$LBDELPHESROOT/options/LbDelphes.py")
            
#--Number of events
nEvts = 1000
LHCbApp().EvtMax = nEvts

#--Generator phase, set random numbers
gaussGen = GenInit("GaussGen")
gaussGen.FirstEventNumber = 1
gaussGen.RunNumber        = 1082

#genMonitor = GaudiSequencer( "GenMonitor" )
#genMonitor.Members += [ "DumpHepMCTree/DumpSignal", "DumpHepMC/DumpAll"]
#delphesMonitor = GaudiSequencer( "DelphesMonitor" )
#delphesMonitor.Members += [ "PrintMCDecayTreeAlg/PrintMCInputDelphes",  "PrintMCDecayTreeAlg/PrintMCOutputDelphes" ]
#from Configurables import PrintMCDecayTreeAlg
#PrintMCDecayTreeAlg("PrintMCOutputDelphes").MCParticleLocation = "MCFast/MCParticles"
#PrintMCDecayTreeAlg("PrintMCOutputDelphes").MCParticleLocation = "Rec/Track/Best"
#PrintMCDecayTreeAlg("PrintMCOutputDelphes").MCParticleLocation = "Rec/ProtoP/Charged"
#PrintMCDecayTreeAlg("PrintMCOutputDelphes").MCParticleLocation = "Rec/ProtoP/Neutrals"


#--Set name of output files for given job and read in options
idFile = 'Gauss_'+str(eventType)
HistogramPersistencySvc().OutputFile = idFile+'_histos.root'
#--- Save ntuple with hadronic cross section information
ApplicationMgr().ExtSvc += [ "NTupleSvc" ]
NTupleSvc().Output = ["FILE1 DATAFILE='GaussTuple_{idFile}.root' TYP='ROOT' OPT='NEW'".format(idFile=eventType)]
       
FileCatalog().Catalogs = [ "xmlcatalog_file:Gauss_LbDelphes_0.xml" ]


#write to TES
def writeHits():    
    OutputStream("GaussTape").ItemList.append("/Event/MC/Vertices#1")
    OutputStream("GaussTape").ItemList.append("/Event/MC/Particles#1")
    OutputStream("GaussTape").ItemList.append("/Event/MCFast/MCParticles#1")
    OutputStream("GaussTape").ItemList.append("/Event/MCFast/MCVertices#1")
    OutputStream("GaussTape").ItemList.append("/Event/MCFast/MCSimpleParticles#1")
    OutputStream("GaussTape").ItemList.append("/Event/Rec/ProtoP/Charged#1")
    OutputStream("GaussTape").ItemList.append("/Event/Rec/ProtoP/Neutrals#1")
    OutputStream("GaussTape").ItemList.append("/Event/Rec/Track/Best#1")
    OutputStream("GaussTape").ItemList.append("/Event/Rec/Rich/PIDs#1")
    OutputStream("GaussTape").ItemList.append("/Event/Rec/Calo/Photons#1")
    OutputStream("GaussTape").ItemList.append("/Event/Rec/Calo/EcalClusters#1")
    OutputStream("GaussTape").ItemList.append("/Event/MC/DigiHeader#1")
    OutputStream("GaussTape").ItemList.append("/Event/DAQ/RawEvent#1")
    OutputStream("GaussTape").ItemList.append("/Event/DAQ/ODIN#1")
    OutputStream("GaussTape").ItemList.append("/Event/Rec/Vertex/Primary#1")
    print(OutputStream("GaussTape"))
appendPostConfigAction(writeHits)

