import FWCore.ParameterSet.Config as cms

from MuonAnalysis.TagAndProbe.nearbyMuonsInfo_cfi import nearbyMuonsInfo as tagProbeSeparation

tagProbeStaSeparation = tagProbeSeparation.clone(
    src = cms.InputTag("tpPairsSta"), 
    ) 

#########################################################################################
##        Object counting modules                                                      ##
#########################################################################################

nverticesModule = cms.EDProducer("VertexMultiplicityCounter", 
    probes = cms.InputTag("tagMuons"),
    objects = cms.InputTag("offlinePrimaryVertices"),
    objectSelection = cms.string("!isFake && ndof > 4 && abs(z) <= 25 && position.Rho <= 2"),
)

njets30Module = cms.EDProducer("CandCleanedMultiplicityCounter", 
    pairs   = cms.InputTag("tpPairs"),
    objects = cms.InputTag("ak4PFJetsCHS"),
    objectSelection = cms.string("abs(eta) < 5 && pt > 30"), 
    minTagObjDR   = cms.double(0.3),
    minProbeObjDR = cms.double(0.3),
)

#########################################################################################
##        Tracking-related modules                                                     ##
#########################################################################################

## Now I have to define the passing probes for tracking
## first remove low pt tracks which will not make muons anyway
pCutTracks = cms.EDFilter("TrackSelector", 
    src = cms.InputTag("generalTracks"),      
    cut = cms.string("pt > 2 || (abs(eta) > 1 && p > 2)"),
)
tkTracks = cms.EDProducer("ConcreteChargedCandidateProducer", 
    src = cms.InputTag("pCutTracks"),
    particleType = cms.string("mu+"),
)

## Filter out the J/Psi's, to compute fake matching rate
tkTracksNoJPsi = cms.EDProducer("CandidateResonanceInefficiencyCreator",
    src = cms.InputTag("tkTracks"),
    tags = cms.InputTag("tagMuons"),
    mass    = cms.double(3.096),
    massMin = cms.double(2.85), ## Should cut away
    massMax = cms.double(3.25), ## 99.5% of signal
    onlyBestMatch = cms.bool(False),
    outputMode = cms.string("RefToBaseVector"),
)
tkTracksNoBestJPsi = tkTracksNoJPsi.clone(onlyBestMatch = True)

## Filter out the Z's, to compute fake matching rate
tkTracksNoZ = cms.EDProducer("CandidateResonanceInefficiencyCreator",
    src = cms.InputTag("tkTracks"),
    tags = cms.InputTag("tagMuons"),
    mass    = cms.double(91.2),
    massMin = cms.double(40),  ## Should cut away most
    massMax = cms.double(200), ## of the signal
    onlyBestMatch = cms.bool(True),
    outputMode = cms.string("RefToBaseVector"),
)

staToTkMatch = cms.EDProducer("MatcherUsingTracksWithTagAssoc",
    src     = cms.InputTag("probeMuonsSta"),
    matched = cms.InputTag("tkTracks"),  
    tags      = cms.InputTag("tagMuons"),
    tagDeltaZ = cms.double(1.0),
    algorithm = cms.string("byDirectComparison"), 
    srcTrack     = cms.string("muon"),    srcState = cms.string("atVertex"), 
    matchedTrack = cms.string("tracker"), matchedState = cms.string("atVertex"),
    maxDeltaR        = cms.double(1.),   # large range in DR (we can tighten it later)
    maxDeltaEta      = cms.double(0.4),  # small in eta, which is more precise
    maxDeltaLocalPos = cms.double(100),
    maxDeltaPtRel    = cms.double(5),   # |pt(sta) - pt(tk)|/pt(tk)
    sortBy           = cms.string("deltaR"),
    requireSameCharge = cms.bool(True),
)
staToTkMatchNoJPsi = staToTkMatch.clone(matched = 'tkTracksNoJPsi')
staToTkMatchNoBestJPsi = staToTkMatch.clone(matched = 'tkTracksNoBestJPsi')
staToTkMatchNoZ = staToTkMatch.clone(matched = 'tkTracksNoZ')

preTkMatchSequenceJPsi = cms.Sequence( pCutTracks + tkTracks + tkTracksNoJPsi + tkTracksNoBestJPsi )
staToTkMatchSequenceJPsi = cms.Sequence(
    preTkMatchSequenceJPsi * staToTkMatch * staToTkMatchNoJPsi * staToTkMatchNoBestJPsi     
)

