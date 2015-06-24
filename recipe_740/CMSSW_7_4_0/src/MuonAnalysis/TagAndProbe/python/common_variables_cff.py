import FWCore.ParameterSet.Config as cms

KinematicVariables = cms.PSet(
    pt  = cms.string("pt"),
    p   = cms.string("p"),
    eta = cms.string("eta"),
    phi = cms.string("phi"),
    abseta = cms.string("abs(eta)"),
    charge = cms.string("charge")
)
IsolationVariables = cms.PSet(
    tkIso  = cms.string("isolationR03.sumPt"),
    ecalIso = cms.string("isolationR03.emEt"),
    hcalIso = cms.string("isolationR03.hadEt"),
    combRelIso = cms.string("(isolationR03.emEt + isolationR03.hadEt + isolationR03.sumPt)/pt"),
    
    chargedHadIso03 = cms.string("pfIsolationR03().sumChargedHadronPt"),
    puIso03 = cms.string("pfIsolationR03().sumPUPt"),
    neutralHadIso03 = cms.string("pfIsolationR03().sumNeutralHadronEt"),
    photonIso03 = cms.string("pfIsolationR03().sumPhotonEt"),
    chargedParticleIso03 = cms.string("pfIsolationR03().sumChargedParticlePt"),
    combRelIsoPF03 = cms.string("(pfIsolationR03().sumChargedHadronPt + pfIsolationR03().sumNeutralHadronEt + pfIsolationR03().sumPhotonEt)/pt"),
    combRelIsoPF03dBeta = cms.string("(pfIsolationR03().sumChargedHadronPt + max(pfIsolationR03().sumNeutralHadronEt + pfIsolationR03().sumPhotonEt - pfIsolationR03().sumPUPt/2,0.0))/pt"),
    chargedHadIso04 = cms.string("pfIsolationR04().sumChargedHadronPt"),
    puIso04 = cms.string("pfIsolationR04().sumPUPt"),
    neutralHadIso04 = cms.string("pfIsolationR04().sumNeutralHadronEt"),
    photonIso04 = cms.string("pfIsolationR04().sumPhotonEt"),
    chargedParticleIso04 = cms.string("pfIsolationR04().sumChargedParticlePt"),
    combRelIsoPF04 = cms.string("(pfIsolationR04().sumChargedHadronPt + pfIsolationR04().sumNeutralHadronEt + pfIsolationR04().sumPhotonEt)/pt"),
    combRelIsoPF04dBeta = cms.string("(pfIsolationR04().sumChargedHadronPt + max(pfIsolationR04().sumNeutralHadronEt + pfIsolationR04().sumPhotonEt - pfIsolationR04().sumPUPt/2,0.0))/pt"),
)

