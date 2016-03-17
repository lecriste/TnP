import FWCore.ParameterSet.Config as cms

### USAGE:
###    cmsRun fitMuonID.py <scenario>
### scenarios:
###   - data_all (default)
###   - signal_mc

import sys
args = sys.argv[1:]
if (sys.argv[0] == "cmsRun"): args = sys.argv[2:]
scenario = "data_all"
if len(args) > 0: scenario = args[0]
print "Will run scenario ", scenario

process = cms.Process("TagProbe")

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.source = cms.Source("EmptySource")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

print "About to define TagProbeFitTreeAnalyzer"

Template = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
    WeightVariable = cms.string("weight"),
    NumCPU = cms.uint32(1),
    SaveWorkspace = cms.bool(False),

    Variables = cms.PSet(
        mass = cms.vstring("Tag-muon Mass", "2.9", "3.3", "GeV/c^{2}"), #2.8-3.35
        p  = cms.vstring("muon p", "0", "1000", "GeV/c"),
        pt = cms.vstring("muon p_{T}", "0", "1000", "GeV/c"),
        eta = cms.vstring("muon #eta", "-2.5", "2.5", ""),
        abseta = cms.vstring("muon |#eta|", "0", "2.5", ""),
        tag_pt = cms.vstring("Tag p_{T}", "0", "1000", "GeV/c"),
        tag_abseta = cms.vstring("Tag |#eta|", "0", "2.5", ""),
        tag_nVertices = cms.vstring("Number of vertices", "0", "999", ""),
        tag_nVerticesDA = cms.vstring("Number of vertices", "0", "999", ""),
        #
        pair_pt = cms.vstring("dimuon p_{T}", "0", "1000", "GeV/c"),
        pair_absrapidity = cms.vstring("dimuon |y|", "0", "2.5", ""),
        pair_dphiVtxTimesQ = cms.vstring("q1 * (#phi1-#phi2)", "-6", "6", ""),
        pair_drM1   = cms.vstring("#Delta R(Station 1)", "-99999", "999999", "rad"),
        pair_distM1 = cms.vstring("dist(Station 1)", "-99999", "999999", "cm"),
        pair_dz = cms.vstring("dz","-5","5",""),
        pair_probeMultiplicity = cms.vstring("multiplicity","0","99",""),
        dB = cms.vstring("dB", "-1000", "1000", ""),
        dzPV = cms.vstring("dzPV", "-1000", "1000", ""),
        dxyBS = cms.vstring("dxyBS", "-1000", "1000", ""),
        tkValidHits = cms.vstring("track.numberOfValidHits", "-1", "999", ""),
        tkTrackerLay = cms.vstring("track.hitPattern.trackerLayersWithMeasurement", "-1", "999", ""),
        tkValidPixelHits = cms.vstring("track.hitPattern.numberOfValidPixelHits", "-1", "999", ""),
        tkPixelLay = cms.vstring("track.hitPattern.pixelLayersWithMeasurement", "-1", "999", ""),
        tkChi2 = cms.vstring("track.normalizedChi2", "-1", "999", ""),
        numberOfMatchedStations = cms.vstring("numberOfMatchedStations", "-1", "99", ""),
        glbChi2 = cms.vstring("global.normalizedChi2", "-9999", "9999", ""),
        glbValidMuHits = cms.vstring("globalTrack.numberOfValidMuonHits", "-1", "9999", ""),
        caloComp = cms.vstring("caloCompatibility","-1","5",""),
        # Added for mediumVar
        validFraction = cms.vstring("innerTrack.validFraction","-9999","9999",""),
        chi2LPosition = cms.vstring("combinedQuality.chi2LocalPosition","-9999","9999",""),
        tkKink = cms.vstring("combinedQuality.trkKink","-9999","9999",""),
        segmComp = cms.vstring("segmentCompatibility","-1","5",""),
        # tracking efficiency
        tk_deltaR   = cms.vstring("Match #Delta R",    "0", "1000", ""),
        tk_deltaEta = cms.vstring("Match #Delta #eta", "0", "1000", ""),
        tk_deltaR_NoJPsi   = cms.vstring("Unmatch #Delta R",    "0", "1000", ""),
        tk_deltaEta_NoJPsi = cms.vstring("Unmatch #Delta #eta", "0", "1000", ""),
        tk_deltaR_NoBestJPsi   = cms.vstring("Unmatch #Delta R",    "0", "1000", ""),
        tk_deltaEta_NoBestJPsi = cms.vstring("Unmatch #Delta #eta", "0", "1000", ""),
        #
        weight = cms.vstring("weight","0","10","") # There is no problem by defining more variables and categories than are present in the TTree as long as they are not used in the Efficiency calculations.
    ),

    Categories = cms.PSet(
        TM   = cms.vstring("Tracker muon", "dummy[pass=1,fail=0]"),
        TMA   = cms.vstring("Tracker muon", "dummy[pass=1,fail=0]"),
        Glb   = cms.vstring("Global", "dummy[pass=1,fail=0]"),
        Loose   = cms.vstring("Loose", "dummy[pass=1,fail=0]"),
        VBTF  = cms.vstring("VBTFLike", "dummy[pass=1,fail=0]"),
        TMOST = cms.vstring("TMOneStationTight", "dummy[pass=1,fail=0]"),
        PF = cms.vstring("PF", "dummy[pass=1,fail=0]"),
        Track_HP = cms.vstring("Track_HP", "dummy[pass=1,fail=0]"),
        Tight2012 = cms.vstring("Tight Id. Muon", "dummy[pass=1,fail=0]"),
        Medium = cms.vstring("Medium Id. Muon", "dummy[pass=1,fail=0]"),
	# 2012 triggers
        #Mu5_Track2_Jpsi_TK = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        #Mu7_Track7_Jpsi_TK = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        #tag_Mu5_Track2_Jpsi_MU = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        #tag_Mu7_Track7_Jpsi_MU = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
	# 2015 triggers
        tag_Mu7p5_MU = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        Mu7p5_Track2_Jpsi_TK = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        tag_Mu7p5_Track2_Jpsi_MU = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        Mu7p5_Track3p5_Jpsi_TK = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        tag_Mu7p5_Track3p5_Jpsi_MU = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        Mu7p5_Track7_Jpsi_TK = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        tag_Mu7p5_Track7_Jpsi_MU = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        #
        Mu7p5_L2Mu2_Jpsi_L2 = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        tag_Mu7p5_L2Mu2_Jpsi_MU = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        Mu7p5_L2Mu2_L2 = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        # Onia triggers
        Dimuon16_L1L2 = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        Dimuon10_L1L2 = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        #
        Mu_L3 = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        #
        # vertexing efficiency
        Dimuon6_Jpsi_NoVertexing = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        tag_Dimuon6_Jpsi_NoVertexing = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        Dimuon0er16_Jpsi_NoVertexing = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        tag_Dimuon0er16_Jpsi_NoVertexing = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        Dimuon16_Jpsi = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        Dimuon10_Jpsi_Barrel = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        #
        mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
        # test
        DoubleMu17TkMu8_TkMu8leg = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        tag_DoubleMu17TkMu8_TkMu8leg = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        Mu8 = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        tag_Mu8 = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        # Mu25
        Mu25TkMu0Onia_TM = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        tag_Mu25TkMu0Onia_L3_MU = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        # Mu16
        Mu16TkMu0Onia_TM = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        tag_Mu16TkMu0Onia_L3_MU = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),

        ),

   Expressions = cms.PSet(
     LooseVar = cms.vstring("LooseVar", "PF==1 && (Glb==1 || TM==1) ", "PF", "Glb", "TM"),
     Loose2015Var = cms.vstring("Loose2015Var", "PF==1", "PF"),
     oldSoftVar = cms.vstring("oldSoftVar", "TMOST ==1 && tkTrackerLay > 5 && tkPixelLay > 1 && tkChi2 < 1.8 && abs(dzPV) < 30 && abs(dB) < 3", "TMOST","tkTrackerLay", "tkPixelLay", "tkChi2", "dzPV", "dB"),
     # without chi2 cut
     #oldSoftVar = cms.vstring("oldSoftVar", "TMOST ==1 && tkTrackerLay > 5 && tkPixelLay > 1 && abs(dzPV) < 30 && abs(dB) < 3", "TMOST","tkTrackerLay", "tkPixelLay", "dzPV", "dB"),
     #changed cuts
     #oldSoftVar = cms.vstring("oldSoftVar", "TMOST ==1", "TMOST"),
     #oldSoftVar = cms.vstring("oldSoftVar", "TMOST ==1 && abs(dzPV) < 20", "TMOST", "dzPV"),
     #oldSoftVar = cms.vstring("oldSoftVar", "TMOST ==1 && abs(dzPV) < 20 && abs(dB) < 0.3", "TMOST", "dzPV", "dB"),
     #oldSoftVar = cms.vstring("oldSoftVar", "TMOST ==1 && abs(dzPV) < 20 && abs(dB) < 0.3 && tkPixelLay > 0", "TMOST", "dzPV", "dB", "tkPixelLay"),
     #oldSoftVar = cms.vstring("oldSoftVar", "TMOST ==1 && abs(dzPV) < 20 && abs(dB) < 0.3 && tkPixelLay > 0 && tkTrackerLay > 5", "TMOST", "dzPV", "dB", "tkPixelLay", "tkTrackerLay"),
     #MediumVar = cms.vstring("MediumVar", "Loose==1 && validFraction > 0.8 && ((Glb==1 && glbChi2 < 3 && chi2LPosition < 12 && tkKink < 20 && segmComp > 0.303) || segmComp> 0.451)", "Loose", "validFraction", "Glb", "glbChi2", "chi2LPosition", "tkKink", "segmComp"), # already defined in the tree
     MediumVar = cms.vstring("MediumVar", "Medium==1", "Medium"),
     TightVar = cms.vstring("TightVar", "PF==1 && Glb==1 && tkChi2 < 10 && glbValidMuHits > 0 && numberOfMatchedStations > 1 && abs(dB) < 0.2 && abs(dzPV) < 0.5 && tkValidPixelHits > 0 && tkTrackerLay > 5", "PF", "Glb", "tkChi2", "glbValidMuHits", "numberOfMatchedStations", "dB",  "dzPV", "tkValidPixelHits", "tkTrackerLay" ),
     Tight2012_zIPCutVar = cms.vstring("Tight2012_zIPCut", "Tight2012 == 1 && abs(dzPV) < 0.5", "Tight2012", "dzPV"),
     # new SoftMuon ID 2012
     SoftVar = cms.vstring("SoftVar", "TMOST == 1 && tkTrackerLay > 5 && tkPixelLay > 0 && abs(dzPV) < 20 && abs(dB) < 0.3 && Track_HP == 1", "TMOST","tkTrackerLay", "tkPixelLay", "dzPV", "dB", "Track_HP"),
     ),

   Cuts = cms.PSet(
          Loose2012 = cms.vstring("Loose", "LooseVar", "0.5"),
          Loose2015 = cms.vstring("Loose2015", "Loose2015Var", "0.5"),
          Medium2015 = cms.vstring("Medium2015", "MediumVar", "0.5"),
          Tight2012 = cms.vstring("Tight", "TightVar", "0.5"),
          Tight2012_zIPCut = cms.vstring("Tight2012_zIPCut", "Tight2012_zIPCutVar", "0.5"),
          oldSoft2012 = cms.vstring("oldSoft", "oldSoftVar", "0.5"),
          Soft2012 = cms.vstring("Soft", "SoftVar", "0.5"),
          ),

   PDFs = cms.PSet(
        signalPlusBkg = cms.vstring(
            "CBShape::signal(mass, mean[3.1,3.0,3.2], sigma[0.05,0.02,0.06], alpha[3., 0.5, 5.], n[1, 0.1, 100.])",
            #"Chebychev::backgroundPass(mass, {cPass[0,-0.5,0.5], cPass2[0,-0.5,0.5]})",
            #"Chebychev::backgroundFail(mass, {cFail[0,-0.5,0.5], cFail2[0,-0.5,0.5]})",
            #"Gaussian::signal(mass, mean[3.1,3.0,3.2], sigma[0.05,0.02,0.1])",
            "Exponential::backgroundPass(mass, lp[0,-5,5])",
            "Exponential::backgroundFail(mass, lf[0,-5,5])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        )
    ),

    binnedFit = cms.bool(True),
    binsForFit = cms.uint32(40),

    Efficiencies = cms.PSet(), # will be filled later
)

