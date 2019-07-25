## 
##  Example on how to run only the generator phase
##  It can be passed as additional argument to gaudirun.py directly
##   > gaudirun.py $APPCONFIGOPTS/Gauss/MC09-b5TeV-md100.py \
##                 $APPCONFIGOPTS/Conditions/MC09-20090602-vc-md100.py \
##                 $DECFILESROOT/options/EVENTTYPE.opts \
##                 $LBPYTHIAROOT/options/Pythia.opts \
##                 $GAUSSOPTS/GenStandAlone.py \
##                 $GAUSSOPTS/Gauss-Job.py
##  or you can set the property in your Gauss-Job.py
##  Port to python of GenStandAlone.opts
## 

from Configurables import Gauss
from Gaudi.Configuration import * 
import os
Gauss().Phases = ["Generator"]

def delphesForGauss():
    from Configurables import (GaudiSequencer, SimInit, DelphesAlg,
                               ApplicationMgr, DelphesHist, DelphesTuple,
                               DelphesProto, DelphesCaloProto, BooleInit, PGPrimaryVertex)

    from Configurables import ( DelphesRecoSummary,
                                DelphesParticleId,
                                ChargedProtoCombineDLLsAlg,
                                ChargedProtoParticleAddRichInfo,
                                ChargedProtoParticleAddMuonInfo  )

    DelphesPID = DelphesParticleId ( "DelphesParticleId",
                                     RichGan   = {
        ###### New Yandex models
        'mu+': "/eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/FastFastRICH_Cramer_muon_tfScaler/",
        'mu-': "/eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/FastFastRICH_Cramer_muon_tfScaler/",
        'p+': "/eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/FastFastRICH_Cramer_proton_tfScaler/",
        'p~-': "/eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/FastFastRICH_Cramer_proton_tfScaler/",
        'K+': "/eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/FastFastRICH_Cramer_kaon_tfScaler/",
        'K-': "/eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/FastFastRICH_Cramer_kaon_tfScaler/",
        'pi+': "/eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/FastFastRICH_Cramer_pion_tfScaler/",
        'pi-': "/eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/FastFastRICH_Cramer_pion_tfScaler/",
                  },
                                     RichGanInput = 'x',
                                     RichGanOutput = 'QuantileTransformerTF_3/stack',
                                     
                                     MuonLLGan = {
        'mu+' : "/eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/diamondGan-2019-04-2401_43_08.499323/",
        'mu-' : "/eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/diamondGan-2019-04-2401_43_08.499323/",
        'pi+' : "/eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/MuGanPion-2019-04-2913_16_04.022940/",
        'pi-' : "/eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/MuGanPion-2019-04-2913_16_04.022940/",
        'K+'  : "/eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/MuGanKaon-2019-04-2913_16_43.860800/",
        'K-'  : "/eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/MuGanKaon-2019-04-2913_16_43.860800/",
        'p+'  : "/eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/MuGanProton-2019-04-3000_01_07.504122/",
        'p~-' : "/eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/MuGanProton-2019-04-3000_01_07.504122/",
        },
                                     MuonLLGanInput = 'X_gen',
                                             MuonLLGanOutput = 'output',
                                     
                                     isMuonMlp = {
        'mu+' : "/eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/MuonIsMuon2019-05-03__11_11_19.978969/",
        'mu-' : "/eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/MuonIsMuon2019-05-03__11_11_19.978969/",
        'pi+' : "/eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/PionIsMuon2019-05-03__11_12_17.633997/",
        'pi-' : "/eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/PionIsMuon2019-05-03__11_12_17.633997/",
        'K+'  : "/eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/KaonIsMuon2019-05-03__11_11_58.436823/",
        'K-'  : "/eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/KaonIsMuon2019-05-03__11_11_58.436823/",
        'p+'  : "/eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/ProtonIsMuon2019-05-03__11_09_52.500469/",
        'p~-' : "/eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/ProtonIsMuon2019-05-03__11_09_52.500469/",
        },
                                     isMuonMlpInput = 'inputds',
                                     isMuonMlpOutput = 'strided_slice',
                                     
                                     #OutputLevel = VERBOSE,
                                     )

    DelphesRecStat = DelphesRecoSummary ('DelphesRecoSummary',
          nTracksHistogramFile = "root://eosuser.cern.ch//eos/lhcb/user/l/landerli/FastSimulationModels/v20190503/KS0_nTracks_Brunel.root",
          nTracksHistogramName = "dataHist",
          #OutputLevel = VERBOSE,
        )

    #make the default card
    from LbDelphes.LbDelphesCardTemplates import DelphesCard
    c = DelphesCard.DelphesCard(name="delphes_card",
                                year='2012',
                                magPolarity='up',
                                efficiencies = True,
                                resolutions = True
                               )
    # #configure the card here for expert users
    # #c.modules['ECAL'].custom_xy_binning(...)
    c.FinalizeCard()
    #PGPrimaryVertex().OutputLevel=DEBUG
    PGPrimaryVertex().OutputVerticesName = '/Event/Rec/Vertex/Primary'
    PGPrimaryVertex().InputVerticesName = '/Event/MCFast/MCVertices'
    DelphesAlg().LHCbDelphesCardLocation = '$PWD/'+c.name+'.tcl'
    DelphesAlg().DelphesTrackLocation = 'FinalTrackMerger/tracks'
    #DelphesAlg().OutputLevel=VERBOSE
    
    DelphesCaloProto().LHCbDelphesCardLocation = DelphesAlg().LHCbDelphesCardLocation 
    DelphesProto().TrackLUT = "$LBDELPHESROOT/LookUpTables/lutTrack.dat"
    DelphesProto().TrackCovarianceLUT = "$LBDELPHESROOT/LookUpTables/lutCovarianceProf.dat"
    #DelphesProto().OutputLevel=VERBOSE
    #DelphesCaloProto().OutputLevel=DEBUG
    #DelphesTuple().OutputLevel=DEBUG
    delphesSeq = GaudiSequencer("DelphesSeq")
    delphesSeq.Members = [ SimInit("InitDelphes") ]    
    delphesSeq.Members += [ DelphesAlg("DelphesAlg")]
    delphesSeq.Members += [ DelphesHist("DelphesHist") ]
    delphesSeq.Members += [ DelphesProto("DelphesProto") ]
    #delphesSeq.Members += [ DelphesRecStat ] 
    #delphesSeq.Members += [ DelphesPID ] 
    delphesSeq.Members += [ ChargedProtoParticleAddRichInfo ('ChargedProtoParticleAddRichInfo') ] 
    delphesSeq.Members += [ ChargedProtoParticleAddMuonInfo ('ChargedProtoParticleAddMuonInfo') ] 
    delphesSeq.Members += [ ChargedProtoCombineDLLsAlg ('ChargedProtoCombineDLLsAlg') ]
    delphesSeq.Members += [ DelphesCaloProto("DelphesCaloProto") ]
    delphesSeq.Members += [ DelphesTuple("DelphesTuple") ]
    delphesSeq.Members += [ BooleInit("BooleInit", ModifyOdin = True) ]
    delphesSeq.Members += [ PGPrimaryVertex("PGPrimaryVertex")]
    delphesSeq.Members += [ GaudiSequencer("DelphesMonitor") ]

    ApplicationMgr().TopAlg += [ delphesSeq ]

appendPostConfigAction( delphesForGauss )