MuonIDVariables = cms.PSet(
    caloCompatibility = cms.string("? isCaloCompatibilityValid ? caloCompatibility : -1"),
    numberOfMatches   = cms.string("? isMatchesValid ? numberOfMatches : -1"),
    numberOfMatchedStations = cms.string("? isMatchesValid ? numberOfMatchedStations : -1"),
    segmentCompatibility = cms.string("segmentCompatibility"),
)
MuonCaloVariables = cms.PSet(
    hadEnergy   = cms.string("calEnergy.had"),
    emEnergy    = cms.string("calEnergy.em"),
    hadS9Energy = cms.string("calEnergy.hadS9"),
    emS9Energy  = cms.string("calEnergy.emS9"),
)
TrackQualityVariables = cms.PSet(
    # 2D variables
    dB          = cms.string("dB"),
    edB         = cms.string("edB"),
    # 3D variables
    IP = cms.string('abs(dB("PV3D"))'),
    IPError = cms.string('edB("PV3D")'),
    SIP = cms.string('abs(dB("PV3D")/edB("PV3D"))'),
    # Hits and such
    tkValidHits = cms.string("? track.isNull ? 0 : track.numberOfValidHits"),
    tkTrackerLay = cms.string("? track.isNull ? 0 : track.hitPattern.trackerLayersWithMeasurement"),
    tkValidPixelHits = cms.string("? track.isNull ? 0 : track.hitPattern.numberOfValidPixelHits"),
    tkPixelLay  = cms.string("? track.isNull ? 0 : track.hitPattern.pixelLayersWithMeasurement"),
    tkExpHitIn = cms.string("? track.isNull ? 0 : track.hitPattern.numberOfLostHits('MISSING_INNER_HITS')"),
    tkExpHitOut = cms.string("? track.isNull ? 0 : track.hitPattern.numberOfLostHits('MISSING_OUTER_HITS')"),
    tkHitFract  = cms.string("? track.isNull ? 0 : track.hitPattern.numberOfValidHits/(track.hitPattern.numberOfValidHits+track.hitPattern.numberOfLostHits('TRACK_HITS')+track.hitPattern.numberOfLostHits('MISSING_INNER_HITS')+ track.hitPattern.numberOfLostHits('MISSING_OUTER_HITS') )"),
    tkChi2 = cms.string("? track.isNull ? -1 : track.normalizedChi2"),
    tkPtError = cms.string("? track.isNull ? -1 : track.ptError"),
    tkSigmaPtOverPt = cms.string("? track.isNull ? -1 : track.ptError/track.pt"),
    tkKink = cms.string("combinedQuality.trkKink"),
)
GlobalTrackQualityVariables = cms.PSet(
    glbChi2 = cms.string("? globalTrack.isNull ? -1 : globalTrack.normalizedChi2"),
    glbValidMuHits = cms.string("? globalTrack.isNull ? 0 : globalTrack.hitPattern.numberOfValidMuonHits"),
    glbPtError = cms.string("? globalTrack.isNull ? -1 : globalTrack.ptError"),
    glbSigmaPtOverPt = cms.string("? globalTrack.isNull ? -1 : globalTrack.ptError/globalTrack.pt"),
    chi2LocMom = cms.string("combinedQuality.chi2LocalMomentum"),
    chi2LocPos = cms.string("combinedQuality.chi2LocalPosition"),
    glbTrackProb = cms.string("combinedQuality.glbTrackProbability"),
)
StaOnlyVariables = cms.PSet(
    staQoverP      = cms.string("? outerTrack.isNull() ? 0 : outerTrack.qoverp"),
    staQoverPerror = cms.string("? outerTrack.isNull() ? 0 : outerTrack.qoverpError"),
    staValidStations = cms.string("? outerTrack.isNull() ? -1 : outerTrack.hitPattern.muonStationsWithValidHits()"),
)
L1Variables = cms.PSet(
    l1pt = cms.string("? userCand('muonL1Info').isNull ? 0 : userCand('muonL1Info').pt"),
    l1q  = cms.string("userInt('muonL1Info:quality')"),
    l1dr = cms.string("userFloat('muonL1Info:deltaR')"),
    l1ptByQ = cms.string("? userCand('muonL1Info:ByQ').isNull ? 0 : userCand('muonL1Info:ByQ').pt"),
    l1qByQ  = cms.string("userInt('muonL1Info:qualityByQ')"),
    l1drByQ = cms.string("userFloat('muonL1Info:deltaRByQ')"),
)
L2Variables = cms.PSet(
    l2pt  = cms.string("? triggerObjectMatchesByCollection('hltL2MuonCandidates').empty() ? 0 : triggerObjectMatchesByCollection('hltL2MuonCandidates').at(0).pt"),
    l2eta = cms.string("? triggerObjectMatchesByCollection('hltL2MuonCandidates').empty() ? 0 : triggerObjectMatchesByCollection('hltL2MuonCandidates').at(0).eta"),
    l2dr  = cms.string("? triggerObjectMatchesByCollection('hltL2MuonCandidates').empty() ? 999 : "+
                      " deltaR( eta, phi, " +
                      "         triggerObjectMatchesByCollection('hltL2MuonCandidates').at(0).eta, "+
                      "         triggerObjectMatchesByCollection('hltL2MuonCandidates').at(0).phi ) ")
)
L3Variables = cms.PSet(
    l3pt = cms.string("? triggerObjectMatchesByCollection('hltL3MuonCandidates').empty() ? 0 : triggerObjectMatchesByCollection('hltL3MuonCandidates').at(0).pt"),
    l3dr = cms.string("? triggerObjectMatchesByCollection('hltL3MuonCandidates').empty() ? 999 : "+
                      " deltaR( eta, phi, " +
                      "         triggerObjectMatchesByCollection('hltL3MuonCandidates').at(0).eta, "+
                      "         triggerObjectMatchesByCollection('hltL3MuonCandidates').at(0).phi ) ")
)
TriggerVariables = cms.PSet(L1Variables, L2Variables, L3Variables)
AllVariables = cms.PSet(KinematicVariables, IsolationVariables, MuonIDVariables, MuonCaloVariables, TrackQualityVariables, GlobalTrackQualityVariables, L1Variables, L2Variables, L3Variables)

