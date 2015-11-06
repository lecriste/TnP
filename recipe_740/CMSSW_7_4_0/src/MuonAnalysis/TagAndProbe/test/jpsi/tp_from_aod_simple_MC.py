import FWCore.ParameterSet.Config as cms

process = cms.Process("TagProbe")

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.source = cms.Source("PoolSource", 
                            fileNames = cms.untracked.vstring(),
                            skipEvents = cms.untracked.uint32( 0 ),
                            )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(
                                                                     50000 ) # 660Kb in 70' on 50K events, 405Kb in 15' on 10K events for the official BPH MC
                                        # 4.8Mb in 1h on 84597 (=-1) events for the MC from Muon POG 
                                        )  


process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load("Configuration.StandardSequences.Reconstruction_cff")

import os
if   "CMSSW_5_3_" in os.environ['CMSSW_VERSION']:
    process.GlobalTag.globaltag = cms.string('START53_V14::All')
    process.source.fileNames = [
        '/store/relval/CMSSW_5_3_6-START53_V14/RelValJpsiMM/GEN-SIM-RECO/v2/00000/C475A7F8-352A-E211-91A9-001A92971B68.root',
        '/store/relval/CMSSW_5_3_6-START53_V14/RelValJpsiMM/GEN-SIM-RECO/v2/00000/C2D08A6A-322A-E211-AC25-0030486792AC.root',
    ]
elif "CMSSW_5_2_" in os.environ['CMSSW_VERSION']:
    process.GlobalTag.globaltag = cms.string('START52_V5::All')
    process.source.fileNames = [
        '/store/relval/CMSSW_5_2_3/RelValJpsiMM/GEN-SIM-RECO/START52_V5-v1/0043/E8286D9A-077A-E111-813F-0018F3D095EA.root',
        '/store/relval/CMSSW_5_2_3/RelValJpsiMM/GEN-SIM-RECO/START52_V5-v1/0043/C033D80B-077A-E111-8951-003048678B08.root',
        '/store/relval/CMSSW_5_2_3/RelValJpsiMM/GEN-SIM-RECO/START52_V5-v1/0043/B837A248-2C7A-E111-BA34-003048678FB8.root',
        '/store/relval/CMSSW_5_2_3/RelValJpsiMM/GEN-SIM-RECO/START52_V5-v1/0043/304746CC-097A-E111-A71F-003048FFD76E.root',
    ]
elif "CMSSW_7_4_" in os.environ['CMSSW_VERSION']:
    process.GlobalTag.globaltag = cms.string('MCRUN2_74_V9')
    process.source.fileNames = [
        # MC from Muon POG
        #'/store/mc/RunIISpring15DR74/JpsiToMuMu_JPsiPt7_13TeV-pythia8/AODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/183C894F-C008-E511-AFB5-0025905A606A.root',
        #'/store/mc/RunIISpring15DR74/JpsiToMuMu_JPsiPt7_13TeV-pythia8/AODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/3615E328-D708-E511-B2F9-003048FFD752.root',
        #'/store/mc/RunIISpring15DR74/JpsiToMuMu_JPsiPt7_13TeV-pythia8/AODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/561562A2-D708-E511-B06E-0025905B8576.root',
        #'/store/mc/RunIISpring15DR74/JpsiToMuMu_JPsiPt7_13TeV-pythia8/AODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/6E145BC4-D708-E511-99CF-002481E94BCA.root',
        #'/store/mc/RunIISpring15DR74/JpsiToMuMu_JPsiPt7_13TeV-pythia8/AODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/7E81F237-C808-E511-90F4-00261894383E.root',
        #'/store/mc/RunIISpring15DR74/JpsiToMuMu_JPsiPt7_13TeV-pythia8/AODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/888136A8-D708-E511-823C-002590A2CD68.root',
        #'/store/mc/RunIISpring15DR74/JpsiToMuMu_JPsiPt7_13TeV-pythia8/AODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/08135FA6-6E0C-E511-9A97-002618943948.root',
        #'/store/mc/RunIISpring15DR74/JpsiToMuMu_JPsiPt7_13TeV-pythia8/AODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/283882C6-860C-E511-AB1C-0026189438C9.root',
        #'/store/mc/RunIISpring15DR74/JpsiToMuMu_JPsiPt7_13TeV-pythia8/AODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/76BD42C8-FE08-E511-BAB9-0025905A60DE.root',
        #'/store/mc/RunIISpring15DR74/JpsiToMuMu_JPsiPt7_13TeV-pythia8/AODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/9AA472CE-FE08-E511-BEE3-0025905B8582.root',
        #'/store/mc/RunIISpring15DR74/JpsiToMuMu_JPsiPt7_13TeV-pythia8/AODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/C81001CF-860C-E511-A5B7-0025905A6088.root',
        #'/store/mc/RunIISpring15DR74/JpsiToMuMu_JPsiPt7_13TeV-pythia8/AODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/F87F150E-710C-E511-9F33-0025905A60BC.root'
        #
        # BPH MC
        '/store/mc/RunIISpring15DR74/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/AODSIM/Asympt50ns_MCRUN2_74_V9A-v2/80000/EE4E7950-D726-E511-8751-001E67A404B0.root',
        '/store/mc/RunIISpring15DR74/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/AODSIM/Asympt50ns_MCRUN2_74_V9A-v2/20000/0072AAD1-7028-E511-8448-0025905A612E.root',
        '/store/mc/RunIISpring15DR74/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/AODSIM/Asympt50ns_MCRUN2_74_V9A-v2/20000/00C6C123-0428-E511-92F2-D4AE526A091F.root',
        '/store/mc/RunIISpring15DR74/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/AODSIM/Asympt50ns_MCRUN2_74_V9A-v2/20000/026710B4-5F27-E511-B9D3-B8CA3A70A520.root',
        '/store/mc/RunIISpring15DR74/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/AODSIM/Asympt50ns_MCRUN2_74_V9A-v2/20000/02D22B1C-D626-E511-8850-002590D60026.root',
        '/store/mc/RunIISpring15DR74/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/AODSIM/Asympt50ns_MCRUN2_74_V9A-v2/20000/04C3F72A-D126-E511-B12F-00238BBD7594.root',
        '/store/mc/RunIISpring15DR74/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/AODSIM/Asympt50ns_MCRUN2_74_V9A-v2/20000/08FCBA7F-D126-E511-99C8-0025905964A6.root',
        '/store/mc/RunIISpring15DR74/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/AODSIM/Asympt50ns_MCRUN2_74_V9A-v2/20000/0A4AB9B0-3827-E511-8277-0025905B857C.root',
        '/store/mc/RunIISpring15DR74/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/AODSIM/Asympt50ns_MCRUN2_74_V9A-v2/20000/0C175E3E-E627-E511-ADEB-6C3BE5B58000.root',
    ]
