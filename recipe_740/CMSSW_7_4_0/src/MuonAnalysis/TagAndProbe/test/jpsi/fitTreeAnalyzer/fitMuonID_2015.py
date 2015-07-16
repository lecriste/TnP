import FWCore.ParameterSet.Config as cms

### USAGE:
###    cmsRun fitMuonID.py <scenario>
### scenarios:
###   - data_all (default)
###   - signal_mc

import sys
args = sys.argv[1:]
if (sys.argv[0] == "cmsRun"): args =sys.argv[2:]
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

Template = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
    NumCPU = cms.uint32(1),
    SaveWorkspace = cms.bool(False),
    Variables = cms.PSet(
        mass = cms.vstring("Tag-muon Mass", "2.9", "3.3", "GeV/c^{2}"), #2.8-3.35
        p  = cms.vstring("muon p", "0", "1000", "GeV/c"),
        pt = cms.vstring("muon p_{T}", "0", "1000", "GeV/c"),
        eta = cms.vstring("muon #eta", "-2.5", "2.5", ""),
        abseta = cms.vstring("muon |#eta|", "0", "2.5", ""),
        tag_pt = cms.vstring("Tag p_{T}",    "0", "1000", "GeV/c"),
        tag_nVertices = cms.vstring("Number of vertices", "0", "999", ""),
        tag_nVerticesDA = cms.vstring("Number of vertices", "0", "999", ""),
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
        # Added by Monika Sharma for mediumVar
        validFraction = cms.vstring("innerTrack.validFraction","-9999","9999",""),
        chi2LPosition = cms.vstring("combinedQuality.chi2LocalPosition","-9999","9999",""),
        tkKink = cms.vstring("combinedQuality.trkKink","-9999","9999",""),
        segmComp = cms.vstring("segmentCompatibility","-1","5","")
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
        Tight2012 = cms.vstring("Tight Muon", "dummy[pass=1,fail=0]"),
        Mu7p5_Track2_Jpsi_TK = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        tag_Mu7p5_Track2_Jpsi_MU = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        Mu7p5_Track3p5_Jpsi_TK = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        tag_Mu7p5_Track3p5_Jpsi_MU = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        Mu7p5_Track7_Jpsi_TK = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        tag_Mu7p5_Track7_Jpsi_MU = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        Mu7p5_L2Mu2_Jpsi_TK = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        tag_Mu7p5_L2Mu2_Jpsi_MU = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        # test
        DoubleMu17TkMu8_TkMu8leg = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        tag_DoubleMu17TkMu8_TkMu8leg = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
        Mu8 = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        tag_Mu8 = cms.vstring("ProbeTrigger_Track0", "dummy[pass=1,fail=0]"),
        ),

    Expressions = cms.PSet(
     LooseVar = cms.vstring("LooseVar", "PF==1 && (Glb==1 || TM==1) ", "PF", "Glb", "TM"),
     oldSoftVar = cms.vstring("oldSoftVar", "TMOST ==1 && tkTrackerLay > 5 && tkPixelLay > 1 && tkChi2 < 1.8 && abs(dzPV) < 30 && abs(dB) < 3", "TMOST","tkTrackerLay", "tkPixelLay", "tkChi2", "dzPV", "dB"),
     MediumVar = cms.vstring("MediumVar", "Loose==1 && validFraction > 0.8 && ((Glb==1 && glbChi2 < 3 && chi2LPosition < 12 && tkKink < 20 && segmComp > 0.303) || segmComp> 0.451)", "Loose", "validFraction", "Glb", "glbChi2", "chi2LPosition", "tkKink", "segmComp"),
     TightVar = cms.vstring("TightVar", "PF==1 && Glb==1 && tkChi2 < 10 && glbValidMuHits > 0 && numberOfMatchedStations > 1 && abs(dB) < 0.2 && abs(dzPV) < 0.5 && tkValidPixelHits > 0 && tkTrackerLay > 5", "PF", "Glb", "tkChi2", "glbValidMuHits", "numberOfMatchedStations", "dB",  "dzPV", "tkValidPixelHits", "tkTrackerLay" ),
     #newID
     SoftVar = cms.vstring("SoftVar", "TMOST ==1 && tkTrackerLay > 5 && tkPixelLay > 0 && abs(dzPV) < 20 && abs(dB) < 0.3 && Track_HP == 1", "TMOST","tkTrackerLay", "tkPixelLay", "dzPV", "dB", "Track_HP"),
     ),

    Cuts = cms.PSet(
     Loose2012 = cms.vstring("Loose", "LooseVar", "0.5"),
     Tight2012 = cms.vstring("Tight", "TightVar", "0.5"),
     oldSoft2012 = cms.vstring("oldSoft", "oldSoftVar", "0.5"),
     Soft2012 = cms.vstring("Soft", "SoftVar", "0.5"),
    ),

    PDFs = cms.PSet(
        signalPlusBkg = cms.vstring(
            "CBShape::signal(mass, mean[3.1,3.0,3.2], sigma[0.05,0.02,0.06], alpha[3., 0.5, 5.], n[1, 0.1, 100.])",
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

# pick muons that bend apart from each other
SEPARATED = cms.PSet(pair_drM1 = cms.vdouble(0.5,10),
                     pair_probeMultiplicity = cms.vdouble(0.5,1.5),
                     )

PT_ETA_BINS = cms.PSet(SEPARATED,
                       #pt = cms.vdouble(2.0, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.5, 5.0, 6.0, 8.0, 10.0, 15.0, 20.0),
                       pt = cms.vdouble(2.0, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.5, 5.0, 6.0, 8.0, 10.0, 15.0, 20.0, 30.0, 40.0),
                       #abseta = cms.vdouble(0.0,0.9,1.2,2.1)
                       abseta = cms.vdouble(0.0,0.9,1.2,2.1,2.4)
                       )

VTX_BINS = cms.PSet(SEPARATED,
                    abseta = cms.vdouble(0.0, 2.1),
                    pt     = cms.vdouble(8.0, 20.0),
                    tag_nVertices = cms.vdouble(0.5,2.5,4.5,6.5,8.5,10.5,12.5,14.5,16.5,18.5,20.5,22.5,24.5,26.5,28.5,30.5)
                    )

ETA_BINS = cms.PSet(SEPARATED,
                    pt     = cms.vdouble(8.0, 20.0),
                    eta = cms.vdouble(-2.1,-1.6,-1.2,-0.9,-0.6,-0.3,-0.2,0.2,0.3,0.6,0.9,1.2,1.6,2.1,),
                    )

PLATEAU_ABSETA = cms.PSet(SEPARATED,
                    abseta = cms.vdouble(0.0, 0.9, 1.2, 2.1),
                    pt     = cms.vdouble(8.0, 20.0),
                    )

PT_ABSETA_WIDE = cms.PSet(SEPARATED,
                          abseta = cms.vdouble(0.0, 1.2, 2.4),
                          pt     = cms.vdouble(5.0, 7.0, 20.0),
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
    InputFileNames = cms.vstring('/afs/cern.ch/user/m/msharma/public/tnpJPsi_Data.root'),

    InputTreeName = cms.string("fitter_tree"),
    InputDirectoryName = cms.string("tpTree"),
    #InputDirectoryName = cms.string("tpTreeSta"),
    OutputFileName = cms.string("TnP_MuonID_%s.root" % scenario),
    Efficiencies = cms.PSet(),
)

IDS = ["Soft2012"]
TRIGS = [ (2,'Mu7p5_L2Mu2_Jpsi'), (2,'Mu7p5_Track2_Jpsi'), (3.5,'Mu7p5_Track3p5_Jpsi'), (7,'Mu7p5_Track7_Jpsi') ]
#TRIGS = [ (0,'Mu8') ]

if "mc" in scenario:
     process.TnP_MuonID.InputFileNames = ['root://cmsxrootd.fnal.gov///store/user/lecriste/TnP/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/crab_TnP_MC_request/150710_153845/0000/tnpJPsi_MC_1.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_MC_Mu8.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_MC_Monika.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_MC_benchmark_10k.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_MC_Mu8.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_MC_noFilter.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_MC.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_MC_oldMatching.root']
     #process.TnP_MuonID.InputFileNames = ['../tnpJPsi_MC_oldTriggers.root']

ALLBINS =  [("pt_abseta",PT_ETA_BINS)]

for ID in IDS:
     if len(args) > 1 and args[1] in IDS and ID != args[1]: continue
     for X,B in ALLBINS:
          if len(args) > 2 and X not in args[2:]: continue
          module = process.TnP_MuonID.clone(OutputFileName = cms.string("TnP_MuonID_%s_%s_%s.root" % (scenario, ID, X)))
          #
          DEN = B.clone()
          setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
                    EfficiencyCategoryAndState = cms.vstring(ID,"above"),     # ??
                    UnbinnedVariables = cms.vstring("mass"),
                    BinnedVariables = DEN,
                    BinToPDFmap = cms.vstring("signalPlusBkg")
                    )
                  )
          #
          for PTMIN, TRIG in TRIGS:
               TRIGLABEL=""
               if "pt_" in X:
                    TRIGLABEL="_"+TRIG
               else:
                    if TRIG != "Mu7p5_Track2": continue # use only one trigger except for turn-on
               DEN = B.clone()
               if hasattr(DEN, "pt"):
                    DEN.pt = cms.vdouble(*[i for i in B.pt if i >= PTMIN])
                    if len(DEN.pt) == 1: DEN.pt = cms.vdouble(PTMIN, DEN.pt[0])
               if TRIG != "Mu8":
                    setattr(DEN, "tag_%s_MU" % TRIG, cms.vstring("pass"))
                    setattr(DEN,     "%s_TK" % TRIG, cms.vstring("pass"))
               else:
                    setattr(DEN, "tag_%s" % TRIG, cms.vstring("pass"))
                    setattr(DEN,     "%s" % TRIG, cms.vstring("pass"))
               #setattr(DEN, "TM", cms.vstring("pass"))
               #if "calomu" in scenario: DEN.Calo = cms.vstring("pass")
               setattr(module.Efficiencies, ID+"_"+X+TRIGLABEL, cms.PSet(
                   EfficiencyCategoryAndState = cms.vstring(ID,"above"),     # ??
                   UnbinnedVariables = cms.vstring("mass"),
                   BinnedVariables = DEN,
                   BinToPDFmap = cms.vstring("signalPlusBkg")
               ))
               if "mc" in scenario:
                    setattr(module.Efficiencies, ID+"_"+X+TRIGLABEL+"_mcTrue", cms.PSet(
                        EfficiencyCategoryAndState = cms.vstring(ID,"above"),  # ?? "pass"
                        UnbinnedVariables = cms.vstring("mass"),
                        BinnedVariables = DEN.clone(mcTrue = cms.vstring("true"))
                    ))
          setattr(process, "TnP_MuonID_"+ID+"_"+X, module)
          setattr(process, "run_"+ID+"_"+X, cms.Path(module))