print "TagProbeFitTreeAnalyzer defined!"

# pick muons that bend apart from each other
SEPARATED = cms.PSet(pair_drM1 = cms.vdouble(0.5,10),
                     pair_probeMultiplicity = cms.vdouble(0.5,1.5),
                     #pair_dz = cms.vdouble(-0.1,0.1),
                     #caloComp = cms.vdouble(0.5,5),
                     )
SEPARATED_allPairs = cms.PSet(pair_drM1 = cms.vdouble(0.5,10),
                     #pair_dz = cms.vdouble(-0.1,0.1),
                     #caloComp = cms.vdouble(0.5,5),
                     )
NOTSEPARATED = cms.PSet(#pair_drM1 = cms.vdouble(0.5,10),
                     pair_probeMultiplicity = cms.vdouble(0.5,1.5),
                     #pair_dz = cms.vdouble(-0.1,0.1),
                     #caloComp = cms.vdouble(0.5,5),
                     )
NOTSEPARATED_allPairs = cms.PSet(#pair_drM1 = cms.vdouble(0.5,10),
                     #pair_probeMultiplicity = cms.vdouble(0.5,1.5),
                     #pair_dz = cms.vdouble(-0.1,0.1),
                     #caloComp = cms.vdouble(0.5,5),
                     )