else: raise RuntimeError, "Unknown CMSSW version %s" % os.environ['CMSSW_VERSION']



## ==== Fast Filters ====
process.goodVertexFilter = cms.EDFilter("VertexSelector",
    src = cms.InputTag("offlinePrimaryVertices"),
    cut = cms.string("!isFake && ndof > 4 && abs(z) <= 25 && position.Rho <= 2"),
    filter = cms.bool(True),
)
process.noScraping = cms.EDFilter("FilterOutScraping",
    applyfilter = cms.untracked.bool(True),
    debugOn = cms.untracked.bool(False), ## Or 'True' to get some per-event info
    numtrack = cms.untracked.uint32(10),
    thresh = cms.untracked.double(0.25)
)
process.fastFilter = cms.Sequence(process.goodVertexFilter + process.noScraping)

process.load("HLTrigger.HLTfilters.triggerResultsFilter_cfi")
process.triggerResultsFilter.triggerConditions = cms.vstring( 'HLT_Mu*_L2Mu*' )
process.triggerResultsFilter.l1tResults = ''
process.triggerResultsFilter.throw = True
#process.triggerResultsFilter.hltResults = cms.InputTag( "TriggerResults", "", "REDIGI38XPU" )
process.triggerResultsFilter.hltResults = cms.InputTag( "TriggerResults", "", "HLT" )
process.HLTMu   = process.triggerResultsFilter.clone(triggerConditions = ['HLT_Mu*_L2Mu*'])
process.HLTBoth = process.triggerResultsFilter.clone(triggerConditions = ['HLT_Mu*_L2Mu*', 'HLT_Mu*_Track*_Jpsi*'])
#process.HLTMu   = process.triggerResultsFilter.clone(triggerConditions = ['HLT_Mu*_L2Mu*', 'HLT_Mu*']) # for Mu8 test
#process.HLTBoth = process.triggerResultsFilter.clone(triggerConditions = ['HLT_Mu*_L2Mu*', 'HLT_Mu*_Track*_Jpsi*', 'HLT_Mu*']) # for Mu8 test
process.HLTBoth_withDimuon = process.triggerResultsFilter.clone(triggerConditions = [ 'HLT_Mu*_L2Mu*', 'HLT_Mu*_Track*_Jpsi*', 'HLT_Mu*', 'HLT_Dimuon*' ])

##    __  __                       
##   |  \/  |_   _  ___  _ __  ___ 
##   | |\/| | | | |/ _ \| '_ \/ __|
##   | |  | | |_| | (_) | | | \__ \
##   |_|  |_|\__,_|\___/|_| |_|___/
##                                 
## ==== Merge CaloMuons and Tracks into the collection of reco::Muons  ====
from RecoMuon.MuonIdentification.calomuons_cfi import calomuons;
process.mergedMuons = cms.EDProducer("CaloMuonMerger",
    mergeTracks = cms.bool(True),
    mergeCaloMuons = cms.bool(False), # AOD
    muons     = cms.InputTag("muons"), 
    caloMuons = cms.InputTag("calomuons"),
    tracks    = cms.InputTag("generalTracks"),
    minCaloCompatibility = calomuons.minCaloCompatibility,
    ## Apply some minimal pt cut
    muonsCut     = cms.string("track.isNonnull && pt > 2"),
    caloMuonsCut = cms.string("pt > 2"),
    tracksCut    = cms.string("pt > 2"),
)

## ==== Trigger matching
process.load("MuonAnalysis.MuonAssociators.patMuonsWithTrigger_cff")
## with some customization
#process.muonMatchHLTL2.maxDeltaR = 0.3 # Zoltan tuning - it was 0.5 # present in Zmumu
#process.muonMatchHLTL3.maxDeltaR = 0.1 # present in Zmumu
from MuonAnalysis.MuonAssociators.patMuonsWithTrigger_cff import *
changeRecoMuonInput(process, "mergedMuons")
#useExtendedL1Match(process)
#addHLTL1Passthrough(process)
#changeTriggerProcessName(process, "*")

from MuonAnalysis.TagAndProbe.common_variables_cff import *
process.load("MuonAnalysis.TagAndProbe.common_modules_cff")

process.tagMuons = cms.EDFilter("PATMuonSelector",
    src = cms.InputTag("patMuonsWithTrigger"),
    cut = cms.string("(isGlobalMuon || numberOfMatchedStations > 1) && pt > 7.5 && !triggerObjectMatchesByCollection('hltL3MuonCandidates').empty()"),
)

process.oneTag  = cms.EDFilter("CandViewCountFilter", src = cms.InputTag("tagMuons"), minNumber = cms.uint32(1))

process.probeMuons = cms.EDFilter("PATMuonSelector",
    src = cms.InputTag("patMuonsWithTrigger"),
    #cut = cms.string("track.isNonnull && (!triggerObjectMatchesByCollection('hltMuTrackJpsiEffCtfTrackCands').empty() || !triggerObjectMatchesByCollection('hltMuTrackJpsiCtfTrackCands').empty() || !triggerObjectMatchesByCollection('hltL2MuonCandidates').empty())"), # Run-I
    cut = cms.string("track.isNonnull && !triggerObjectMatchesByCollection('hltTracksIter').empty()"),
    #cut = cms.string("track.isNonnull") # for Mu8 test
)