preTkMatchSequenceZ = cms.Sequence( pCutTracks + tkTracks + tkTracksNoZ )
staToTkMatchSequenceZ = cms.Sequence(
    preTkMatchSequenceZ * staToTkMatch * staToTkMatchNoZ     
)

#########################################################################################
##        Isolation modules                                                            ##
#########################################################################################

import RecoMuon.MuonIsolationProducers.muIsoDepositTk_cfi
probeMuonsIsoDepositTk = RecoMuon.MuonIsolationProducers.muIsoDepositTk_cfi.muIsoDepositTk.clone()
probeMuonsIsoDepositTk.IOPSet.inputMuonCollection = 'probeMuons'
probeMuonsIsoFromDepsTk = cms.EDProducer("CandIsolatorFromDeposits", 
    deposits = cms.VPSet( cms.PSet(
        src = cms.InputTag("probeMuonsIsoDepositTk"),
        mode = cms.string('sum'),
        weight = cms.string('1'),
        deltaR = cms.double(0.3),
        vetos = cms.vstring('0.01'),
        skipDefaultVeto = cms.bool(True),
        label = cms.string('tkDep'),
    ))
)
probeMuonsRelIsoFromDepsTk = probeMuonsIsoFromDepsTk.clone()
probeMuonsRelIsoFromDepsTk.deposits[0].mode = "sumRelative"
probeMuonsIsoValueMaps = cms.EDProducer("AnyNumbersToValueMaps",
    collection = cms.InputTag("probeMuons"),
    associations = cms.VInputTag(cms.InputTag("probeMuonsIsoFromDepsTk"), cms.InputTag("probeMuonsRelIsoFromDepsTk")),
)
probeMuonsIsoSequence = cms.Sequence(
    ( probeMuonsIsoDepositTk * 
        ( probeMuonsIsoFromDepsTk + probeMuonsRelIsoFromDepsTk) 
    ) * probeMuonsIsoValueMaps
)

muonMiniIsoCharged = cms.EDProducer("MuonMiniIso",
    probes = cms.InputTag("probeMuons"),
    pfCandidates = cms.InputTag("pfAllChargedHadronsPFBRECO"),
    dRCandProbeVeto = cms.double(0.0001),
    CandPtThreshold = cms.double(0.0),
)

muonMiniIsoPUCharged = cms.EDProducer("MuonMiniIso",
    probes = cms.InputTag("probeMuons"),
    pfCandidates = cms.InputTag("pfPileUpAllChargedParticlesPFBRECO"),
    dRCandProbeVeto = cms.double(0.0001),
    CandPtThreshold = cms.double(0.0),
)

muonMiniIsoNeutrals = cms.EDProducer("MuonMiniIso",
    probes = cms.InputTag("probeMuons"),
    pfCandidates = cms.InputTag("pfAllNeutralHadronsPFBRECO"),
    dRCandProbeVeto = cms.double(0.01),
    CandPtThreshold = cms.double(1.0),
)

muonMiniIsoPhotons = cms.EDProducer("MuonMiniIso",
    probes = cms.InputTag("probeMuons"),
    pfCandidates = cms.InputTag("pfAllPhotonsPFBRECO"),
    dRCandProbeVeto = cms.double(0.01),
    CandPtThreshold = cms.double(0.5),
)


#########################################################################################
##        Other modules                                                                ##
#########################################################################################

muonDxyPVdzmin = cms.EDProducer("MuonDxyPVdzmin",
    probes = cms.InputTag("probeMuons"),
)
muonDxyPVdzminTags = muonDxyPVdzmin.clone(probes = "tagMuons")

