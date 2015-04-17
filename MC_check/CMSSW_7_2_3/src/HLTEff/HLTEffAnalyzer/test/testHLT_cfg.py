import FWCore.ParameterSet.Config as cms

process = cms.Process("testHLT")

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('PHYS14_25_V1::All')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( -1 ) # MINIAOD: 500 events = 22Kb in 1', 10k events = 40Kb in 1', 200k events = 40kb in 10', 350k events = 41Kb in 15'
    ) # AOD: 1k events = 40Kb in 2', 10k events = 40k in 8'

process.source = cms.Source("PoolSource",
                            skipEvents = cms.untracked.uint32( 0 ),
                            fileNames = cms.untracked.vstring( # set later
                                #'file:myfile.root'
                                #'/store/mc/Phys14DR/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/AODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/02BE6C0D-E46E-E411-89C3-003048F0E1B0.root',
                            )
                        )

dataset = 'miniAOD'
#dataset = 'AOD'

if dataset == 'miniAOD' :
    sourceFiles = cms.untracked.vstring( # MINIAOD        
        '/store/mc/Phys14DR/JpsiToMuMu_JPsiPt7WithFSR_13TeV-pythia6-evtgen/MINIAODSIM/AVE30BX50_tsg_PHYS14_ST_V1-v2/00000/0033C66D-5E9A-E411-8F66-001E6739692D.root',
        '/store/mc/Phys14DR/JpsiToMuMu_JPsiPt7WithFSR_13TeV-pythia6-evtgen/MINIAODSIM/AVE30BX50_tsg_PHYS14_ST_V1-v2/00000/124916F0-5E9A-E411-A9D9-002481E75ED0.root',
        '/store/mc/Phys14DR/JpsiToMuMu_JPsiPt7WithFSR_13TeV-pythia6-evtgen/MINIAODSIM/AVE30BX50_tsg_PHYS14_ST_V1-v2/00000/581837DD-5E9A-E411-B71F-002590A3C954.root',
        '/store/mc/Phys14DR/JpsiToMuMu_JPsiPt7WithFSR_13TeV-pythia6-evtgen/MINIAODSIM/AVE30BX50_tsg_PHYS14_ST_V1-v2/00000/6AEF2574-5E9A-E411-A45D-002590A3C984.root',
        '/store/mc/Phys14DR/JpsiToMuMu_JPsiPt7WithFSR_13TeV-pythia6-evtgen/MINIAODSIM/AVE30BX50_tsg_PHYS14_ST_V1-v2/00000/96983F41-989A-E411-8955-002590A3C954.root',
        '/store/mc/Phys14DR/JpsiToMuMu_JPsiPt7WithFSR_13TeV-pythia6-evtgen/MINIAODSIM/AVE30BX50_tsg_PHYS14_ST_V1-v2/00000/CA7C3DBA-5E9A-E411-8787-002481E14D64.root',
        '/store/mc/Phys14DR/JpsiToMuMu_JPsiPt7WithFSR_13TeV-pythia6-evtgen/MINIAODSIM/AVE30BX50_tsg_PHYS14_ST_V1-v2/00000/EAAB7781-639A-E411-AA7A-002590A3C954.root',
        '/store/mc/Phys14DR/JpsiToMuMu_JPsiPt7WithFSR_13TeV-pythia6-evtgen/MINIAODSIM/AVE30BX50_tsg_PHYS14_ST_V1-v2/10000/62002A98-C999-E411-B9B9-002481E75ED0.root',
        '/store/mc/Phys14DR/JpsiToMuMu_JPsiPt7WithFSR_13TeV-pythia6-evtgen/MINIAODSIM/AVE30BX50_tsg_PHYS14_ST_V1-v2/10000/6A9F3E8C-C999-E411-ADBA-001E6739811A.root',
        '/store/mc/Phys14DR/JpsiToMuMu_JPsiPt7WithFSR_13TeV-pythia6-evtgen/MINIAODSIM/AVE30BX50_tsg_PHYS14_ST_V1-v2/10000/9205F8A8-C999-E411-AAA3-0025B31E330A.root'
    )
