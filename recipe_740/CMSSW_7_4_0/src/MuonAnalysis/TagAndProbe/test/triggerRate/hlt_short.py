# /frozen/2015/25ns14e33/v2.0/HLT/V2 (CMSSW_7_4_2_HLT3)

import FWCore.ParameterSet.Config as cms

fragment = cms.ProcessFragment( "HLT" )

fragment.HLTConfigVersion = cms.PSet(
  tableName = cms.string('/frozen/2015/25ns14e33/v2.0/HLT/V2')
)

fragment.HLTIter4PSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 6 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
fragment.HLTIter3PSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
fragment.HLTIter2PSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
fragment.HLTIter1PSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.2 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
fragment.HLTPSetbJetRegionalTrajectoryFilter = cms.PSet( 
  minPt = cms.double( 1.0 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 8 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
fragment.HLTPSetTrajectoryFilterL3 = cms.PSet( 
  minPt = cms.double( 0.5 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 1000000000 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
fragment.HLTPSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
fragment.HLTPSetTrajectoryFilterForElectrons = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minPt = cms.double( 2.0 ),
  minHitsMinPt = cms.int32( -1 ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( -1 ),
  maxConsecLostHits = cms.int32( 1 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minimumNumberOfHits = cms.int32( 5 ),
  chargeSignificance = cms.double( -1.0 )
)
fragment.HLTPSetMuonCkfTrajectoryFilter = cms.PSet( 
  minPt = cms.double( 0.9 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( -1 ),
  maxConsecLostHits = cms.int32( 1 ),
  chargeSignificance = cms.double( -1.0 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minimumNumberOfHits = cms.int32( 5 )
)
fragment.HLTPSetMuTrackJpsiTrajectoryFilter = cms.PSet( 
  minPt = cms.double( 10.0 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 8 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
fragment.HLTPSetMuTrackJpsiEffTrajectoryFilter = cms.PSet( 
  minPt = cms.double( 1.0 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 9 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
fragment.HLTPSetCkfTrajectoryFilter = cms.PSet( 
  minPt = cms.double( 0.9 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( -1 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
fragment.HLTPSetCkf3HitTrajectoryFilter = cms.PSet( 
  minPt = cms.double( 0.9 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( -1 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
fragment.HLTIter4PSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter4PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter4ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  minNrOfHitsForRebuild = cms.untracked.int32( 4 )
)
fragment.HLTIter3PSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter3PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter3ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
fragment.HLTIter2PSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter2PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter2ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
fragment.HLTIter1PSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter1PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter1ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
fragment.HLTPSetTrajectoryBuilderForElectrons = cms.PSet( 
  propagatorAlong = cms.string( "hltESPFwdElectronPropagator" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTrajectoryFilterForElectrons" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "hltESPBwdElectronPropagator" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 90.0 )
)
fragment.HLTPSetMuTrackJpsiTrajectoryBuilder = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuTrackJpsiTrajectoryFilter" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
fragment.HLTPSetMuTrackJpsiEffTrajectoryBuilder = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuTrackJpsiEffTrajectoryFilter" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
fragment.HLTPSetMuonCkfTrajectoryBuilder = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryFilter" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "MuonCkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  useSeedLayer = cms.bool( False ),
  deltaEta = cms.double( -1.0 ),
  deltaPhi = cms.double( -1.0 ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  rescaleErrorIfFail = cms.double( 1.0 ),
  propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 )
)
fragment.HLTPSetPvClusterComparer = cms.PSet( 
  track_pt_min = cms.double( 2.5 ),
  track_pt_max = cms.double( 10.0 ),
  track_chi2_max = cms.double( 9999999.0 ),
  track_prob_min = cms.double( -1.0 )
)
fragment.HLTIter0PSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter0PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator9" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
fragment.HLTIter0PSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
fragment.HLTPSetPvClusterComparerForBTag = cms.PSet( 
  track_pt_min = cms.double( 0.1 ),
  track_pt_max = cms.double( 20.0 ),
  track_chi2_max = cms.double( 20.0 ),
  track_prob_min = cms.double( -1.0 )
)
fragment.HLTSeedFromConsecutiveHitsTripletOnlyCreator = cms.PSet( 
  ComponentName = cms.string( "SeedFromConsecutiveHitsTripletOnlyCreator" ),
  propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  SeedMomentumForBOFF = cms.double( 5.0 ),
  OriginTransverseErrorMultiplier = cms.double( 1.0 ),
  MinOneOverPtError = cms.double( 1.0 ),
  magneticField = cms.string( "ParabolicMf" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  forceKinematicWithRegionDirection = cms.bool( False )
)
fragment.HLTSeedFromConsecutiveHitsCreator = cms.PSet( 
  ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
  propagator = cms.string( "PropagatorWithMaterial" ),
  SeedMomentumForBOFF = cms.double( 5.0 ),
  OriginTransverseErrorMultiplier = cms.double( 1.0 ),
  MinOneOverPtError = cms.double( 1.0 ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  forceKinematicWithRegionDirection = cms.bool( False ),
  magneticField = cms.string( "" )
)
fragment.HLTIter0HighPtTkMuPSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter0PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 4 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
fragment.HLTIter2HighPtTkMuPSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter2HighPtTkMuPSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  MeasurementTrackerName = cms.string( "hltIter2HighPtTkMuESPMeasurementTracker" )
)
fragment.HLTIter2HighPtTkMuPSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 3 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
fragment.HLTPSetPvClusterComparerForIT = cms.PSet( 
  track_pt_min = cms.double( 1.0 ),
  track_pt_max = cms.double( 20.0 ),
  track_chi2_max = cms.double( 20.0 ),
  track_prob_min = cms.double( -1.0 )
)
fragment.HLTSiStripClusterChargeCutNone = cms.PSet(  value = cms.double( -1.0 ) )
fragment.HLTSiStripClusterChargeCutLoose = cms.PSet(  value = cms.double( 1620.0 ) )
fragment.HLTSiStripClusterChargeCutTight = cms.PSet(  value = cms.double( 1945.0 ) )
fragment.HLTSeedFromConsecutiveHitsCreatorIT = cms.PSet( 
  ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
  propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  SeedMomentumForBOFF = cms.double( 5.0 ),
  OriginTransverseErrorMultiplier = cms.double( 1.0 ),
  MinOneOverPtError = cms.double( 1.0 ),
  magneticField = cms.string( "ParabolicMf" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  forceKinematicWithRegionDirection = cms.bool( False )
)
fragment.HLTSeedFromProtoTracks = cms.PSet( 
  ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
  propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  SeedMomentumForBOFF = cms.double( 5.0 ),
  MinOneOverPtError = cms.double( 1.0 ),
  magneticField = cms.string( "ParabolicMf" ),
  TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
  OriginTransverseErrorMultiplier = cms.double( 1.0 ),
  forceKinematicWithRegionDirection = cms.bool( False )
)
fragment.streams = cms.PSet( 
  A = cms.vstring( 'HCalNZS',
    'HcalHPDNoise',
    'InitialPD',
    'Templates' ),
  ALCALUMIPIXELS = cms.vstring( 'AlCaLumiPixels' ),
  ALCAPHISYM = cms.vstring( 'AlCaPhiSym' ),
  Calibration = cms.vstring( 'TestEnablesEcalHcalDT' ),
  EcalCalibration = cms.vstring( 'EcalLaser' ),
  Express = cms.vstring( 'Express' ),
  RPCMON = cms.vstring( 'RPCMonitor' )
)
fragment.datasets = cms.PSet( 
  AlCaLumiPixels = cms.vstring( 'AlCa_LumiPixels_Random_v1',
    'AlCa_LumiPixels_ZeroBias_v2' ),
  AlCaPhiSym = cms.vstring( 'AlCa_EcalPhiSym_v2' ),
  EcalLaser = cms.vstring( 'HLT_EcalCalibration_v1' ),
  Express = cms.vstring( 'HLT_HT2000_v1',
    'HLT_HT2500_v1',
    'HLT_MET250_v1',
    'HLT_MET300_v1',
    'HLT_Mu300_v1',
    'HLT_Mu350_v1',
    'HLT_PFMET300_NoiseCleaned_v1',
    'HLT_PFMET400_NoiseCleaned_v1',
    'HLT_Photon500_v1',
    'HLT_Photon600_v1' ),
  HCalNZS = cms.vstring( 'HLT_HcalNZS_v2',
    'HLT_HcalPhiSym_v2',
    'HLT_HcalUTCA_v2' ),
  HcalHPDNoise = cms.vstring( 'HLT_GlobalRunHPDNoise_v2',
    'HLT_L1Tech_HBHEHO_totalOR_v2',
    'HLT_L1Tech_HCAL_HF_single_channel_v2' ),
  InitialPD = ( cms.vstring( 'HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV0p41_v2',
    'HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v2',
    'HLT_AK8PFJet360_TrimMass30_v2',
    'HLT_Activity_Ecal_SC7_v2',
    'HLT_BTagMu_DiJet110_Mu5_v2',
    'HLT_BTagMu_DiJet20_Mu5_v2',
    'HLT_BTagMu_DiJet40_Mu5_v2',
    'HLT_BTagMu_DiJet70_Mu5_v2',
    'HLT_BTagMu_Jet300_Mu5_v2',
    'HLT_CaloJet500_NoJetID_v2',
    'HLT_CaloMET200_NoiseCleaned_v2',
    'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p7_v1',
    'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v1',
    'HLT_DiCentralPFJet55_PFMET110_NoiseCleaned_v1',
    'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v2',
    'HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140_v2',
    'HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu80_v2',
    'HLT_DiPFJetAve100_HFJEC_v2',
    'HLT_DiPFJetAve160_HFJEC_v2',
    'HLT_DiPFJetAve220_HFJEC_v2',
    'HLT_DiPFJetAve300_HFJEC_v2',
    'HLT_DiPFJetAve30_HFJEC_v2',
    'HLT_DiPFJetAve60_HFJEC_v2',
    'HLT_DiPFJetAve80_HFJEC_v2',
    'HLT_Dimuon0_Jpsi_Muon_v2',
    'HLT_Dimuon0_Phi_Barrel_v2',
    'HLT_Dimuon0_Upsilon_Muon_v2',
    'HLT_Dimuon0er16_Jpsi_NoOS_NoVertexing_v2',
    'HLT_Dimuon0er16_Jpsi_NoVertexing_v2',
    'HLT_Dimuon10_Jpsi_Barrel_v2',
    'HLT_Dimuon13_PsiPrime_v2',
    'HLT_Dimuon13_Upsilon_v2',
    'HLT_Dimuon16_Jpsi_v2',
    'HLT_Dimuon20_Jpsi_v2',
    'HLT_Dimuon6_Jpsi_NoVertexing_v2',
    'HLT_Dimuon8_PsiPrime_Barrel_v2',
    'HLT_Dimuon8_Upsilon_Barrel_v2',
    'HLT_Diphoton10_10_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass10_ForMC_v1',
    'HLT_Diphoton30EB_18EB_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55_v1',
    'HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55_v1',
    'HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelSeedMatch_Mass70_v1',
    'HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v1',
    'HLT_Diphoton30_18_Solid_R9Id_AND_IsoCaloId_AND_HE_R9Id_Mass55_v1',
    'HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf_v1',
    'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW_v2',
    'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v2',
    'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300_v2',
    'HLT_DoubleIsoMu17_eta2p1_v2',
    'HLT_DoubleJet90_Double30_DoubleCSV0p5_v2',
    'HLT_DoubleJet90_Double30_TripleCSV0p5_v2',
    'HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v2',
    'HLT_DoubleMu18NoFiltersNoVtx_v2',
    'HLT_DoubleMu23NoFiltersNoVtxDisplaced_v2',
    'HLT_DoubleMu28NoFiltersNoVtxDisplaced_v2',
    'HLT_DoubleMu33NoFiltersNoVtx_v2',
    'HLT_DoubleMu38NoFiltersNoVtx_v2',
    'HLT_DoubleMu4_3_Bs_v2',
    'HLT_DoubleMu4_3_Jpsi_Displaced_v2',
    'HLT_DoubleMu4_JpsiTrk_Displaced_v2',
    'HLT_DoubleMu4_LowMassNonResonantTrk_Displaced_v2',
    'HLT_DoubleMu4_PsiPrimeTrk_Displaced_v2',
    'HLT_DoubleMu8_Mass8_PFHT300_v2',
    'HLT_DoublePhoton85_v2',
    'HLT_ECALHT800_v2',
    'HLT_Ele105_CaloIdVT_GsfTrkIdT_v2',
    'HLT_Ele10_CaloIdM_TrackIdM_CentralPFJet30_BTagCSV0p5PF_v2',
    'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v2',
    'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_v2',
    'HLT_Ele12_CaloIdM_TrackIdM_PFJet30_v2',
    'HLT_Ele15_IsoVVVL_BTagtop8CSV07_PFHT400_v2',
    'HLT_Ele15_IsoVVVL_PFHT350_PFMET70_v1',
    'HLT_Ele15_IsoVVVL_PFHT600_v2',
    'HLT_Ele15_PFHT300_v2',
    'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v2',
    'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v2',
    'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_v2',
    'HLT_Ele18_CaloIdL_TrackIdL_IsoVL_PFJet30_v2',
    'HLT_Ele18_CaloIdM_TrackIdM_PFJet30_v2',
    'HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v1',
    'HLT_Ele22_eta2p1_WPLoose_Gsf_v1',
    'HLT_Ele22_eta2p1_WPTight_Gsf_v1',
    'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v2',
    'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_v2',
    'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v2',
    'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v2',
    'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v2',
    'HLT_Ele25WP60_Ele8_Mass55_v1',
    'HLT_Ele25WP60_SC4_Mass55_v2',
    'HLT_Ele27_eta2p1_WPLoose_Gsf_CentralPFJet30_BTagCSV07_v1',
    'HLT_Ele27_eta2p1_WPLoose_Gsf_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v1',
    'HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v1',
    'HLT_Ele27_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v1',
    'HLT_Ele27_eta2p1_WPLoose_Gsf_TriCentralPFJet30_v1',
    'HLT_Ele27_eta2p1_WPLoose_Gsf_TriCentralPFJet50_40_30_v1',
    'HLT_Ele27_eta2p1_WPLoose_Gsf_v1',
    'HLT_Ele27_eta2p1_WPTight_Gsf_v1',
    'HLT_Ele32_eta2p1_WPLoose_Gsf_CentralPFJet30_BTagCSV07_v1',
    'HLT_Ele32_eta2p1_WPLoose_Gsf_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v1',
    'HLT_Ele32_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v1',
    'HLT_Ele32_eta2p1_WPLoose_Gsf_TriCentralPFJet30_v1',
    'HLT_Ele32_eta2p1_WPLoose_Gsf_TriCentralPFJet50_40_30_v1',
    'HLT_Ele32_eta2p1_WPLoose_Gsf_v1',
    'HLT_Ele32_eta2p1_WPTight_Gsf_v1',
    'HLT_Ele33_CaloIdL_TrackIdL_IsoVL_PFJet30_v2',
    'HLT_Ele33_CaloIdM_TrackIdM_PFJet30_v2',
    'HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v2',
    'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v2',
    'HLT_HT350_DisplacedDijet40_DisplacedTrack_v2',
    'HLT_HT350_DisplacedDijet80_DisplacedTrack_v2',
    'HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v2',
    'HLT_HT500_DisplacedDijet40_Inclusive_v2',
    'HLT_HT550_DisplacedDijet40_Inclusive_v2',
    'HLT_HT650_DisplacedDijet80_Inclusive_v2',
    'HLT_HT750_DisplacedDijet80_Inclusive_v2',
    'HLT_IsoMu16_eta2p1_CaloMET30_LooseIsoPFTau50_Trk30_eta2p1_v2',
    'HLT_IsoMu16_eta2p1_CaloMET30_v2',
    'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1_v2',
    'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v2',
    'HLT_IsoMu17_eta2p1_MediumIsoPFTau40_Trk1_eta2p1_Reg_v2',
    'HLT_IsoMu17_eta2p1_v2',
    'HLT_IsoMu20_eta2p1_CentralPFJet30_BTagCSV07_v2',
    'HLT_IsoMu20_eta2p1_TriCentralPFJet30_v2',
    'HLT_IsoMu20_eta2p1_TriCentralPFJet50_40_30_v2',
    'HLT_IsoMu20_eta2p1_v2',
    'HLT_IsoMu20_v2',
    'HLT_IsoMu24_eta2p1_CentralPFJet30_BTagCSV07_v2',
    'HLT_IsoMu24_eta2p1_LooseIsoPFTau20_v2',
    'HLT_IsoMu24_eta2p1_TriCentralPFJet30_v2',
    'HLT_IsoMu24_eta2p1_TriCentralPFJet50_40_30_v2',
    'HLT_IsoMu24_eta2p1_v2',
    'HLT_IsoMu27_v2',
    'HLT_IsoTkMu20_eta2p1_v2',
    'HLT_IsoTkMu20_v2',
    'HLT_IsoTkMu24_eta2p1_v2',
    'HLT_IsoTkMu27_v2',
    'HLT_IsoTrackHB_v1',
    'HLT_IsoTrackHE_v1',
    'HLT_JetE30_NoBPTX3BX_NoHalo_v2',
    'HLT_JetE30_NoBPTX_v2',
    'HLT_JetE50_NoBPTX3BX_NoHalo_v2',
    'HLT_JetE70_NoBPTX3BX_NoHalo_v2',
    'HLT_L1SingleEG5_OR_EG10_OR_EG20_v2',
    'HLT_L1SingleMuOpen_DT_v2',
    'HLT_L1SingleMuOpen_v2',
    'HLT_L1Tech_DT_GlobalOR_v2',
    'HLT_L1_TripleJet_VBF_v2',
    'HLT_L2DoubleMu23_NoVertex_v2',
    'HLT_L2DoubleMu28_NoVertex_2Cha_Angle2p5_Mass10_v2',
    'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_Mass10_v2',
    'HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v2',
    'HLT_L2Mu10_NoVertex_NoBPTX_v2',
    'HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_v2',
    'HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_NoHalo_v2',
    'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET120_v2',
    'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET80_v2',
    'HLT_LooseIsoPFTau50_Trk30_eta2p1_v2',
    'HLT_MET75_IsoTrk50_v2',
    'HLT_MET90_IsoTrk50_v2',
    'HLT_MonoCentralPFJet80_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v2',
    'HLT_MonoCentralPFJet80_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v2',
    'HLT_Mu10_CentralPFJet30_BTagCSV0p5PF_v2',
    'HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v2',
    'HLT_Mu12_Photon25_CaloIdL_L1ISO_v2',
    'HLT_Mu12_Photon25_CaloIdL_L1OR_v2',
    'HLT_Mu12_Photon25_CaloIdL_v2',
    'HLT_Mu14er_PFMET100_NoiseCleaned_v1',
    'HLT_Mu15_IsoVVVL_BTagCSV07_PFHT400_v2',
    'HLT_Mu15_IsoVVVL_PFHT350_PFMET70_v1',
    'HLT_Mu15_IsoVVVL_PFHT600_v2',
    'HLT_Mu15_PFHT300_v2',
    'HLT_Mu16_TkMu0_dEta18_Onia_v2',
    'HLT_Mu16_TkMu0_dEta18_Phi_v2',
    'HLT_Mu16_eta2p1_CaloMET30_v2',
    'HLT_Mu17_Mu8_DZ_v2',
    'HLT_Mu17_Mu8_SameSign_DPhi_v2',
    'HLT_Mu17_Mu8_SameSign_v2',
    'HLT_Mu17_Photon30_CaloIdL_L1ISO_v2',
    'HLT_Mu17_Photon35_CaloIdL_L1ISO_v2',
    'HLT_Mu17_TkMu8_DZ_v2',
    'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v2',
    'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v2',
    'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v2',
    'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v2',
    'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v2',
    'HLT_Mu17_TrkIsoVVL_v2',
    'HLT_Mu17_v2',
    'HLT_Mu20_v2',
    'HLT_Mu23NoFiltersNoVtx_Photon23_CaloIdL_v2',
    'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v2',
    'HLT_Mu24_TrkIsoVVL_v2',
    'HLT_Mu24_eta2p1_v2',
    'HLT_Mu24_v2',
    'HLT_Mu25_TkMu0_dEta18_Onia_v2',
    'HLT_Mu27_TkMu8_v2',
    'HLT_Mu27_v2',
    'HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v2',
    'HLT_Mu28NoFiltersNoVtx_CentralCaloJet40_v2',
    'HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose_v2',
    'HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL_v2',
    'HLT_Mu30_TkMu11_v2',
    'HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose_v2',
    'HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Tight_v2',
    'HLT_Mu33NoFiltersNoVtxDisplaced_Photon33_CaloIdL_v2',
    'HLT_Mu34_TrkIsoVVL_v2',
    'HLT_Mu34_v2',
    'HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v2',
    'HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight_v2',
    'HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose_v2',
    'HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v2',
    'HLT_Mu3er_PFHT140_PFMET125_NoiseCleaned_v2',
    'HLT_Mu40_TkMu11_v2',
    'HLT_Mu40_eta2p1_PFJet200_PFJet50_v2',
    'HLT_Mu42NoFiltersNoVtx_Photon42_CaloIdL_v2',
    'HLT_Mu45_eta2p1_v2',
    'HLT_Mu50_v2',
    'HLT_Mu6_PFHT200_PFMET100_NoiseCleaned_v1',
    'HLT_Mu6_PFHT200_PFMET80_NoiseCleaned_BTagCSV07_v1',
    'HLT_Mu7p5_L2Mu2_Jpsi_v2',
    'HLT_Mu7p5_L2Mu2_Upsilon_v2',
    'HLT_Mu7p5_Track2_Jpsi_v2',
    'HLT_Mu7p5_Track2_Upsilon_v2',
    'HLT_Mu7p5_Track3p5_Jpsi_v2',
    'HLT_Mu7p5_Track3p5_Upsilon_v2',
    'HLT_Mu7p5_Track7_Jpsi_v2',
    'HLT_Mu7p5_Track7_Upsilon_v2',
    'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v2',
    'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v2',
    'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v2',
    'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v2',
    'HLT_Mu8_TrkIsoVVL_v2',
    'HLT_Mu8_v2',
    'HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63_v1',
    'HLT_PFHT200_v1',
    'HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58_v1',
    'HLT_PFHT250_v1',
    'HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54_v1',
    'HLT_PFHT300_v1',
    'HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53_v1',
    'HLT_PFHT350_PFMET100_NoiseCleaned_v1',
    'HLT_PFHT350_v2',
    'HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52_v1',
    'HLT_PFHT400_SixJet30_BTagCSV0p5_2PFBTagCSV_v2',
    'HLT_PFHT400_SixJet30_v2',
    'HLT_PFHT400_v1',
    'HLT_PFHT450_SixJet40_PFBTagCSV_v2',
    'HLT_PFHT450_SixJet40_v2',
    'HLT_PFHT475_v1',
    'HLT_PFHT550_4Jet_v2',
    'HLT_PFHT600_v2',
    'HLT_PFHT650_4Jet_v2',
    'HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v2',
    'HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v2',
    'HLT_PFHT650_v2',
    'HLT_PFHT750_4JetPt50_v1',
    'HLT_PFHT800_v1')+cms.vstring( 'HLT_PFJet140_v2',
    'HLT_PFJet200_v2',
    'HLT_PFJet260_v2',
    'HLT_PFJet320_v2',
    'HLT_PFJet400_v2',
    'HLT_PFJet40_v2',
    'HLT_PFJet450_v2',
    'HLT_PFJet500_v2',
    'HLT_PFJet60_v2',
    'HLT_PFJet80_v2',
    'HLT_PFMET100_PFMHT100_IDTight_v1',
    'HLT_PFMET110_PFMHT110_IDTight_v1',
    'HLT_PFMET120_NoiseCleaned_BTagCSV07_v2',
    'HLT_PFMET120_NoiseCleaned_Mu5_v2',
    'HLT_PFMET120_PFMHT120_IDTight_v1',
    'HLT_PFMET170_NoiseCleaned_v2',
    'HLT_PFMET90_PFMHT90_IDTight_v1',
    'HLT_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v2',
    'HLT_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v2',
    'HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_PFMET40_v2',
    'HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_VBF_v2',
    'HLT_Photon120_R9Id90_HE10_IsoM_v2',
    'HLT_Photon120_v2',
    'HLT_Photon135_PFMET100_NoiseCleaned_v2',
    'HLT_Photon165_HE10_v2',
    'HLT_Photon165_R9Id90_HE10_IsoM_v2',
    'HLT_Photon175_v2',
    'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_PFMET40_v2',
    'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_VBF_v2',
    'HLT_Photon22_R9Id90_HE10_IsoM_v2',
    'HLT_Photon22_v2',
    'HLT_Photon250_NoHE_v2',
    'HLT_Photon26_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon16_AND_HE10_R9Id65_Eta2_Mass60_v2',
    'HLT_Photon300_NoHE_v2',
    'HLT_Photon30_R9Id90_HE10_IsoM_v2',
    'HLT_Photon30_v2',
    'HLT_Photon36_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon22_AND_HE10_R9Id65_Eta2_Mass15_v2',
    'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_PFMET40_v2',
    'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_VBF_v2',
    'HLT_Photon36_R9Id90_HE10_IsoM_v2',
    'HLT_Photon36_v2',
    'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_PFMET40_v2',
    'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_VBF_v2',
    'HLT_Photon50_R9Id90_HE10_IsoM_v2',
    'HLT_Photon50_v2',
    'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_PFMET40_v2',
    'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_VBF_v2',
    'HLT_Photon75_R9Id90_HE10_IsoM_v2',
    'HLT_Photon75_v2',
    'HLT_Photon90_CaloIdL_PFHT500_v2',
    'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_PFMET40_v2',
    'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_VBF_v2',
    'HLT_Photon90_R9Id90_HE10_IsoM_v2',
    'HLT_Photon90_v2',
    'HLT_Physics_v2',
    'HLT_QuadJet45_DoubleCSV0p5_v2',
    'HLT_QuadJet45_TripleCSV0p5_v2',
    'HLT_QuadMuon0_Dimuon0_Jpsi_v2',
    'HLT_QuadMuon0_Dimuon0_Upsilon_v2',
    'HLT_QuadPFJet_DoubleBTagCSV_VBF_Mqq200_v2',
    'HLT_QuadPFJet_DoubleBTagCSV_VBF_Mqq240_v2',
    'HLT_QuadPFJet_SingleBTagCSV_VBF_Mqq460_v2',
    'HLT_QuadPFJet_SingleBTagCSV_VBF_Mqq500_v2',
    'HLT_QuadPFJet_VBF_v2',
    'HLT_Random_v1',
    'HLT_Rsq0p25_v1',
    'HLT_Rsq0p30_v1',
    'HLT_RsqMR240_Rsq0p09_MR200_4jet_v1',
    'HLT_RsqMR240_Rsq0p09_MR200_v1',
    'HLT_RsqMR270_Rsq0p09_MR200_4jet_v1',
    'HLT_RsqMR270_Rsq0p09_MR200_v1',
    'HLT_TkMu20_v2',
    'HLT_TkMu24_eta2p1_v2',
    'HLT_TkMu27_v2',
    'HLT_TripleMu_12_10_5_v2',
    'HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx_v2',
    'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v2',
    'HLT_VBF_DisplacedJet40_DisplacedTrack_v2',
    'HLT_VBF_DisplacedJet40_Hadronic_v2',
    'HLT_VBF_DisplacedJet40_TightID_DisplacedTrack_v2',
    'HLT_VBF_DisplacedJet40_TightID_Hadronic_v2',
    'HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v2',
    'HLT_VBF_DisplacedJet40_VTightID_Hadronic_v2',
    'HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v2',
    'HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v2',
    'HLT_ZeroBias_v2') ),
  RPCMonitor = cms.vstring( 'AlCa_RPCMuonNoHits_v2',
    'AlCa_RPCMuonNoTriggers_v2',
    'AlCa_RPCMuonNormalisation_v2' ),
  Templates = cms.vstring( 'HLT_AK4CaloJetsForMC_v2',
    'HLT_AK4PFJetsForMC_v2',
    'HLT_AK8CaloHTForMC_v2',
    'HLT_AK8PFHTForMC_v2',
    'HLT_AK8PFJetsForMC_v2',
    'HLT_AK8TrimPFJetsForMC_v2',
    'HLT_CaloHTForMC_v2',
    'HLT_CaloMETCleanedForMC_v2',
    'HLT_CaloMETForMC_v2',
    'HLT_CaloMHTForMC_v2',
    'HLT_DoubleEle5_CaloIdL_GsfTrkIdVL_MW_ForMC_v1',
    'HLT_DoubleGlbTrkMu_TrkIsoVVL_DZ_SaveObjects_v2',
    'HLT_DoubleMuNoFiltersNoVtx_SaveObjects_v2',
    'HLT_DoubleMu_TrkIsoVVL_DZ_SaveObjects_v2',
    'HLT_Ele15_Ele10_CaloIdL_TrackIdL_IsoVL_DZ_ForMC_v1',
    'HLT_Ele5_WPLoose_Gsf_ForMC_v1',
    'HLT_IsoMu_SaveObjects_v2',
    'HLT_IsoTkMu15_SaveObjects_v2',
    'HLT_PFHTForMC_v2',
    'HLT_PFMETForMC_v2',
    'HLT_PFMHTForMC_v2',
    'HLT_ReducedIterativeTracking_v2' ),
  TestEnablesEcalHcalDT = cms.vstring( 'HLT_EcalCalibration_v1',
    'HLT_HcalCalibration_v1' )
)

fragment.hltESSHcalSeverityLevel = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "HcalSeverityLevelComputerRcd" ),
    firstValid = cms.vuint32( 1 )
)
fragment.hltESSEcalSeverityLevel = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "EcalSeverityLevelAlgoRcd" ),
    firstValid = cms.vuint32( 1 )
)
fragment.hltESSBTagRecord = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "JetTagComputerRecord" ),
    firstValid = cms.vuint32( 1 )
)
fragment.CSCINdexerESSource = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "CSCIndexerRecord" ),
    firstValid = cms.vuint32( 1 )
)
fragment.CSCChannelMapperESSource = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "CSCChannelMapperRecord" ),
    firstValid = cms.vuint32( 1 )
)

fragment.hltESPDisplacedDijethltPromptTrackCountingESProducerLong = cms.ESProducer( "PromptTrackCountingESProducer",
  maxImpactParameterSig = cms.double( 999999.0 ),
  deltaR = cms.double( -1.0 ),
  minimumImpactParameter = cms.double( -1.0 ),
  maximumDecayLength = cms.double( 999999.0 ),
  impactParameterType = cms.int32( 1 ),
  trackQualityClass = cms.string( "any" ),
  deltaRmin = cms.double( 0.0 ),
  maxImpactParameter = cms.double( 0.2 ),
  useSignedImpactParameterSig = cms.bool( True ),
  maximumDistanceToJetAxis = cms.double( 999999.0 ),
  nthTrack = cms.int32( -1 )
)
fragment.hltESPDisplacedDijethltPromptTrackCountingESProducer = cms.ESProducer( "PromptTrackCountingESProducer",
  maxImpactParameterSig = cms.double( 999999.0 ),
  deltaR = cms.double( -1.0 ),
  minimumImpactParameter = cms.double( -1.0 ),
  maximumDecayLength = cms.double( 999999.0 ),
  impactParameterType = cms.int32( 1 ),
  trackQualityClass = cms.string( "any" ),
  deltaRmin = cms.double( 0.0 ),
  maxImpactParameter = cms.double( 0.1 ),
  useSignedImpactParameterSig = cms.bool( True ),
  maximumDistanceToJetAxis = cms.double( 999999.0 ),
  nthTrack = cms.int32( -1 )
)
fragment.hltESPDisplacedDijethltTrackCounting2D1st = cms.ESProducer( "TrackCountingESProducer",
  b_pT = cms.double( 0.3684 ),
  deltaR = cms.double( -1.0 ),
  minimumImpactParameter = cms.double( 0.05 ),
  a_dR = cms.double( -0.001053 ),
  min_pT = cms.double( 120.0 ),
  maximumDistanceToJetAxis = cms.double( 9999999.0 ),
  max_pT = cms.double( 500.0 ),
  impactParameterType = cms.int32( 1 ),
  trackQualityClass = cms.string( "any" ),
  useVariableJTA = cms.bool( False ),
  min_pT_dRcut = cms.double( 0.5 ),
  max_pT_trackPTcut = cms.double( 3.0 ),
  max_pT_dRcut = cms.double( 0.1 ),
  b_dR = cms.double( 0.6263 ),
  a_pT = cms.double( 0.005263 ),
  maximumDecayLength = cms.double( 999999.0 ),
  nthTrack = cms.int32( 1 ),
  useSignedImpactParameterSig = cms.bool( False )
)
fragment.hltESPDisplacedDijethltTrackCounting2D2ndLong = cms.ESProducer( "TrackCountingESProducer",
  b_pT = cms.double( 0.3684 ),
  deltaR = cms.double( -1.0 ),
  minimumImpactParameter = cms.double( 0.2 ),
  a_dR = cms.double( -0.001053 ),
  min_pT = cms.double( 120.0 ),
  maximumDistanceToJetAxis = cms.double( 9999999.0 ),
  max_pT = cms.double( 500.0 ),
  impactParameterType = cms.int32( 1 ),
  trackQualityClass = cms.string( "any" ),
  useVariableJTA = cms.bool( False ),
  min_pT_dRcut = cms.double( 0.5 ),
  max_pT_trackPTcut = cms.double( 3.0 ),
  max_pT_dRcut = cms.double( 0.1 ),
  b_dR = cms.double( 0.6263 ),
  a_pT = cms.double( 0.005263 ),
  maximumDecayLength = cms.double( 999999.0 ),
  nthTrack = cms.int32( 2 ),
  useSignedImpactParameterSig = cms.bool( True )
)
fragment.hltESPAK8CaloCorrection = cms.ESProducer( "JetCorrectionESChain",
  correctors = cms.vstring( 'hltESPAK8CaloFastJetCorrectionESProducer',
    'hltESPAK8CaloRelativeCorrectionESProducer',
    'hltESPAK8CaloAbsoluteCorrectionESProducer' )
)
fragment.hltESPAK8CaloFastJetCorrectionESProducer = cms.ESProducer( "L1FastjetCorrectionESProducer",
  srcRho = cms.InputTag( "hltFixedGridRhoFastjetAllCalo" ),
  algorithm = cms.string( "AK8CaloHLT" ),
  level = cms.string( "L1FastJet" )
)
fragment.hltESPAK8CaloRelativeCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK8CaloHLT" ),
  level = cms.string( "L2Relative" )
)
fragment.hltESPAK8CaloAbsoluteCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK8CaloHLT" ),
  level = cms.string( "L3Absolute" )
)
fragment.hltESPAK8PFCorrection = cms.ESProducer( "JetCorrectionESChain",
  correctors = cms.vstring( 'hltESPAK8PFFastJetCorrectionESProducer',
    'hltESPAK8PFRelativeCorrectionESProducer',
    'hltESPAK8PFAbsoluteCorrectionESProducer' )
)
fragment.hltESPAK8PFFastJetCorrectionESProducer = cms.ESProducer( "L1FastjetCorrectionESProducer",
  srcRho = cms.InputTag( "hltFixedGridRhoFastjetAll" ),
  algorithm = cms.string( "AK8PFHLT" ),
  level = cms.string( "L1FastJet" )
)
fragment.hltESPAK8PFRelativeCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK8PFHLT" ),
  level = cms.string( "L2Relative" )
)
fragment.hltESPAK8PFAbsoluteCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK8PFHLT" ),
  level = cms.string( "L3Absolute" )
)
fragment.hltDisplacedDijethltESPTrackCounting2D1st = cms.ESProducer( "TrackCountingESProducer",
  b_pT = cms.double( 0.3684 ),
  deltaR = cms.double( -1.0 ),
  minimumImpactParameter = cms.double( 0.05 ),
  a_dR = cms.double( -0.001053 ),
  min_pT = cms.double( 120.0 ),
  maximumDistanceToJetAxis = cms.double( 9999999.0 ),
  max_pT = cms.double( 500.0 ),
  impactParameterType = cms.int32( 1 ),
  trackQualityClass = cms.string( "any" ),
  useVariableJTA = cms.bool( False ),
  min_pT_dRcut = cms.double( 0.5 ),
  max_pT_trackPTcut = cms.double( 3.0 ),
  max_pT_dRcut = cms.double( 0.1 ),
  b_dR = cms.double( 0.6263 ),
  a_pT = cms.double( 0.005263 ),
  maximumDecayLength = cms.double( 999999.0 ),
  nthTrack = cms.int32( 1 ),
  useSignedImpactParameterSig = cms.bool( False )
)
fragment.hltDisplacedDijethltESPPromptTrackCountingESProducer = cms.ESProducer( "PromptTrackCountingESProducer",
  maxImpactParameterSig = cms.double( 999999.0 ),
  deltaR = cms.double( -1.0 ),
  minimumImpactParameter = cms.double( -1.0 ),
  maximumDecayLength = cms.double( 999999.0 ),
  impactParameterType = cms.int32( 1 ),
  trackQualityClass = cms.string( "any" ),
  deltaRmin = cms.double( 0.0 ),
  maxImpactParameter = cms.double( 0.1 ),
  useSignedImpactParameterSig = cms.bool( True ),
  maximumDistanceToJetAxis = cms.double( 999999.0 ),
  nthTrack = cms.int32( -1 )
)
fragment.hltESPAK4CaloCorrection = cms.ESProducer( "JetCorrectionESChain",
  correctors = cms.vstring( 'hltESPAK4CaloFastJetCorrectionESProducer',
    'hltESPAK4CaloRelativeCorrectionESProducer',
    'hltESPAK4CaloAbsoluteCorrectionESProducer' )
)
fragment.hltESPAK4PFCorrection = cms.ESProducer( "JetCorrectionESChain",
  correctors = cms.vstring( 'hltESPAK4PFFastJetCorrectionESProducer',
    'hltESPAK4PFRelativeCorrectionESProducer',
    'hltESPAK4PFAbsoluteCorrectionESProducer' )
)
fragment.hltESPAK4CaloFastJetCorrectionESProducer = cms.ESProducer( "L1FastjetCorrectionESProducer",
  srcRho = cms.InputTag( "hltFixedGridRhoFastjetAllCalo" ),
  algorithm = cms.string( "AK4CaloHLT" ),
  level = cms.string( "L1FastJet" )
)
fragment.hltESPAK4PFFastJetCorrectionESProducer = cms.ESProducer( "L1FastjetCorrectionESProducer",
  srcRho = cms.InputTag( "hltFixedGridRhoFastjetAll" ),
  algorithm = cms.string( "AK4PFHLT" ),
  level = cms.string( "L1FastJet" )
)
fragment.hltESPAK4PFRelativeCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK4PFHLT" ),
  level = cms.string( "L2Relative" )
)
fragment.hltESPAK4CaloRelativeCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK4CaloHLT" ),
  level = cms.string( "L2Relative" )
)
fragment.hltESPAK4CaloAbsoluteCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK4CaloHLT" ),
  level = cms.string( "L3Absolute" )
)
fragment.hltESPAK4PFAbsoluteCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK4PFHLT" ),
  level = cms.string( "L3Absolute" )
)
fragment.MaterialPropagatorParabolicMF = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialParabolicMf" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
fragment.OppositeMaterialPropagatorParabolicMF = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
fragment.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  version = cms.string( "Parabolic" ),
  parameters = cms.PSet(  BValue = cms.string( "" ) ),
  label = cms.untracked.string( "ParabolicMf" )
)
fragment.hltESPChi2MeasurementEstimator9 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 9.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator9" )
)
fragment.hltESPChi2MeasurementEstimator16 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 16.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator16" )
)
fragment.hltESPChi2MeasurementEstimator30 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 30.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator30" )
)
fragment.hltESPChi2ChargeMeasurementEstimator30 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 30.0 ),
  ComponentName = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  pTChargeCutThreshold = cms.double( -1.0 ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  nSigma = cms.double( 3.0 )
)
fragment.AnyDirectionAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  MaxDPhi = cms.double( 1.6 ),
  ComponentName = cms.string( "AnyDirectionAnalyticalPropagator" ),
  PropagationDirection = cms.string( "anyDirection" )
)
fragment.CSCChannelMapperESProducer = cms.ESProducer( "CSCChannelMapperESProducer",
  AlgoName = cms.string( "CSCChannelMapperPostls1" )
)
fragment.CSCIndexerESProducer = cms.ESProducer( "CSCIndexerESProducer",
  AlgoName = cms.string( "CSCIndexerPostls1" )
)
fragment.CaloTopologyBuilder = cms.ESProducer( "CaloTopologyBuilder" )
fragment.CaloTowerConstituentsMapBuilder = cms.ESProducer( "CaloTowerConstituentsMapBuilder",
  appendToDataLabel = cms.string( "" ),
  MapFile = cms.untracked.string( "Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz" )
)
fragment.CastorDbProducer = cms.ESProducer( "CastorDbProducer",
  appendToDataLabel = cms.string( "" )
)
fragment.ClusterShapeHitFilterESProducer = cms.ESProducer( "ClusterShapeHitFilterESProducer",
  ComponentName = cms.string( "ClusterShapeHitFilter" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  PixelShapeFile = cms.string( "RecoPixelVertexing/PixelLowPtUtilities/data/pixelShape.par" )
)
fragment.hltESPChi2ChargeMeasurementEstimator9 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 9.0 ),
  ComponentName = cms.string( "hltESPChi2ChargeMeasurementEstimator9" ),
  pTChargeCutThreshold = cms.double( 15.0 ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  nSigma = cms.double( 3.0 )
)
fragment.hltESPChi2ChargeMeasurementEstimator16 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 16.0 ),
  ComponentName = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  pTChargeCutThreshold = cms.double( -1.0 ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  nSigma = cms.double( 3.0 )
)
fragment.MaterialPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterial" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
fragment.OppositeMaterialPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialOpposite" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
fragment.SteppingHelixPropagatorAny = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "anyDirection" ),
  useTuningForL2Speed = cms.bool( False ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "SteppingHelixPropagatorAny" )
)
fragment.TransientTrackBuilderESProducer = cms.ESProducer( "TransientTrackBuilderESProducer",
  ComponentName = cms.string( "TransientTrackBuilder" )
)
fragment.caloDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "CaloDetIdAssociator" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 70 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
fragment.cosmicsNavigationSchoolESProducer = cms.ESProducer( "NavigationSchoolESProducer",
  ComponentName = cms.string( "CosmicNavigationSchool" ),
  SimpleMagneticField = cms.string( "" )
)
fragment.ecalDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "EcalDetIdAssociator" ),
  etaBinSize = cms.double( 0.02 ),
  nEta = cms.int32( 300 ),
  nPhi = cms.int32( 360 ),
  includeBadChambers = cms.bool( False )
)
fragment.ecalSeverityLevel = cms.ESProducer( "EcalSeverityLevelESProducer",
  dbstatusMask = cms.PSet( 
    kGood = cms.vstring( 'kOk' ),
    kProblematic = cms.vstring( 'kDAC',
      'kNoLaser',
      'kNoisy',
      'kNNoisy',
      'kNNNoisy',
      'kNNNNoisy',
      'kNNNNNoisy',
      'kFixedG6',
      'kFixedG1',
      'kFixedG0' ),
    kRecovered = cms.vstring(  ),
    kTime = cms.vstring(  ),
    kWeird = cms.vstring(  ),
    kBad = cms.vstring( 'kNonRespondingIsolated',
      'kDeadVFE',
      'kDeadFE',
      'kNoDataNoTP' )
  ),
  timeThresh = cms.double( 2.0 ),
  flagMask = cms.PSet( 
    kGood = cms.vstring( 'kGood' ),
    kProblematic = cms.vstring( 'kPoorReco',
      'kPoorCalib',
      'kNoisy',
      'kSaturated' ),
    kRecovered = cms.vstring( 'kLeadingEdgeRecovered',
      'kTowerRecovered' ),
    kTime = cms.vstring( 'kOutOfTime' ),
    kWeird = cms.vstring( 'kWeird',
      'kDiWeird' ),
    kBad = cms.vstring( 'kFaultyHardware',
      'kDead',
      'kKilled' )
  )
)
fragment.hcalDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "HcalDetIdAssociator" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 70 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
fragment.hcalRecAlgos = cms.ESProducer( "HcalRecAlgoESProducer",
  RecoveredRecHitBits = cms.vstring( 'TimingAddedBit',
    'TimingSubtractedBit' ),
  SeverityLevels = cms.VPSet( 
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 0 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( 'HcalCellCaloTowerProb' ),
      Level = cms.int32( 1 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HSCP_R1R2',
  'HSCP_FracLeader',
  'HSCP_OuterEnergy',
  'HSCP_ExpFit',
  'ADCSaturationBit',
  'HBHEIsolatedNoise',
  'AddedSimHcalNoise' ),
      ChannelStatus = cms.vstring( 'HcalCellExcludeFromHBHENoiseSummary' ),
      Level = cms.int32( 5 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HBHEHpdHitMultiplicity',
  'HBHEPulseShape',
  'HOBit',
  'HFInTimeWindow',
  'ZDCBit',
  'CalibrationBit',
  'TimingErrorBit',
  'HBHETriangleNoise',
  'HBHETS4TS5Noise' ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 8 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HFLongShort',
  'HFPET',
  'HFS8S1Ratio',
  'HFDigiTime' ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 11 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HBHEFlatNoise',
  'HBHESpikeNoise' ),
      ChannelStatus = cms.vstring( 'HcalCellCaloTowerMask' ),
      Level = cms.int32( 12 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( 'HcalCellHot' ),
      Level = cms.int32( 15 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( 'HcalCellOff',
        'HcalCellDead' ),
      Level = cms.int32( 20 )
    )
  ),
  DropChannelStatusBits = cms.vstring( 'HcalCellMask',
    'HcalCellOff',
    'HcalCellDead' )
)
fragment.hltCombinedSecondaryVertex = cms.ESProducer( "CombinedSecondaryVertexESProducer",
  trackPairV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.03 ) ),
  useTrackWeights = cms.bool( True ),
  useCategories = cms.bool( True ),
  pseudoMultiplicityMin = cms.uint32( 2 ),
  categoryVariableName = cms.string( "vertexCategory" ),
  trackSelection = cms.PSet( 
    totalHitsMin = cms.uint32( 0 ),
    jetDeltaRMax = cms.double( 0.3 ),
    qualityClass = cms.string( "any" ),
    pixelHitsMin = cms.uint32( 0 ),
    sip3dSigMin = cms.double( -99999.9 ),
    sip3dSigMax = cms.double( 99999.9 ),
    normChi2Max = cms.double( 99999.9 ),
    maxDistToAxis = cms.double( 0.07 ),
    sip2dValMax = cms.double( 99999.9 ),
    maxDecayLen = cms.double( 5.0 ),
    ptMin = cms.double( 0.0 ),
    sip2dSigMax = cms.double( 99999.9 ),
    sip2dSigMin = cms.double( -99999.9 ),
    sip3dValMax = cms.double( 99999.9 ),
    sip2dValMin = cms.double( -99999.9 ),
    sip3dValMin = cms.double( -99999.9 )
  ),
  calibrationRecords = cms.vstring( 'CombinedSVRecoVertex',
    'CombinedSVPseudoVertex',
    'CombinedSVNoVertex' ),
  correctVertexMass = cms.bool( True ),
  charmCut = cms.double( 1.5 ),
  vertexFlip = cms.bool( False ),
  minimumTrackWeight = cms.double( 0.5 ),
  pseudoVertexV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.05 ) ),
  trackMultiplicityMin = cms.uint32( 3 ),
  trackPseudoSelection = cms.PSet( 
    totalHitsMin = cms.uint32( 0 ),
    jetDeltaRMax = cms.double( 0.3 ),
    qualityClass = cms.string( "any" ),
    pixelHitsMin = cms.uint32( 0 ),
    sip3dSigMin = cms.double( -99999.9 ),
    sip3dSigMax = cms.double( 99999.9 ),
    normChi2Max = cms.double( 99999.9 ),
    maxDistToAxis = cms.double( 0.07 ),
    sip2dValMax = cms.double( 99999.9 ),
    maxDecayLen = cms.double( 5.0 ),
    ptMin = cms.double( 0.0 ),
    sip2dSigMax = cms.double( 99999.9 ),
    sip2dSigMin = cms.double( 2.0 ),
    sip3dValMax = cms.double( 99999.9 ),
    sip2dValMin = cms.double( -99999.9 ),
    sip3dValMin = cms.double( -99999.9 )
  ),
  trackSort = cms.string( "sip2dSig" ),
  trackFlip = cms.bool( False )
)
fragment.hltCombinedSecondaryVertexV2 = cms.ESProducer( "CombinedSecondaryVertexESProducer",
  trackPairV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.03 ) ),
  useTrackWeights = cms.bool( True ),
  useCategories = cms.bool( True ),
  pseudoMultiplicityMin = cms.uint32( 2 ),
  categoryVariableName = cms.string( "vertexCategory" ),
  trackSelection = cms.PSet( 
    b_pT = cms.double( 0.3684 ),
    max_pT = cms.double( 500.0 ),
    useVariableJTA = cms.bool( False ),
    maxDecayLen = cms.double( 5.0 ),
    sip3dValMin = cms.double( -99999.9 ),
    max_pT_dRcut = cms.double( 0.1 ),
    a_pT = cms.double( 0.005263 ),
    totalHitsMin = cms.uint32( 0 ),
    jetDeltaRMax = cms.double( 0.3 ),
    a_dR = cms.double( -0.001053 ),
    maxDistToAxis = cms.double( 0.07 ),
    ptMin = cms.double( 0.0 ),
    qualityClass = cms.string( "any" ),
    pixelHitsMin = cms.uint32( 0 ),
    sip2dValMax = cms.double( 99999.9 ),
    max_pT_trackPTcut = cms.double( 3.0 ),
    sip2dValMin = cms.double( -99999.9 ),
    normChi2Max = cms.double( 99999.9 ),
    sip3dValMax = cms.double( 99999.9 ),
    sip3dSigMin = cms.double( -99999.9 ),
    min_pT = cms.double( 120.0 ),
    min_pT_dRcut = cms.double( 0.5 ),
    sip2dSigMax = cms.double( 99999.9 ),
    sip3dSigMax = cms.double( 99999.9 ),
    sip2dSigMin = cms.double( -99999.9 ),
    b_dR = cms.double( 0.6263 )
  ),
  calibrationRecords = cms.vstring( 'CombinedSVIVFV2RecoVertex',
    'CombinedSVIVFV2PseudoVertex',
    'CombinedSVIVFV2NoVertex' ),
  correctVertexMass = cms.bool( True ),
  charmCut = cms.double( 1.5 ),
  vertexFlip = cms.bool( False ),
  minimumTrackWeight = cms.double( 0.5 ),
  pseudoVertexV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.05 ) ),
  trackMultiplicityMin = cms.uint32( 3 ),
  trackPseudoSelection = cms.PSet( 
    b_pT = cms.double( 0.3684 ),
    max_pT = cms.double( 500.0 ),
    useVariableJTA = cms.bool( False ),
    maxDecayLen = cms.double( 5.0 ),
    sip3dValMin = cms.double( -99999.9 ),
    max_pT_dRcut = cms.double( 0.1 ),
    a_pT = cms.double( 0.005263 ),
    totalHitsMin = cms.uint32( 0 ),
    jetDeltaRMax = cms.double( 0.3 ),
    a_dR = cms.double( -0.001053 ),
    maxDistToAxis = cms.double( 0.07 ),
    ptMin = cms.double( 0.0 ),
    qualityClass = cms.string( "any" ),
    pixelHitsMin = cms.uint32( 0 ),
    sip2dValMax = cms.double( 99999.9 ),
    max_pT_trackPTcut = cms.double( 3.0 ),
    sip2dValMin = cms.double( -99999.9 ),
    normChi2Max = cms.double( 99999.9 ),
    sip3dValMax = cms.double( 99999.9 ),
    sip3dSigMin = cms.double( -99999.9 ),
    min_pT = cms.double( 120.0 ),
    min_pT_dRcut = cms.double( 0.5 ),
    sip2dSigMax = cms.double( 99999.9 ),
    sip3dSigMax = cms.double( 99999.9 ),
    sip2dSigMin = cms.double( 2.0 ),
    b_dR = cms.double( 0.6263 )
  ),
  trackSort = cms.string( "sip2dSig" ),
  trackFlip = cms.bool( False )
)
fragment.hltESPAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  MaxDPhi = cms.double( 1.6 ),
  ComponentName = cms.string( "hltESPAnalyticalPropagator" ),
  PropagationDirection = cms.string( "alongMomentum" )
)
fragment.hltESPBwdAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  MaxDPhi = cms.double( 1.6 ),
  ComponentName = cms.string( "hltESPBwdAnalyticalPropagator" ),
  PropagationDirection = cms.string( "oppositeToMomentum" )
)
fragment.hltESPBwdElectronPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "hltESPBwdElectronPropagator" ),
  Mass = cms.double( 5.11E-4 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
fragment.hltESPCloseComponentsMerger5D = cms.ESProducer( "CloseComponentsMergerESProducer5D",
  ComponentName = cms.string( "hltESPCloseComponentsMerger5D" ),
  MaxComponents = cms.int32( 12 ),
  DistanceMeasure = cms.string( "hltESPKullbackLeiblerDistance5D" )
)
fragment.hltESPDummyDetLayerGeometry = cms.ESProducer( "DetLayerGeometryESProducer",
  ComponentName = cms.string( "hltESPDummyDetLayerGeometry" )
)
fragment.hltESPElectronMaterialEffects = cms.ESProducer( "GsfMaterialEffectsESProducer",
  BetheHeitlerParametrization = cms.string( "BetheHeitler_cdfmom_nC6_O5.par" ),
  EnergyLossUpdator = cms.string( "GsfBetheHeitlerUpdator" ),
  ComponentName = cms.string( "hltESPElectronMaterialEffects" ),
  MultipleScatteringUpdator = cms.string( "MultipleScatteringUpdator" ),
  Mass = cms.double( 5.11E-4 ),
  BetheHeitlerCorrection = cms.int32( 2 )
)
fragment.hltESPFastSteppingHelixPropagatorAny = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "anyDirection" ),
  useTuningForL2Speed = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPFastSteppingHelixPropagatorAny" )
)
fragment.hltESPFastSteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  useTuningForL2Speed = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" )
)
fragment.hltESPFittingSmootherIT = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPTrajectoryFitterRK" ),
  MinNumberOfHits = cms.int32( 3 ),
  Smoother = cms.string( "hltESPTrajectorySmootherRK" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  ComponentName = cms.string( "hltESPFittingSmootherIT" ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  RejectTracks = cms.bool( True )
)
fragment.hltESPFittingSmootherRK = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPTrajectoryFitterRK" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPTrajectorySmootherRK" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  ComponentName = cms.string( "hltESPFittingSmootherRK" ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  RejectTracks = cms.bool( True )
)
fragment.hltESPFwdElectronPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPFwdElectronPropagator" ),
  Mass = cms.double( 5.11E-4 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
fragment.hltESPGlobalDetLayerGeometry = cms.ESProducer( "GlobalDetLayerGeometryESProducer",
  ComponentName = cms.string( "hltESPGlobalDetLayerGeometry" )
)
fragment.hltESPGsfElectronFittingSmoother = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPGsfTrajectoryFitter" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPGsfTrajectorySmoother" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  ComponentName = cms.string( "hltESPGsfElectronFittingSmoother" ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  RejectTracks = cms.bool( True )
)
fragment.hltESPGsfTrajectoryFitter = cms.ESProducer( "GsfTrajectoryFitterESProducer",
  Merger = cms.string( "hltESPCloseComponentsMerger5D" ),
  ComponentName = cms.string( "hltESPGsfTrajectoryFitter" ),
  MaterialEffectsUpdator = cms.string( "hltESPElectronMaterialEffects" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" ),
  GeometricalPropagator = cms.string( "hltESPAnalyticalPropagator" )
)
fragment.hltESPGsfTrajectorySmoother = cms.ESProducer( "GsfTrajectorySmootherESProducer",
  ErrorRescaling = cms.double( 100.0 ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" ),
  Merger = cms.string( "hltESPCloseComponentsMerger5D" ),
  ComponentName = cms.string( "hltESPGsfTrajectorySmoother" ),
  GeometricalPropagator = cms.string( "hltESPBwdAnalyticalPropagator" ),
  MaterialEffectsUpdator = cms.string( "hltESPElectronMaterialEffects" )
)
fragment.hltESPKFFittingSmoother = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPKFTrajectoryFitter" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPKFTrajectorySmoother" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  ComponentName = cms.string( "hltESPKFFittingSmoother" ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  RejectTracks = cms.bool( True )
)
fragment.hltESPKFFittingSmootherForL2Muon = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPKFTrajectoryFitterForL2Muon" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPKFTrajectorySmootherForL2Muon" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  ComponentName = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  RejectTracks = cms.bool( True )
)
fragment.hltESPKFTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectoryFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
fragment.hltESPKFTrajectoryFitterForL2Muon = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectoryFitterForL2Muon" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
fragment.hltESPKFTrajectorySmoother = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmoother" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
fragment.hltESPKFTrajectorySmootherForL2Muon = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmootherForL2Muon" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
fragment.hltESPKFTrajectorySmootherForMuonTrackLoader = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 10.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPSmartPropagatorAnyOpposite" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
fragment.hltESPKFUpdator = cms.ESProducer( "KFUpdatorESProducer",
  ComponentName = cms.string( "hltESPKFUpdator" )
)
fragment.hltESPKullbackLeiblerDistance5D = cms.ESProducer( "DistanceBetweenComponentsESProducer5D",
  ComponentName = cms.string( "hltESPKullbackLeiblerDistance5D" ),
  DistanceMeasure = cms.string( "KullbackLeibler" )
)
fragment.hltESPL3MuKFTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPSmartPropagatorAny" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
fragment.hltESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  UseStripStripQualityDB = cms.bool( True ),
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltESPMeasurementTracker" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  UsePixelModuleQualityDB = cms.bool( True ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  SiStripQualityLabel = cms.string( "" ),
  UseStripModuleQualityDB = cms.bool( True ),
  MaskBadAPVFibers = cms.bool( True )
)
fragment.hltESPMuonTransientTrackingRecHitBuilder = cms.ESProducer( "MuonTransientTrackingRecHitBuilderESProducer",
  ComponentName = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" )
)
fragment.hltESPPixelCPEGeneric = cms.ESProducer( "PixelCPEGenericESProducer",
  useLAAlignmentOffsets = cms.bool( False ),
  DoCosmics = cms.bool( False ),
  eff_charge_cut_highX = cms.double( 1.0 ),
  eff_charge_cut_highY = cms.double( 1.0 ),
  inflate_all_errors_no_trk_angle = cms.bool( False ),
  eff_charge_cut_lowY = cms.double( 0.0 ),
  eff_charge_cut_lowX = cms.double( 0.0 ),
  UseErrorsFromTemplates = cms.bool( True ),
  TruncatePixelCharge = cms.bool( True ),
  size_cutY = cms.double( 3.0 ),
  size_cutX = cms.double( 3.0 ),
  useLAWidthFromDB = cms.bool( False ),
  inflate_errors = cms.bool( False ),
  Alpha2Order = cms.bool( True ),
  ClusterProbComputationFlag = cms.int32( 0 ),
  PixelErrorParametrization = cms.string( "NOTcmsim" ),
  EdgeClusterErrorX = cms.double( 50.0 ),
  EdgeClusterErrorY = cms.double( 85.0 ),
  LoadTemplatesFromDB = cms.bool( True ),
  ComponentName = cms.string( "hltESPPixelCPEGeneric" ),
  IrradiationBiasCorrection = cms.bool( False )
)
fragment.hltESPRungeKuttaTrackerPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( True )
)
fragment.hltESPSmartPropagator = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
  MuonPropagator = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagator" )
)
fragment.hltESPSmartPropagatorAny = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagatorAny" )
)
fragment.hltESPSmartPropagatorAnyOpposite = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterialOpposite" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagatorAnyOpposite" )
)
fragment.hltESPSoftLeptonByDistance = cms.ESProducer( "LeptonTaggerByDistanceESProducer",
  distance = cms.double( 0.5 )
)
fragment.hltESPSteppingHelixPropagatorAlong = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "alongMomentum" ),
  useTuningForL2Speed = cms.bool( False ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPSteppingHelixPropagatorAlong" )
)
fragment.hltESPSteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  useTuningForL2Speed = cms.bool( False ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPSteppingHelixPropagatorOpposite" )
)
fragment.hltESPStripCPEfromTrackAngle = cms.ESProducer( "StripCPEESProducer",
  ComponentType = cms.string( "StripCPEfromTrackAngle" ),
  ComponentName = cms.string( "hltESPStripCPEfromTrackAngle" ),
  parameters = cms.PSet( 
    mLC_P2 = cms.double( 0.3 ),
    mLC_P1 = cms.double( 0.618 ),
    mLC_P0 = cms.double( -0.326 ),
    useLegacyError = cms.bool( False ),
    mTEC_P1 = cms.double( 0.471 ),
    mTEC_P0 = cms.double( -1.885 ),
    mTOB_P0 = cms.double( -1.026 ),
    mTOB_P1 = cms.double( 0.253 ),
    mTIB_P0 = cms.double( -0.742 ),
    mTIB_P1 = cms.double( 0.202 ),
    mTID_P0 = cms.double( -1.427 ),
    mTID_P1 = cms.double( 0.433 ),
    maxChgOneMIP = cms.double( 6000.0 )
  )
)
fragment.hltESPTTRHBWithTrackAngle = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBWithTrackAngle" )
)
fragment.hltESPTTRHBuilderPixelOnly = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "Fake" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBuilderPixelOnly" )
)
fragment.hltESPTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.5 ),
  ValidHitBonus = cms.double( 100.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 0.0 ),
  allowSharedFirstHit = cms.bool( False )
)
fragment.hltESPTrajectoryFitterRK = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPTrajectoryFitterRK" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
fragment.hltESPTrajectorySmootherRK = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPTrajectorySmootherRK" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
fragment.hoDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "HODetIdAssociator" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 30 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
fragment.muonDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "MuonDetIdAssociator" ),
  etaBinSize = cms.double( 0.125 ),
  nEta = cms.int32( 48 ),
  nPhi = cms.int32( 48 ),
  includeBadChambers = cms.bool( False )
)
fragment.navigationSchoolESProducer = cms.ESProducer( "NavigationSchoolESProducer",
  ComponentName = cms.string( "SimpleNavigationSchool" ),
  SimpleMagneticField = cms.string( "ParabolicMf" )
)
fragment.preshowerDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "PreshowerDetIdAssociator" ),
  etaBinSize = cms.double( 0.1 ),
  nEta = cms.int32( 60 ),
  nPhi = cms.int32( 30 ),
  includeBadChambers = cms.bool( False )
)
fragment.siPixelQualityESProducer = cms.ESProducer( "SiPixelQualityESProducer",
  ListOfRecordToMerge = cms.VPSet( 
    cms.PSet(  record = cms.string( "SiPixelQualityFromDbRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiPixelDetVOffRcd" ),
      tag = cms.string( "" )
    )
  )
)
fragment.siPixelTemplateDBObjectESProducer = cms.ESProducer( "SiPixelTemplateDBObjectESProducer" )
fragment.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer( "SiStripBackPlaneCorrectionDepESProducer",
  LatencyRecord = cms.PSet( 
    record = cms.string( "SiStripLatencyRcd" ),
    label = cms.untracked.string( "" )
  ),
  BackPlaneCorrectionDeconvMode = cms.PSet( 
    record = cms.string( "SiStripBackPlaneCorrectionRcd" ),
    label = cms.untracked.string( "deconvolution" )
  ),
  BackPlaneCorrectionPeakMode = cms.PSet( 
    record = cms.string( "SiStripBackPlaneCorrectionRcd" ),
    label = cms.untracked.string( "peak" )
  )
)
fragment.siStripLorentzAngleDepESProducer = cms.ESProducer( "SiStripLorentzAngleDepESProducer",
  LatencyRecord = cms.PSet( 
    record = cms.string( "SiStripLatencyRcd" ),
    label = cms.untracked.string( "" )
  ),
  LorentzAngleDeconvMode = cms.PSet( 
    record = cms.string( "SiStripLorentzAngleRcd" ),
    label = cms.untracked.string( "deconvolution" )
  ),
  LorentzAnglePeakMode = cms.PSet( 
    record = cms.string( "SiStripLorentzAngleRcd" ),
    label = cms.untracked.string( "peak" )
  )
)