process.tpPairs = cms.EDProducer("CandViewShallowCloneCombiner",
    cut = cms.string('2.8 < mass < 3.4 && abs(daughter(0).vz - daughter(1).vz) < 1'),
    decay = cms.string('tagMuons@+ probeMuons@-')
)
process.onePair = cms.EDFilter("CandViewCountFilter", src = cms.InputTag("tpPairs"), minNumber = cms.uint32(1))

process.tagMuonsMCMatch = cms.EDProducer("MCMatcher", # cut on deltaR, deltaPt/Pt; pick best by deltaR
    src     = cms.InputTag("tagMuons"), # RECO objects to match
    matched = cms.InputTag("goodGenMuonsFromJpsi"),   # mc-truth particle collection
    mcPdgId     = cms.vint32(13),  # one or more PDG ID (13 = muon); absolute values (see below)
    checkCharge = cms.bool(False), # True = require RECO and MC objects to have the same charge
    mcStatus = cms.vint32(1),      # PYTHIA status code (1 = stable, 2 = shower, 3 = hard scattering)
    maxDeltaR = cms.double(0.3),   # Minimum deltaR for the match
    maxDPtRel = cms.double(0.5),   # Minimum deltaPt/Pt for the match
    resolveAmbiguities = cms.bool(True),    # Forbid two RECO objects to match to the same GEN object
    resolveByMatchQuality = cms.bool(True), # False = just match input in order; True = pick lowest deltaR pair first
)
process.probeMuonsMCMatch = process.tagMuonsMCMatch.clone(src = "probeMuons", maxDeltaR = 0.3, maxDPtRel = 1.0, resolveAmbiguities = False,  resolveByMatchQuality = False)

from MuonAnalysis.TagAndProbe.muon.tag_probe_muon_extraIso_cff import ExtraIsolationVariables

#process.load("MuonAnalysis.TagAndProbe.mvaIsoVariables_cff")
#from MuonAnalysis.TagAndProbe.mvaIsoVariables_cff import MVAIsoVariablesPlain, MVAIsoVariablesPlainTag
#process.load("MuonAnalysis.TagAndProbe.radialIso_cfi")

process.tpTree = cms.EDAnalyzer("TagProbeFitTreeProducer",
    # choice of tag and probe pairs, and arbitration
    tagProbePairs = cms.InputTag("tpPairs"),
    arbitration   = cms.string("None"),
    # probe variables: all useful ones
    variables = cms.PSet(
        AllVariables,
        ExtraIsolationVariables,
        dxyBS = cms.InputTag("muonDxyPVdzmin","dxyBS"),
        dxyPVdzmin = cms.InputTag("muonDxyPVdzmin","dxyPVdzmin"),
        dzPV = cms.InputTag("muonDxyPVdzmin","dzPV"),
        nSplitTk  = cms.InputTag("splitTrackTagger"),
    ),
    flags = cms.PSet(
       TrackQualityFlags,
       MuonIDFlags,
       HighPtTriggerFlags,
       HighPtTriggerFlagsDebug,
       LowPtTriggerFlagsPhysics,
       LowPtTriggerFlagsEfficienciesProbe,
       Acc_JPsi = cms.string("(abs(eta) <= 1.3 && pt > 3.3) || (1.3 < abs(eta) <= 2.2 && p > 2.9) || (2.2 < abs(eta) <= 2.4  && pt > 0.8)"),
    ),
    tagVariables = cms.PSet(
        pt  = cms.string('pt'),
        eta = cms.string('eta'),
        phi = cms.string('phi'),
        nVertices = cms.InputTag("nverticesModule"),
        l1rate = cms.InputTag("l1rate"),
        bx     = cms.InputTag("l1rate","bx"),
    ),
    tagFlags = cms.PSet(
        HighPtTriggerFlags,
        HighPtTriggerFlagsDebug,
        LowPtTriggerFlagsPhysics,
        LowPtTriggerFlagsEfficienciesTag,
    ),
    pairVariables = cms.PSet(
        pt = cms.string("pt"),
        dphiVtxTimesQ = cms.InputTag("tagProbeSeparation", "dphiVtxTimesQ"),
        drM1          = cms.InputTag("tagProbeSeparation", "drM1"),
        dphiM1        = cms.InputTag("tagProbeSeparation", "dphiM1"),
        distM1        = cms.InputTag("tagProbeSeparation", "distM1"),
        drM2          = cms.InputTag("tagProbeSeparation", "drM2"),
        dphiM2        = cms.InputTag("tagProbeSeparation", "dphiM2"),
        distM2        = cms.InputTag("tagProbeSeparation", "distM2"),
        drVtx         = cms.InputTag("tagProbeSeparation", "drVtx"),
        dz            = cms.string("daughter(0).vz - daughter(1).vz"),
        probeMultiplicity = cms.InputTag("probeMultiplicity"),
    ),
    pairFlags = cms.PSet(),
    isMC           = cms.bool(True),
    addRunLumiInfo = cms.bool(True),
    tagMatches       = cms.InputTag("tagMuonsMCMatch"),
    probeMatches     = cms.InputTag("probeMuonsMCMatch"),
    motherPdgId      = cms.vint32(443),
    makeMCUnbiasTree       = cms.bool(False),
    checkMotherInUnbiasEff = cms.bool(True),
    allProbes              = cms.InputTag("probeMuons"),
)


process.load("MuonAnalysis.TagAndProbe.muon.tag_probe_muon_extraIso_cfi")

#process.load("TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAny_cfi")
#process.load("TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi")
#process.load("TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorOpposite_cfi")
#process.load("RecoMuon.DetLayers.muonDetLayerGeometry_cfi")