#                     pair_distM1 = cms.vdouble(200,1000))
#SEPARATED = cms.PSet(pair_dphiVtxTimesQ = cms.vdouble(-3.14,0), #seagulls
#                     pair_drM1 = cms.vdouble(0.5,10),
#                     pair_distM1 = cms.vdouble(200,1000))
#SEPARATED = cms.PSet(pair_dphiVtxTimesQ = cms.vdouble(0,3.14),) #cowboys
#                     pair_drM1 = cms.vdouble(0.5,10),
#                     pair_distM1 = cms.vdouble(200,1000))
#
# defined by Leo
SEAGULL = cms.PSet(pair_dphiVtxTimesQ = cms.vdouble(-3.14,0), #seagull (~= pair_drM1>0.5)
                   )
COWBOY = cms.PSet(pair_dphiVtxTimesQ = cms.vdouble(0,3.14), #cowboy (~= pair_drM1<0.5)
                   )

pT_binning_2012 = cms.vdouble(2.0, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.5, 5.0, 6.0, 8.0, 10.0, 15.0, 20.0) # 2012
pT_binning_2015 = cms.vdouble(2.0, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.5, 5.0, 6.0, 8.0, 10.0, 15.0, 20.0, 30.0, 40.0)
pT_binning_47ipb = cms.vdouble(2.0, 2.5, 3.0, 3.5, 4.0, 4.75, 5.5, 7.5, 10.0, 20.0, 40.0)
pT_binning_25ns = cms.vdouble(2.0, 2.5, 3.0, 3.5, 4.0, 4.75, 5.5, 7.5, 10.0, 15.0, 20.0, 40.0)

abseta_binning_47ipb = cms.vdouble(0.0, 0.9, 1.2, 2.1, 2.4)
abseta_binning_25ns = cms.vdouble(0.0, 0.9, 1.2, 1.6, 2.1, 2.4)
abseta_binning_25ns_v2 = cms.vdouble(0.0, 0.2, 0.3, 0.9 , 1.2, 1.6, 2.1, 2.4)
absy_binning_25ns = cms.vdouble(0.0, 0.3, 0.6, 0.9, 1.2, 1.6, 2.1, 2.4)

PT_ETA_BINS = cms.PSet(   SEPARATED,
                          #pt = pT_binning_2012,
                          #pt = pT_binning_2015,
                          pt = pT_binning_47ipb,
                          eta = cms.vdouble(-2.4,-2.1,-1.2,-0.9,0.0,0.9,1.2,2.1,2.4)
                       )

PT_ABSETA_BINS = cms.PSet(   SEPARATED,
                          #pt = pT_binning_2012,
                          #pt = pT_binning_2015,
                          pt = pT_binning_47ipb,
                          #abseta = cms.vdouble(0.0,0.9,1.2,2.1) # 2012
                          abseta = abseta_binning_47ipb
                       )

PT_ABSETA_BINS = cms.PSet(   SEPARATED,
                          #pt = pT_binning_2012,
                          #pt = pT_binning_2015,
                          pt = pT_binning_47ipb,
                          #abseta = cms.vdouble(0.0,0.9,1.2,2.1) # 2012
                          abseta = abseta_binning_47ipb
                       )

PT_ABSETA_BINS_allPairs = cms.PSet(   SEPARATED_allPairs,
                          #pt = pT_binning_2012,
                          #pt = pT_binning_2015,
                          #pt = pT_binning_47ipb,
                          pt = pT_binning_25ns,
                          #abseta = cms.vdouble(0.0,0.9,1.2,2.1) # 2012
                          #abseta = abseta_binning_47ipb,
                          #abseta = abseta_binning_25ns
                          abseta = abseta_binning_25ns_v2
                       )

PT_ABSETA_BINS_notSeparated = cms.PSet(   NOTSEPARATED,
                          #pt = pT_binning_2012,
                          #pt = pT_binning_2015,
                          #pt = pT_binning_47ipb,
                          pt = pT_binning_25ns,
                          #abseta = abseta_binning_47ipb
                          abseta = abseta_binning_25ns_v2
                       )

PT_BINS_notSeparated = cms.PSet(   NOTSEPARATED,
                          #pt = pT_binning_2012,
                          #pt = pT_binning_2015,
                          pt = pT_binning_47ipb,
                          #abseta = cms.vdouble(0.0,0.9,1.2,2.1) # 2012
                          abseta = cms.vdouble(0.0,2.4)
                       )

PT_BINS_ABSETA2p4 = cms.PSet(   SEPARATED,
                          #pt = pT_binning_2012,
                          #pt = pT_binning_2015,
                          pt = pT_binning_47ipb,
                          #abseta = cms.vdouble(0.0,0.9,1.2,2.1) # 2012
                          abseta = cms.vdouble(0.0,2.4)
                       )

PT_ABSY_BINS_notSeparated_pair = cms.PSet(   NOTSEPARATED,
                                               #pt = pT_binning_2012,
                                               #pt = pT_binning_2015,
                                               #pair_pt = cms.vdouble(10.0, 16.0, 20.0, 40.0),
                                               pair_pt = cms.vdouble(10.0, 13.0, 16.0, 18.0, 20.0, 30.0, 40.0),
                                               #pair_absrapidity = abseta_binning_47ipb
                                               pair_absrapidity = absy_binning_25ns
                                               )