TrackQualityFlags = cms.PSet(
    Track_HP  = cms.string("? track.isNonnull ? track.quality('highPurity') : 0"),
)
MuonIDFlags = cms.PSet(
    Calo   = cms.string("isCaloMuon"),
    Glb    = cms.string("isGlobalMuon"),
    GlbPT  = cms.string("muonID('GlobalMuonPromptTight')"),
    TM     = cms.string("isTrackerMuon"),
    TMA    = cms.string("muonID('TrackerMuonArbitrated')"),
    PF     = cms.string("isPFMuon()"),
    TMLSAT = cms.string("muonID('TMLastStationAngTight')"),
    TMLST  = cms.string("muonID('TMLastStationTight')"),
    TMOSL  = cms.string("muonID('TMOneStationLoose')"),
    TMOST  = cms.string("muonID('TMOneStationTight')"),
    TMOSTQual  = cms.string("muonID('TMOneStationTight') && track.numberOfValidHits > 10 && track.normalizedChi2()<1.8 && track.hitPattern.pixelLayersWithMeasurement>1"),
    VBTF   = cms.string("numberOfMatchedStations > 1 && muonID('GlobalMuonPromptTight') && abs(dB) < 0.2 && "+
                        "track.numberOfValidHits > 10 && track.hitPattern.numberOfValidPixelHits > 0"),
    VBTF_nL8    = cms.string("numberOfMatchedStations > 1 && muonID('GlobalMuonPromptTight') && abs(dB) < 0.2 && "+
                        "track.hitPattern.trackerLayersWithMeasurement > 8 && track.hitPattern.numberOfValidPixelHits > 0"),
    VBTF_nL9    = cms.string("numberOfMatchedStations > 1 && muonID('GlobalMuonPromptTight') && abs(dB) < 0.2 && "+
                        "track.hitPattern.trackerLayersWithMeasurement > 9 && track.hitPattern.numberOfValidPixelHits > 0"),
    Tight2012   = cms.string("isPFMuon && numberOfMatchedStations > 1 && muonID('GlobalMuonPromptTight') && abs(dB) < 0.2 && "+
                        "track.hitPattern.trackerLayersWithMeasurement > 5 && track.hitPattern.numberOfValidPixelHits > 0"),
    Medium      = cms.string("isPFMuon && innerTrack.validFraction >= 0.8 && ( isGlobalMuon && globalTrack.normalizedChi2 < 3 && combinedQuality.chi2LocalPosition < 12 && combinedQuality.trkKink < 20 && segmentCompatibility >= 0.303 || segmentCompatibility >= 0.451 )"),
    HWWID =  cms.string("( ((isGlobalMuon() && "
                        "    globalTrack.normalizedChi2 <10 &&" +
                        "    globalTrack.hitPattern.numberOfValidMuonHits > 0 && " + 
                        "    numberOfMatches > 1 ) || " + 
                        "   (isTrackerMuon() && muonID('TMLastStationTight')) ) && " +
                        " isPFMuon && "+
                        " combinedQuality.trkKink < 20 &&" +
                        " innerTrack.hitPattern.trackerLayersWithMeasurement > 5 &&" +
                        " innerTrack.hitPattern.numberOfValidPixelHits > 0 && " + 
                        " abs(track.ptError / pt) < 0.10 )"),
)