process.tnpSimpleSequence = cms.Sequence(
    process.goodGenMuonsFromJpsi +
    process.tagMuons   * process.tagMuonsMCMatch   +
    process.oneTag     +
    process.probeMuons * process.probeMuonsMCMatch +
    process.tpPairs    +
    process.onePair    +
    process.muonDxyPVdzmin +
    process.nverticesModule +
    process.tagProbeSeparation +
    process.computeCorrectedIso + 
    process.probeMultiplicity + 
    process.splitTrackTagger +
    process.l1rate +
    process.tpTree
)

process.tagAndProbe = cms.Path( 
    process.fastFilter +
    process.HLTBoth    +
    process.mergedMuons                 *
    process.patMuonsWithTriggerSequence *
    process.tnpSimpleSequence
)

# OnePair tree for vertexing filter efficiency
process.tpTreeOnePair = process.tpTree.clone(
   arbitration   = "OnePair",
   # a few L1,L2,L3 variables in Ilse's file
   pairVariables = cms.PSet(
        process.tpTree.pairVariables,
        rapidity      = cms.string("rapidity"),
        absrapidity   = cms.string("abs(rapidity)"),
        prescaled     = cms.InputTag("tagProbeSeparation", "prescaled"),
        VtxProb       = cms.InputTag("tagProbeSeparation", "VtxProb"),
        VtxCosPA      = cms.InputTag("tagProbeSeparation", "VtxCosPA"),
        VtxLxySig     = cms.InputTag("tagProbeSeparation", "VtxLxySig"),
        VtxLxy        = cms.InputTag("tagProbeSeparation", "VtxLxy"),
        VtxL3d        = cms.InputTag("tagProbeSeparation", "VtxL3d"),
        DCA           = cms.InputTag("tagProbeSeparation", "DCA"),
        ),
)

process.tnpSimpleSequenceOnePair = cms.Sequence(
    process.goodGenMuonsFromJpsi +
    process.tagMuons * process.tagMuonsMCMatch +
    process.probeMuons * process.probeMuonsMCMatch +
    process.tpPairs    +
    process.muonDxyPVdzmin +
    process.nverticesModule    +
    process.tagProbeSeparation +
    process.computeCorrectedIso +
    process.splitTrackTagger + 
    process.l1rate +
    process.tpTreeOnePair
)

process.tagAndProbeOnePair = cms.Path( 
    process.fastFilter +
    process.HLTBoth_withDimuon    +
    process.mergedMuons                 *
    process.patMuonsWithTriggerSequence *
    process.tnpSimpleSequenceOnePair
)


##    _____               _    _             
##   |_   _| __ __ _  ___| | _(_)_ __   __ _ 
##     | || '__/ _` |/ __| |/ / | '_ \ / _` |
##     | || | | (_| | (__|   <| | | | | (_| |
##     |_||_|  \__,_|\___|_|\_\_|_| |_|\__, |
##                                     |___/ 

## Then make another collection for standalone muons, using standalone track to define the 4-momentum
process.muonsSta = cms.EDProducer("RedefineMuonP4FromTrack",
    src   = cms.InputTag("muons"),
    track = cms.string("outer"),
)
## Match to trigger, to measure the efficiency of HLT tracking
from PhysicsTools.PatAlgos.tools.helpers import *
process.patMuonsWithTriggerSequenceSta = cloneProcessingSnippet(process, process.patMuonsWithTriggerSequence, "Sta")
process.muonMatchHLTL2Sta.maxDeltaR = 0.5
process.muonMatchHLTL3Sta.maxDeltaR = 0.5
massSearchReplaceAnyInputTag(process.patMuonsWithTriggerSequenceSta, "mergedMuons", "muonsSta")

## Define probes and T&P pairs
process.probeMuonsSta = cms.EDFilter("PATMuonSelector",
    src = cms.InputTag("patMuonsWithTriggerSta"),
    cut = cms.string("outerTrack.isNonnull && !triggerObjectMatchesByCollection('hltL2MuonCandidates').empty()"),
)
process.probeMuonsMCMatchSta = process.tagMuonsMCMatch.clone(src = "probeMuonsSta")
process.tpPairsSta = process.tpPairs.clone(decay = "tagMuons@+ probeMuonsSta@-", cut = "2 < mass < 5")

process.onePairSta = cms.EDFilter("CandViewCountFilter", src = cms.InputTag("tpPairsSta"), minNumber = cms.uint32(1))

process.staToTkMatch.maxDeltaR     = 0.3
process.staToTkMatch.maxDeltaPtRel = 2.
process.staToTkMatchNoJPsi.maxDeltaR     = 0.3
process.staToTkMatchNoJPsi.maxDeltaPtRel = 2.

#process.load("MuonAnalysis.TagAndProbe.tracking_reco_info_cff")