PT_ABSYLARGE_BINS_notSeparated_pair = cms.PSet(   NOTSEPARATED,
                                               #pt = pT_binning_2012,
                                               #pt = pT_binning_2015,
                                               #pair_pt = cms.vdouble(10.0, 16.0, 20.0, 40.0),
                                               pair_pt = cms.vdouble(10.0, 13.0, 16.0, 18.0, 20.0, 30.0, 40.0),
                                               #pair_absrapidity = abseta_binning_47ipb
                                               pair_absrapidity = cms.vdouble(0.,1.2)
                                               )

PT_ABSETA_BINS_notSeparated_allPairs = cms.PSet(   NOTSEPARATED_allPairs,
                                                   #pt = pT_binning_2012,
                                                   #pt = pT_binning_2015,
                                                   pt = pT_binning_47ipb,
                                                   #abseta = cms.vdouble(0.0,0.9,1.2,2.1) # 2012
                                                   abseta = abseta_binning_47ipb
                                                   )

PT_ABSETA_BINS_SEAGULL = cms.PSet(   SEAGULL,
                                     #pt = pT_binning_2012,
                                     #pt = pT_binning_2015,
                                     #pt = pT_binning_47ipb,
                                     pt = pT_binning_25ns,
                                     #abseta = cms.vdouble(0.0,0.9,1.2,2.1) # 2012
                                     #abseta = abseta_binning_47ipb
                                     abseta = abseta_binning_25ns_v2
                                     )

PT_ABSETA_BINS_SEAGULL_separated = cms.PSet(   SEAGULL,
                                               SEPARATED_allPairs,
                                               #pt = pT_binning_2012,
                                               #pt = pT_binning_2015,
                                               #pt = pT_binning_47ipb,
                                               pt = pT_binning_25ns,
                                               #abseta = cms.vdouble(0.0,0.9,1.2,2.1) # 2012
                                               #abseta = abseta_binning_47ipb
                                               #abseta = abseta_binning_25ns
                                               abseta = abseta_binning_25ns_v2
                                               )

PT_ABSETA_BINS_COWBOY = cms.PSet(    COWBOY,
                                     #pt = pT_binning_2012,
                                     #pt = pT_binning_2015,
                                     #pt = pT_binning_47ipb,
                                     pt = pT_binning_25ns,
                                     #abseta = cms.vdouble(0.0,0.9,1.2,2.1) # 2012
                                     #abseta = abseta_binning_47ipb
                                     abseta = abseta_binning_25ns_v2
                                     )

PT_ABSETA_BINS_COWBOY_separated = cms.PSet(    COWBOY,
                                               SEPARATED_allPairs,
                                               #pt = pT_binning_2012,
                                               #pt = pT_binning_2015,
                                               #pt = pT_binning_47ipb,
                                               pt = pT_binning_25ns,
                                               #abseta = cms.vdouble(0.0,0.9,1.2,2.1) # 2012
                                               #abseta = abseta_binning_47ipb
                                               #abseta = abseta_binning_25ns
                                               abseta = abseta_binning_25ns_v2
                                               )

PT_BINS = cms.PSet(       SEPARATED,
                          #pt = pT_binning_2012
                          #pt = pT_binning_2015,
			  pt = pT_binning_47ipb
                          ) # check abseta var limits

VTX_BINS = cms.PSet(      SEPARATED,
                          abseta = cms.vdouble(0.0, 2.1),
                          pt     = cms.vdouble(8.0, 20.0),
                          tag_nVertices = cms.vdouble(0.5,2.5,4.5,6.5,8.5,10.5,12.5,14.5,16.5,18.5,20.5,22.5,24.5,26.5,28.5,30.5)
                          #tag_nVerticesDA = cms.vdouble(0.5,2.5,4.5,6.5,8.5,10.5,12.5,14.5,16.5,18.5,20.5,22.5,24.5,26.5,28.5,30.5)
                          )

VTX_BINS_noSoft = cms.PSet(      SEPARATED,
                          abseta = cms.vdouble(0.0, 2.4),
                          pt     = cms.vdouble(8.0, 500.0),
			  tag_nVertices = cms.vdouble(0.5,3.5,6.5,9.5,12.5,15.5,18.5,21.5,24.5,27.5,30.5),
                          )

ETA_BINS = cms.PSet(      SEPARATED,
                          pt     = cms.vdouble(8.0, 20.0),
                          eta = cms.vdouble(-2.1,-1.6,-1.2,-0.9,-0.6,-0.3,-0.2,0.2,0.3,0.6,0.9,1.2,1.6,2.1,),
                          )

PLATEAU_ABSETA = cms.PSet(SEPARATED,
                          abseta = cms.vdouble(0.0, 0.9, 1.2, 2.1, 2.4),
                          pt     = cms.vdouble(8.0, 20.0),
                          )

PLATEAU_ETA = cms.PSet(   SEPARATED,
                          eta = cms.vdouble(-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4),
                          pt     = cms.vdouble(8.0, 500.0),
                          )

PT_ABSETA_WIDE = cms.PSet(SEPARATED,
                          abseta = cms.vdouble(0.0, 1.2, 2.4),
                          pt     = cms.vdouble(5.0, 7.0, 20.0),
                          )

TURNON_ABSETA = cms.PSet( SEPARATED,
                          abseta = cms.vdouble(0.0, 0.9, 1.2, 2.1, 2.4),
                          pt     = cms.vdouble(3.0, 5.0),
                          )