probeMultiplicity = cms.EDProducer("ProbeMulteplicityProducer",
   pairs = cms.InputTag("tpPairs"),
   #pairCut  = cms.string(""),  # count only probes whose pairs satisfy this cut
   #probeCut = cms.string(""),  # count only probes satisfying this cut
)
probeStaMultiplicity = probeMultiplicity.clone(
    pairs = cms.InputTag("tpPairsSta"), 
) 
#
probeMultiplicityTMGM = cms.EDProducer("ProbeMulteplicityProducer",
   pairs = cms.InputTag("tpPairs"),
   #pairCut  = cms.string(""),  # count only probes whose pairs satisfy this cut
   probeCut = cms.string("isTrackerMuon || isGlobalMuon"),  # count only probes satisfying this cut
)
probeMultiplicityPt10M60140 = cms.EDProducer("ProbeMulteplicityProducer",
   pairs = cms.InputTag("tpPairs"),
   pairCut  = cms.string("mass > 60 && mass < 140"),  # count only probes whose pairs satisfy this cut
   probeCut = cms.string("pt > 10"),  # count only probes satisfying this cut
)
probeMultiplicities = cms.Sequence(probeMultiplicity  + probeMultiplicityTMGM + probeMultiplicityPt10M60140)


bestPairByZMass = cms.EDProducer("BestPairByMass",
    pairs = cms.InputTag("tpPairs"),
    mass  = cms.double(91.2),
)

splitTrackTagger = cms.EDProducer("NearbyCandCountComputer",
    probes = cms.InputTag("probeMuons"),
    objects = cms.InputTag("probeMuons"),
    deltaR  = cms.double(0.03),
    pairSelection = cms.string("mu1.charge == mu2.charge && "+ 
                               "abs(mu1.vz - mu2.vz) - 3*hypot(mu1.track.dzError,mu2.track.dzError) < 1 && "+
                               "abs(mu1.track.hitPattern.numberOfValidPixelHits - mu2.track.hitPattern.numberOfValidPixelHits) >= 2 && "+
                               "abs(mu1.track.hitPattern.numberOfLostHits('MISSING_OUTER_HITS') - mu2.track.hitPattern.numberOfLostHits('MISSING_OUTER_HITS')) >= 2 && "+
                               "( abs(mu1.pt - mu2.pt) - 10*hypot(mu1.track.ptError,mu2.track.ptError) )/min(mu1.pt, mu2.pt) < 0"),
)
#numberOfLostHits('MISSING_INNER_HITS')

l1rate = cms.EDProducer("ComputeL1TriggerRate",
    probes = cms.InputTag("tagMuons"),
    scalers = cms.InputTag("scalersRawToDigi"),
)

newTunePVals = cms.EDProducer("HighPtMuonsInfo",
    src = cms.InputTag("tpPairs"),
)

genWeightInfo = cms.EDProducer("GenWeightInfo",
    pairTag= cms.InputTag("tpPairs"),
    genInfoTag= cms.InputTag("generator")
)

l1hltprescale = cms.EDProducer("ComputeL1HLTPrescales",
    probes = cms.InputTag("tagMuons"),
    hltConfig = cms.string("HLT"),
    hltPaths = cms.vstring("HLT_Mu17_v", "HLT_Mu8_v"),
)

goodGenMuons = cms.EDFilter("GenParticleSelector",
    src = cms.InputTag("genParticles"),
    cut = cms.string("abs(pdgId) == 13 && pt > 3 && abs(eta) < 2.4 && status == 1 && isPromptFinalState")
)

goodGenMuonsFromJpsi = cms.EDFilter("GenParticleSelector",
    src = cms.InputTag("genParticles"),
    cut = cms.string("abs(pdgId) == 13 && abs(eta) < 2.4 && numberOfMothers == 1 && motherRef.pdgId == 443")
)

softIDToGenMatch = cms.EDProducer("MatcherUsingTracksWithTagAssoc",
    src     = cms.InputTag("probeMuons"),
    matched = cms.InputTag("goodGenMuonsFromJpsi"),  
    tags      = cms.InputTag("tagMuons"), # needed just to ask for #Deltaz < tagDeltaZ
    tagDeltaZ = cms.double(1.0),
    algorithm = cms.string("byDirectComparison"), 
    srcTrack     = cms.string("muon"),    srcState = cms.string("atVertex"), 
    matchedTrack = cms.string("tracker"), matchedState = cms.string("atVertex"),
    maxDeltaR        = cms.double(1.),   # large range in DR (we can tighten it later)
    maxDeltaEta      = cms.double(0.4),  # small in eta, which is more precise
    maxDeltaLocalPos = cms.double(100),
    maxDeltaPtRel    = cms.double(5),   # |pt(src) - pt(matched)|/pt(matched)
    sortBy           = cms.string("deltaR"),
    requireSameCharge = cms.bool(True),
    softID = cms.bool(False),
    objCut = cms.string("")
)