process.tpTreeSta = process.tpTree.clone(
    tagProbePairs = "tpPairsSta",
    #arbitration   = "OneProbe", # present in Zmumu
    variables = cms.PSet(
        KinematicVariables, 
        #StaOnlyVariables, # present in Zmumu
        ## track matching variables
        tk_deltaR     = cms.InputTag("staToTkMatch","deltaR"),
        tk_deltaEta   = cms.InputTag("staToTkMatch","deltaEta"),
        tk_deltaR_NoJPsi     = cms.InputTag("staToTkMatchNoJPsi","deltaR"),
        tk_deltaEta_NoJPsi   = cms.InputTag("staToTkMatchNoJPsi","deltaEta"),
        tk_deltaR_NoBestJPsi     = cms.InputTag("staToTkMatchNoBestJPsi","deltaR"),
        tk_deltaEta_NoBestJPsi   = cms.InputTag("staToTkMatchNoBestJPsi","deltaEta"),
    ),
    flags = cms.PSet(
        #Mu5_L2Mu3_Jpsi_L2 = LowPtTriggerFlagsEfficienciesProbe.Mu5_L2Mu3_Jpsi_L2,
        LowPtTriggerFlagsEfficienciesProbe,
        outerValidHits = cms.string("outerTrack.numberOfValidHits > 0"),
        TM  = cms.string("isTrackerMuon"),
        Glb = cms.string("isGlobalMuon"),
        Tk  = cms.string("track.isNonnull"),
        #StaTkSameCharge = cms.string("outerTrack.isNonnull && innerTrack.isNonnull && (outerTrack.charge == innerTrack.charge)"), # present in Zmumu
    ),
    tagVariables = cms.PSet(
        pt = cms.string("pt"),
        eta = cms.string("eta"),
        phi = cms.string("phi"),
        nVertices = cms.InputTag("nverticesModule"),
        #combRelIso = cms.string("(isolationR03.emEt + isolationR03.hadEt + isolationR03.sumPt)/pt"),
        #chargedHadIso04 = cms.string("pfIsolationR04().sumChargedHadronPt"),
        #neutralHadIso04 = cms.string("pfIsolationR04().sumNeutralHadronEt"),
        #photonIso04 = cms.string("pfIsolationR04().sumPhotonEt"),
        #combRelIsoPF04dBeta = IsolationVariables.combRelIsoPF04dBeta,
    ),
    tagFlags = cms.PSet(
        #Mu5_L2Mu3_Jpsi_MU = LowPtTriggerFlagsEfficienciesTag.Mu5_L2Mu3_Jpsi_MU,
        LowPtTriggerFlagsEfficienciesTag,
        ),
    pairVariables = cms.PSet(
        pt = cms.string("pt"),
        #
        dphiVtxTimesQ = cms.InputTag("tagProbeStaSeparation", "dphiVtxTimesQ"),
        drM1          = cms.InputTag("tagProbeStaSeparation", "drM1"),
        dphiM1        = cms.InputTag("tagProbeStaSeparation", "dphiM1"),
        distM1        = cms.InputTag("tagProbeStaSeparation", "distM1"),
        drM2          = cms.InputTag("tagProbeStaSeparation", "drM2"),
        dphiM2        = cms.InputTag("tagProbeStaSeparation", "dphiM2"),
        distM2        = cms.InputTag("tagProbeStaSeparation", "distM2"),
        drVtx         = cms.InputTag("tagProbeStaSeparation", "drVtx"),
        dz            = cms.string("daughter(0).vz - daughter(1).vz"),
        probeMultiplicity = cms.InputTag("probeStaMultiplicity"),
        #
        rapidity = cms.string("rapidity"),
        deltaR   = cms.string("deltaR(daughter(0).eta, daughter(0).phi, daughter(1).eta, daughter(1).phi)"), 
        ),
    pairFlags     = cms.PSet(),
    allProbes     = "probeMuonsSta",
    probeMatches  = "probeMuonsMCMatchSta",
)

process.tnpSimpleSequenceSta = cms.Sequence(
    process.tagMuons   * process.tagMuonsMCMatch   +
    process.oneTag     +
    process.probeMuonsSta * process.probeMuonsMCMatchSta +
    process.tpPairsSta      +
    process.onePairSta      +
    process.nverticesModule +
    process.tagProbeStaSeparation +
    process.probeStaMultiplicity + 
    process.staToTkMatchSequenceJPsi +
    process.l1rate +
    process.tpTreeSta
)

process.RandomNumberGeneratorService.tkTracksNoJPsi      = cms.PSet( initialSeed = cms.untracked.uint32(81) )
process.RandomNumberGeneratorService.tkTracksNoBestJPsi  = cms.PSet( initialSeed = cms.untracked.uint32(81) )

if True: # turn on for tracking efficiency from RECO/AOD + earlyGeneralTracks 
    process.tracksNoMuonSeeded = cms.EDFilter("TrackSelector",
                                              src = cms.InputTag("generalTracks"),
                                              #cut = cms.string(" || ".join("isAlgoInMask('%s')" % a for a in [
                    #'initialStep', 'lowPtTripletStep', 'pixelPairStep', 'detachedTripletStep',
                    #'mixedTripletStep', 'pixelLessStep', 'tobTecStep', 'jetCoreRegionalStep'] ) ) # not working
                                              cut = cms.string("")
                                              )
    process.pCutTracks0 = process.pCutTracks.clone(src = 'tracksNoMuonSeeded')
    #process.pCutTracks0 = process.pCutTracks.clone(src = 'earlyGeneralTracks') # not working
    #process.pCutTracks0 = process.pCutTracks.clone() # an alternative to 'tracksNoMuonSeeded'
    process.tkTracks0 = process.tkTracks.clone(src = 'pCutTracks0')
    process.tkTracksNoJPsi0 = process.tkTracksNoJPsi.clone(src = 'tkTracks0')
    process.tkTracksNoBestJPsi0 = process.tkTracksNoBestJPsi.clone(src = 'tkTracks0')
    process.RandomNumberGeneratorService.tkTracksNoJPsi0      = cms.PSet( initialSeed = cms.untracked.uint32(81) )
    process.RandomNumberGeneratorService.tkTracksNoBestJPsi0  = cms.PSet( initialSeed = cms.untracked.uint32(81) )
    process.preTkMatchSequenceJPsi.replace( 
            process.tkTracksNoJPsi, process.tkTracksNoJPsi +
            process.tracksNoMuonSeeded + process.pCutTracks0 + process.tkTracks0 + process.tkTracksNoJPsi0 + process.tkTracksNoBestJPsi0
            #process.pCutTracks0 + process.tkTracks0 + process.tkTracksNoJPsi0 + process.tkTracksNoBestJPsi0
    )
    process.staToTkMatch0 = process.staToTkMatch.clone(matched = 'tkTracks0')
    process.staToTkMatchNoJPsi0 = process.staToTkMatchNoJPsi.clone(matched = 'tkTracksNoJPsi0')
    process.staToTkMatchNoBestJPsi0 = process.staToTkMatchNoBestJPsi.clone(matched = 'tkTracksNoJPsi0')
    process.staToTkMatchSequenceJPsi.replace( process.staToTkMatch, process.staToTkMatch + process.staToTkMatch0 )
    process.staToTkMatchSequenceJPsi.replace( process.staToTkMatchNoJPsi, process.staToTkMatchNoJPsi + process.staToTkMatchNoJPsi0 )
    process.staToTkMatchSequenceJPsi.replace( process.staToTkMatchNoBestJPsi, process.staToTkMatchNoBestJPsi + process.staToTkMatchNoBestJPsi0 )
    process.tpTreeSta.variables.tk0_deltaR     = cms.InputTag("staToTkMatch0","deltaR")
    process.tpTreeSta.variables.tk0_deltaEta   = cms.InputTag("staToTkMatch0","deltaEta")
    process.tpTreeSta.variables.tk0_deltaR_NoJPsi   = cms.InputTag("staToTkMatchNoJPsi0","deltaR")
    process.tpTreeSta.variables.tk0_deltaEta_NoJPsi = cms.InputTag("staToTkMatchNoJPsi0","deltaEta")
    process.tpTreeSta.variables.tk0_deltaR_NoBestJPsi   = cms.InputTag("staToTkMatchNoBestJPsi0","deltaR")
    process.tpTreeSta.variables.tk0_deltaEta_NoBestJPsi = cms.InputTag("staToTkMatchNoBestJPsi0","deltaEta")