# Prefix should be "./" only
PREFIX="/afs/cern.ch/work/l/lecriste/TnP/Ilse/CMSSW_5_3_22/test/"
process.TnP_MuonID = Template.clone(
     #InputFileNames = cms.vstring(
     #    PREFIX+'tnpJPsi_Run2012A.root',
     #    PREFIX+'tnpJPsi_Run2012B.root',
     #    PREFIX+'tnpJPsi_Run2012C.root',
     #    PREFIX+'tnpJPsi_Run2012D.root',
     #),
     ##InputFileNames = cms.vstring('/afs/cern.ch/user/m/msharma/public/tnpJPsi_Data.root'), # 400k events, no JSON
     ##InputFileNames = cms.vstring('/afs/cern.ch/user/m/msharma/public/tnpJPsi_DataJuly232015.root'), # 800k events, no JSON
     ##InputFileNames = cms.vstring('/afs/cern.ch/user/m/msharma/public/tnpJPsi_Data_246908-251883_JSON_MuonPhys_v2.root'),
     ##InputFileNames = cms.vstring('/afs/cern.ch/work/l/lecriste/TnP/recipe_740/CMSSW_7_4_0/src/MuonAnalysis/TagAndProbe/test/jpsi/tnpJPsi_Charmonium_PromptReco_50ns_first47pb.root'),
     ##InputFileNames = cms.vstring('/afs/cern.ch/work/l/lecriste/TnP/recipe_740/CMSSW_7_4_0/src/MuonAnalysis/TagAndProbe/test/jpsi/tnpJPsi_Charmonium_PromptReco_50ns_first47ipb_OniaTriggersFlags.root'),
     #InputFileNames = cms.vstring('/afs/cern.ch/work/l/lecriste/TnP/recipe_740/CMSSW_7_4_0/src/MuonAnalysis/TagAndProbe/test/jpsi/tnpJPsi_Charmonium_PromptReco_50ns_first47ipb_vertexingTriggersFlags.root'),
     ##InputFileNames = cms.vstring('/afs/cern.ch/work/l/lecriste/TnP/recipe_740/CMSSW_7_4_0/src/MuonAnalysis/TagAndProbe/test/jpsi/tnpJPsi_Charmonium_PromptReco_50ns.root'),
     #InputFileNames = cms.vstring('/afs/cern.ch/work/l/lecriste/TnP/recipe_740/CMSSW_7_4_0/src/MuonAnalysis/TagAndProbe/test/jpsi/tnpJPsi_Data25ns.root'),
     #InputFileNames = cms.vstring('/afs/cern.ch/work/l/lecriste/TnP/recipe_740/CMSSW_7_4_0/src/MuonAnalysis/TagAndProbe/test/jpsi/tnpJPsi_Data25ns_golden.root'),
     #InputFileNames = cms.vstring('/afs/cern.ch/work/l/lecriste/TnP/recipe_740/CMSSW_7_4_0/src/MuonAnalysis/TagAndProbe/test/jpsi/tnpJPsi_Data25ns_golden_Mu8.root'), # Mu8 test
     InputFileNames = cms.vstring('/afs/cern.ch/work/l/lecriste/TnP/recipe_740/CMSSW_7_4_0/src/MuonAnalysis/TagAndProbe/test/jpsi/tnpJPsi_Data25ns_golden_withMu25.root'),
     #InputFileNames = cms.vstring('/afs/cern.ch/work/l/lecriste/TnP/recipe_740/CMSSW_7_4_0/src/MuonAnalysis/TagAndProbe/test/jpsi/tnpJPsi_Data25ns_golden_withMu16.root'),
     #
     InputTreeName = cms.string("fitter_tree"),
     InputDirectoryName = cms.string("tpTree"),
     #InputDirectoryName = cms.string("tpTreeSta"),
     OutputFileName = cms.string("TnP_MuonID_%s.root" %scenario),
     Efficiencies = cms.PSet(),
)

IDS = ["Soft2012"]
#IDS = ["oldSoft2012"]
#IDS = ["Loose2012"]
#IDS = ["Loose2012", "Soft2012", "newSoft2012"]
#IDS = [ "Glb", "TMOST", "VBTF", "PF" ]
# Carlo request:
#IDS = ["Loose2015", "Soft2012", "Medium2015", "Tight2012_zIPCut"]

#TRIGS = [ (2,'Mu7p5_L2Mu2_Jpsi'), (2,'Mu7p5_Track2_Jpsi'), (3.5,'Mu7p5_Track3p5_Jpsi'), (7,'Mu7p5_Track7_Jpsi') ]
#TRIGS = [ (2,'Mu7p5_Track2_Jpsi'), (7,'Mu7p5_Track7_Jpsi') ]
TRIGS = [ (2,'Mu7p5_Track2_Jpsi') ]
#TRIGS = [ (2,'Mu8') ] # Mu8 test
#TRIGS = [ (7,'Mu7p5_Track7_Jpsi') ]
#TRIGS = [ (0,'Mu8'), (0,'Mu17') ] 
#TRIGS = [ (0,'DoubleMu17TkMu8_TkMu8leg') ]

UnbinnedVars = cms.vstring("mass")
if "mc" in scenario:
     UnbinnedVars = cms.vstring("mass","weight")
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_officialBPHMC25ns_withMu25_withNVtxWeights.root']
     process.TnP_MuonID.InputFileNames = ['../tnpJPsi_officialBPHMC25ns_withAllTagVars_withNVtxWeightsFromGolden.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_officialBPHMC25ns_withNVtxWeightsFromGolden.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_officialBPHMC25ns_withNVtxWeightsFromMuonPhys.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_officialBPHMC25ns.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_officialBPHMC25ns.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_officialBPHMC_withAllTagVars.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_officialBPHMC_vertexingTriggersFlags.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_officialBPHMC_OniaTriggersFlags.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_officialBPHMC.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_officialBPHMC_30M.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_officialBPHMC_Mu8.root'] # Mu8 test
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_MC_total.root']
     #process.TnP_MuonID.InputFileNames = ['root://cmsxrootd.fnal.gov///store/user/lecriste/TnP/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/crab_TnP_MC_request/150710_153845/0000/tnpJPsi_MC_1.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_MC_Monika.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_MC_benchmark_10k.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_MC_Mu8.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_MC_noFilter.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_MC.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_MC_oldMatching.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_MC_oldTriggers.root']

if "25ns" in process.TnP_MuonID.InputFileNames[0]:
     mode = "25ns_"
else: mode = ""