fragment.hltTriggerType = cms.EDFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 1 )
)
fragment.hltGtDigis = cms.EDProducer( "L1GlobalTriggerRawToDigi",
    DaqGtFedId = cms.untracked.int32( 813 ),
    Verbosity = cms.untracked.int32( 0 ),
    UnpackBxInEvent = cms.int32( 5 ),
    ActiveBoardsMask = cms.uint32( 0xffff ),
    DaqGtInputTag = cms.InputTag( "rawDataCollector" )
)
fragment.hltCaloStage1Digis = cms.EDProducer( "L1TRawToDigi",
    FWId = cms.untracked.int32( 2 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    Setup = cms.string( "stage1::CaloSetup" ),
    FedId = cms.int32( 1352 )
)
fragment.hltCaloStage1LegacyFormatDigis = cms.EDProducer( "L1TCaloUpgradeToGCTConverter",
    InputHFCountsCollection = cms.InputTag( 'hltCaloStage1Digis','HFBitCounts' ),
    InputHFSumsCollection = cms.InputTag( 'hltCaloStage1Digis','HFRingSums' ),
    InputRlxTauCollection = cms.InputTag( 'hltCaloStage1Digis','rlxTaus' ),
    InputIsoTauCollection = cms.InputTag( 'hltCaloStage1Digis','isoTaus' ),
    InputCollection = cms.InputTag( "hltCaloStage1Digis" )
)
fragment.hltL1GtObjectMap = cms.EDProducer( "L1GlobalTrigger",
    TechnicalTriggersUnprescaled = cms.bool( True ),
    ProduceL1GtObjectMapRecord = cms.bool( True ),
    AlgorithmTriggersUnmasked = cms.bool( False ),
    EmulateBxInEvent = cms.int32( 1 ),
    AlgorithmTriggersUnprescaled = cms.bool( True ),
    ProduceL1GtDaqRecord = cms.bool( False ),
    ReadTechnicalTriggerRecords = cms.bool( True ),
    RecordLength = cms.vint32( 3, 0 ),
    TechnicalTriggersUnmasked = cms.bool( False ),
    ProduceL1GtEvmRecord = cms.bool( False ),
    GmtInputTag = cms.InputTag( "hltGtDigis" ),
    TechnicalTriggersVetoUnmasked = cms.bool( True ),
    AlternativeNrBxBoardEvm = cms.uint32( 0 ),
    TechnicalTriggersInputTags = cms.VInputTag( 'simBscDigis' ),
    CastorInputTag = cms.InputTag( "castorL1Digis" ),
    GctInputTag = cms.InputTag( "hltCaloStage1LegacyFormatDigis" ),
    AlternativeNrBxBoardDaq = cms.uint32( 0 ),
    WritePsbL1GtDaqRecord = cms.bool( False ),
    BstLengthBytes = cms.int32( -1 )
)
fragment.hltL1extraParticles = cms.EDProducer( "L1ExtraParticlesProd",
    tauJetSource = cms.InputTag( 'hltCaloStage1LegacyFormatDigis','tauJets' ),
    etHadSource = cms.InputTag( "hltCaloStage1LegacyFormatDigis" ),
    isoTauJetSource = cms.InputTag( 'hltCaloStage1LegacyFormatDigis','isoTauJets' ),
    etTotalSource = cms.InputTag( "hltCaloStage1LegacyFormatDigis" ),
    centralBxOnly = cms.bool( True ),
    centralJetSource = cms.InputTag( 'hltCaloStage1LegacyFormatDigis','cenJets' ),
    etMissSource = cms.InputTag( "hltCaloStage1LegacyFormatDigis" ),
    hfRingEtSumsSource = cms.InputTag( "hltCaloStage1LegacyFormatDigis" ),
    produceMuonParticles = cms.bool( True ),
    forwardJetSource = cms.InputTag( 'hltCaloStage1LegacyFormatDigis','forJets' ),
    ignoreHtMiss = cms.bool( False ),
    htMissSource = cms.InputTag( "hltCaloStage1LegacyFormatDigis" ),
    produceCaloParticles = cms.bool( True ),
    muonSource = cms.InputTag( "hltGtDigis" ),
    isolatedEmSource = cms.InputTag( 'hltCaloStage1LegacyFormatDigis','isoEm' ),
    nonIsolatedEmSource = cms.InputTag( 'hltCaloStage1LegacyFormatDigis','nonIsoEm' ),
    hfRingBitCountsSource = cms.InputTag( "hltCaloStage1LegacyFormatDigis" )
)
fragment.hltScalersRawToDigi = cms.EDProducer( "ScalersRawToDigi",
    scalersInputTag = cms.InputTag( "rawDataCollector" )
)
fragment.hltOnlineBeamSpot = cms.EDProducer( "BeamSpotOnlineProducer",
    maxZ = cms.double( 40.0 ),
    src = cms.InputTag( "hltScalersRawToDigi" ),
    gtEvmLabel = cms.InputTag( "" ),
    changeToCMSCoordinates = cms.bool( False ),
    setSigmaZ = cms.double( 0.0 ),
    maxRadius = cms.double( 2.0 )
)
fragment.hltL1sMu5 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu5" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
fragment.hltPreMu7p5Track2Jpsi = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
fragment.hltL1fMu7p5TrackFiltered0 = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sMu5" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
fragment.hltMuonDTDigis = cms.EDProducer( "DTUnpackingModule",
    useStandardFEDid = cms.bool( True ),
    maxFEDid = cms.untracked.int32( 779 ),
    inputLabel = cms.InputTag( "rawDataCollector" ),
    minFEDid = cms.untracked.int32( 770 ),
    dataType = cms.string( "DDU" ),
    readOutParameters = cms.PSet( 
      debug = cms.untracked.bool( False ),
      rosParameters = cms.PSet( 
        writeSC = cms.untracked.bool( True ),
        readingDDU = cms.untracked.bool( True ),
        performDataIntegrityMonitor = cms.untracked.bool( False ),
        readDDUIDfromDDU = cms.untracked.bool( True ),
        debug = cms.untracked.bool( False ),
        localDAQ = cms.untracked.bool( False )
      ),
      localDAQ = cms.untracked.bool( False ),
      performDataIntegrityMonitor = cms.untracked.bool( False )
    ),
    dqmOnly = cms.bool( False )
)
fragment.hltDt1DRecHits = cms.EDProducer( "DTRecHitProducer",
    debug = cms.untracked.bool( False ),
    recAlgoConfig = cms.PSet( 
      tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
      minTime = cms.double( -3.0 ),
      stepTwoFromDigi = cms.bool( False ),
      doVdriftCorr = cms.bool( True ),
      debug = cms.untracked.bool( False ),
      maxTime = cms.double( 420.0 ),
      tTrigModeConfig = cms.PSet( 
        vPropWire = cms.double( 24.4 ),
        doTOFCorrection = cms.bool( True ),
        tofCorrType = cms.int32( 0 ),
        wirePropCorrType = cms.int32( 0 ),
        tTrigLabel = cms.string( "" ),
        doWirePropCorrection = cms.bool( True ),
        doT0Correction = cms.bool( True ),
        debug = cms.untracked.bool( False )
      ),
      useUncertDB = cms.bool( True )
    ),
    dtDigiLabel = cms.InputTag( "hltMuonDTDigis" ),
    recAlgo = cms.string( "DTLinearDriftFromDBAlgo" )
)
fragment.hltDt4DSegments = cms.EDProducer( "DTRecSegment4DProducer",
    debug = cms.untracked.bool( False ),
    Reco4DAlgoName = cms.string( "DTCombinatorialPatternReco4D" ),
    recHits2DLabel = cms.InputTag( "dt2DSegments" ),
    recHits1DLabel = cms.InputTag( "hltDt1DRecHits" ),
    Reco4DAlgoConfig = cms.PSet( 
      segmCleanerMode = cms.int32( 2 ),
      Reco2DAlgoName = cms.string( "DTCombinatorialPatternReco" ),
      recAlgoConfig = cms.PSet( 
        tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
        minTime = cms.double( -3.0 ),
        stepTwoFromDigi = cms.bool( False ),
        doVdriftCorr = cms.bool( True ),
        debug = cms.untracked.bool( False ),
        maxTime = cms.double( 420.0 ),
        tTrigModeConfig = cms.PSet( 
          vPropWire = cms.double( 24.4 ),
          doTOFCorrection = cms.bool( True ),
          tofCorrType = cms.int32( 0 ),
          wirePropCorrType = cms.int32( 0 ),
          tTrigLabel = cms.string( "" ),
          doWirePropCorrection = cms.bool( True ),
          doT0Correction = cms.bool( True ),
          debug = cms.untracked.bool( False )
        ),
        useUncertDB = cms.bool( True )
      ),
      nSharedHitsMax = cms.int32( 2 ),
      hit_afterT0_resolution = cms.double( 0.03 ),
      Reco2DAlgoConfig = cms.PSet( 
        segmCleanerMode = cms.int32( 2 ),
        recAlgoConfig = cms.PSet( 
          tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
          minTime = cms.double( -3.0 ),
          stepTwoFromDigi = cms.bool( False ),
          doVdriftCorr = cms.bool( True ),
          debug = cms.untracked.bool( False ),
          maxTime = cms.double( 420.0 ),
          tTrigModeConfig = cms.PSet( 
            vPropWire = cms.double( 24.4 ),
            doTOFCorrection = cms.bool( True ),
            tofCorrType = cms.int32( 0 ),
            wirePropCorrType = cms.int32( 0 ),
            tTrigLabel = cms.string( "" ),
            doWirePropCorrection = cms.bool( True ),
            doT0Correction = cms.bool( True ),
            debug = cms.untracked.bool( False )
          ),
          useUncertDB = cms.bool( True )
        ),
        nSharedHitsMax = cms.int32( 2 ),
        AlphaMaxPhi = cms.double( 1.0 ),
        hit_afterT0_resolution = cms.double( 0.03 ),
        MaxAllowedHits = cms.uint32( 50 ),
        performT0_vdriftSegCorrection = cms.bool( False ),
        AlphaMaxTheta = cms.double( 0.9 ),
        debug = cms.untracked.bool( False ),
        recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
        nUnSharedHitsMin = cms.int32( 2 ),
        performT0SegCorrection = cms.bool( False ),
        perform_delta_rejecting = cms.bool( False )
      ),
      performT0_vdriftSegCorrection = cms.bool( False ),
      debug = cms.untracked.bool( False ),
      recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
      nUnSharedHitsMin = cms.int32( 2 ),
      AllDTRecHits = cms.bool( True ),
      performT0SegCorrection = cms.bool( False ),
      perform_delta_rejecting = cms.bool( False )
    )
)
fragment.hltMuonCSCDigis = cms.EDProducer( "CSCDCCUnpacker",
    PrintEventNumber = cms.untracked.bool( False ),
    SuppressZeroLCT = cms.untracked.bool( True ),
    UseExaminer = cms.bool( True ),
    Debug = cms.untracked.bool( False ),
    ErrorMask = cms.uint32( 0x0 ),
    InputObjects = cms.InputTag( "rawDataCollector" ),
    ExaminerMask = cms.uint32( 0x1febf3f6 ),
    runDQM = cms.untracked.bool( False ),
    UnpackStatusDigis = cms.bool( False ),
    VisualFEDInspect = cms.untracked.bool( False ),
    FormatedEventDump = cms.untracked.bool( False ),
    UseFormatStatus = cms.bool( True ),
    UseSelectiveUnpacking = cms.bool( True ),
    VisualFEDShort = cms.untracked.bool( False )
)
fragment.hltCsc2DRecHits = cms.EDProducer( "CSCRecHitDProducer",
    XTasymmetry_ME1b = cms.double( 0.0 ),
    XTasymmetry_ME1a = cms.double( 0.0 ),
    ConstSyst_ME1a = cms.double( 0.022 ),
    ConstSyst_ME1b = cms.double( 0.007 ),
    XTasymmetry_ME41 = cms.double( 0.0 ),
    CSCStripxtalksOffset = cms.double( 0.03 ),
    CSCUseCalibrations = cms.bool( True ),
    CSCUseTimingCorrections = cms.bool( True ),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32( 2 ),
    XTasymmetry_ME22 = cms.double( 0.0 ),
    UseFivePoleFit = cms.bool( True ),
    XTasymmetry_ME21 = cms.double( 0.0 ),
    ConstSyst_ME21 = cms.double( 0.0 ),
    CSCDebug = cms.untracked.bool( False ),
    ConstSyst_ME22 = cms.double( 0.0 ),
    CSCUseGasGainCorrections = cms.bool( False ),
    XTasymmetry_ME31 = cms.double( 0.0 ),
    readBadChambers = cms.bool( True ),
    NoiseLevel_ME13 = cms.double( 8.0 ),
    NoiseLevel_ME12 = cms.double( 9.0 ),
    NoiseLevel_ME32 = cms.double( 9.0 ),
    NoiseLevel_ME31 = cms.double( 9.0 ),
    XTasymmetry_ME32 = cms.double( 0.0 ),
    ConstSyst_ME41 = cms.double( 0.0 ),
    CSCStripClusterSize = cms.untracked.int32( 3 ),
    CSCStripClusterChargeCut = cms.double( 25.0 ),
    CSCStripPeakThreshold = cms.double( 10.0 ),
    readBadChannels = cms.bool( False ),
    UseParabolaFit = cms.bool( False ),
    XTasymmetry_ME13 = cms.double( 0.0 ),
    XTasymmetry_ME12 = cms.double( 0.0 ),
    wireDigiTag = cms.InputTag( 'hltMuonCSCDigis','MuonCSCWireDigi' ),
    ConstSyst_ME12 = cms.double( 0.0 ),
    ConstSyst_ME13 = cms.double( 0.0 ),
    ConstSyst_ME32 = cms.double( 0.0 ),
    ConstSyst_ME31 = cms.double( 0.0 ),
    UseAverageTime = cms.bool( False ),
    NoiseLevel_ME1a = cms.double( 7.0 ),
    NoiseLevel_ME1b = cms.double( 8.0 ),
    CSCWireClusterDeltaT = cms.int32( 1 ),
    CSCUseStaticPedestals = cms.bool( False ),
    stripDigiTag = cms.InputTag( 'hltMuonCSCDigis','MuonCSCStripDigi' ),
    CSCstripWireDeltaTime = cms.int32( 8 ),
    NoiseLevel_ME21 = cms.double( 9.0 ),
    NoiseLevel_ME22 = cms.double( 9.0 ),
    NoiseLevel_ME41 = cms.double( 9.0 )
)
fragment.hltCscSegments = cms.EDProducer( "CSCSegmentProducer",
    inputObjects = cms.InputTag( "hltCsc2DRecHits" ),
    algo_psets = cms.VPSet( 
      cms.PSet(  chamber_types = cms.vstring( 'ME1/a',
  'ME1/b',
  'ME1/2',
  'ME1/3',
  'ME2/1',
  'ME2/2',
  'ME3/1',
  'ME3/2',
  'ME4/1',
  'ME4/2' ),
        algo_name = cms.string( "CSCSegAlgoST" ),
        parameters_per_chamber_type = cms.vint32( 2, 1, 1, 1, 1, 1, 1, 1, 1, 1 ),
        algo_psets = cms.VPSet( 
          cms.PSet(  maxRatioResidualPrune = cms.double( 3.0 ),
            yweightPenalty = cms.double( 1.5 ),
            maxRecHitsInCluster = cms.int32( 20 ),
            dPhiFineMax = cms.double( 0.025 ),
            preClusteringUseChaining = cms.bool( True ),
            ForceCovariance = cms.bool( False ),
            hitDropLimit6Hits = cms.double( 0.3333 ),
            NormChi2Cut2D = cms.double( 20.0 ),
            BPMinImprovement = cms.double( 10000.0 ),
            Covariance = cms.double( 0.0 ),
            tanPhiMax = cms.double( 0.5 ),
            SeedBig = cms.double( 0.0015 ),
            onlyBestSegment = cms.bool( False ),
            dRPhiFineMax = cms.double( 8.0 ),
            SeedSmall = cms.double( 2.0E-4 ),
            curvePenalty = cms.double( 2.0 ),
            dXclusBoxMax = cms.double( 4.0 ),
            BrutePruning = cms.bool( True ),
            curvePenaltyThreshold = cms.double( 0.85 ),
            CorrectTheErrors = cms.bool( True ),
            hitDropLimit4Hits = cms.double( 0.6 ),
            useShowering = cms.bool( False ),
            CSCDebug = cms.untracked.bool( False ),
            tanThetaMax = cms.double( 1.2 ),
            NormChi2Cut3D = cms.double( 10.0 ),
            minHitsPerSegment = cms.int32( 3 ),
            ForceCovarianceAll = cms.bool( False ),
            yweightPenaltyThreshold = cms.double( 1.0 ),
            prePrunLimit = cms.double( 3.17 ),
            hitDropLimit5Hits = cms.double( 0.8 ),
            preClustering = cms.bool( True ),
            prePrun = cms.bool( True ),
            maxDPhi = cms.double( 999.0 ),
            maxDTheta = cms.double( 999.0 ),
            Pruning = cms.bool( True ),
            dYclusBoxMax = cms.double( 8.0 )
          ),
          cms.PSet(  maxRatioResidualPrune = cms.double( 3.0 ),
            yweightPenalty = cms.double( 1.5 ),
            maxRecHitsInCluster = cms.int32( 24 ),
            dPhiFineMax = cms.double( 0.025 ),
            preClusteringUseChaining = cms.bool( True ),
            ForceCovariance = cms.bool( False ),
            hitDropLimit6Hits = cms.double( 0.3333 ),
            NormChi2Cut2D = cms.double( 20.0 ),
            BPMinImprovement = cms.double( 10000.0 ),
            Covariance = cms.double( 0.0 ),
            tanPhiMax = cms.double( 0.5 ),
            SeedBig = cms.double( 0.0015 ),
            onlyBestSegment = cms.bool( False ),
            dRPhiFineMax = cms.double( 8.0 ),
            SeedSmall = cms.double( 2.0E-4 ),
            curvePenalty = cms.double( 2.0 ),
            dXclusBoxMax = cms.double( 4.0 ),
            BrutePruning = cms.bool( True ),
            curvePenaltyThreshold = cms.double( 0.85 ),
            CorrectTheErrors = cms.bool( True ),
            hitDropLimit4Hits = cms.double( 0.6 ),
            useShowering = cms.bool( False ),
            CSCDebug = cms.untracked.bool( False ),
            tanThetaMax = cms.double( 1.2 ),
            NormChi2Cut3D = cms.double( 10.0 ),
            minHitsPerSegment = cms.int32( 3 ),
            ForceCovarianceAll = cms.bool( False ),
            yweightPenaltyThreshold = cms.double( 1.0 ),
            prePrunLimit = cms.double( 3.17 ),
            hitDropLimit5Hits = cms.double( 0.8 ),
            preClustering = cms.bool( True ),
            prePrun = cms.bool( True ),
            maxDPhi = cms.double( 999.0 ),
            maxDTheta = cms.double( 999.0 ),
            Pruning = cms.bool( True ),
            dYclusBoxMax = cms.double( 8.0 )
          )
        )
      )
    ),
    algo_type = cms.int32( 1 )
)
fragment.hltMuonRPCDigis = cms.EDProducer( "RPCUnpackingModule",
    InputLabel = cms.InputTag( "rawDataCollector" ),
    doSynchro = cms.bool( False )
)
fragment.hltRpcRecHits = cms.EDProducer( "RPCRecHitProducer",
    recAlgoConfig = cms.PSet(  ),
    deadvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCDeadVec.dat" ),
    rpcDigiLabel = cms.InputTag( "hltMuonRPCDigis" ),
    maskvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCMaskVec.dat" ),
    recAlgo = cms.string( "RPCRecHitStandardAlgo" ),
    deadSource = cms.string( "File" ),
    maskSource = cms.string( "File" )
)
fragment.hltL2OfflineMuonSeeds = cms.EDProducer( "MuonSeedGenerator",
    SMB_21 = cms.vdouble( 1.043, -0.124, 0.0, 0.183, 0.0, 0.0 ),
    SMB_20 = cms.vdouble( 1.011, -0.052, 0.0, 0.188, 0.0, 0.0 ),
    SMB_22 = cms.vdouble( 1.474, -0.758, 0.0, 0.185, 0.0, 0.0 ),
    OL_2213 = cms.vdouble( 0.117, 0.0, 0.0, 0.044, 0.0, 0.0 ),
    SME_11 = cms.vdouble( 3.295, -1.527, 0.112, 0.378, 0.02, 0.0 ),
    SME_13 = cms.vdouble( -1.286, 1.711, 0.0, 0.356, 0.0, 0.0 ),
    SME_12 = cms.vdouble( 0.102, 0.599, 0.0, 0.38, 0.0, 0.0 ),
    DT_34_2_scale = cms.vdouble( -11.901897, 0.0 ),
    OL_1213_0_scale = cms.vdouble( -4.488158, 0.0 ),
    OL_1222_0_scale = cms.vdouble( -5.810449, 0.0 ),
    DT_13 = cms.vdouble( 0.315, 0.068, -0.127, 0.051, -0.002, 0.0 ),
    DT_12 = cms.vdouble( 0.183, 0.054, -0.087, 0.028, 0.002, 0.0 ),
    DT_14 = cms.vdouble( 0.359, 0.052, -0.107, 0.072, -0.004, 0.0 ),
    CSC_13_3_scale = cms.vdouble( -1.701268, 0.0 ),
    DT_24_2_scale = cms.vdouble( -6.63094, 0.0 ),
    CSC_23 = cms.vdouble( -0.081, 0.113, -0.029, 0.015, 0.008, 0.0 ),
    CSC_24 = cms.vdouble( 0.004, 0.021, -0.002, 0.053, 0.0, 0.0 ),
    OL_2222 = cms.vdouble( 0.107, 0.0, 0.0, 0.04, 0.0, 0.0 ),
    DT_14_2_scale = cms.vdouble( -4.808546, 0.0 ),
    SMB_10 = cms.vdouble( 1.387, -0.038, 0.0, 0.19, 0.0, 0.0 ),
    SMB_11 = cms.vdouble( 1.247, 0.72, -0.802, 0.229, -0.075, 0.0 ),
    SMB_12 = cms.vdouble( 2.128, -0.956, 0.0, 0.199, 0.0, 0.0 ),
    SME_21 = cms.vdouble( -0.529, 1.194, -0.358, 0.472, 0.086, 0.0 ),
    SME_22 = cms.vdouble( -1.207, 1.491, -0.251, 0.189, 0.243, 0.0 ),
    DT_13_2_scale = cms.vdouble( -4.257687, 0.0 ),
    CSC_34 = cms.vdouble( 0.062, -0.067, 0.019, 0.021, 0.003, 0.0 ),
    SME_22_0_scale = cms.vdouble( -3.457901, 0.0 ),
    DT_24_1_scale = cms.vdouble( -7.490909, 0.0 ),
    OL_1232_0_scale = cms.vdouble( -5.964634, 0.0 ),
    DT_23_1_scale = cms.vdouble( -5.320346, 0.0 ),
    SME_13_0_scale = cms.vdouble( 0.104905, 0.0 ),
    SMB_22_0_scale = cms.vdouble( 1.346681, 0.0 ),
    CSC_12_1_scale = cms.vdouble( -6.434242, 0.0 ),
    DT_34 = cms.vdouble( 0.044, 0.004, -0.013, 0.029, 0.003, 0.0 ),
    SME_32 = cms.vdouble( -0.901, 1.333, -0.47, 0.41, 0.073, 0.0 ),
    SME_31 = cms.vdouble( -1.594, 1.482, -0.317, 0.487, 0.097, 0.0 ),
    CSC_13_2_scale = cms.vdouble( -6.077936, 0.0 ),
    crackEtas = cms.vdouble( 0.2, 1.6, 1.7 ),
    SME_11_0_scale = cms.vdouble( 1.325085, 0.0 ),
    SMB_20_0_scale = cms.vdouble( 1.486168, 0.0 ),
    DT_13_1_scale = cms.vdouble( -4.520923, 0.0 ),
    CSC_24_1_scale = cms.vdouble( -6.055701, 0.0 ),
    CSC_01_1_scale = cms.vdouble( -1.915329, 0.0 ),
    DT_23 = cms.vdouble( 0.13, 0.023, -0.057, 0.028, 0.004, 0.0 ),
    DT_24 = cms.vdouble( 0.176, 0.014, -0.051, 0.051, 0.003, 0.0 ),
    SMB_12_0_scale = cms.vdouble( 2.283221, 0.0 ),
    deltaPhiSearchWindow = cms.double( 0.25 ),
    SMB_30_0_scale = cms.vdouble( -3.629838, 0.0 ),
    SME_42 = cms.vdouble( -0.003, 0.005, 0.005, 0.608, 0.076, 0.0 ),
    SME_41 = cms.vdouble( -0.003, 0.005, 0.005, 0.608, 0.076, 0.0 ),
    deltaEtaSearchWindow = cms.double( 0.2 ),
    CSC_12_2_scale = cms.vdouble( -1.63622, 0.0 ),
    DT_34_1_scale = cms.vdouble( -13.783765, 0.0 ),
    CSC_34_1_scale = cms.vdouble( -11.520507, 0.0 ),
    OL_2213_0_scale = cms.vdouble( -7.239789, 0.0 ),
    SMB_32_0_scale = cms.vdouble( -3.054156, 0.0 ),
    CSC_12_3_scale = cms.vdouble( -1.63622, 0.0 ),
    deltaEtaCrackSearchWindow = cms.double( 0.25 ),
    SME_21_0_scale = cms.vdouble( -0.040862, 0.0 ),
    OL_1232 = cms.vdouble( 0.184, 0.0, 0.0, 0.066, 0.0, 0.0 ),
    DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
    SMB_10_0_scale = cms.vdouble( 2.448566, 0.0 ),
    EnableDTMeasurement = cms.bool( True ),
    CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
    CSC_23_2_scale = cms.vdouble( -6.079917, 0.0 ),
    scaleDT = cms.bool( True ),
    DT_12_2_scale = cms.vdouble( -3.518165, 0.0 ),
    OL_1222 = cms.vdouble( 0.848, -0.591, 0.0, 0.062, 0.0, 0.0 ),
    CSC_23_1_scale = cms.vdouble( -19.084285, 0.0 ),
    OL_1213 = cms.vdouble( 0.96, -0.737, 0.0, 0.052, 0.0, 0.0 ),
    CSC_02 = cms.vdouble( 0.612, -0.207, 0.0, 0.067, -0.001, 0.0 ),
    CSC_03 = cms.vdouble( 0.787, -0.338, 0.029, 0.101, -0.008, 0.0 ),
    CSC_01 = cms.vdouble( 0.166, 0.0, 0.0, 0.031, 0.0, 0.0 ),
    SMB_32 = cms.vdouble( 0.67, -0.327, 0.0, 0.22, 0.0, 0.0 ),
    SMB_30 = cms.vdouble( 0.505, -0.022, 0.0, 0.215, 0.0, 0.0 ),
    SMB_31 = cms.vdouble( 0.549, -0.145, 0.0, 0.207, 0.0, 0.0 ),
    crackWindow = cms.double( 0.04 ),
    CSC_14_3_scale = cms.vdouble( -1.969563, 0.0 ),
    SMB_31_0_scale = cms.vdouble( -3.323768, 0.0 ),
    DT_12_1_scale = cms.vdouble( -3.692398, 0.0 ),
    SMB_21_0_scale = cms.vdouble( 1.58384, 0.0 ),
    DT_23_2_scale = cms.vdouble( -5.117625, 0.0 ),
    SME_12_0_scale = cms.vdouble( 2.279181, 0.0 ),
    DT_14_1_scale = cms.vdouble( -5.644816, 0.0 ),
    beamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    SMB_11_0_scale = cms.vdouble( 2.56363, 0.0 ),
    EnableCSCMeasurement = cms.bool( True ),
    CSC_14 = cms.vdouble( 0.606, -0.181, -0.002, 0.111, -0.003, 0.0 ),
    OL_2222_0_scale = cms.vdouble( -7.667231, 0.0 ),
    CSC_13 = cms.vdouble( 0.901, -1.302, 0.533, 0.045, 0.005, 0.0 ),
    CSC_12 = cms.vdouble( -0.161, 0.254, -0.047, 0.042, -0.007, 0.0 )
)
fragment.hltL2MuonSeeds = cms.EDProducer( "L2MuonSeedGenerator",
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'SteppingHelixPropagatorAny' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    InputObjects = cms.InputTag( "hltL1extraParticles" ),
    L1MaxEta = cms.double( 2.5 ),
    OfflineSeedLabel = cms.untracked.InputTag( "hltL2OfflineMuonSeeds" ),
    L1MinPt = cms.double( 0.0 ),
    L1MinQuality = cms.uint32( 1 ),
    GMTReadoutCollection = cms.InputTag( "hltGtDigis" ),
    UseUnassociatedL1 = cms.bool( False ),
    UseOfflineSeed = cms.untracked.bool( True ),
    Propagator = cms.string( "SteppingHelixPropagatorAny" )
)
fragment.hltL2Muons = cms.EDProducer( "L2MuonProducer",
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny',
        'hltESPFastSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    InputObjects = cms.InputTag( "hltL2MuonSeeds" ),
    SeedTransformerParameters = cms.PSet( 
      Fitter = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      NMinRecHits = cms.uint32( 2 ),
      UseSubRecHits = cms.bool( False ),
      Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      RescaleError = cms.double( 100.0 )
    ),
    L2TrajBuilderParameters = cms.PSet( 
      DoRefit = cms.bool( False ),
      SeedPropagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      FilterParameters = cms.PSet( 
        NumberOfSigma = cms.double( 3.0 ),
        FitDirection = cms.string( "insideOut" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        MaxChi2 = cms.double( 1000.0 ),
        MuonTrajectoryUpdatorParameters = cms.PSet( 
          MaxChi2 = cms.double( 25.0 ),
          RescaleErrorFactor = cms.double( 100.0 ),
          Granularity = cms.int32( 0 ),
          ExcludeRPCFromFit = cms.bool( False ),
          UseInvalidHits = cms.bool( True ),
          RescaleError = cms.bool( False )
        ),
        EnableRPCMeasurement = cms.bool( True ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        EnableDTMeasurement = cms.bool( True ),
        RPCRecSegmentLabel = cms.InputTag( "hltRpcRecHits" ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        EnableCSCMeasurement = cms.bool( True )
      ),
      NavigationType = cms.string( "Standard" ),
      SeedTransformerParameters = cms.PSet( 
        Fitter = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        NMinRecHits = cms.uint32( 2 ),
        UseSubRecHits = cms.bool( False ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        RescaleError = cms.double( 100.0 )
      ),
      DoBackwardFilter = cms.bool( True ),
      SeedPosition = cms.string( "in" ),
      BWFilterParameters = cms.PSet( 
        NumberOfSigma = cms.double( 3.0 ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        FitDirection = cms.string( "outsideIn" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        MaxChi2 = cms.double( 100.0 ),
        MuonTrajectoryUpdatorParameters = cms.PSet( 
          MaxChi2 = cms.double( 25.0 ),
          RescaleErrorFactor = cms.double( 100.0 ),
          Granularity = cms.int32( 0 ),
          ExcludeRPCFromFit = cms.bool( False ),
          UseInvalidHits = cms.bool( True ),
          RescaleError = cms.bool( False )
        ),
        EnableRPCMeasurement = cms.bool( True ),
        BWSeedType = cms.string( "fromGenerator" ),
        EnableDTMeasurement = cms.bool( True ),
        RPCRecSegmentLabel = cms.InputTag( "hltRpcRecHits" ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        EnableCSCMeasurement = cms.bool( True )
      ),
      DoSeedRefit = cms.bool( False )
    ),
    DoSeedRefit = cms.bool( False ),
    TrackLoaderParameters = cms.PSet( 
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      DoSmoothing = cms.bool( False ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        BeamSpotPosition = cms.vdouble( 0.0, 0.0, 0.0 ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
    ),
    MuonTrajectoryBuilder = cms.string( "Exhaustive" )
)
fragment.hltL2MuonCandidates = cms.EDProducer( "L2MuonCandidateProducer",
    InputObjects = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
fragment.hltL2fMu7p5TrackL2Filtered7 = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltL1fMu7p5TrackFiltered0" ),
    MinPt = cms.double( 7.0 ),
    MinN = cms.int32( 1 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
fragment.hltSiPixelDigis = cms.EDProducer( "SiPixelRawToDigi",
    UseQualityInfo = cms.bool( False ),
    UsePilotBlade = cms.bool( False ),
    UsePhase1 = cms.bool( False ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    IncludeErrors = cms.bool( False ),
    ErrorList = cms.vint32(  ),
    Regions = cms.PSet(  ),
    Timing = cms.untracked.bool( False ),
    UserErrorList = cms.vint32(  )
)
fragment.hltSiPixelClusters = cms.EDProducer( "SiPixelClusterProducer",
    src = cms.InputTag( "hltSiPixelDigis" ),
    ChannelThreshold = cms.int32( 1000 ),
    maxNumberOfClusters = cms.int32( 20000 ),
    VCaltoElectronGain = cms.int32( 65 ),
    MissCalibrate = cms.untracked.bool( True ),
    SplitClusters = cms.bool( False ),
    VCaltoElectronOffset = cms.int32( -414 ),
    payloadType = cms.string( "HLT" ),
    SeedThreshold = cms.int32( 1000 ),
    ClusterThreshold = cms.double( 4000.0 )
)
fragment.hltSiPixelClustersCache = cms.EDProducer( "SiPixelClusterShapeCacheProducer",
    src = cms.InputTag( "hltSiPixelClusters" ),
    onDemand = cms.bool( False )
)
fragment.hltSiPixelRecHits = cms.EDProducer( "SiPixelRecHitConverter",
    VerboseLevel = cms.untracked.int32( 0 ),
    src = cms.InputTag( "hltSiPixelClusters" ),
    CPE = cms.string( "hltESPPixelCPEGeneric" )
)
fragment.hltSiStripExcludedFEDListProducer = cms.EDProducer( "SiStripExcludedFEDListProducer",
    ProductLabel = cms.InputTag( "rawDataCollector" )
)
fragment.hltSiStripRawToClustersFacility = cms.EDProducer( "SiStripClusterizerFromRaw",
    ProductLabel = cms.InputTag( "rawDataCollector" ),
    DoAPVEmulatorCheck = cms.bool( False ),
    Algorithms = cms.PSet( 
      SiStripFedZeroSuppressionMode = cms.uint32( 4 ),
      CommonModeNoiseSubtractionMode = cms.string( "Median" ),
      PedestalSubtractionFedMode = cms.bool( True ),
      TruncateInSuppressor = cms.bool( True ),
      doAPVRestore = cms.bool( False ),
      useCMMeanMap = cms.bool( False )
    ),
    Clusterizer = cms.PSet( 
      ChannelThreshold = cms.double( 2.0 ),
      MaxSequentialBad = cms.uint32( 1 ),
      MaxSequentialHoles = cms.uint32( 0 ),
      Algorithm = cms.string( "ThreeThresholdAlgorithm" ),
      MaxAdjacentBad = cms.uint32( 0 ),
      QualityLabel = cms.string( "" ),
      SeedThreshold = cms.double( 3.0 ),
      ClusterThreshold = cms.double( 5.0 ),
      setDetId = cms.bool( True ),
      RemoveApvShots = cms.bool( True ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) )
    ),
    onDemand = cms.bool( True )
)
fragment.hltSiStripClusters = cms.EDProducer( "MeasurementTrackerEventProducer",
    inactivePixelDetectorLabels = cms.VInputTag(  ),
    stripClusterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
    pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
    switchOffPixelsIfEmpty = cms.bool( True ),
    inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
    skipClusters = cms.InputTag( "" ),
    measurementTracker = cms.string( "hltESPMeasurementTracker" )
)
fragment.hltL3TrajSeedOIState = cms.EDProducer( "TSGFromL2Muon",
    TkSeedGenerator = cms.PSet( 
      propagatorCompatibleName = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
      option = cms.uint32( 3 ),
      maxChi2 = cms.double( 40.0 ),
      errorMatrixPset = cms.PSet( 
        atIP = cms.bool( True ),
        action = cms.string( "use" ),
        errorMatrixValuesPSet = cms.PSet( 
          pf3_V12 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V13 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V11 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V14 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V15 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          yAxis = cms.vdouble( 0.0, 1.0, 1.4, 10.0 ),
          pf3_V33 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          zAxis = cms.vdouble( -3.14159, 3.14159 ),
          pf3_V44 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          xAxis = cms.vdouble( 0.0, 13.0, 30.0, 70.0, 1000.0 ),
          pf3_V22 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V23 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V45 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V55 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V34 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V35 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V25 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V24 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          )
        )
      ),
      propagatorName = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
      manySeeds = cms.bool( False ),
      copyMuonRecHit = cms.bool( False ),
      ComponentName = cms.string( "TSGForRoadSearch" ),
      MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" )
    ),
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPSteppingHelixPropagatorOpposite',
        'hltESPSteppingHelixPropagatorAlong' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
    MuonTrackingRegionBuilder = cms.PSet(  ),
    PCut = cms.double( 2.5 ),
    TrackerSeedCleaner = cms.PSet(  ),
    PtCut = cms.double( 1.0 )
)
fragment.hltL3TrackCandidateFromL2OIState = cms.EDProducer( "CkfTrajectoryMaker",
    src = cms.InputTag( "hltL3TrajSeedOIState" ),
    reverseTrajectories = cms.bool( True ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    trackCandidateAlso = cms.bool( True ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" ),
    maxNSeeds = cms.uint32( 100000 )
)
fragment.hltL3TkTracksFromL2OIState = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltL3TrackCandidateFromL2OIState" ),
    SimpleMagneticField = cms.string( "" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIterX" ),
    alias = cms.untracked.string( "" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( False ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
fragment.hltL3MuonsOIState = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    L3TrajBuilderParameters = cms.PSet( 
      ScaleTECyFactor = cms.double( -1.0 ),
      GlbRefitterParameters = cms.PSet( 
        TrackerSkipSection = cms.int32( -1 ),
        DoPredictionsOnly = cms.bool( False ),
        PropDirForCosmics = cms.bool( False ),
        HitThreshold = cms.int32( 1 ),
        MuonHitsOption = cms.int32( 1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        TrackerSkipSystem = cms.int32( -1 ),
        DYTthrs = cms.vint32( 30, 15 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      MuonTrackingRegionBuilder = cms.PSet( 
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        OnDemand = cms.double( -1.0 ),
        Rescale_Dz = cms.double( 3.0 ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Rescale_phi = cms.double( 3.0 ),
        Eta_fixed = cms.double( 0.2 ),
        DeltaZ_Region = cms.double( 15.9 ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        Eta_min = cms.double( 0.05 ),
        Phi_fixed = cms.double( 0.2 ),
        DeltaR = cms.double( 0.2 ),
        EscapePt = cms.double( 1.5 ),
        UseFixedRegion = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        Rescale_eta = cms.double( 3.0 ),
        Phi_min = cms.double( 0.05 ),
        UseVertex = cms.bool( False ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
      ),
      RefitRPCHits = cms.bool( True ),
      PCut = cms.double( 2.5 ),
      TrackTransformer = cms.PSet( 
        DoPredictionsOnly = cms.bool( False ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" )
      ),
      GlobalMuonTrackMatcher = cms.PSet( 
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        MinP = cms.double( 2.5 ),
        MinPt = cms.double( 1.0 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        LocChi2Cut = cms.double( 0.001 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_3 = cms.double( 7.0 ),
        Quality_2 = cms.double( 15.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        Quality_1 = cms.double( 20.0 )
      ),
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2OIState" ),
      tkTrajBeamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      tkTrajMaxChi2 = cms.double( 9999.0 ),
      tkTrajMaxDXYBeamSpot = cms.double( 0.2 ),
      tkTrajVertex = cms.InputTag( "pixelVertices" ),
      tkTrajUseVertex = cms.bool( False )
    ),
    TrackLoaderParameters = cms.PSet( 
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      SmoothTkTrack = cms.untracked.bool( False ),
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( False ),
      DoSmoothing = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
fragment.hltL3TrajSeedOIHit = cms.EDProducer( "TSGFromL2Muon",
    TkSeedGenerator = cms.PSet( 
      PSetNames = cms.vstring( 'skipTSG',
        'iterativeTSG' ),
      L3TkCollectionA = cms.InputTag( "hltL3MuonsOIState" ),
      iterativeTSG = cms.PSet( 
        ErrorRescaling = cms.double( 3.0 ),
        beamSpot = cms.InputTag( "unused" ),
        MaxChi2 = cms.double( 40.0 ),
        errorMatrixPset = cms.PSet( 
          atIP = cms.bool( True ),
          action = cms.string( "use" ),
          errorMatrixValuesPSet = cms.PSet( 
            pf3_V12 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V13 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V11 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            pf3_V14 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V15 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            yAxis = cms.vdouble( 0.0, 1.0, 1.4, 10.0 ),
            pf3_V33 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            zAxis = cms.vdouble( -3.14159, 3.14159 ),
            pf3_V44 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            xAxis = cms.vdouble( 0.0, 13.0, 30.0, 70.0, 1000.0 ),
            pf3_V22 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            pf3_V23 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V45 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V55 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            pf3_V34 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V35 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V25 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V24 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            )
          )
        ),
        UpdateState = cms.bool( True ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        SelectState = cms.bool( False ),
        SigmaZ = cms.double( 25.0 ),
        ResetMethod = cms.string( "matrix" ),
        ComponentName = cms.string( "TSGFromPropagation" ),
        UseVertexState = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAnyOpposite" ),
        MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" )
      ),
      skipTSG = cms.PSet(  ),
      ComponentName = cms.string( "DualByL2TSG" )
    ),
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'PropagatorWithMaterial',
        'hltESPSmartPropagatorAnyOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
    MuonTrackingRegionBuilder = cms.PSet(  ),
    PCut = cms.double( 2.5 ),
    TrackerSeedCleaner = cms.PSet( 
      cleanerFromSharedHits = cms.bool( True ),
      ptCleaner = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      directionCleaner = cms.bool( True )
    ),
    PtCut = cms.double( 1.0 )
)
fragment.hltL3TrackCandidateFromL2OIHit = cms.EDProducer( "CkfTrajectoryMaker",
    src = cms.InputTag( "hltL3TrajSeedOIHit" ),
    reverseTrajectories = cms.bool( True ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    trackCandidateAlso = cms.bool( True ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" ),
    maxNSeeds = cms.uint32( 100000 )
)
fragment.hltL3TkTracksFromL2OIHit = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltL3TrackCandidateFromL2OIHit" ),
    SimpleMagneticField = cms.string( "" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIterX" ),
    alias = cms.untracked.string( "" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( False ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
fragment.hltL3MuonsOIHit = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    L3TrajBuilderParameters = cms.PSet( 
      ScaleTECyFactor = cms.double( -1.0 ),
      GlbRefitterParameters = cms.PSet( 
        TrackerSkipSection = cms.int32( -1 ),
        DoPredictionsOnly = cms.bool( False ),
        PropDirForCosmics = cms.bool( False ),
        HitThreshold = cms.int32( 1 ),
        MuonHitsOption = cms.int32( 1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        TrackerSkipSystem = cms.int32( -1 ),
        DYTthrs = cms.vint32( 30, 15 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      MuonTrackingRegionBuilder = cms.PSet( 
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        OnDemand = cms.double( -1.0 ),
        Rescale_Dz = cms.double( 3.0 ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Rescale_phi = cms.double( 3.0 ),
        Eta_fixed = cms.double( 0.2 ),
        DeltaZ_Region = cms.double( 15.9 ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        Eta_min = cms.double( 0.05 ),
        Phi_fixed = cms.double( 0.2 ),
        DeltaR = cms.double( 0.2 ),
        EscapePt = cms.double( 1.5 ),
        UseFixedRegion = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        Rescale_eta = cms.double( 3.0 ),
        Phi_min = cms.double( 0.05 ),
        UseVertex = cms.bool( False ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
      ),
      RefitRPCHits = cms.bool( True ),
      PCut = cms.double( 2.5 ),
      TrackTransformer = cms.PSet( 
        DoPredictionsOnly = cms.bool( False ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" )
      ),
      GlobalMuonTrackMatcher = cms.PSet( 
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        MinP = cms.double( 2.5 ),
        MinPt = cms.double( 1.0 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        LocChi2Cut = cms.double( 0.001 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_3 = cms.double( 7.0 ),
        Quality_2 = cms.double( 15.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        Quality_1 = cms.double( 20.0 )
      ),
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2OIHit" ),
      tkTrajBeamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      tkTrajMaxChi2 = cms.double( 9999.0 ),
      tkTrajMaxDXYBeamSpot = cms.double( 0.2 ),
      tkTrajVertex = cms.InputTag( "pixelVertices" ),
      tkTrajUseVertex = cms.bool( False )
    ),
    TrackLoaderParameters = cms.PSet( 
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      SmoothTkTrack = cms.untracked.bool( False ),
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( False ),
      DoSmoothing = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
fragment.hltL3TkFromL2OICombination = cms.EDProducer( "L3TrackCombiner",
    labels = cms.VInputTag( 'hltL3MuonsOIState','hltL3MuonsOIHit' )
)
fragment.hltPixelLayerTriplets = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.0036 )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.006 )
    ),
    TIB = cms.PSet(  )
)
fragment.hltPixelLayerPairs = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix2+BPix3',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix1+FPix2_pos',
      'BPix1+FPix2_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'BPix2+FPix2_pos',
      'BPix2+FPix2_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.0036 )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.006 )
    ),
    TIB = cms.PSet(  )
)
fragment.hltMixedLayerPairs = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix2+BPix3',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix1+FPix2_pos',
      'BPix1+FPix2_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'BPix2+FPix2_pos',
      'BPix2+FPix2_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg',
      'FPix2_pos+TEC1_pos',
      'FPix2_pos+TEC2_pos',
      'TEC1_pos+TEC2_pos',
      'TEC2_pos+TEC3_pos',
      'FPix2_neg+TEC1_neg',
      'FPix2_neg+TEC2_neg',
      'TEC1_neg+TEC2_neg',
      'TEC2_neg+TEC3_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet( 
      useRingSlector = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      minRing = cms.int32( 1 ),
      maxRing = cms.int32( 1 ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) )
    ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.0036 )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.006 )
    ),
    TIB = cms.PSet(  )
)
fragment.hltL3TrajSeedIOHit = cms.EDProducer( "TSGFromL2Muon",
    TkSeedGenerator = cms.PSet( 
      PSetNames = cms.vstring( 'skipTSG',
        'iterativeTSG' ),
      L3TkCollectionA = cms.InputTag( "hltL3TkFromL2OICombination" ),
      iterativeTSG = cms.PSet( 
        firstTSG = cms.PSet( 
          ComponentName = cms.string( "TSGFromOrderedHits" ),
          OrderedHitsFactoryPSet = cms.PSet( 
            ComponentName = cms.string( "StandardHitTripletGenerator" ),
            GeneratorPSet = cms.PSet( 
              useBending = cms.bool( True ),
              useFixedPreFiltering = cms.bool( False ),
              maxElement = cms.uint32( 0 ),
              phiPreFiltering = cms.double( 0.3 ),
              extraHitRPhitolerance = cms.double( 0.06 ),
              useMultScattering = cms.bool( True ),
              ComponentName = cms.string( "PixelTripletHLTGenerator" ),
              extraHitRZtolerance = cms.double( 0.06 ),
              SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) )
            ),
            SeedingLayers = cms.InputTag( "hltPixelLayerTriplets" )
          ),
          TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
          SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromConsecutiveHitsCreator" ) )
        ),
        PSetNames = cms.vstring( 'firstTSG',
          'secondTSG' ),
        ComponentName = cms.string( "CombinedTSG" ),
        thirdTSG = cms.PSet( 
          PSetNames = cms.vstring( 'endcapTSG',
            'barrelTSG' ),
          barrelTSG = cms.PSet(  ),
          endcapTSG = cms.PSet( 
            ComponentName = cms.string( "TSGFromOrderedHits" ),
            OrderedHitsFactoryPSet = cms.PSet( 
              maxElement = cms.uint32( 0 ),
              ComponentName = cms.string( "StandardHitPairGenerator" ),
              useOnDemandTracker = cms.untracked.int32( 0 ),
              SeedingLayers = cms.InputTag( "hltMixedLayerPairs" )
            ),
            TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
          ),
          etaSeparation = cms.double( 2.0 ),
          ComponentName = cms.string( "DualByEtaTSG" ),
          SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromConsecutiveHitsCreator" ) )
        ),
        secondTSG = cms.PSet( 
          ComponentName = cms.string( "TSGFromOrderedHits" ),
          OrderedHitsFactoryPSet = cms.PSet( 
            maxElement = cms.uint32( 0 ),
            ComponentName = cms.string( "StandardHitPairGenerator" ),
            useOnDemandTracker = cms.untracked.int32( 0 ),
            SeedingLayers = cms.InputTag( "hltPixelLayerPairs" )
          ),
          TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
          SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromConsecutiveHitsCreator" ) )
        )
      ),
      skipTSG = cms.PSet(  ),
      ComponentName = cms.string( "DualByL2TSG" )
    ),
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'PropagatorWithMaterial' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
    MuonTrackingRegionBuilder = cms.PSet( 
      EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
      EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
      OnDemand = cms.double( -1.0 ),
      Rescale_Dz = cms.double( 3.0 ),
      vertexCollection = cms.InputTag( "pixelVertices" ),
      Rescale_phi = cms.double( 3.0 ),
      Eta_fixed = cms.double( 0.2 ),
      DeltaZ_Region = cms.double( 15.9 ),
      MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
      PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
      Eta_min = cms.double( 0.1 ),
      Phi_fixed = cms.double( 0.2 ),
      DeltaR = cms.double( 0.2 ),
      EscapePt = cms.double( 1.5 ),
      UseFixedRegion = cms.bool( False ),
      PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
      Rescale_eta = cms.double( 3.0 ),
      Phi_min = cms.double( 0.1 ),
      UseVertex = cms.bool( False ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
    ),
    PCut = cms.double( 2.5 ),
    TrackerSeedCleaner = cms.PSet( 
      cleanerFromSharedHits = cms.bool( True ),
      ptCleaner = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      directionCleaner = cms.bool( True )
    ),
    PtCut = cms.double( 1.0 )
)
fragment.hltL3TrackCandidateFromL2IOHit = cms.EDProducer( "CkfTrajectoryMaker",
    src = cms.InputTag( "hltL3TrajSeedIOHit" ),
    reverseTrajectories = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    trackCandidateAlso = cms.bool( True ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" ),
    maxNSeeds = cms.uint32( 100000 )
)
fragment.hltL3TkTracksFromL2IOHit = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltL3TrackCandidateFromL2IOHit" ),
    SimpleMagneticField = cms.string( "" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIterX" ),
    alias = cms.untracked.string( "" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( False ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
fragment.hltL3MuonsIOHit = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    L3TrajBuilderParameters = cms.PSet( 
      ScaleTECyFactor = cms.double( -1.0 ),
      GlbRefitterParameters = cms.PSet( 
        TrackerSkipSection = cms.int32( -1 ),
        DoPredictionsOnly = cms.bool( False ),
        PropDirForCosmics = cms.bool( False ),
        HitThreshold = cms.int32( 1 ),
        MuonHitsOption = cms.int32( 1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        TrackerSkipSystem = cms.int32( -1 ),
        DYTthrs = cms.vint32( 30, 15 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      MuonTrackingRegionBuilder = cms.PSet( 
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        OnDemand = cms.double( -1.0 ),
        Rescale_Dz = cms.double( 3.0 ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Rescale_phi = cms.double( 3.0 ),
        Eta_fixed = cms.double( 0.2 ),
        DeltaZ_Region = cms.double( 15.9 ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        Eta_min = cms.double( 0.05 ),
        Phi_fixed = cms.double( 0.2 ),
        DeltaR = cms.double( 0.2 ),
        EscapePt = cms.double( 1.5 ),
        UseFixedRegion = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        Rescale_eta = cms.double( 3.0 ),
        Phi_min = cms.double( 0.05 ),
        UseVertex = cms.bool( False ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
      ),
      RefitRPCHits = cms.bool( True ),
      PCut = cms.double( 2.5 ),
      TrackTransformer = cms.PSet( 
        DoPredictionsOnly = cms.bool( False ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" )
      ),
      GlobalMuonTrackMatcher = cms.PSet( 
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        MinP = cms.double( 2.5 ),
        MinPt = cms.double( 1.0 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        LocChi2Cut = cms.double( 0.001 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_3 = cms.double( 7.0 ),
        Quality_2 = cms.double( 15.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        Quality_1 = cms.double( 20.0 )
      ),
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2IOHit" ),
      tkTrajBeamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      tkTrajMaxChi2 = cms.double( 9999.0 ),
      tkTrajMaxDXYBeamSpot = cms.double( 0.2 ),
      tkTrajVertex = cms.InputTag( "pixelVertices" ),
      tkTrajUseVertex = cms.bool( False )
    ),
    TrackLoaderParameters = cms.PSet( 
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      SmoothTkTrack = cms.untracked.bool( False ),
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( False ),
      DoSmoothing = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
fragment.hltL3TrajectorySeed = cms.EDProducer( "L3MuonTrajectorySeedCombiner",
    labels = cms.VInputTag( 'hltL3TrajSeedIOHit','hltL3TrajSeedOIState','hltL3TrajSeedOIHit' )
)
fragment.hltL3TrackCandidateFromL2 = cms.EDProducer( "L3TrackCandCombiner",
    labels = cms.VInputTag( 'hltL3TrackCandidateFromL2IOHit','hltL3TrackCandidateFromL2OIHit','hltL3TrackCandidateFromL2OIState' )
)
fragment.hltL3TkTracksMergeStep1 = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltL3TkTracksFromL2OIState','hltL3TkTracksFromL2OIHit' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 100.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltL3TkTracksFromL2OIState','hltL3TkTracksFromL2OIHit' ),
    LostHitPenalty = cms.double( 0.0 ),
    newQuality = cms.string( "confirmed" )
)
fragment.hltL3TkTracksFromL2 = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltL3TkTracksMergeStep1','hltL3TkTracksFromL2IOHit' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 100.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltL3TkTracksMergeStep1','hltL3TkTracksFromL2IOHit' ),
    LostHitPenalty = cms.double( 0.0 ),
    newQuality = cms.string( "confirmed" )
)
fragment.hltL3MuonsLinksCombination = cms.EDProducer( "L3TrackLinksCombiner",
    labels = cms.VInputTag( 'hltL3MuonsOIState','hltL3MuonsOIHit','hltL3MuonsIOHit' )
)
fragment.hltL3Muons = cms.EDProducer( "L3TrackCombiner",
    labels = cms.VInputTag( 'hltL3MuonsOIState','hltL3MuonsOIHit','hltL3MuonsIOHit' )
)
fragment.hltL3MuonCandidates = cms.EDProducer( "L3MuonCandidateProducer",
    InputLinksObjects = cms.InputTag( "hltL3MuonsLinksCombination" ),
    InputObjects = cms.InputTag( "hltL3Muons" ),
    MuonPtOption = cms.string( "Tracker" )
)
fragment.hltL3fLMu7p5TrackL3Filtered7p5 = cms.EDFilter( "HLTMuonL3PreFilter",
    MaxNormalizedChi2 = cms.double( 9999.0 ),
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fMu7p5TrackL2Filtered7" ),
    MinNmuonHits = cms.int32( 0 ),
    MinN = cms.int32( 1 ),
    MinTrackPt = cms.double( 0.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxDXYBeamSpot = cms.double( 9999.0 ),
    MinNhits = cms.int32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDz = cms.double( 9999.0 ),
    MaxPtDifference = cms.double( 9999.0 ),
    MaxDr = cms.double( 2.0 ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    MinDXYBeamSpot = cms.double( -1.0 ),
    MinDr = cms.double( -1.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinPt = cms.double( 7.5 )
)
fragment.hltL3MuonVertex = cms.EDProducer( "VertexFromTrackProducer",
    verbose = cms.untracked.bool( False ),
    useTriggerFilterElectrons = cms.bool( False ),
    beamSpotLabel = cms.InputTag( "hltOnlineBeamSpot" ),
    isRecoCandidate = cms.bool( True ),
    trackLabel = cms.InputTag( "hltL3MuonCandidates" ),
    useTriggerFilterMuons = cms.bool( False ),
    useBeamSpot = cms.bool( True ),
    vertexLabel = cms.InputTag( "notUsed" ),
    triggerFilterElectronsSrc = cms.InputTag( "notUsed" ),
    triggerFilterMuonsSrc = cms.InputTag( "notUsed" ),
    useVertex = cms.bool( False )
)
fragment.hltPixelTracksL3Muon = cms.EDProducer( "PixelTrackProducer",
    useFilterWithES = cms.bool( False ),
    FilterPSet = cms.PSet( 
      chi2 = cms.double( 1000.0 ),
      nSigmaTipMaxTolerance = cms.double( 0.0 ),
      ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
      nSigmaInvPtTolerance = cms.double( 0.0 ),
      ptMin = cms.double( 0.1 ),
      tipMax = cms.double( 1.0 )
    ),
    passLabel = cms.string( "" ),
    FitterPSet = cms.PSet( 
      ComponentName = cms.string( "PixelFitterByHelixProjections" ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      fixImpactParameter = cms.double( 0.0 )
    ),
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "GlobalTrackingRegionWithVerticesProducer" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.2 ),
        ptMin = cms.double( 0.9 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        nSigmaZ = cms.double( 4.0 ),
        sigmaZVertex = cms.double( 4.0 ),
        fixedError = cms.double( 0.5 ),
        useFixedError = cms.bool( True ),
        useFoundVertices = cms.bool( True ),
        useFakeVertices = cms.bool( True ),
        VertexCollection = cms.InputTag( "hltL3MuonVertex" )
      )
    ),
    CleanerPSet = cms.PSet(  ComponentName = cms.string( "PixelTrackCleanerBySharedHits" ) ),
    OrderedHitsFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      GeneratorPSet = cms.PSet( 
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 100000 ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.06 ),
        useMultScattering = cms.bool( True ),
        SeedComparitorPSet = cms.PSet( 
          ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
          clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCache" )
        ),
        extraHitRZtolerance = cms.double( 0.06 ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" )
      ),
      SeedingLayers = cms.InputTag( "hltPixelLayerTriplets" )
    )
)
fragment.hltPixelVerticesL3Muon = cms.EDProducer( "PixelVertexProducer",
    WtAverage = cms.bool( True ),
    Method2 = cms.bool( True ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPvClusterComparer" ) ),
    Verbosity = cms.int32( 0 ),
    UseError = cms.bool( True ),
    TrackCollection = cms.InputTag( "hltPixelTracksL3Muon" ),
    PtMin = cms.double( 1.0 ),
    NTrkMin = cms.int32( 2 ),
    ZOffset = cms.double( 5.0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    ZSeparation = cms.double( 0.05 )
)
fragment.hltPixelTracksForSeedsL3Muon = cms.EDProducer( "PixelTrackProducer",
    useFilterWithES = cms.bool( False ),
    FilterPSet = cms.PSet( 
      chi2 = cms.double( 1000.0 ),
      nSigmaTipMaxTolerance = cms.double( 0.0 ),
      ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
      nSigmaInvPtTolerance = cms.double( 0.0 ),
      ptMin = cms.double( 0.1 ),
      tipMax = cms.double( 1.0 )
    ),
    passLabel = cms.string( "" ),
    FitterPSet = cms.PSet( 
      ComponentName = cms.string( "PixelFitterByHelixProjections" ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      fixImpactParameter = cms.double( 0.0 )
    ),
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "CandidateSeededTrackingRegionsProducer" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.1 ),
        ptMin = cms.double( 0.9 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        mode = cms.string( "VerticesFixed" ),
        input = cms.InputTag( "hltL3MuonCandidates" ),
        maxNRegions = cms.int32( 10 ),
        vertexCollection = cms.InputTag( "hltPixelVerticesL3Muon" ),
        maxNVertices = cms.int32( 1 ),
        zErrorBeamSpot = cms.double( 24.2 ),
        deltaEta = cms.double( 0.3 ),
        deltaPhi = cms.double( 0.3 ),
        nSigmaZVertex = cms.double( 3.0 ),
        nSigmaZBeamSpot = cms.double( 4.0 ),
        zErrorVetex = cms.double( 0.2 )
      )
    ),
    CleanerPSet = cms.PSet(  ComponentName = cms.string( "PixelTrackCleanerBySharedHits" ) ),
    OrderedHitsFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      GeneratorPSet = cms.PSet( 
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 100000 ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.06 ),
        useMultScattering = cms.bool( True ),
        SeedComparitorPSet = cms.PSet( 
          ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
          clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCache" )
        ),
        extraHitRZtolerance = cms.double( 0.06 ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" )
      ),
      SeedingLayers = cms.InputTag( "hltPixelLayerTriplets" )
    )
)
fragment.hltIter0L3MuonPixelSeedsFromPixelTracks = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
    useEventsWithNoVertex = cms.bool( True ),
    originHalfLength = cms.double( 0.2 ),
    useProtoTrackKinematics = cms.bool( False ),
    usePV = cms.bool( False ),
    SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromProtoTracks" ) ),
    InputVertexCollection = cms.InputTag( "hltPixelVerticesL3Muon" ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    InputCollection = cms.InputTag( "hltPixelTracksForSeedsL3Muon" ),
    originRadius = cms.double( 0.1 )
)
fragment.hltIter0L3MuonCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter0L3MuonPixelSeedsFromPixelTracks" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter0PSetTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
fragment.hltIter0L3MuonCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter0L3MuonCkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIterX" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
fragment.hltIter0L3MuonTrackSelectionHighPurity = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 100.0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "highPurity" ),
    minNumberLayers = cms.uint32( 3 ),
    chi2n_par = cms.double( 0.7 ),
    useVtxError = cms.bool( False ),
    nSigmaZ = cms.double( 3.0 ),
    dz_par2 = cms.vdouble( 0.4, 4.0 ),
    applyAdaptedPVCuts = cms.bool( True ),
    min_eta = cms.double( -9999.0 ),
    dz_par1 = cms.vdouble( 0.35, 4.0 ),
    copyTrajectories = cms.untracked.bool( True ),
    vtxNumber = cms.int32( -1 ),
    max_d0NoPV = cms.double( 100.0 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 1 ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    max_relpterr = cms.double( 9999.0 ),
    copyExtras = cms.untracked.bool( True ),
    max_z0NoPV = cms.double( 100.0 ),
    vertexCut = cms.string( "tracksSize>=3" ),
    max_z0 = cms.double( 100.0 ),
    useVertices = cms.bool( True ),
    min_nhits = cms.uint32( 0 ),
    src = cms.InputTag( "hltIter0L3MuonCtfWithMaterialTracks" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 9999.0 ),
    vertices = cms.InputTag( "hltPixelVerticesL3Muon" ),
    max_eta = cms.double( 9999.0 ),
    d0_par2 = cms.vdouble( 0.4, 4.0 ),
    d0_par1 = cms.vdouble( 0.3, 4.0 ),
    res_par = cms.vdouble( 0.003, 0.001 ),
    minHitsToBypassChecks = cms.uint32( 20 )
)
fragment.hltIter1L3MuonClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltIter0L3MuonTrackSelectionHighPurity" ),
    oldClusterRemovalInfo = cms.InputTag( "" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClusters" ),
    TrackQuality = cms.string( "highPurity" )
)
fragment.hltIter1L3MuonMaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltIter1L3MuonClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClusters" )
)
fragment.hltIter1L3MuonPixelLayerTriplets = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.0036 ),
      useErrorsFromParam = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter1L3MuonClustersRefRemoval" ),
      hitErrorRPhi = cms.double( 0.0051 )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.006 ),
      useErrorsFromParam = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter1L3MuonClustersRefRemoval" ),
      hitErrorRPhi = cms.double( 0.0027 )
    ),
    TIB = cms.PSet(  )
)
fragment.hltIter1L3MuonPixelSeeds = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "CandidateSeededTrackingRegionsProducer" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.05 ),
        ptMin = cms.double( 0.5 ),
        deltaPhi = cms.double( 0.3 ),
        deltaEta = cms.double( 0.3 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        mode = cms.string( "VerticesFixed" ),
        input = cms.InputTag( "hltL3MuonCandidates" ),
        maxNRegions = cms.int32( 10 ),
        vertexCollection = cms.InputTag( "hltPixelVerticesL3Muon" ),
        maxNVertices = cms.int32( 1 ),
        zErrorBeamSpot = cms.double( 24.2 ),
        nSigmaZVertex = cms.double( 3.0 ),
        nSigmaZBeamSpot = cms.double( 4.0 ),
        zErrorVetex = cms.double( 0.1 ),
        measurementTrackerName = cms.string( "hltIter1L3MuonMaskedMeasurementTrackerEvent" )
      )
    ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    ClusterCheckPSet = cms.PSet( 
      PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClusters" ),
      MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
      doClusterCheck = cms.bool( False ),
      ClusterCollectionLabel = cms.InputTag( "hltSiStripClusters" ),
      MaxNumberOfPixelClusters = cms.uint32( 10000 )
    ),
    OrderedHitsFactoryPSet = cms.PSet( 
      maxElement = cms.uint32( 0 ),
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      GeneratorPSet = cms.PSet( 
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 100000 ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.032 ),
        useMultScattering = cms.bool( True ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" ),
        extraHitRZtolerance = cms.double( 0.037 ),
        SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) )
      ),
      SeedingLayers = cms.InputTag( "hltIter1L3MuonPixelLayerTriplets" )
    ),
    SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromConsecutiveHitsTripletOnlyCreator" ) )
)
fragment.hltIter1L3MuonCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter1L3MuonPixelSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter1L3MuonMaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter1PSetTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
fragment.hltIter1L3MuonCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter1L3MuonCkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter1L3MuonMaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIterX" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
fragment.hltIter1L3MuonTrackSelectionHighPurityLoose = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 100.0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "highPurity" ),
    minNumberLayers = cms.uint32( 3 ),
    chi2n_par = cms.double( 0.7 ),
    useVtxError = cms.bool( False ),
    nSigmaZ = cms.double( 3.0 ),
    dz_par2 = cms.vdouble( 0.9, 3.0 ),
    applyAdaptedPVCuts = cms.bool( True ),
    min_eta = cms.double( -9999.0 ),
    dz_par1 = cms.vdouble( 0.8, 3.0 ),
    copyTrajectories = cms.untracked.bool( True ),
    vtxNumber = cms.int32( -1 ),
    max_d0NoPV = cms.double( 100.0 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 1 ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    max_relpterr = cms.double( 9999.0 ),
    copyExtras = cms.untracked.bool( True ),
    max_z0NoPV = cms.double( 100.0 ),
    vertexCut = cms.string( "tracksSize>=3" ),
    max_z0 = cms.double( 100.0 ),
    useVertices = cms.bool( True ),
    min_nhits = cms.uint32( 0 ),
    src = cms.InputTag( "hltIter1L3MuonCtfWithMaterialTracks" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 9999.0 ),
    vertices = cms.InputTag( "hltPixelVerticesL3Muon" ),
    max_eta = cms.double( 9999.0 ),
    d0_par2 = cms.vdouble( 0.9, 3.0 ),
    d0_par1 = cms.vdouble( 0.85, 3.0 ),
    res_par = cms.vdouble( 0.003, 0.001 ),
    minHitsToBypassChecks = cms.uint32( 20 )
)
fragment.hltIter1L3MuonTrackSelectionHighPurityTight = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 100.0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "highPurity" ),
    minNumberLayers = cms.uint32( 5 ),
    chi2n_par = cms.double( 0.4 ),
    useVtxError = cms.bool( False ),
    nSigmaZ = cms.double( 3.0 ),
    dz_par2 = cms.vdouble( 1.0, 4.0 ),
    applyAdaptedPVCuts = cms.bool( True ),
    min_eta = cms.double( -9999.0 ),
    dz_par1 = cms.vdouble( 1.0, 4.0 ),
    copyTrajectories = cms.untracked.bool( True ),
    vtxNumber = cms.int32( -1 ),
    max_d0NoPV = cms.double( 100.0 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 1 ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    max_relpterr = cms.double( 9999.0 ),
    copyExtras = cms.untracked.bool( True ),
    max_z0NoPV = cms.double( 100.0 ),
    vertexCut = cms.string( "tracksSize>=3" ),
    max_z0 = cms.double( 100.0 ),
    useVertices = cms.bool( True ),
    min_nhits = cms.uint32( 0 ),
    src = cms.InputTag( "hltIter1L3MuonCtfWithMaterialTracks" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 9999.0 ),
    vertices = cms.InputTag( "hltPixelVerticesL3Muon" ),
    max_eta = cms.double( 9999.0 ),
    d0_par2 = cms.vdouble( 1.0, 4.0 ),
    d0_par1 = cms.vdouble( 1.0, 4.0 ),
    res_par = cms.vdouble( 0.003, 0.001 ),
    minHitsToBypassChecks = cms.uint32( 20 )
)
fragment.hltIter1L3MuonTrackSelectionHighPurity = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter1L3MuonTrackSelectionHighPurityLoose','hltIter1L3MuonTrackSelectionHighPurityTight' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIter1L3MuonTrackSelectionHighPurityLoose','hltIter1L3MuonTrackSelectionHighPurityTight' ),
    LostHitPenalty = cms.double( 20.0 ),
    newQuality = cms.string( "confirmed" )
)
fragment.hltIter1L3MuonMerged = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter0L3MuonTrackSelectionHighPurity','hltIter1L3MuonTrackSelectionHighPurity' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIter0L3MuonTrackSelectionHighPurity','hltIter1L3MuonTrackSelectionHighPurity' ),
    LostHitPenalty = cms.double( 20.0 ),
    newQuality = cms.string( "confirmed" )
)
fragment.hltIter2L3MuonClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 16.0 ),
    trajectories = cms.InputTag( "hltIter1L3MuonTrackSelectionHighPurity" ),
    oldClusterRemovalInfo = cms.InputTag( "hltIter1L3MuonClustersRefRemoval" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClusters" ),
    TrackQuality = cms.string( "highPurity" )
)
fragment.hltIter2L3MuonMaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltIter2L3MuonClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClusters" )
)
fragment.hltIter2L3MuonPixelLayerPairs = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix2+BPix3',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix1+FPix2_pos',
      'BPix1+FPix2_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'BPix2+FPix2_pos',
      'BPix2+FPix2_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.0036 ),
      useErrorsFromParam = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter2L3MuonClustersRefRemoval" ),
      hitErrorRPhi = cms.double( 0.0051 )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.006 ),
      useErrorsFromParam = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter2L3MuonClustersRefRemoval" ),
      hitErrorRPhi = cms.double( 0.0027 )
    ),
    TIB = cms.PSet(  )
)
fragment.hltIter2L3MuonPixelSeeds = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "CandidateSeededTrackingRegionsProducer" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.025 ),
        ptMin = cms.double( 1.2 ),
        deltaPhi = cms.double( 0.3 ),
        deltaEta = cms.double( 0.3 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        mode = cms.string( "VerticesFixed" ),
        input = cms.InputTag( "hltL3MuonCandidates" ),
        maxNRegions = cms.int32( 10 ),
        vertexCollection = cms.InputTag( "hltPixelVerticesL3Muon" ),
        maxNVertices = cms.int32( 1 ),
        zErrorBeamSpot = cms.double( 24.2 ),
        nSigmaZVertex = cms.double( 3.0 ),
        nSigmaZBeamSpot = cms.double( 4.0 ),
        zErrorVetex = cms.double( 0.05 ),
        measurementTrackerName = cms.string( "hltIter2L3MuonMaskedMeasurementTrackerEvent" )
      )
    ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    ClusterCheckPSet = cms.PSet( 
      PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClusters" ),
      MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
      doClusterCheck = cms.bool( False ),
      ClusterCollectionLabel = cms.InputTag( "hltSiStripClusters" ),
      MaxNumberOfPixelClusters = cms.uint32( 10000 )
    ),
    OrderedHitsFactoryPSet = cms.PSet( 
      maxElement = cms.uint32( 0 ),
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      GeneratorPSet = cms.PSet( 
        maxElement = cms.uint32( 100000 ),
        SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) )
      ),
      SeedingLayers = cms.InputTag( "hltIter2L3MuonPixelLayerPairs" )
    ),
    SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromConsecutiveHitsCreatorIT" ) )
)
fragment.hltIter2L3MuonCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter2L3MuonPixelSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter2L3MuonMaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter2PSetTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
fragment.hltIter2L3MuonCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter2L3MuonCkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter2L3MuonMaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIterX" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
fragment.hltIter2L3MuonTrackSelectionHighPurity = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 100.0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "highPurity" ),
    minNumberLayers = cms.uint32( 3 ),
    chi2n_par = cms.double( 0.7 ),
    useVtxError = cms.bool( False ),
    nSigmaZ = cms.double( 3.0 ),
    dz_par2 = cms.vdouble( 0.4, 4.0 ),
    applyAdaptedPVCuts = cms.bool( True ),
    min_eta = cms.double( -9999.0 ),
    dz_par1 = cms.vdouble( 0.35, 4.0 ),
    copyTrajectories = cms.untracked.bool( True ),
    vtxNumber = cms.int32( -1 ),
    max_d0NoPV = cms.double( 100.0 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 1 ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    max_relpterr = cms.double( 9999.0 ),
    copyExtras = cms.untracked.bool( True ),
    max_z0NoPV = cms.double( 100.0 ),
    vertexCut = cms.string( "tracksSize>=3" ),
    max_z0 = cms.double( 100.0 ),
    useVertices = cms.bool( True ),
    min_nhits = cms.uint32( 0 ),
    src = cms.InputTag( "hltIter2L3MuonCtfWithMaterialTracks" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 9999.0 ),
    vertices = cms.InputTag( "hltPixelVerticesL3Muon" ),
    max_eta = cms.double( 9999.0 ),
    d0_par2 = cms.vdouble( 0.4, 4.0 ),
    d0_par1 = cms.vdouble( 0.3, 4.0 ),
    res_par = cms.vdouble( 0.003, 0.001 ),
    minHitsToBypassChecks = cms.uint32( 20 )
)
fragment.hltIter2L3MuonMerged = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter1L3MuonMerged','hltIter2L3MuonTrackSelectionHighPurity' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIter1L3MuonMerged','hltIter2L3MuonTrackSelectionHighPurity' ),
    LostHitPenalty = cms.double( 20.0 ),
    newQuality = cms.string( "confirmed" )
)
fragment.hltTracksIter = cms.EDProducer( "ConcreteChargedCandidateProducer",
    src = cms.InputTag( "hltIter2L3MuonMerged" ),
    particleType = cms.string( "mu+" )
)
fragment.hltMu7p5Track2JpsiTrackMassFiltered = cms.EDFilter( "HLTMuonTrackMassFilter",
    saveTags = cms.bool( True ),
    MaxDCAMuonTrack = cms.double( 0.5 ),
    PreviousCandTag = cms.InputTag( "hltL3fLMu7p5TrackL3Filtered7p5" ),
    TrackTag = cms.InputTag( "hltTracksIter" ),
    MaxTrackDz = cms.double( 999.0 ),
    MaxTrackNormChi2 = cms.double( 10.0 ),
    MinTrackPt = cms.double( 2.0 ),
    MinTrackHits = cms.int32( 8 ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    MaxMasses = cms.vdouble( 3.35 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxTrackEta = cms.double( 999.0 ),
    checkCharge = cms.bool( True ),
    MinMasses = cms.vdouble( 2.8 ),
    CutCowboys = cms.bool( False ),
    MaxTrackDxy = cms.double( 999.0 ),
    MinTrackP = cms.double( 3.5 )
)
fragment.hltBoolEnd = cms.EDFilter( "HLTBool",
    result = cms.bool( True )
)

fragment.HLTL1UnpackerSequence = cms.Sequence( fragment.hltGtDigis + fragment.hltCaloStage1Digis + fragment.hltCaloStage1LegacyFormatDigis + fragment.hltL1GtObjectMap + fragment.hltL1extraParticles )
fragment.HLTBeamSpot = cms.Sequence( fragment.hltScalersRawToDigi + fragment.hltOnlineBeamSpot )
fragment.HLTBeginSequence = cms.Sequence( fragment.hltTriggerType + fragment.HLTL1UnpackerSequence + fragment.HLTBeamSpot )
fragment.HLTMuonLocalRecoSequence = cms.Sequence( fragment.hltMuonDTDigis + fragment.hltDt1DRecHits + fragment.hltDt4DSegments + fragment.hltMuonCSCDigis + fragment.hltCsc2DRecHits + fragment.hltCscSegments + fragment.hltMuonRPCDigis + fragment.hltRpcRecHits )
fragment.HLTL2muonrecoNocandSequence = cms.Sequence( fragment.HLTMuonLocalRecoSequence + fragment.hltL2OfflineMuonSeeds + fragment.hltL2MuonSeeds + fragment.hltL2Muons )
fragment.HLTL2muonrecoSequence = cms.Sequence( fragment.HLTL2muonrecoNocandSequence + fragment.hltL2MuonCandidates )
fragment.HLTDoLocalPixelSequence = cms.Sequence( fragment.hltSiPixelDigis + fragment.hltSiPixelClusters + fragment.hltSiPixelClustersCache + fragment.hltSiPixelRecHits )
fragment.HLTDoLocalStripSequence = cms.Sequence( fragment.hltSiStripExcludedFEDListProducer + fragment.hltSiStripRawToClustersFacility + fragment.hltSiStripClusters )
fragment.HLTL3muonTkCandidateSequence = cms.Sequence( fragment.HLTDoLocalPixelSequence + fragment.HLTDoLocalStripSequence + fragment.hltL3TrajSeedOIState + fragment.hltL3TrackCandidateFromL2OIState + fragment.hltL3TkTracksFromL2OIState + fragment.hltL3MuonsOIState + fragment.hltL3TrajSeedOIHit + fragment.hltL3TrackCandidateFromL2OIHit + fragment.hltL3TkTracksFromL2OIHit + fragment.hltL3MuonsOIHit + fragment.hltL3TkFromL2OICombination + fragment.hltPixelLayerTriplets + fragment.hltPixelLayerPairs + fragment.hltMixedLayerPairs + fragment.hltL3TrajSeedIOHit + fragment.hltL3TrackCandidateFromL2IOHit + fragment.hltL3TkTracksFromL2IOHit + fragment.hltL3MuonsIOHit + fragment.hltL3TrajectorySeed + fragment.hltL3TrackCandidateFromL2 )
fragment.HLTL3muonrecoNocandSequence = cms.Sequence( fragment.HLTL3muonTkCandidateSequence + fragment.hltL3TkTracksMergeStep1 + fragment.hltL3TkTracksFromL2 + fragment.hltL3MuonsLinksCombination + fragment.hltL3Muons )
fragment.HLTL3muonrecoSequence = cms.Sequence( fragment.HLTL3muonrecoNocandSequence + fragment.hltL3MuonCandidates )
fragment.HLTPixelTrackingL3Muon = cms.Sequence( fragment.hltL3MuonVertex + fragment.HLTDoLocalPixelSequence + fragment.hltPixelLayerTriplets + fragment.hltPixelTracksL3Muon + fragment.hltPixelVerticesL3Muon )
fragment.HLTIterativeTrackingL3MuonIteration0 = cms.Sequence( fragment.hltPixelTracksForSeedsL3Muon + fragment.hltIter0L3MuonPixelSeedsFromPixelTracks + fragment.hltIter0L3MuonCkfTrackCandidates + fragment.hltIter0L3MuonCtfWithMaterialTracks + fragment.hltIter0L3MuonTrackSelectionHighPurity )
fragment.HLTIterativeTrackingL3MuonIteration1 = cms.Sequence( fragment.hltIter1L3MuonClustersRefRemoval + fragment.hltIter1L3MuonMaskedMeasurementTrackerEvent + fragment.hltIter1L3MuonPixelLayerTriplets + fragment.hltIter1L3MuonPixelSeeds + fragment.hltIter1L3MuonCkfTrackCandidates + fragment.hltIter1L3MuonCtfWithMaterialTracks + fragment.hltIter1L3MuonTrackSelectionHighPurityLoose + fragment.hltIter1L3MuonTrackSelectionHighPurityTight + fragment.hltIter1L3MuonTrackSelectionHighPurity )
fragment.HLTIterativeTrackingL3MuonIteration2 = cms.Sequence( fragment.hltIter2L3MuonClustersRefRemoval + fragment.hltIter2L3MuonMaskedMeasurementTrackerEvent + fragment.hltIter2L3MuonPixelLayerPairs + fragment.hltIter2L3MuonPixelSeeds + fragment.hltIter2L3MuonCkfTrackCandidates + fragment.hltIter2L3MuonCtfWithMaterialTracks + fragment.hltIter2L3MuonTrackSelectionHighPurity )
fragment.HLTIterativeTrackingL3MuonIter02 = cms.Sequence( fragment.HLTIterativeTrackingL3MuonIteration0 + fragment.HLTIterativeTrackingL3MuonIteration1 + fragment.hltIter1L3MuonMerged + fragment.HLTIterativeTrackingL3MuonIteration2 + fragment.hltIter2L3MuonMerged )
fragment.HLTTrackReconstructionIter02 = cms.Sequence( fragment.HLTPixelTrackingL3Muon + fragment.HLTDoLocalStripSequence + fragment.HLTIterativeTrackingL3MuonIter02 )
fragment.HLTEndSequence = cms.Sequence( fragment.hltBoolEnd )

fragment.HLT_Mu7p5_Track2_Jpsi_v2 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sMu5 + fragment.hltPreMu7p5Track2Jpsi + fragment.hltL1fMu7p5TrackFiltered0 + fragment.HLTL2muonrecoSequence + fragment.hltL2fMu7p5TrackL2Filtered7 + fragment.HLTL3muonrecoSequence + fragment.hltL3fLMu7p5TrackL3Filtered7p5 + fragment.HLTTrackReconstructionIter02 + fragment.hltTracksIter + fragment.hltMu7p5Track2JpsiTrackMassFiltered + fragment.HLTEndSequence )


fragment.HLTSchedule = cms.Schedule( *(fragment.HLT_Mu7p5_Track2_Jpsi_v2 ))


# add release-specific customizations
from HLTrigger.Configuration.customizeHLTforCMSSW import customiseHLTforCMSSW
fragment = customiseHLTforCMSSW(fragment,menuType="GRun",fastSim=False)

# dummyfy hltGetConditions in cff's
if 'hltGetConditions' in fragment.__dict__ and 'HLTriggerFirstPath' in fragment.__dict__ :
    fragment.hltDummyConditions = cms.EDFilter( "HLTBool",
        result = cms.bool( True )
    )
    fragment.HLTriggerFirstPath.replace(fragment.hltGetConditions,fragment.hltDummyConditions)