process.tagAndProbeSta = cms.Path( 
    process.fastFilter +
    process.HLTMu      +
    process.muonsSta                       +
    process.patMuonsWithTriggerSequenceSta +
    process.tnpSimpleSequenceSta
)


if True: # turn on for tracking efficiency using gen particles as probe
    process.probeGen = cms.EDFilter("GenParticleSelector",
                                    src = cms.InputTag("genParticles"),
                                    cut = cms.string("abs(pdgId) == 13 && pt > 2 && abs(eta) < 2.4 && numberOfMothers == 1 && motherRef.pdgId == 443"),
                                    )
    process.tpPairsTkGen = process.tpPairs.clone(decay = "tagMuons@+ probeGen@-", cut = '2 < mass < 5')
    process.genToTkMatch    = process.staToTkMatch.clone(src = "probeGen", srcTrack="none")
    process.genToTkMatchNoJPsi = process.staToTkMatchNoJPsi.clone(src = "probeGen", srcTrack="none")
    process.genToTkMatchNoBestJPsi = process.staToTkMatchNoBestJPsi.clone(src = "probeGen", srcTrack="none")
    process.genToTkMatch0    = process.staToTkMatch0.clone(src = "probeGen", srcTrack="none")
    process.genToTkMatchNoJPsi0 = process.staToTkMatchNoJPsi0.clone(src = "probeGen", srcTrack="none")
    process.genToTkMatchNoBestJPsi0 = process.staToTkMatchNoBestJPsi0.clone(src = "probeGen", srcTrack="none")
    process.probeMuonsMCMatchGen = process.tagMuonsMCMatch.clone(src = "probeGen")
    #
    #BMuQual = cms.string("muonID('TMOneStationTight') &&" + "(track.hitPattern.trackerLayersWithMeasurement > 5 && track.hitPattern.pixelLayersWithMeasurement > 1  && " + "track.chi2 / track.ndof < 1.8 && abs(dB) < 3.0 && abs(track.dz) < 30.0)"),
    #process.genTosoftIDMatch = process.softIDToGenMatch.clone(objCut = "muonID('TMOneStationTight') &&" + "(track.hitPattern.trackerLayersWithMeasurement > 5 && track.hitPattern.pixelLayersWithMeasurement > 0  && " + "&& abs(dB) < 0.3 && abs(track.dz) < 20.0)")
    process.genTosoftIDMatch = process.softIDToGenMatch.clone(objCut = "(track.hitPattern.trackerLayersWithMeasurement > 5 && track.hitPattern.pixelLayersWithMeasurement > 0  && " + "&& abs(dB) < 0.3 && abs(track.dz) < 20.0)")
    #
    process.tpTreeGen = process.tpTreeSta.clone(
        tagProbePairs = "tpPairsTkGen",
        arbitration   = "OneProbe",
        variables = cms.PSet(
            KinematicVariables, 
            ## track matching variables
            tk_deltaR     = cms.InputTag("genToTkMatch","deltaR"),
            tk_deltaEta   = cms.InputTag("genToTkMatch","deltaEta"),
            tk_deltaR_NoJPsi   = cms.InputTag("genToTkMatchNoJPsi","deltaR"),
            tk_deltaEta_NoJPsi = cms.InputTag("genToTkMatchNoJPsi","deltaEta"),
            tk_deltaR_NoBestJPsi  = cms.InputTag("genToTkMatchNoBestJPsi","deltaR"),
            tk_deltaEta_NoBestJPsi = cms.InputTag("genToTkMatchNoBestJPsi","deltaEta"),
            ## track matching variables (early general tracks)
            tk0_deltaR     = cms.InputTag("genToTkMatch0","deltaR"),
            tk0_deltaEta   = cms.InputTag("genToTkMatch0","deltaEta"),
            tk0_deltaR_NoJPsi   = cms.InputTag("genToTkMatchNoJPsi0","deltaR"),
            tk0_deltaEta_NoJPsi = cms.InputTag("genToTkMatchNoJPsi0","deltaEta"),
            tk0_deltaR_NoBestJPsi   = cms.InputTag("genToTkMatchNoBestJPsi0","deltaR"),
            tk0_deltaEta_NoBestJPsi = cms.InputTag("genToTkMatchNoBestJPsi0","deltaEta"),
            ## softID matching variables
            tk_deltaR     = cms.InputTag("genTosoftIDMatch","deltaR"),
            tk_deltaEta   = cms.InputTag("genTosoftIDMatch","deltaEta"),
            ),
        flags = cms.PSet(
            ),
        tagVariables = cms.PSet(
            pt = cms.string("pt"),
            eta = cms.string("eta"),
            phi = cms.string("phi"),
            nVertices   = cms.InputTag("nverticesModule"),
            ),
        pairVariables = cms.PSet(
            #nJets30 = cms.InputTag("njets30ModuleSta"),
            dz      = cms.string("daughter(0).vz - daughter(1).vz"),
            pt      = cms.string("pt"), 
            rapidity = cms.string("rapidity"),
            deltaR   = cms.string("deltaR(daughter(0).eta, daughter(0).phi, daughter(1).eta, daughter(1).phi)"), 
            ),
        pairFlags = cms.PSet(),
        allProbes     = cms.InputTag("probeGen"),
        probeMatches  = cms.InputTag("probeMuonsMCMatchGen"),
        )

    process.tagAndProbeTkGen = cms.Path( 
        process.goodGenMuonsFromJpsi + # added by me
        process.fastFilter +
        process.mergedMuons + process.patMuonsWithTriggerSequence + process.tagMuons * process.tagMuonsMCMatch + # added by me
        process.probeGen +
        process.tpPairsTkGen + 
        process.nverticesModule +
        process.preTkMatchSequenceJPsi + 
        process.genToTkMatch + process.genToTkMatchNoJPsi + process.genToTkMatchNoBestJPsi + 
        process.genToTkMatch0 + process.genToTkMatchNoJPsi0 + process.genToTkMatchNoBestJPsi0 +
        process.probeMuonsMCMatchGen +
        process.tpTreeGen
        )