#ALLBINS =  [("plateau_abseta",PLATEAU_ABSETA)]
#ALLBINS =  [("pt_eta",PT_ETA_BINS)]
#ALLBINS =  [("pt_abseta",PT_ABSETA_BINS)]
#ALLBINS =  [("pt_abseta_seagull",PT_ABSETA_BINS_SEAGULL), ("pt_abseta_cowboy",PT_ABSETA_BINS_COWBOY)]
#ALLBINS =  [("pt_abseta_allPairs",PT_ABSETA_BINS_allPairs)]
#ALLBINS =  [("pt_abseta_notSeparated",PT_ABSETA_BINS_notSeparated)]
ALLBINS =  [("pt_abseta_notSeparated",PT_ABSETA_BINS_notSeparated), ("pt_abseta_seagull",PT_ABSETA_BINS_SEAGULL), ("pt_abseta_cowboy",PT_ABSETA_BINS_COWBOY)]
#ALLBINS =  [("pt_abseta_separated",PT_ABSETA_BINS_allPairs), ("pt_abseta_seagull_separated",PT_ABSETA_BINS_SEAGULL_separated), ("pt_abseta_cowboy_separated",PT_ABSETA_BINS_COWBOY_separated)]
#ALLBINS =  [("pt_eta2p4_notSeparated",PT_BINS_notSeparated)]
#ALLBINS =  [("pt_abseta2p4",PT_BINS_ABSETA2p4)]
#ALLBINS =  [("pt_abseta_notSeparated",PT_ABSETA_BINS_notSeparated),("pt_eta2p4_notSeparated",PT_BINS_notSeparated)]
#ALLBINS =  [("pt_abseta_notSeparated_allPairs",PT_ABSETA_BINS_notSeparated_allPairs)]
#ALLBINS =  [("ptTurnOn_abseta",TURNON_ABSETA)]
#ALLBINS =  [("pt_abseta",PT_ABSETA_BINS), ("plateau_abseta",PLATEAU_ABSETA)]
#ALLBINS =  [("vtx",VTX_BINS)]
#ALLBINS =  [("vtx",VTX_BINS_noSoft)]
#ALLBINS =  [("plateau_abseta",PLATEAU_ABSETA), ("vtx",VTX_BINS), ("eta",ETA_BINS)]
#ALLBINS =  [("pt_abseta",PT_ABSETA_BINS), ("vtx",VTX_BINS), ("eta",ETA_BINS)]
#ALLBINS =  [("pt_abseta",PT_ABSETA_BINS), ("vtx",VTX_BINS), ("plateau",PLATEAU_ABSETA)]
#ALLBINS += [("pt_abseta_wide",PT_ABSETA_WIDE)]
#ALLBINS =  [("ptPlateau_eta",PLATEAU_ETA)]

triggerEff = True
#triggerEff = False
Mu25_test = False
#Mu25_test = True
Mu16_test = False
if "Mu16" in process.TnP_MuonID.InputFileNames[0]:
     Mu16_test = True

print "Going to define TagProbeFitTreeAnalyzer for " + ', '.join(IDS) + " efficiency (trigger efficiency is " + str(triggerEff) + ")\nusing as input file: " + process.TnP_MuonID.InputFileNames[0]