HighPtTriggerFlags = cms.PSet(
   Mu40      = cms.string("!triggerObjectMatchesByPath('HLT_Mu40_v*',1,0).empty()"),
   Mu40_eta2p1 = cms.string("!triggerObjectMatchesByPath('HLT_Mu40_eta2p1_v*',1,0).empty()"),
   IsoMu24   = cms.string("!triggerObjectMatchesByPath('HLT_IsoMu24_v*',1,0).empty()"),
   IsoMu24_eta2p1   = cms.string("!triggerObjectMatchesByPath('HLT_IsoMu24_eta2p1_v*',1,0).empty()"),
   IsoMu30   = cms.string("!triggerObjectMatchesByPath('HLT_IsoMu30_v*',1,0).empty()"),
   
   ## Heavily prescaled but still useful
   Mu17 = cms.string("!triggerObjectMatchesByPath('HLT_Mu17_v*',1,0).empty()"),
   Mu8  = cms.string("!triggerObjectMatchesByPath('HLT_Mu8_v*',1,0).empty()"),

   DoubleMu17Mu8_Mu17 = cms.string("!triggerObjectMatchesByPath('HLT_Mu17_Mu8_v*',1,0).empty() && (!triggerObjectMatchesByFilter('hltL3fL1DoubleMu10MuOpenL1f0L2f10L3Filtered17').empty() || !triggerObjectMatchesByFilter('hltL3fL1DoubleMu10MuOpenOR3p5L1f0L2f10L3Filtered17').empty())"),
   DoubleMu17Mu8_Mu17leg = cms.string("!triggerObjectMatchesByFilter('hltL3fL1DoubleMu10MuOpenL1f0L2f10L3Filtered17').empty() || !triggerObjectMatchesByFilter('hltL3fL1DoubleMu10MuOpenOR3p5L1f0L2f10L3Filtered17').empty()"),
   DoubleMu17Mu8_Mu8leg = cms.string("!triggerObjectMatchesByFilter('hltL3pfL1DoubleMu10MuOpenL1f0L2pf0L3PreFiltered8').empty() || !triggerObjectMatchesByFilter('hltL3pfL1DoubleMu10MuOpenOR3p5L1f0L2pf0L3PreFiltered8').empty()"),
   DoubleMu17TkMu8_Mu17 = cms.string("!triggerObjectMatchesByPath('HLT_Mu17_TkMu8_v*',1,0).empty() && (!triggerObjectMatchesByFilter('hltL3fL1sMu10MuOpenL1f0L2f10L3Filtered17').empty() || !triggerObjectMatchesByFilter('hltL3fL1sMu10MuOpenOR3p5L1f0L2f10L3Filtered17').empty())"),
   DoubleMu17TkMu8_Mu17leg = cms.string("!triggerObjectMatchesByFilter('hltL3fL1sMu10MuOpenL1f0L2f10L3Filtered17').empty() || !triggerObjectMatchesByFilter('hltL3fL1sMu10MuOpenOR3p5L1f0L2f10L3Filtered17').empty()"),
   DoubleMu17TkMu8_TkMu8leg = cms.string("!triggerObjectMatchesByFilter('hltDiMuonGlbFiltered17TrkFiltered8').empty()"),
   DoubleMu17TkMu8NoDZ_Mu17 = cms.string("!triggerObjectMatchesByPath('HLT_Mu17_TkMu8_NoDZ_v*',1,0).empty() && !triggerObjectMatchesByFilter('hltL3fL1sMu10MuOpenOR3p5L1f0L2f10L3Filtered17').empty()"),
   DoubleMu13Mu8NoDZ_Mu13 = cms.string("!triggerObjectMatchesByPath('HLT_Mu13_Mu8_NoDZ_v*',1,0).empty() && !triggerObjectMatchesByFilter('hltL3fL1DoubleMu10MuOpenOR3p5L1f0L2f10L3Filtered13').empty()"),
   DoubleMu13Mu8NoDZ_Mu8leg = cms.string("!triggerObjectMatchesByFilter('hltL3pfL1DoubleMu10MuOpenOR3p5L1f0L2pf0L3PreFiltered8').empty()"),
)
HighPtTriggerFlagsDebug = cms.PSet(
                                   #Empty at the moment
                                   )


LowPtTriggerFlagsPhysics = cms.PSet(
                                    #Empty at the moment
                                   )

LowPtTriggerFlagsEfficienciesTag = cms.PSet(
   ########## Mu + Track ########## 
   Mu7p5_Track2_Jpsi_MU = cms.string("!triggerObjectMatchesByCollection('hltL3MuonCandidates').empty() && "+
                                     " triggerObjectMatchesByCollection('hltL3MuonCandidates').at(0).hasFilterLabel('hltMu7p5Track2JpsiTrackMassFiltered')"),
   Mu7p5_Track3p5_Jpsi_MU = cms.string("!triggerObjectMatchesByCollection('hltL3MuonCandidates').empty() && "+
                                       " triggerObjectMatchesByCollection('hltL3MuonCandidates').at(0).hasFilterLabel('hltMu7p5Track3p5JpsiTrackMassFiltered')"),
   Mu7p5_Track7_Jpsi_MU = cms.string("!triggerObjectMatchesByCollection('hltL3MuonCandidates').empty() && "+
                                     " triggerObjectMatchesByCollection('hltL3MuonCandidates').at(0).hasFilterLabel('hltMu7p5Track7JpsiTrackMassFiltered')"),
   ########## Mu + L2Mu ##########
   Mu7p5_L2Mu2_Jpsi_MU = cms.string("!triggerObjectMatchesByCollection('hltL3MuonCandidates').empty() && "+
                                 " triggerObjectMatchesByCollection('hltL3MuonCandidates').at(0).hasFilterLabel('hltMu7p5L2Mu2JpsiTrackMassFiltered')"),
)