if True: # turn on for tracking efficiency using L1 seeds
    process.probeL1 = cms.EDFilter("CandViewSelector",
        src = cms.InputTag("l1extraParticles"),
        cut = cms.string("pt >= 2 && abs(eta) < 2.4"),
    )
    process.tpPairsTkL1 = process.tpPairs.clone(decay = "tagMuons@+ probeL1@-", cut = 'mass > 2')
    process.l1ToTkMatch    = process.staToTkMatch.clone(src = "probeL1", srcTrack="none")
    process.l1ToTkMatchNoJPsi = process.staToTkMatchNoJPsi.clone(src = "probeL1", srcTrack="none")
    process.l1ToTkMatchNoBestJPsi = process.staToTkMatchNoBestJPsi.clone(src = "probeL1", srcTrack="none")
    process.l1ToTkMatch0    = process.staToTkMatch0.clone(src = "probeL1", srcTrack="none")
    process.l1ToTkMatchNoJPsi0 = process.staToTkMatchNoJPsi0.clone(src = "probeL1", srcTrack="none")
    process.l1ToTkMatchNoBestJPsi0 = process.staToTkMatchNoBestJPsi0.clone(src = "probeL1", srcTrack="none")
    process.probeMuonsMCMatchL1 = process.tagMuonsMCMatch.clone(src = "probeL1")
    process.tpTreeL1 = process.tpTreeSta.clone(
        tagProbePairs = "tpPairsTkL1",
        arbitration   = "OneProbe",
        variables = cms.PSet(
            KinematicVariables,
            bx = cms.string("bx"),
            quality = cms.string("gmtMuonCand.quality"),
            ## track matching variables
            tk_deltaR     = cms.InputTag("l1ToTkMatch","deltaR"),
            tk_deltaEta   = cms.InputTag("l1ToTkMatch","deltaEta"),
            tk_deltaR_NoJPsi   = cms.InputTag("l1ToTkMatchNoJPsi","deltaR"),
            tk_deltaEta_NoJPsi = cms.InputTag("l1ToTkMatchNoJPsi","deltaEta"),
            tk_deltaR_NoBestJPsi   = cms.InputTag("l1ToTkMatchNoBestJPsi","deltaR"),
            tk_deltaEta_NoBestJPsi = cms.InputTag("l1ToTkMatchNoBestJPsi","deltaEta"),
            ## track matching variables (early general tracks)
            tk0_deltaR     = cms.InputTag("l1ToTkMatch0","deltaR"),
            tk0_deltaEta   = cms.InputTag("l1ToTkMatch0","deltaEta"),
            tk0_deltaR_NoJPsi   = cms.InputTag("l1ToTkMatchNoJPsi0","deltaR"),
            tk0_deltaEta_NoJPsi = cms.InputTag("l1ToTkMatchNoJPsi0","deltaEta"),
            tk0_deltaR_NoBestJPsi   = cms.InputTag("l1ToTkMatchNoBestJPsi0","deltaR"),
            tk0_deltaEta_NoBestJPsi = cms.InputTag("l1ToTkMatchNoBestJPsi0","deltaEta"),
        ),
        flags = cms.PSet(
        ),
        tagVariables = cms.PSet(
            pt = cms.string("pt"),
            eta = cms.string("eta"),
            phi = cms.string("phi"),
            nVertices   = cms.InputTag("nverticesModule"),
	    #ERICA:to check if for the JPsi is valid
            #combRelIso = cms.string("(isolationR03.emEt + isolationR03.hadEt + isolationR03.sumPt)/pt"),
            #chargedHadIso04 = cms.string("pfIsolationR04().sumChargedHadronPt"),
            #neutralHadIso04 = cms.string("pfIsolationR04().sumNeutralHadronEt"),
            #photonIso04 = cms.string("pfIsolationR04().sumPhotonEt"),
            #combRelIsoPF04dBeta = IsolationVariables.combRelIsoPF04dBeta,
        ),
        pairVariables = cms.PSet(
            #nJets30 = cms.InputTag("njets30ModuleSta"),
            pt      = cms.string("pt"),
            rapidity = cms.string("rapidity"),
            deltaR   = cms.string("deltaR(daughter(0).eta, daughter(0).phi, daughter(1).eta, daughter(1).phi)"),
        ),
        pairFlags = cms.PSet(),
        allProbes     = cms.InputTag("probeL1"),
        probeMatches  = cms.InputTag("probeMuonsMCMatchL1"),
    )
    process.tagAndProbeTkL1 = cms.Path(
        process.fastFilter +
        process.probeL1 +
        process.tpPairsTkL1 +
        process.preTkMatchSequenceJPsi +
        process.l1ToTkMatch + 
        process.l1ToTkMatchNoJPsi + process.l1ToTkMatchNoBestJPsi +
        process.l1ToTkMatch0 + 
        process.l1ToTkMatchNoJPsi0 + process.l1ToTkMatchNoBestJPsi0 +
        process.probeMuonsMCMatchL1 +
        process.tpTreeL1
    )