for ID in IDS:
     #if len(args) > 1 and args[1] in IDS and ID != args[1]: continue
     if len(args) > 1 and ID != args[1]: continue
     for X,B in ALLBINS:
          if len(args) > 2 and X not in args[2:]: continue
          module = process.TnP_MuonID.clone(OutputFileName = cms.string(
                    "TnP_MuonID__%s_%s_%s_%s.root" %(scenario, mode, ID, X)))
          if "Mu8" in process.TnP_MuonID.InputFileNames[0]:
               #module.OutputFileName = module.OutputFileName.replace(".root","_Mu8.root")
               module.OutputFileName = cms.string(
                    "TnP_MuonID__%s_%s_%s_%s_Mu8.root" %(scenario, mode, ID, X))
          #DEN = B.clone()
          #setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
          #          EfficiencyCategoryAndState = cms.vstring(ID,"above"),     # ??
          #          UnbinnedVariables = UnbinnedVars,
          #          BinnedVariables = DEN,
          #          BinToPDFmap = cms.vstring("signalPlusBkg")
          #          )
          #        )
          #
          for PTMIN, TRIG in TRIGS:
               TRIGLABEL=""
               #if "pt_" in X:
               if "pt" in X or "vtx" in X:
                    TRIGLABEL="_"+TRIG
               else:
                    #if TRIG != "Mu7p5_Track2_Jpsi": continue # use only one trigger except for turn-on ("turn-on" = ""pt_" in X")
                    if TRIG != "Mu7p5_Track7_Jpsi" and TRIG != "Mu8": continue # use only one trigger except for turn-on ("turn-on" = ""pt_" in X")
               DEN = B.clone()
               if hasattr(DEN, "pt"):
                    DEN.pt = cms.vdouble(*[i for i in B.pt if i >= PTMIN])
                    if len(DEN.pt) == 0: raise RuntimeError, "Make sure PTMIN is less than at least one B.pt element!"
                    if len(DEN.pt) == 1: DEN.pt = cms.vdouble(PTMIN, DEN.pt[0])
               DEN_forSoftID = DEN.clone()
               DEN_withSoftID = DEN.clone( # check variables bounds if input file changes
                                          TMOST = cms.vstring("pass"), tkTrackerLay = cms.vint32(6,18), tkPixelLay = cms.vint32(1,5), dzPV = cms.vdouble(-20,20), dB = cms.vdouble(-0.3,0.3), Track_HP = cms.vstring("pass"),
                                          )
               DEN_forL1L2 = DEN_withSoftID.clone()
               if TRIG != "Mu8":
                    setattr(DEN_forSoftID, "tag_%s_MU" %TRIG, cms.vstring("pass"))
                    setattr(DEN_forSoftID,     "%s_TK" %TRIG, cms.vstring("pass"))
                    setattr(DEN_forL1L2, "tag_%s_MU" %TRIG, cms.vstring("pass"))
                    setattr(DEN_forL1L2,     "%s_TK" %TRIG, cms.vstring("pass"))
               else:
                    setattr(DEN_forSoftID, "tag_%s" % TRIG, cms.vstring("pass"))
                    #setattr(DEN_forSoftID,     "%s" % TRIG, cms.vstring("pass"))
               #setattr(DEN_forSoftID, "TM", cms.vstring("pass"))
               #if "calomu" in scenario: DEN_forSoftID.Calo = cms.vstring("pass")
               setattr(module.Efficiencies, ID+"_"+X+TRIGLABEL, cms.PSet(
                         EfficiencyCategoryAndState = cms.vstring(ID,"above"),     # ??
                         UnbinnedVariables = UnbinnedVars,
                         BinnedVariables = DEN_forSoftID,
                         BinToPDFmap = cms.vstring("signalPlusBkg")
                         ))
               # L1L2 w.r.t. SoftMuon ID
               absetaMax = 1.6
               if Mu25_test:
                    # Mu25
		    DEN_Mu25 = DEN_withSoftID.clone( tag_abseta = cms.vdouble(0.0, absetaMax), tag_Mu25TkMu0Onia_L3_MU = cms.vstring("pass"), Mu25TkMu0Onia_TM = cms.vstring("pass") )
                    if hasattr(DEN_Mu26, "abseta"):
                         DEN_Mu26.abseta = cms.vdouble(*[i for i in DEN.abseta if i < absetaMax])
                         DEN_Mu26.abseta.append(absetaMax)
		    setattr(module.Efficiencies, "Mu25_"+X, cms.PSet(
                    	    EfficiencyCategoryAndState = cms.vstring("Dimuon10_Jpsi_Barrel","pass"),
                            UnbinnedVariables = UnbinnedVars,
                            BinnedVariables = DEN_Mu25,
                            BinToPDFmap = cms.vstring("signalPlusBkg"),
                            ))
               if Mu16_test:
                    # Mu16
                    DEN_Mu16 = DEN_withSoftID.clone( tag_abseta = cms.vdouble(0.0, absetaMax), tag_Mu16TkMu0Onia_L3_MU = cms.vstring("pass"), Mu16TkMu0Onia_TM = cms.vstring("pass") )
                    if hasattr(DEN_Mu16, "abseta"):
                         DEN_Mu16.abseta = cms.vdouble(*[i for i in DEN.abseta if i < absetaMax])
                         DEN_Mu16.abseta.append(absetaMax)
                    setattr(module.Efficiencies, "Mu16_"+X, cms.PSet(
                            #EfficiencyCategoryAndState = cms.vstring("Dimuon10_Jpsi_Barrel","pass"), # L3 filter
                            #EfficiencyCategoryAndState = cms.vstring("Dimuon10_L1L2","pass"), # L2 filter
                            EfficiencyCategoryAndState = cms.vstring("Dimuon10_L1L2","pass", "Mu_L3","pass"), # L2 + Mu_L3 filter
                            UnbinnedVariables = UnbinnedVars,
                            BinnedVariables = DEN_Mu16,
                            BinToPDFmap = cms.vstring("signalPlusBkg"),
                            ))

               if triggerEff:
                    # for L3
                    DEN_forL3 = DEN_withSoftID.clone()
                    setattr(DEN_forL3, "tag_Mu7p5_L2Mu2_Jpsi_MU", cms.vstring("pass"))
                    #
                    #tag_pt_min = 10.0 # for full-coverage trigger
                    tag_pt_min = 11.0 # for full-coverage trigger
                    for L1L2, DEN_L1L2, DEN_L3 in [("Dimuon16_L1L2",DEN_forL1L2.clone(tag_pt = cms.vdouble(tag_pt_min, 1000.0)),DEN_forL3.clone(tag_pt = cms.vdouble(tag_pt_min, 1000.0))),
                                                   ("Dimuon10_L1L2",DEN_forL1L2.clone(tag_abseta = cms.vdouble(0.0, absetaMax)),DEN_forL3.clone(tag_abseta = cms.vdouble(0.0, absetaMax)))]: 
                         if "Dimuon10" in L1L2:
                              if hasattr(DEN_L1L2, "abseta"):
                                   DEN_L1L2.abseta = cms.vdouble(*[i for i in DEN.abseta if i < absetaMax])
                                   DEN_L1L2.abseta.append(absetaMax)
                              if hasattr(DEN_L3, "abseta"):
                                   DEN_L3.abseta = DEN_L1L2.abseta
                         setattr(module.Efficiencies, L1L2+"_"+X+TRIGLABEL, cms.PSet(
                                   EfficiencyCategoryAndState = cms.vstring(L1L2,"pass"),
                                   UnbinnedVariables = UnbinnedVars,
                                   BinnedVariables = DEN_L1L2,
                                   BinToPDFmap = cms.vstring("signalPlusBkg"),
                                   ))
                         # L3 w.r.t. L1L2
                         setattr(DEN_L3, L1L2, cms.vstring("pass"))
                         setattr(module.Efficiencies, "L3_wrt_"+L1L2+"_"+X, cms.PSet(
                                   EfficiencyCategoryAndState = cms.vstring("Mu_L3","pass"),
                                   UnbinnedVariables = UnbinnedVars,
                                   BinnedVariables = DEN_L3,
                                   BinToPDFmap = cms.vstring("signalPlusBkg"),
                                   ))
               #if "plateau" in X: module.SaveWorkspace = True
               ## mc efficiency, if scenario is mc
               #if "mc" in scenario:
               #     setattr(module.Efficiencies, ID+"_"+X+TRIGLABEL+"_mcTrue", cms.PSet(
               #         EfficiencyCategoryAndState = cms.vstring(ID,"above"),  # ?? "pass"
               #         UnbinnedVariables = UnbinnedVars,
               #         BinnedVariables = DEN.clone(mcTrue = cms.vstring("true"))
               #     ))
          # comment the following two lines to not run this efficiency
          #setattr(process, "TnP_MuonID__"+ID+"_"+X, module)
          #setattr(process, "run_"+ID+"_"+X, cms.Path(module))



########## Tracking efficiency ########## 
#ALLBINS =  [("pt_abseta_notSeparated_allPairs",PT_ABSETA_BINS_notSeparated_allPairs)]
TRIGS = [ (2,'Mu7p5_L2Mu2_Jpsi') ]
matches = [(1.0,0.4), (0.7,0.3), (0.5,0.2), (0.3,0.15), (0.1,0.1)]
#effs    = ["", "_NoJPsi", "_NoBestJPsi"]
effs    = [""]

process.TnP_Tracking = Template.clone(
     #InputFileNames = cms.vstring('/afs/cern.ch/work/l/lecriste/TnP/recipe_740/CMSSW_7_4_0/src/MuonAnalysis/TagAndProbe/test/jpsi/tnpJPsi_Charmonium_PromptReco_50ns_first47ipb_correctL2.root'),
     InputFileNames = process.TnP_MuonID.InputFileNames,
     InputDirectoryName = cms.string("tpTreeSta"),
     InputTreeName = cms.string("fitter_tree"),
     OutputFileName = cms.string("TnP_Tracking_%s.root" % scenario),
     Efficiencies = cms.PSet(),
     #Cuts = cms.PSet(),
)
if "mc" in scenario:
     process.TnP_Tracking.InputFileNames = process.TnP_MuonID.InputFileNames