LowPtTriggerFlagsEfficienciesProbe = cms.PSet(
    ########## Mu + Track ##########
    #Mu7p5_Track2_Jpsi_TK = cms.string("!triggerObjectMatchesByCollection('hltMuTrackJpsiEffCtfTrackCands').empty() && "+
    #                                  " triggerObjectMatchesByCollection('hltMuTrackJpsiEffCtfTrackCands').at(0).hasFilterLabel('hltMu7p5Track2JpsiTrackMassFiltered')"),
    #Mu7p5_Track3p5_Jpsi_TK = cms.string("!triggerObjectMatchesByCollection('hltMuTrackJpsiEffCtfTrackCands').empty() && "+
    #                                    " triggerObjectMatchesByCollection('hltMuTrackJpsiEffCtfTrackCands').at(0).hasFilterLabel('hltMu7p5Track3p5JpsiTrackMassFiltered')"),
    #Mu7p5_Track7_Jpsi_TK = cms.string("!triggerObjectMatchesByCollection('hltMuTrackJpsiEffCtfTrackCands').empty() && "+
    #                                  " triggerObjectMatchesByCollection('hltMuTrackJpsiEffCtfTrackCands').at(0).hasFilterLabel('hltMu7p5Track7JpsiTrackMassFiltered')"),
    Mu7p5_Track2_Jpsi_TK = cms.string("!triggerObjectMatchesByCollection('hltTracksIter').empty()"
                                      + "&& triggerObjectMatchesByCollection('hltTracksIter').at(0).hasFilterLabel('hltMu7p5Track2JpsiTrackMassFiltered')"
                                      ),
    Mu7p5_Track3p5_Jpsi_TK = cms.string("!triggerObjectMatchesByCollection('hltTracksIter').empty()"
                                        + "&& triggerObjectMatchesByCollection('hltTracksIter').at(0).hasFilterLabel('hltMu7p5Track3p5JpsiTrackMassFiltered')"
                                        ),
    Mu7p5_Track7_Jpsi_TK = cms.string("!triggerObjectMatchesByCollection('hltTracksIter').empty()"
                                      + "&& triggerObjectMatchesByCollection('hltTracksIter').at(0).hasFilterLabel('hltMu7p5Track7JpsiTrackMassFiltered')"
                                      ),
    ########## Mu + L2Mu ##########
    Mu7p5_L2Mu2_Jpsi_L2 = cms.string("!triggerObjectMatchesByCollection('hltL2MuonCandidates').empty()"
                                     + "&& triggerObjectMatchesByCollection('hltL2MuonCandidates').at(0).hasFilterLabel('hltMu7p5L2Mu2JpsiTrackMassFiltered')"
                                     ),
   
    )

LowPtTriggerFlagsEfficiencies = cms.PSet(LowPtTriggerFlagsEfficienciesTag,LowPtTriggerFlagsEfficienciesProbe)

LowPtTriggerFlagsEfficienciesProbe_L2 = cms.PSet(
    ########## Mu + Track ##########
    Mu7p5_Track2_Jpsi_TK = cms.string("!triggerObjectMatchesByCollection('hltL2MuonCandidates').empty()"
                                      #+ "&& triggerObjectMatchesByCollection('hltL2MuonCandidates').at(0).hasFilterLabel('hltMu7p5Track2JpsiTrackMassFiltered')"
                                      ),
    Mu7p5_Track3p5_Jpsi_TK = cms.string("!triggerObjectMatchesByCollection('hltL2MuonCandidates').empty()"
                                        #+ "&& triggerObjectMatchesByCollection('hltL2MuonCandidates').at(0).hasFilterLabel('hltMu7p5Track3p5JpsiTrackMassFiltered')"
                                        ),
    Mu7p5_Track7_Jpsi_TK = cms.string("!triggerObjectMatchesByCollection('hltL2MuonCandidates').empty()"
                                      #+ "&& triggerObjectMatchesByCollection('hltL2MuonCandidates').at(0).hasFilterLabel('hltMu7p5Track7JpsiTrackMassFiltered')"
                                      ),
    ########## Mu + L2Mu ##########
    Mu7p5_L2Mu2_Jpsi_L2 = cms.string("!triggerObjectMatchesByCollection('hltL2MuonCandidates').empty()"
                                     + "&& triggerObjectMatchesByCollection('hltL2MuonCandidates').at(0).hasFilterLabel('hltMu7p5L2Mu2JpsiTrackMassFiltered')"
                                     ),
   
    )