##    _____     _          ____       _            
##   |  ___|_ _| | _____  |  _ \ __ _| |_ ___  ___ 
##   | |_ / _` | |/ / _ \ | |_) / _` | __/ _ \/ __|
##   |  _| (_| |   <  __/ |  _ < (_| | ||  __/\__ \
##   |_|  \__,_|_|\_\___| |_| \_\__,_|\__\___||___/
##                                                 
##       
#process.load("MuonAnalysis.TagAndProbe.fakerate_all_cff")
#
#process.fakeRateJetPlusProbeTree = process.tpTree.clone(
#    tagProbePairs = 'jetPlusProbe',
#    arbitration   = 'None',
#    tagVariables = process.JetPlusProbeTagVariables,
#    tagFlags = cms.PSet(),
#    pairVariables = cms.PSet(deltaPhi = cms.string("deltaPhi(daughter(0).phi, daughter(1).phi)")),
#    pairFlags     = cms.PSet(),
#    isMC = False, # MC matches not in place for FR yet
#)
#process.fakeRateWPlusProbeTree = process.tpTree.clone(
#    tagProbePairs = 'wPlusProbe',
#    arbitration   = 'None',
#    tagVariables = process.WPlusProbeTagVariables,
#    tagFlags = cms.PSet(),
#    pairVariables = cms.PSet(),
#    pairFlags     = cms.PSet(SameSign = cms.string('daughter(0).daughter(0).charge == daughter(1).charge')),
#    isMC = False, # MC matches not in place for FR yet
#)
#process.fakeRateZPlusProbeTree = process.tpTree.clone(
#    tagProbePairs = 'zPlusProbe',
#    arbitration   = 'None',
#    tagVariables  = process.ZPlusProbeTagVariables,
#    tagFlags      = cms.PSet(),
#    pairVariables = cms.PSet(),
#    pairFlags     = cms.PSet(),
#    isMC = False, # MC matches not in place for FR yet
#)
#
#process.fakeRateJetPlusProbe = cms.Path(
#    process.fastFilter +
#    process.mergedMuons * process.patMuonsWithTriggerSequence +
#    process.tagMuons + process.probeMuons + process.extraProbeVariablesSeq +
#    process.jetPlusProbeSequence +
#    process.fakeRateJetPlusProbeTree
#)
#process.fakeRateWPlusProbe = cms.Path(
#    process.fastFilter +
#    process.mergedMuons * process.patMuonsWithTriggerSequence +
#    process.tagMuons + process.probeMuons + process.extraProbeVariablesSeq +
#    process.wPlusProbeSequence +
#    process.fakeRateWPlusProbeTree
#)
#process.fakeRateZPlusProbe = cms.Path(
#    process.fastFilter +
#    process.mergedMuons * process.patMuonsWithTriggerSequence +
#    process.tagMuons + process.probeMuons + process.extraProbeVariablesSeq +
#    process.zPlusProbeSequence +
#    process.fakeRateZPlusProbeTree
#)

process.schedule = cms.Schedule(
    process.tagAndProbe, 
    process.tagAndProbeSta,
    process.tagAndProbeOnePair,
    process.tagAndProbeTkGen, 
    #process.tagAndProbeTkL1, 
    #process.fakeRateJetPlusProbe,
    #process.fakeRateWPlusProbe,
    #process.fakeRateZPlusProbe,
    )


process.TFileService = cms.Service("TFileService",
                                   #fileName = cms.string("tnpJPsi_MC.root")
                                   fileName = cms.string("tnpJPsi_officialBPHMC.root")
                                   )

# use this if you want to compute also 'unbiased' efficiencies, 
# - you have to remove all filters
# - you have to remove trigger requirements on the probes (but you can add a flag for them in the tree)
# note that it will be *much* slower and make a *much* bigger output tree!
if False:
    process.tagAndProbe.remove(process.oneTag)
    process.tagAndProbe.remove(process.onePair)
    process.tagAndProbe.remove(process.HLTBoth)
    process.tpTree.flags.TP_Probe_Cut = cms.string(process.probeMuons.cut.value())
    process.probeMuons.cut = "track.isNonnull"
    process.tpTree.makeMCUnbiasTree = True
if False:
    process.tagAndProbeSta.remove(process.oneTag)
    process.tagAndProbeSta.remove(process.onePairSta)
    process.tagAndProbeSta.remove(process.HLTMu)
    process.tpTreeSta.flags.TP_Probe_Cut = cms.string(process.probeMuonsSta.cut.value())
    process.probeMuonsSta.cut = "outerTrack.isNonnull"
    process.tpTreeSta.makeMCUnbiasTree = True


if True: # enable and do cmsRun tp_from_aod_MC.py /eos/path/to/run/on [ extra_postfix ] to run on all files in that eos path 
    import sys
    args = sys.argv[1:]
    if (sys.argv[0] == "cmsRun"): args = sys.argv[2:]
    scenario = args[0] if len(args) > 0 else ""
    if scenario:
        if scenario.startswith("/"):
            import subprocess
	    #files in eos
            files = subprocess.check_output([ "/afs/cern.ch/project/eos/installation/0.3.15/bin/eos.select", "ls", scenario ])
            process.source.fileNames = [ scenario+"/"+f for f in files.split() ]
	    #files in local
            #files = subprocess.check_output([ "ls", scenario ])
            #process.source.fileNames = [ "file:"+scenario+"/"+f for f in files.split() ]
            import os.path
            process.TFileService.fileName = "tnpJPsi_MC_%s.root" % os.path.basename(scenario)
        else:
            process.TFileService.fileName = "tnpJPsi_MC_%s.root" % scenario
    if len(args) > 1:
        process.TFileService.fileName = process.TFileService.fileName.value().replace(".root", ".%s.root" % args[1])