#sampleToPdfMap = { "":"gaussPlusCubic", "NoJPsi":"gaussPlusFloatCubic", "NoBestJPsi":"gaussPlusFloatCubic"}
sampleToPdfMap = { "":"signalPlusBkg", "NoJPsi":"gaussPlusFloatCubic", "NoBestJPsi":"gaussPlusFloatCubic"}

for X,B in ALLBINS:
     if len(args) > 2 and X not in args[2:]: continue
     module = process.TnP_Tracking.clone(OutputFileName = cms.string("TnP_Tracking__%s_%s_%s.root" % (scenario, mode, X)))
     #
     for PTMIN, TRIG in TRIGS:
          TRIGLABEL=""
          #if "pt_" in X:
          if "pt" in X or "vtx" in X:
               TRIGLABEL="_"+TRIG
          else:
               #if TRIG != "Mu7p5_Track2_Jpsi": continue # use only one trigger except for turn-on ("turn-on" = ""pt_" in X")
               if TRIG != "Mu7p5_Track7_Jpsi" and TRIG != "Mu8": continue # use only one trigger except for turn-on ("turn-on" = ""pt_" in X")
          DEN = B.clone()
          if hasattr(DEN, "pt"):
               DEN.pt = cms.vdouble(*[i for i in B.pt if i >= PTMIN])
               if len(DEN.pt) == 0: raise RuntimeError, "Make sure PTMIN is less than at least one B.pt element!"
               if len(DEN.pt) == 1: DEN.pt = cms.vdouble(PTMIN, DEN.pt[0])
          setattr(DEN, "tag_%s_MU" %TRIG, cms.vstring("pass"))
          setattr(DEN,     "%s_L2" %TRIG, cms.vstring("pass"))
          #
          for (DR, DETA) in matches:
               label = "DR%.1f_DEta%.1f" % (DR, DETA)
               #if len(args) > 1 and args[1] != label: 
               #     print "Skipping "+label
               #     continue
               for eff in effs:
                    label = label.replace(".","p") + eff
                    #
                    setattr(module.Cuts, "#DeltaR_cut",   cms.vstring("tk_deltaR"+eff, "tk_deltaR"+eff, str(DR)))
                    setattr(module.Cuts, "#Delta#eta_cut", cms.vstring("tk_deltaEta"+eff, "tk_deltaEta"+eff, str(DETA)))
                    setattr(module.Efficiencies, "eff_"+label, cms.PSet(
                              EfficiencyCategoryAndState = cms.vstring("#DeltaR_cut","below", "#Delta#eta_cut","below"),
                              UnbinnedVariables = UnbinnedVars,
                              BinToPDFmap = cms.vstring(sampleToPdfMap[eff.replace("_","")]),
                              BinnedVariables = DEN,
                              ))
     #setattr(process, "TnP_Tracking__"+X, module)
     #setattr(process, "p_TnP_Tracking_"+X, cms.Path(module))


########## Vertexing efficiency ########## 
if triggerEff:
     ALLBINS =  [("pt_absrapidity_notSeparated",PT_ABSY_BINS_notSeparated_pair),("pt_absrapidityLarge_notSeparated",PT_ABSYLARGE_BINS_notSeparated_pair)]
     TRIGS = [ (16,'Dimuon6_Jpsi_NoVertexing','Dimuon16_Jpsi'), (10,'Dimuon0er16_Jpsi_NoVertexing','Dimuon10_Jpsi_Barrel') ]

     process.TnP_Vertexing = Template.clone(
          #InputFileNames = cms.vstring('/afs/cern.ch/work/l/lecriste/TnP/recipe_740/CMSSW_7_4_0/src/MuonAnalysis/TagAndProbe/test/jpsi/tnpJPsi_Charmonium_PromptReco_50ns_first47ipb_correctL2.root'),
          InputFileNames = process.TnP_MuonID.InputFileNames,
          InputDirectoryName = cms.string("tpTreeOnePair"),
          InputTreeName = cms.string("fitter_tree"),
          OutputFileName = cms.string("TnP_Vertexing_%s.root" % scenario),
          Efficiencies = cms.PSet(),
          )
     if "mc" in scenario:
          process.TnP_Vertexing.InputFileNames = process.TnP_MuonID.InputFileNames

     for X,B in ALLBINS:
          if len(args) > 2 and X not in args[2:]: continue
          module = process.TnP_Vertexing.clone(OutputFileName = cms.string("TnP_Vertexing__%s_%s_%s.root" % (scenario, mode, X)))
          #
          for PTMIN, TRIG_noVtx, TRIG in TRIGS:
               TRIGLABEL="_"+TRIG
               #
               DEN = B.clone()
               if hasattr(DEN, "pair_pt"):
                    DEN.pair_pt = cms.vdouble(*[i for i in B.pair_pt if i >= PTMIN])
                    if len(DEN.pair_pt) == 0: raise RuntimeError, "Make sure PTMIN is less than at least one B.pt element!"
                    if len(DEN.pair_pt) == 1: DEN.pair_pt = cms.vdouble(PTMIN, DEN.pair_pt[0])
               setattr(DEN, "tag_%s" %TRIG_noVtx, cms.vstring("pass"))
               setattr(DEN,     "%s" %TRIG_noVtx, cms.vstring("pass"))
               #
               if "er16" in TRIG_noVtx:
                    absyMax = 1.6
                    if hasattr(DEN, "pair_absrapidity"):
                         DEN.pair_absrapidity = cms.vdouble(*[i for i in B.pair_absrapidity if i < absyMax])
                         DEN.pair_absrapidity.append(absyMax)
                         #DEN = DEN.clone(abseta = cms.vdouble(0.0, absyMax))
                         #DEN = DEN.clone(tag_abseta = cms.vdouble(0.0, absyMax))
               #
               setattr(module.Efficiencies, TRIG+"_wrt_"+TRIG_noVtx, cms.PSet(
                         EfficiencyCategoryAndState = cms.vstring(TRIG,"pass"),
                         UnbinnedVariables = UnbinnedVars,
                         BinToPDFmap = cms.vstring("signalPlusBkg"),
                         BinnedVariables = DEN,
                         ))
          # comment the following two lines to not run this efficiency
          setattr(process, "TnP_Vertexing__"+X, module)
          setattr(process, "p_TnP_vertexing_"+X, cms.Path(module))


print "End of configuration file"