elif dataset == 'AOD' :
    sourceFiles = cms.untracked.vstring( # AOD
        '/store/mc/Phys14DR/JpsiToMuMu_JPsiPt7WithFSR_13TeV-pythia6-evtgen/AODSIM/AVE30BX50_tsg_PHYS14_ST_V1-v2/00000/0242F210-A299-E411-9003-002481E1506A.root'
    )

process.PoolSource.fileNames = sourceFiles ;

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("HLT.root"),
                                   closeFileFast = cms.untracked.bool(True)
                                   )

if dataset == 'miniAOD' :
    process.TFileService.fileName = cms.string("miniAOD.root")
elif dataset == 'AOD' :
    process.TFileService.fileName = cms.string("AOD.root")

process.analyzeHLT = cms.EDAnalyzer('HLTEffAnalyzer',
                                    dataset = cms.untracked.string( dataset ),
                                    DataType = cms.untracked.string('SimData'),
                                    triggerEvent = cms.InputTag("hltTriggerSummaryAOD","","HLT"),
                                    triggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                                    #vtxTag = cms.InputTag(""), # set later
                                    #pruned = cms.InputTag(""), # set later
                                    #MuonCollectionLabel = cms.InputTag(""), # set later
                                    #Debug = cms.untracked.bool(True),
				    #
				    deltaR_bins = cms.int32( 110 ),
				    deltaR_binMin = cms.double( 0 ),
				    deltaR_binMax = cms.double( 1.1 ),
				    pT_bins = cms.vdouble(2, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.5, 5, 6, 8, 10, 15, 20),
				    eta_bins = cms.vdouble(-2.1, -1.6, -1.2, -0.9, -0.6, -0.3, -0.2, 0.2, 0.3, 0.6, 0.9, 1.2, 1.6, 2.1),
				    nVtx_bins = cms.vdouble(0.5, 2.5, 4.5, 6.5, 8.5, 10.5, 12.5, 14.5, 16.5, 18.5, 20.5, 22.5, 24.5, 26.5, 28.5, 30.5),
				    #
				    propM1 = cms.PSet(
                                        useStation2 = cms.bool(False), 
        				useTrack = cms.string("tracker"),
        				useState = cms.string("atVertex"),  # in AOD
        				useSimpleGeometry = cms.bool(True), # use just one cylinder and two planes, not all the fancy chambers
    				    ),
    				    propM2 = cms.PSet(
        				useStation2 = cms.bool(True), 
        				useTrack = cms.string("tracker"),
        				useState = cms.string("atVertex"),  # in AOD
        				useSimpleGeometry = cms.bool(True), # use just one cylinder and two planes, not all the fancy chambers
    				    ),				    
				    deltaR_cowBoys = cms.double(0.5),
				    deltaR_max = cms.double(0.2)
#BPH:
#J/psi: 2, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.5, 5, 5.5, 6, 7, 9, 11, 14, 17, 20
#Z: 2, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.5, 5, 5.5, 6, 7, 9, 11, 14, 17, 20
#J/psi vs Z comparison: 5, 10, 14, 17, 20    
                                )

if dataset == 'miniAOD' :
    process.analyzeHLT.vtxTag = cms.InputTag("offlineSlimmedPrimaryVertices") # miniAOD goodPrimaryVertices                                    
    process.analyzeHLT.pruned = cms.InputTag("prunedGenParticles")
    process.analyzeHLT.MuonCollectionLabel = cms.InputTag("slimmedMuons")
elif dataset == 'AOD' :
    process.analyzeHLT.vtxTag = cms.InputTag("offlinePrimaryVertices")
    process.analyzeHLT.pruned = cms.InputTag("genParticles")
    process.analyzeHLT.MuonCollectionLabel = cms.InputTag('muons','','RECO') 
                                    
process.p = cms.Path( process.analyzeHLT
                  )

