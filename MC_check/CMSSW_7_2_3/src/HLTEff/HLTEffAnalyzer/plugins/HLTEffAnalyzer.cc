// -*- C++ -*-
//
// Package:    HLTEff/HLTEffAnalyzer
// Class:      HLTEffAnalyzer
// 
/**\class HLTEffAnalyzer HLTEffAnalyzer.cc HLTEff/HLTEffAnalyzer/plugins/HLTEffAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Raffaella Radogna
//         Created:  Thu, 05 Mar 2015 14:17:53 GMT
//
//


// system include files
#include <memory>
#include <fstream>
#include <sys/time.h>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <math.h>

// root include files
#include "TFile.h"
#include "TH1F.h"
#include "TH2F.h"

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "Geometry/Records/interface/GlobalTrackingGeometryRecord.h"
#include "Geometry/CommonDetUnit/interface/GlobalTrackingGeometry.h"
#include "Geometry/CommonDetUnit/interface/GeomDet.h"

#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "DataFormats/TrajectorySeed/interface/TrajectorySeedCollection.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "RecoMuon/TrackingTools/interface/MuonPatternRecoDumper.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "SimDataFormats/Track/interface/SimTrackContainer.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"

#include "DataFormats/PatCandidates/interface/Muon.h"

#include "DataFormats/HLTReco/interface/TriggerObject.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "FWCore/Common/interface/TriggerNames.h"

#include "DataFormats/VertexReco/interface/Vertex.h"
#include <MuonAnalysis/MuonAssociators/interface/PropagateToMuon.h>

#include "TCanvas.h"
#include "TStyle.h"

//
// class declaration
//
class TFile;
class TH1F;
class TH2F;

using namespace edm;
using namespace std;
using namespace reco;

class HLTEffAnalyzer : public edm::EDAnalyzer {
public:
  explicit HLTEffAnalyzer(const edm::ParameterSet&);
  ~HLTEffAnalyzer();
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
  
private:
  virtual void beginJob() override;
  virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
  virtual void endJob() override;
  
  virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
  //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
  //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
  //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
  
  // ----------member data ---------------------------
  map<string,TH1F*> histContainer_ ;
  map<string,TH2F*> histContainer2D_ ;

  map<string,TH1I*> muonFromJpsi_h ;
  map<string,TH1F*> pT_muonFromJpsi_h, eta_muonFromJpsi_h ;
  map<string,TH1F*> pT_muonFromJpsi[3] ;

  map<string,TH1F*> muons_deltaR_h ;
  map<string,TH1F*> pT_denominator_h, eta_denominator_h, nVtx_denominator_h ;
  map<string,TH1F*> pT_denominator[3], eta_denominator[1], nVtx_denominator[5] ;
  map<string,TH1F*> pT_numerator_h, eta_numerator_h/*, nVtx_numerator_h*/ ;
  map<string,TH1F*> pT_numerator[3], eta_numerator[1]/*, nVtx_numerator[3]*/ ;
  map<string,TH1F*> pT_matchingEff_h, eta_matchingEff_h/*, nVtx_matchingEff_h*/ ;
  map<string,TH1F*> pT_matchingEff[3], eta_matchingEff[1]/*, nVtx_matchingEff[1]*/ ;
  map<string,TH1F*> pT_newSoftMuon_h, eta_newSoftMuon_h, nVtx_newSoftMuon_h ;
  map<string,TH1F*> pT_newSoftMuon[3], eta_newSoftMuon[1], nVtx_newSoftMuon[5] ;  
  map<string,TH1F*> pT_newSoftMuonEff_h, eta_newSoftMuonEff_h, nVtx_newSoftMuonEff_h ;
  map<string,TH1F*> pT_newSoftMuonEff[3], eta_newSoftMuonEff[1], nVtx_newSoftMuonEff[5] ;

  string dataset, theDataType;
  EDGetTokenT<vector<Vertex>> vtxHT_;
  EDGetTokenT<View<GenParticle> > prunedGenToken_;

  //InputTag muonLabel_;
  EDGetTokenT<pat::MuonCollection> muonToken_; // miniAOD
  //EDGetTokenT<reco::MuonCollection> muonToken_; // AOD
  InputTag triggerResultsTag_;
  InputTag triggerEvent_;
  HLTConfigProvider hltConfig;

  int deltaR_bins;
  double deltaR_binMin, deltaR_binMax;
  vector<double> pT_bins, eta_bins, nVtx_bins ;
  PropagateToMuon prop1_, prop2_;
  double deltaR_cowBoys, deltaR_max ;
  bool Debug ;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
HLTEffAnalyzer::HLTEffAnalyzer(const edm::ParameterSet& iConfig):
histContainer_(),
histContainer2D_(),

muonFromJpsi_h(),
pT_muonFromJpsi_h(), eta_muonFromJpsi_h(),
pT_muonFromJpsi(),

muons_deltaR_h(),
pT_denominator_h(), eta_denominator_h(), nVtx_denominator_h(),
pT_denominator(), eta_denominator(), nVtx_denominator(),
pT_numerator_h(), eta_numerator_h(), //nVtx_numerator_h(),
pT_numerator(), eta_numerator(), //nVtx_numerator(),
pT_matchingEff_h(), eta_matchingEff_h(), //nVtx_matchingEff_h(),
pT_matchingEff(), eta_matchingEff(), //nVtx_matchingEff(),
pT_newSoftMuon_h(), eta_newSoftMuon_h(), nVtx_newSoftMuon_h(),
pT_newSoftMuon(), eta_newSoftMuon(), nVtx_newSoftMuon(),
pT_newSoftMuonEff_h(), eta_newSoftMuonEff_h(), nVtx_newSoftMuonEff_h(),
pT_newSoftMuonEff(), eta_newSoftMuonEff(), nVtx_newSoftMuonEff(),
prop1_(iConfig.getParameter<edm::ParameterSet>("propM1")),
prop2_(iConfig.getParameter<edm::ParameterSet>("propM2"))
{
   //now do what ever initialization is needed
    dataset = iConfig.getUntrackedParameter<string>("dataset") ;
    theDataType = iConfig.getUntrackedParameter<string>("DataType") ;
    vtxHT_ = consumes< vector<reco::Vertex> >( iConfig.getParameter< InputTag >("vtxTag") ) ;
    prunedGenToken_ = consumes< View< GenParticle > >(iConfig.getParameter< InputTag >("pruned")) ;
    //muonLabel_ = iConfig.getUntrackedParameter<edm::InputTag>("MuonCollectionLabel");
    muonToken_ = consumes<pat::MuonCollection>(iConfig.getParameter< InputTag >("MuonCollectionLabel")) ; // miniAOD
    //muonToken_ = consumes<reco::MuonCollection>(iConfig.getParameter< InputTag >("MuonCollectionLabel")) ; // AOD
    triggerResultsTag_ = iConfig.getParameter< InputTag >("triggerResultsTag");
    triggerEvent_ = iConfig.getParameter< InputTag >("triggerEvent");

    deltaR_bins = iConfig.getParameter< int >("deltaR_bins");
    deltaR_binMin = iConfig.getParameter< double >("deltaR_binMin");
    deltaR_binMax = iConfig.getParameter< double >("deltaR_binMax");
    pT_bins = iConfig.getParameter< vector<double> >("pT_bins");
    eta_bins = iConfig.getParameter< vector<double> >("eta_bins");
    nVtx_bins = iConfig.getParameter< vector<double> >("nVtx_bins");
    deltaR_cowBoys = iConfig.getParameter< double >("deltaR_cowBoys");
    deltaR_max = iConfig.getParameter< double >("deltaR_max");

    Debug = iConfig.getUntrackedParameter< bool >("Debug",false) ;    
    
    if (theDataType != "RealData" && theDataType != "SimData")
      if (Debug) cout<<"Error in Data Type!!"<<endl;

}


HLTEffAnalyzer::~HLTEffAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

//=======================================================================
void HLTEffAnalyzer::beginRun(edm::Run const& iRun, edm::EventSetup const& iSetup)
{
  /*
    bool changed = true;
    if (hltConfig.init(iRun, iSetup, triggerResultsTag_.process(), changed)) {
        // if init returns TRUE, initialisation has succeeded!
        edm::LogInfo("TriggerBlock") << "HLT config with process name "
        << triggerResultsTag_.process() << " successfully extracted";
    }
    else {
        // if init returns FALSE, initialisation has NOT succeeded, which indicates a problem
        // with the file and/or code and needs to be investigated!
        edm::LogError("TriggerBlock") << "Error! HLT config extraction with process name "
        << triggerResultsTag_.process() << " failed";
        // In this case, all access methods will return empty values!
    }
  */
  //prop1_.init(iSetup);
  //prop2_.init(iSetup);
}

// ------------ method called once each job just before starting event loop  ------------
void 
HLTEffAnalyzer::beginJob()
{
    // register to the TFileService
    edm::Service<TFileService> fs;
    TH1::SetDefaultSumw2();
    histContainer_["hPtSim"] = fs->make<TH1F>("pTSim","p_{T}^{gen} ",5000,0,5000);

    muonFromJpsi_h["nMuonFromJpsi"] = fs->make<TH1I>("nMuonFromJpsi","number of #mu with a J/#psi mother;n(#mu)",5,-0.5,4.5);
    pT_muonFromJpsi_h["pT_muonFromJpsi_h"] = fs->make<TH1F>("pT_muonFromJpsi","p_{T} of #mu with a J/#psi mother;p_{T}(#mu) [GeV]",/*70*/ pT_bins.size() -1,/*0.,140*/ &(pT_bins[0]));
    eta_muonFromJpsi_h["eta_muonFromJpsi_h"] = fs->make<TH1F>("eta_muonFromJpsi","#eta of #mu with a J/#psi mother;#eta(#mu) [GeV]",/*70*/ eta_bins.size() -1,/*0.,140*/ &(eta_bins[0]));
    //
    muons_deltaR_h["muons_deltaR_h"] = fs->make<TH1F>("muons_deltaR","#DeltaR between matched reco #mu;#DeltaR", deltaR_bins, deltaR_binMin, deltaR_binMax);
    // denominator
    pT_denominator_h["pT_denominator_h"] = fs->make<TH1F>("pT_denominator","p_{T} of matched gen #mu;p_{T}(#mu) [GeV]",pT_bins.size() -1, &(pT_bins[0]));
    pT_denominator[0]["pT_denominator"] = fs->make<TH1F>("pT_denominator_barrel","p_{T} of matched gen #mu with |#eta(#mu)|<0.9;p_{T}(#mu) [GeV]",pT_bins.size() -1, &(pT_bins[0]));
    pT_denominator[1]["pT_denominator"] = fs->make<TH1F>("pT_denominator_0p9to1p2","p_{T} of matched gen #mu with 0.9<|#eta(#mu)|<1.2;p_{T}(#mu) [GeV]",pT_bins.size() -1, &(pT_bins[0]));
    pT_denominator[2]["pT_denominator"] = fs->make<TH1F>("pT_denominator_endcap","p_{T} of matched gen #mu with 1.2<|#eta(#mu)|<2.1;p_{T}(#mu) [GeV]",pT_bins.size() -1, &(pT_bins[0]));
    eta_denominator_h["eta_denominator_h"] = fs->make<TH1F>("eta_denominator","#eta of matched gen #mu;#eta(#mu) [GeV]",eta_bins.size() -1, &(eta_bins[0]));
    eta_denominator[0]["eta_denominator"] = fs->make<TH1F>("eta_denominator_8to20","#eta of matched gen #mu with 8<p_{T}(#mu)<20 GeV;#eta(#mu)",eta_bins.size() -1, &(eta_bins[0]));
    nVtx_denominator_h["nVtx_denominator_h"] = fs->make<TH1F>("nVtx_denominator","# of reco vertex for matched #mu;# of vertices",nVtx_bins.size() -1, &(nVtx_bins[0]));
    nVtx_denominator[0]["nVtx_denominator"] = fs->make<TH1F>("nVtx_denominator_barrel","# of reco vertex for matched #mu with |#eta(#mu)|<0.9;# of vertices",nVtx_bins.size() -1, &(nVtx_bins[0]));
    nVtx_denominator[1]["nVtx_denominator"] = fs->make<TH1F>("nVtx_denominator_0p9to1p2","# of reco vertex for matched #mu with 0.9<|#eta(#mu)|<1.2;# of vertices",nVtx_bins.size() -1, &(nVtx_bins[0]));
    nVtx_denominator[2]["nVtx_denominator"] = fs->make<TH1F>("nVtx_denominator_endcap","# of reco vertex for matched #mu with 1.2<|#eta(#mu)|<2.1;# of vertices",nVtx_bins.size() -1, &(nVtx_bins[0]));
    nVtx_denominator[3]["nVtx_denominator"] = fs->make<TH1F>("nVtx_denominator_8to20","# of reco vertex for matched #mu with 8<p_{T}(#mu)<20 GeV;# of vertices",nVtx_bins.size() -1, &(nVtx_bins[0]));
    nVtx_denominator[4]["nVtx_denominator"] = fs->make<TH1F>("nVtx_denominator_8to20_max2p1","# of reco vertex for matched #mu with 8<p_{T}(#mu)<20 GeV && |#eta(#mu)|<2.1;# of vertices",nVtx_bins.size() -1, &(nVtx_bins[0]));

    pT_numerator_h["pT_numerator_h"] = fs->make<TH1F>("pT_numerator","p_{T} of matched reco #mu;p_{T}(#mu) [GeV]",pT_bins.size() -1, &(pT_bins[0]));
    pT_numerator[0]["pT_numerator"] = fs->make<TH1F>("pT_numerator_barrel","p_{T} of matched reco #mu with |#eta(#mu)|<0.9;p_{T}(#mu) [GeV]",pT_bins.size() -1, &(pT_bins[0]));
    pT_numerator[1]["pT_numerator"] = fs->make<TH1F>("pT_numerator_0p9to1p2","p_{T} of matched reco #mu with 0.9<|#eta(#mu)|<1.2;p_{T}(#mu) [GeV]",pT_bins.size() -1, &(pT_bins[0]));
    pT_numerator[2]["pT_numerator"] = fs->make<TH1F>("pT_numerator_endcap","p_{T} of matched reco #mu with 1.2<|#eta(#mu)|<2.1;p_{T}(#mu) [GeV]",pT_bins.size() -1, &(pT_bins[0]));
    eta_numerator_h["eta_numerator_h"] = fs->make<TH1F>("eta_numerator","#eta of matched reco #mu;#eta(#mu) [GeV]",eta_bins.size() -1, &(eta_bins[0]));
    eta_numerator[0]["eta_numerator"] = fs->make<TH1F>("eta_numerator_8to20","p_{T} of matched reco #mu with 8<p_{T}(#mu)<20 GeV;#eta(#mu)",eta_bins.size() -1, &(eta_bins[0]));
    //nVtx_numerator_h["nVtx_numerator_h"] = fs->make<TH1F>("nVtx_numerator","# of reco vertex for matched #mu;# of vertices",nVtx_bins.size() -1, &(nVtx_bins[0]));
    //nVtx_numerator[0]["nVtx_numerator"] = fs->make<TH1F>("nVtx_numerator_barrel","# of reco vertex for matched #mu with |#eta(#mu)|<0.9;# of vertices",nVtx_bins.size() -1, &(nVtx_bins[0]));
    //nVtx_numerator[1]["nVtx_numerator"] = fs->make<TH1F>("nVtx_numerator_0p9to1p2","# of reco vertex for matched #mu with 0.9<|#eta(#mu)|<1.2;# of vertices",nVtx_bins.size() -1, &(nVtx_bins[0]));
    //nVtx_numerator[2]["nVtx_numerator"] = fs->make<TH1i>("nVtx_numerator_endcap","# of reco vertex for matched #mu with 1.2<|#eta(#mu)|<2.1;# of vertices",nVtx_bins.size() -1, &(nVtx_bins[0]));

    pT_matchingEff_h["pT_matchingEff_h"] = fs->make<TH1F>("pT_matchingEff","matching efficiency vs p_{T}(#mu);p_{T}(#mu) [GeV]",pT_bins.size() -1, &(pT_bins[0]));
    pT_matchingEff[0]["pT_matchingEff"] = fs->make<TH1F>("pT_matchingEff_barrel","matching efficiency vs p_{T}(#mu) with |#eta(#mu)|<0.9;p_{T}(#mu) [GeV]",pT_bins.size() -1, &(pT_bins[0]));
    pT_matchingEff[1]["pT_matchingEff"] = fs->make<TH1F>("pT_matchingEff_0p9to1p2","matching efficiency vs p_{T}(#mu) with 0.9<|#eta(#mu)|<1.2;p_{T}(#mu) [GeV]",pT_bins.size() -1, &(pT_bins[0]));
    pT_matchingEff[2]["pT_matchingEff"] = fs->make<TH1F>("pT_matchingEff_endcap","matching efficiency vs p_{T}(#mu) with 1.2<|#eta(#mu)|<2.1;p_{T}(#mu) [GeV]",pT_bins.size() -1, &(pT_bins[0]));
    eta_matchingEff_h["eta_matchingEff_h"] = fs->make<TH1F>("eta_matchingEff","matching efficiency vs #eta(#mu);#eta(#mu) [GeV]",eta_bins.size() -1, &(eta_bins[0]));
    eta_matchingEff[0]["eta_matchingEff"] = fs->make<TH1F>("eta_matchingEff_8to20","matching efficiency vs #eta(#mu) with 8<p_{T}(#mu)<20 GeV;#eta(#mu)",eta_bins.size() -1, &(eta_bins[0]));

    pT_newSoftMuon_h["pT_newSoftMuon_h"] = fs->make<TH1F>("pT_newSoftMuon","p_{T} of matched new-Soft reco #mu;p_{T}(#mu) [GeV]",pT_bins.size() -1, &(pT_bins[0]));
    pT_newSoftMuon[0]["pT_newSoftMuon"] = fs->make<TH1F>("pT_newSoftMuon_barrel","p_{T} of matched new-Soft reco #mu with |#eta(#mu)|<0.9;p_{T}(#mu) [GeV]",pT_bins.size() -1, &(pT_bins[0]));
    pT_newSoftMuon[1]["pT_newSoftMuon"] = fs->make<TH1F>("pT_newSoftMuon_0p9to1p2","p_{T} of matched new-Soft reco #mu with 0.9<|#eta(#mu)|<1.2;p_{T}(#mu) [GeV]",pT_bins.size() -1, &(pT_bins[0]));
    pT_newSoftMuon[2]["pT_newSoftMuon"] = fs->make<TH1F>("pT_newSoftMuon_endcap","p_{T} of matched new-Soft reco #mu with 1.2<|#eta(#mu)|<2.1;p_{T}(#mu) [GeV]",pT_bins.size() -1, &(pT_bins[0]));
    eta_newSoftMuon_h["eta_newSoftMuon_h"] = fs->make<TH1F>("eta_newSoftMuon","#eta of matched new-Soft reco #mu;#eta(#mu) [GeV]",eta_bins.size() -1, &(eta_bins[0]));
    eta_newSoftMuon[0]["eta_newSoftMuon"] = fs->make<TH1F>("eta_newSoftMuon_8to20","#eta of matched new-Soft reco #mu with 8<p_{T}(#mu)<20 GeV;#eta(#mu)",eta_bins.size() -1, &(eta_bins[0]));
    nVtx_newSoftMuon_h["nVtx_newSoftMuon_h"] = fs->make<TH1F>("nVtx_newSoftMuon","# of vertices for matched new-Soft reco #mu;# of vertices",nVtx_bins.size() -1, &(nVtx_bins[0]));
    nVtx_newSoftMuon[0]["nVtx_newSoftMuon"] = fs->make<TH1F>("nVtx_newSoftMuon_barrel","# of vertices for matched new-Soft reco #mu with |#eta(#mu)|<0.9;# of vertices",nVtx_bins.size() -1, &(nVtx_bins[0]));
    nVtx_newSoftMuon[1]["nVtx_newSoftMuon"] = fs->make<TH1F>("nVtx_newSoftMuon_0p9to1p2","# of vertices for matched new-Soft reco #mu with 0.9<|#eta(#mu)|<1.2;# of vertices",nVtx_bins.size() -1, &(nVtx_bins[0]));
    nVtx_newSoftMuon[2]["nVtx_newSoftMuon"] = fs->make<TH1F>("nVtx_newSoftMuon_endcap","# of vertices for matched new-Soft reco #mu with 1.2<|#eta(#mu)|<2.1;# of vertices",nVtx_bins.size() -1, &(nVtx_bins[0]));
    nVtx_newSoftMuon[3]["nVtx_newSoftMuon"] = fs->make<TH1F>("nVtx_newSoftMuon_8to20","# of vertices for matched new-Soft reco #mu with 8<p_{T}(#mu)<20 GeV;# of vertices",nVtx_bins.size() -1, &(nVtx_bins[0]));
    nVtx_newSoftMuon[4]["nVtx_newSoftMuon"] = fs->make<TH1F>("nVtx_newSoftMuon_8to20_max2p1","# of vertices for matched new-Soft reco #mu with 8<p_{T}(#mu)<20 GeV && |#eta(#mu)|<2.1;# of vertices",nVtx_bins.size() -1, &(nVtx_bins[0]));

    pT_newSoftMuonEff_h["pT_newSoftMuonEff_h"] = fs->make<TH1F>("pT_newSoftMuonIDEff","new-Soft #mu ID efficiency vs p_{T}(#mu);p_{T}(#mu) [GeV]",pT_bins.size() -1, &(pT_bins[0]));
    pT_newSoftMuonEff[0]["pT_newSoftMuonEff"] = fs->make<TH1F>("pT_newSoftMuonIDEff_barrel","new-Soft #mu ID efficiency vs p_{T}(#mu) with |#eta(#mu)|<0.9;p_{T}(#mu) [GeV]",pT_bins.size() -1, &(pT_bins[0]));
    pT_newSoftMuonEff[1]["pT_newSoftMuonEff"] = fs->make<TH1F>("pT_newSoftMuonIDEff_0p9to1p2","new-Soft #mu ID efficiency vs p_{T}(#mu) with 0.9<|#eta(#mu)|<1.2;p_{T}(#mu) [GeV]",pT_bins.size() -1, &(pT_bins[0]));
    pT_newSoftMuonEff[2]["pT_newSoftMuonEff"] = fs->make<TH1F>("pT_newSoftMuonIDEff_endcap","new-Soft #mu ID efficiency vs p_{T}(#mu) with 1.2<|#eta(#mu)|<2.1;p_{T}(#mu) [GeV]",pT_bins.size() -1, &(pT_bins[0]));
    eta_newSoftMuonEff_h["eta_newSoftMuonEff_h"] = fs->make<TH1F>("eta_newSoftMuonIDEff","new-Soft #mu ID efficiency vs #eta;#eta(#mu) [GeV]",eta_bins.size() -1, &(eta_bins[0]));
    eta_newSoftMuonEff[0]["eta_newSoftMuonEff"] = fs->make<TH1F>("eta_newSoftMuonIDEff_8to20","new-Soft #mu ID efficiency vs #eta(#mu) with 8<p_{T}(#mu)<20 GeV;#eta(#mu)",eta_bins.size() -1, &(eta_bins[0]));
    nVtx_newSoftMuonEff_h["nVtx_newSoftMuonEff_h"] = fs->make<TH1F>("nVtx_newSoftMuonIDEff","new-Soft #mu ID efficiency vs # of vertices;# of vertices",nVtx_bins.size() -1, &(nVtx_bins[0]));
    nVtx_newSoftMuonEff[0]["nVtx_newSoftMuonEff"] = fs->make<TH1F>("nVtx_newSoftMuonIDEff_barrel","new-Soft #mu ID efficiency vs # of vertices with |#eta(#mu)|<0.9;# of vertices",nVtx_bins.size() -1, &(nVtx_bins[0]));
    nVtx_newSoftMuonEff[1]["nVtx_newSoftMuonEff"] = fs->make<TH1F>("nVtx_newSoftMuonIDEff_0p9to1p2","new-Soft #mu ID efficiency vs # of vertices with 0.9<|#eta(#mu)|<1.2;# of vertices",nVtx_bins.size() -1, &(nVtx_bins[0]));
    nVtx_newSoftMuonEff[2]["nVtx_newSoftMuonEff"] = fs->make<TH1F>("nVtx_newSoftMuonIDEff_endcap","new-Soft #mu ID efficiency vs # of vertices with 1.2<|#eta(#mu)|<2.1;# of vertices",nVtx_bins.size() -1, &(nVtx_bins[0]));
    nVtx_newSoftMuonEff[3]["nVtx_newSoftMuonEff"] = fs->make<TH1F>("nVtx_newSoftMuonIDEff_8to20","new-Soft #mu ID efficiency vs # of vertices with 8<p_{T}(#mu)<20;# of vertices",nVtx_bins.size() -1, &(nVtx_bins[0]));
    nVtx_newSoftMuonEff[4]["nVtx_newSoftMuonEff"] = fs->make<TH1F>("nVtx_newSoftMuonIDEff_8to20_max2p1","new-Soft #mu ID efficiency vs # of vertices with 8<p_{T}(#mu)<20 && |#eta(#mu)|<2.1;# of vertices",nVtx_bins.size() -1, &(nVtx_bins[0]));
}


// ------------ method called for each event  ------------
void
HLTEffAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
        
    //if (theDataType == "SimData") {
    // Get the SimTrack collection from the event
    //edm::Handle<GenParticleCollection> genParticles;
    //iEvent.getByLabel("genParticles", genParticles);
    Handle<edm::View<reco::GenParticle> > genCollection ;
    iEvent.getByToken(prunedGenToken_, genCollection);
    //}

    //Handle<reco::VertexCollection> vtxH;
    Handle< vector<Vertex> > vtxH;
    iEvent.getByToken(vtxHT_, vtxH);
    //const VertexCollection *pvCol = vtxH.product();
    const vector< Vertex > *pvCol = vtxH.product();
    const Vertex* pv = &(*pvCol->begin());
    // cut = cms.string("!isFake && ndof > 4 && abs(z) <= 25 && position.Rho <= 2"),
    vector< Vertex > goodPvCol ;
    for (size_t i = 0; i < pvCol->size(); ++i)
      if ( !(*pvCol)[i].isFake()  &&  (*pvCol)[i].ndof() > 4  &&  fabs((*pvCol)[i].z()) <= 25  &&  (*pvCol)[i].position().Rho() <= 2 )
	goodPvCol.push_back( (*pvCol)[i] ) ;

    if ( vtxH->size() != pvCol->size() ) {
      if (Debug) cout <<"offlinePrimaryVertices size = " <<vtxH->size() <<" " <<pvCol->size() <<endl ;
      if (Debug) cout <<"goodPV size = " <<goodPvCol.size() <<endl ;
    }

    /*
    // Get the RecoTrack collection from the event
    Handle<reco::TrackCollection> staTracks;
    iEvent.getByLabel("globalMuons", staTracks);
    */    
    //Handle<reco::MuonCollection> muons; // AOD
    Handle<pat::MuonCollection> muons; // miniAOD

    //iEvent.getByLabel(muonLabel_, muons);
    iEvent.getByToken(muonToken_, muons);
    // Muons from the AOD muons collection are included in MiniAOD if they pass at least one of these three requirements:
    // - pT > 5 GeV
    // - pT > 3 GeV and any of the following IDs: PF, global, arbitrated tracker, standalone, RPCMuLoose
    // - any pT, if they pass the PF ID. 

    //if (Debug) cout <<"reco tracks size = " <<staTracks->size() <<endl ;
    if (Debug) cout <<"muons collection size = " <<muons->size() <<endl ;
    if (Debug) cout <<"genParticles collection size = " <<genCollection->size() <<endl ;

    vector< GenParticle > stableGenCollection, stableGenMuons ;
    Int_t muonFromJpsi = 0;
    //const Candidate* genMuon[2] = {0,0} ;
    vector <const Candidate*> genMuon ;
    for( size_t i = 0; i < genCollection->size(); ++ i) {
      const GenParticle *p = &(*genCollection)[i] ;
      if ( p->status() == 1 ) {
	stableGenCollection.push_back( *p ) ;
	if ( abs(p->pdgId()) == 13 ) {
	  stableGenMuons.push_back( *p ) ;
	  if ( (p->mother())->pdgId() == 443 ) {
	    muonFromJpsi++ ;
	    //p->charge() > 0 ? genMuon[0] = p : genMuon[1] = p ;
	    genMuon.push_back( p ) ;
	    pT_muonFromJpsi_h["pT_muonFromJpsi_h"]->Fill( p->pt() ) ;
	    eta_muonFromJpsi_h["eta_muonFromJpsi_h"]->Fill( p->eta() ) ;
	  }
	}
      }
      /*
      if ( fabs(p.pdgId()) != 13 ) continue;
      if (Debug) cout<<" muon gen pt: "<<p.pt()<<endl;
      histContainer_["hPtSim"]->Fill(p.pt());   
      */
    }
    muonFromJpsi_h["nMuonFromJpsi"]->Fill( muonFromJpsi ) ;
    if (Debug) cout <<"stableGenParticles collection size = " <<stableGenCollection.size() <<endl ;
    if (Debug) cout <<"stableGenMuons collection size = " <<stableGenMuons.size() <<endl ;

    //Bool_t isValidMuon[2] = {kFALSE, kFALSE} ;
    //const Muon* recoMuon[2] = {0,0} ;
    //const pat::Muon* patMuon[2] = {0,0} ;
    //Float_t deltaR_temp[2] = {1.,1.} ;
    //vector< const pat::Muon* > patMuon( muons->size(), 0) ;
    //vector< Float_t > deltaR_temp( muons->size(), 1.) ;
    struct matchingInfo {
      const pat::Muon* patMuon = 0; // miniAOD
      //const reco::Muon* patMuon = 0; // AOD
      const Candidate* genMuon = 0;
      Float_t deltaR = 1.;
      Bool_t isNewSoftMuon = kFALSE ;
      Bool_t isCowBoy = kFALSE ;
    } muonMatched ;
    vector < matchingInfo > matchedMuons ;
    //vector <Bool_t> isCowBoy(genMuon.size(), kFALSE) ;
    //Float_t muonPt[2] = {-1.,-1.} ;

    /*
    propM1 = cms.PSet(
		      useStation2 = cms.bool(False), 
		      useTrack = cms.string("tracker"),
		      useState = cms.string("atVertex"),  # in AOD
		      useSimpleGeometry = cms.bool(True), # use just one cylinder and two planes, not all the fancy chambers
		      )
    */
    //for (pat::MuonCollection::const_iterator muon = muons->begin(); muon != muons->end(); ++muon) {
    //for ( vector<pat::Muon>::const_iterator muon = muons->begin(); muon != muons->end(); ++muon) {
    for (unsigned int i = 0; i < muons->size(); i++) {
      //if ( muon->numberOfValidHits() > 0  &&  muon->numberOfValidHits() < 1000 ) 
      //if ( (muon->pt() > 1)  &&  (muon->pt() < 100000) ) 
      Float_t deltaR_temp = 1. ;
      Int_t best_j = -1 ;
      //for (Int_t j = 0; j<2; j++) {
      for (UInt_t j = 0; j<genMuon.size(); j++) {
	//isValidMuon[i] = kTRUE ;
	if ( (*muons)[i].charge() * genMuon[j]->charge() > 0 ) { 

	  if ( deltaR((*muons)[i], *genMuon[j]) < deltaR_temp ) { // deltaR with a reco::Muon gives segmentation violation!
	    
	    //deltaR_temp[i] = deltaR((*muons)[i],*genMuon[j]) ;
	    deltaR_temp = deltaR((*muons)[i],*genMuon[j]) ;
	    best_j = abs( j ) ;
	    //patMuon[j] = &((*muons)[i]) ;
	    //recoMuon[j] = &((*muons)[i]) ; // dynamic cast returns always 0
	    //patMuon[j] = &(*muons)[i] ;
	    //patMuon[i] = &(*muons)[i] ;
	    //muonPt[j] = ((*muons)[i]).pt() ;
	  }
	}
      }
      if (best_j >= 0) {
	muonMatched.patMuon = &(*muons)[i]; muonMatched.genMuon = genMuon[best_j]; muonMatched.deltaR = deltaR_temp ; 
	//muonMatched.patMuon = dynamic_cast<const pat::Muon *>(&(*muons)[i]); muonMatched.genMuon = genMuon[best_j]; muonMatched.deltaR = deltaR_temp ; 

	// new Soft nuon ID
	//if ( patMuon[i] ) { //cout <<"pT = " <<matchedMuons[i].patMuon->pt() <<endl ; cout <<"orig pT = " <<muonPt[i] <<endl ; cout <<"# = " <<matchedMuons[i].patMuon->numberOfValidHits() <<endl ;
	//if ( matchedMuons[i].patMuon->track().isNonnull() ) {
	if ( muonMatched.patMuon->track().isNonnull() ) {
	  //if ( (muonMatched.patMuon->track().isAvailable() || muonMatched.patMuon->track().isTransient()) && muonMatched.patMuon->track().isNonnull() ) {
	  //if ( (muonMatched.patMuon->innerTrack().isAvailable() || muonMatched.patMuon->innerTrack().isTransient()) && muonMatched.patMuon->innerTrack().isNonnull() ) {
	  //if ( muonMatched.patMuon->isTrackerMuon() ) {
	  //if ( muonMatched.patMuon->globalTrack().isAvailable() ) {
	  //if ( muonMatched.patMuon->globalTrack().isNonnull() ) 
	  if ( 1 
	       && muon::isGoodMuon(*muonMatched.patMuon, muon::TMOneStationTight)
	       && muonMatched.patMuon->track()->hitPattern().trackerLayersWithMeasurement() > 5
	       && muonMatched.patMuon->track()->hitPattern().pixelLayersWithMeasurement() > 0
	       && muonMatched.patMuon->innerTrack()->quality( TrackBase::highPurity )
	       && fabs(muonMatched.patMuon->innerTrack()->dxy( pv->position() )) < 0.3
	       && fabs(muonMatched.patMuon->innerTrack()->dz( pv->position() )) < 20
	       )
	    muonMatched.isNewSoftMuon = kTRUE ;
	}

	matchedMuons.push_back( muonMatched ) ;
      }
    }
    
    /*if (Debug) {
      cout <<"patMuon[0] = " <<patMuon[0] <<endl ;
      cout <<"patMuon[1] = " <<patMuon[1] <<endl ;
      }*/
    /*
    // new soft Muon ID
    //Bool_t isNewSoftMuon[2] = {kFALSE, kFALSE} ;
    vector<Bool_t> isNewSoftMuon(matchedMuons.size(), kFALSE) ;
    //for (Int_t i = 0; i<2; i++) 
    for (UInt_t i = 0; i<matchedMuons.size(); i++) 
	//}
    
    if (Debug) cout <<"newSoftMuonID created" <<endl ;
    */

    for (UInt_t i = 1; i<matchedMuons.size(); i++) {
      /*
      // Propagate to station 1
      cout <<"before" <<endl ;
      TrajectoryStateOnSurface prop1_M1 = prop1_.extrapolate( *dynamic_cast<const reco::RecoCandidate *>(matchedMuons[i].patMuon) );
      cout <<"middle" <<endl ;
      TrajectoryStateOnSurface prop2_M1 = prop1_.extrapolate( *dynamic_cast<const reco::RecoCandidate *>(matchedMuons[i-1].patMuon) );
      cout <<"after" <<endl ;
      if (prop1_M1.isValid() && prop2_M1.isValid()) {
	Float_t dphiM1 = deltaPhi<float>(prop1_M1.globalPosition().phi(), prop2_M1.globalPosition().phi());
	Float_t drM1 = hypot(dphiM1, std::abs<float>(prop1_M1.globalPosition().eta() - prop2_M1.globalPosition().eta()));
      */
        //if ( deltaR(*genMuon[j],*genMuon[j-1]) < deltaR_cowBoys ) {
	//if ( drM1 < deltaR_cowBoys ) {
        if ( deltaR(*matchedMuons[i].genMuon,*matchedMuons[i-1].genMuon) < deltaR_cowBoys ) {
	  matchedMuons[i].isCowBoy = kTRUE ;
	  matchedMuons[i-1].isCowBoy = kTRUE ;
	}
      //}
    }
    	

    //for (Int_t i = 0; i<2; i++) {
    for (UInt_t i = 0; i<matchedMuons.size(); i++) {
      //if ( recoMuon[i] ) {
      //if ( matchedMuons[i].patMuon ) { 
	//if ( matchedMuons[i].patMuon->track().isNonnull() ) { if (Debug) cout <<"after matchedMuons[i].patMuon->track" <<endl ;
          if ( i > 0 )
	    muons_deltaR_h["muons_deltaR_h"]->Fill( deltaR(*matchedMuons[i].patMuon, *matchedMuons[i-1].patMuon) ) ;
	  if ( matchedMuons[i].deltaR < deltaR_max ) { if (Debug) cout <<"\nbefore fills" <<endl ;
	    if ( !matchedMuons[i].isCowBoy ) {

	      pT_denominator_h["pT_denominator_h"]->Fill( matchedMuons[i].genMuon->pt() ) ;
	      eta_denominator_h["eta_denominator_h"]->Fill( matchedMuons[i].genMuon->eta() ) ;
	      nVtx_denominator_h["nVtx_denominator_h"]->Fill( goodPvCol.size() ) ;
	      if (Debug) cout <<"\nafter first kind of fills" <<endl ;
	      pT_numerator_h["pT_numerator_h"]->Fill( matchedMuons[i].patMuon->pt() ) ;
	      eta_numerator_h["eta_numerator_h"]->Fill( matchedMuons[i].patMuon->eta() ) ;
	      //nVtx_numerator_h["nVtx_numerator_h"]->Fill( ->size() ) ;
	      if ( matchedMuons[i].isNewSoftMuon ) {
		pT_newSoftMuon_h["pT_newSoftMuon_h"]->Fill( matchedMuons[i].patMuon->pt() ) ;
		eta_newSoftMuon_h["eta_newSoftMuon_h"]->Fill( matchedMuons[i].patMuon->eta() ) ;
		nVtx_newSoftMuon_h["nVtx_newSoftMuon_h"]->Fill( goodPvCol.size() ) ;
	      }

	      if ( matchedMuons[i].genMuon->pt() > 8  &&  matchedMuons[i].genMuon->pt() < 20 ) {
		eta_denominator[0]["eta_denominator"]->Fill( matchedMuons[i].genMuon->eta() ) ;
		eta_numerator[0]["eta_numerator"]->Fill( matchedMuons[i].patMuon->eta() ) ;   
		nVtx_denominator[3]["nVtx_denominator"]->Fill( goodPvCol.size() ) ;
		if ( fabs(matchedMuons[i].genMuon->eta()) < 2.1 ) {
		  nVtx_denominator[4]["nVtx_denominator"]->Fill( goodPvCol.size() ) ;
		}
		
		if ( matchedMuons[i].isNewSoftMuon ) {
		  eta_newSoftMuon[0]["eta_newSoftMuon"]->Fill( matchedMuons[i].patMuon->eta() ) ;
		  nVtx_newSoftMuon[3]["nVtx_newSoftMuon"]->Fill( goodPvCol.size() ) ;
		  if ( fabs(matchedMuons[i].genMuon->eta()) < 2.1 ) {
		    nVtx_newSoftMuon[4]["nVtx_newSoftMuon"]->Fill( goodPvCol.size() ) ;
		  }
		}
	      }
	      
	      if ( fabs(matchedMuons[i].genMuon->eta()) < 0.9 ) {
		pT_denominator[0]["pT_denominator"]->Fill( matchedMuons[i].genMuon->pt() ) ;
		pT_numerator[0]["pT_numerator"]->Fill( matchedMuons[i].patMuon->pt() ) ;   
		nVtx_denominator[0]["nVtx_denominator"]->Fill( goodPvCol.size() ) ;
		if ( matchedMuons[i].isNewSoftMuon ) {
		  pT_newSoftMuon[0]["pT_newSoftMuon"]->Fill( matchedMuons[i].patMuon->pt() ) ;
		  nVtx_newSoftMuon[0]["nVtx_newSoftMuon"]->Fill( goodPvCol.size() ) ;
		}
	      } else if ( fabs(matchedMuons[i].genMuon->eta()) < 1.2 ) {
		pT_denominator[1]["pT_denominator"]->Fill( matchedMuons[i].genMuon->pt() ) ;
		pT_numerator[1]["pT_numerator"]->Fill( matchedMuons[i].patMuon->pt() ) ;
		nVtx_denominator[1]["nVtx_denominator"]->Fill( goodPvCol.size() ) ;
		if ( matchedMuons[i].isNewSoftMuon ) {
		  pT_newSoftMuon[1]["pT_newSoftMuon"]->Fill( matchedMuons[i].patMuon->pt() ) ;
		  nVtx_newSoftMuon[1]["nVtx_newSoftMuon"]->Fill( goodPvCol.size() ) ;
		}
	      } else if ( fabs(matchedMuons[i].genMuon->eta()) < 2.1 ) {
		pT_denominator[2]["pT_denominator"]->Fill( matchedMuons[i].genMuon->pt() ) ;
		pT_numerator[2]["pT_numerator"]->Fill( matchedMuons[i].patMuon->pt() ) ;
		nVtx_denominator[2]["nVtx_denominator"]->Fill( goodPvCol.size() ) ;
		if ( matchedMuons[i].isNewSoftMuon ) {
		  pT_newSoftMuon[2]["pT_newSoftMuon"]->Fill( matchedMuons[i].patMuon->pt() ) ;
		  nVtx_newSoftMuon[2]["nVtx_newSoftMuon"]->Fill( goodPvCol.size() ) ;
		}	    
	      }
	    } // if ( !matchedMuons[i].isCowBoy )
	  } // if ( matchedMuons[i].deltaR < deltaR_max )
	//}
      //}
    } // for (UInt_t i = 0; i<matchedMuons.size(); i++)
    if (Debug) cout <<"\nafter fills" <<endl;

    /*
    edm::Handle<edm::TriggerResults> triggerResults;
    iEvent.getByLabel(triggerResultsTag_, triggerResults);
    
    edm::Handle<trigger::TriggerEvent> handleTriggerEvent;
    iEvent.getByLabel(triggerEvent_, handleTriggerEvent );

    const vector<string>& pathList = hltConfig.triggerNames();
    if (Debug) cout <<"path size = " <<pathList.size() <<endl;
    for (vector<string>::const_iterator it = pathList.begin(); it != pathList.end(); ++it) {
        if (Debug) cout <<"path list x run " <<*it <<endl;  
        }
    
    const trigger::TriggerObjectCollection & toc(handleTriggerEvent->getObjects());
    
    for ( size_t ia = 0; ia < handleTriggerEvent->sizeFilters(); ++ ia) {
        const trigger::Keys & k = handleTriggerEvent->filterKeys(ia);
        for (trigger::Keys::const_iterator ki = k.begin(); ki !=k.end(); ++ki ) {
            if (Debug) cout<<" trigger obj pt "<<toc[*ki].pt()<<" id "<< toc[*ki].id()<<" mass "<<toc[*ki].mass()<<endl;
    
        }
    }
    */
}


// ------------ method called once each job just after ending the event loop  ------------
void 
HLTEffAnalyzer::endJob() 
{ // efficiency calculations
  if (Debug) cout <<"\nbefore efficiencies calculations" <<endl;

  pT_matchingEff_h["pT_matchingEff_h"]->Divide(pT_numerator_h["pT_numerator_h"], pT_denominator_h["pT_denominator_h"], 1, 1, "B") ; 
  eta_matchingEff_h["eta_matchingEff_h"]->Divide(eta_numerator_h["eta_numerator_h"], eta_denominator_h["eta_denominator_h"], 1, 1, "B") ; 
  eta_matchingEff_h["eta_matchingEff_h"]->SetMinimum( 0.5 ) ;

  pT_newSoftMuonEff_h["pT_newSoftMuonEff_h"]->Divide(pT_newSoftMuon_h["pT_newSoftMuon_h"], pT_denominator_h["pT_denominator_h"], 1, 1, "B") ;
  //pT_newSoftMuonEff_h["pT_newSoftMuonEff_h"]->SetMaximum( 1.05 ) ; 
  eta_newSoftMuonEff_h["eta_newSoftMuonEff_h"]->Divide(eta_newSoftMuon_h["eta_newSoftMuon_h"], eta_denominator_h["eta_denominator_h"], 1, 1, "B") ; 
  eta_newSoftMuonEff_h["eta_newSoftMuonEff_h"]->SetMinimum( 0.5 ) ;
  nVtx_newSoftMuonEff_h["nVtx_newSoftMuonEff_h"]->Divide(nVtx_newSoftMuon_h["nVtx_newSoftMuon_h"], nVtx_denominator_h["nVtx_denominator_h"], 1, 1, "B") ; 
  nVtx_newSoftMuonEff_h["nVtx_newSoftMuonEff_h"]->SetMinimum( 0.5 ) ;  nVtx_newSoftMuonEff_h["nVtx_newSoftMuonEff_h"]->SetMaximum( 1.3 ) ;
  // 8 < pT < 20
  eta_matchingEff[0]["eta_matchingEff"]->Divide(eta_numerator[0]["eta_numerator"], eta_denominator[0]["eta_denominator"], 1, 1, "B") ; 
  eta_matchingEff[0]["eta_matchingEff"]->SetMinimum( 0 ) ;
  eta_newSoftMuonEff[0]["eta_newSoftMuonEff"]->Divide(eta_newSoftMuon[0]["eta_newSoftMuon"], eta_denominator[0]["eta_denominator"], 1, 1, "B") ; 
  eta_newSoftMuonEff[0]["eta_newSoftMuonEff"]->SetMinimum( 0.5 ) ; eta_newSoftMuonEff[0]["eta_newSoftMuonEff"]->SetMaximum( 1.3 ) ;

  for (Int_t i = 0; i<3; i++) {
    pT_matchingEff[i]["pT_matchingEff"]->Divide(pT_numerator[i]["pT_numerator"], pT_denominator[i]["pT_denominator"], 1, 1, "B") ; 
    pT_matchingEff[i]["pT_matchingEff"]->SetMinimum( 0. ) ; //pT_matchingEff[i]["pT_matchingEff"]->SetMaximum( 1.05 ) ;
    pT_newSoftMuonEff[i]["pT_newSoftMuonEff"]->Divide(pT_newSoftMuon[i]["pT_newSoftMuon"], pT_denominator[i]["pT_denominator"], 1, 1, "B") ; 
    pT_newSoftMuonEff[i]["pT_newSoftMuonEff"]->SetMinimum( 0 ) ; pT_newSoftMuonEff[i]["pT_newSoftMuonEff"]->SetMaximum( 1.8 ) ; // Ilse  
  }

  for (Int_t i = 0; i<5; i++) {
    nVtx_newSoftMuonEff[i]["nVtx_newSoftMuonEff"]->Divide(nVtx_newSoftMuon[i]["nVtx_newSoftMuon"], nVtx_denominator[i]["nVtx_denominator"], 1, 1, "B") ;
    nVtx_newSoftMuonEff[i]["nVtx_newSoftMuonEff"]->SetMinimum( 0.5 ) ; nVtx_newSoftMuonEff[i]["nVtx_newSoftMuonEff"]->SetMaximum( 1.3 ) ;
  }

  // draw plots
  TCanvas *effPlot = new TCanvas("effPlot", "eff_plot", 800, 600);
  gStyle->SetOptStat(10) ;
  gPad->SetGrid() ;

  TString dir = "";
  if (dataset == "miniAOD")
    dir = "miniAODSIM";
  else if (dataset == "AOD")
    dir = "AODSIM";

  // pT
  TString logX = "";
  pT_newSoftMuonEff_h["pT_newSoftMuonEff_h"]->SetLineWidth(2) ; pT_newSoftMuonEff_h["pT_newSoftMuonEff_h"]->SetMarkerStyle(3) ;
  pT_newSoftMuonEff_h["pT_newSoftMuonEff_h"]->Draw("P") ; 
  for (Int_t i = 0; i<=1; i++) {
    gPad->SetLogx(i) ;
    gPad->GetLogx() == 0 ? logX = "" : logX = "_logx" ;
    effPlot->SaveAs(TString::Format( "plots/%s/%s%s.png", dir.Data(), pT_newSoftMuonEff_h["pT_newSoftMuonEff_h"]->GetName(), logX.Data() )) ;
  } gPad->SetLogx(0) ;
  //
  // eta
  eta_newSoftMuonEff_h["eta_newSoftMuonEff_h"]->SetLineWidth(2) ; eta_newSoftMuonEff_h["eta_newSoftMuonEff_h"]->SetMarkerStyle(3) ;
  eta_newSoftMuonEff_h["eta_newSoftMuonEff_h"]->Draw("P") ;
  effPlot->SaveAs(TString::Format( "plots/%s/%s.png", dir.Data(), eta_newSoftMuonEff_h["eta_newSoftMuonEff_h"]->GetName() )) ;
  //
  // nVtx
  nVtx_newSoftMuonEff_h["nVtx_newSoftMuonEff_h"]->SetLineWidth(2) ; nVtx_newSoftMuonEff_h["nVtx_newSoftMuonEff_h"]->SetMarkerStyle(3) ;
  nVtx_newSoftMuonEff_h["nVtx_newSoftMuonEff_h"]->Draw("P") ;
  effPlot->SaveAs(TString::Format( "plots/%s/%s.png", dir.Data(), nVtx_newSoftMuonEff_h["nVtx_newSoftMuonEff_h"]->GetName() )) ;
  //
  // eta with 8 < pT < 20
  eta_newSoftMuonEff[0]["eta_newSoftMuonEff"]->SetLineWidth(2) ; eta_newSoftMuonEff[0]["eta_newSoftMuonEff"]->SetMarkerStyle(3) ;
  eta_newSoftMuonEff[0]["eta_newSoftMuonEff"]->Draw("P") ;
  effPlot->SaveAs(TString::Format( "plots/%s/%s.png", dir.Data(), eta_newSoftMuonEff[0]["eta_newSoftMuonEff"]->GetName() )) ;

  for (Int_t j = 0; j < 3; j++) {
    pT_matchingEff[j]["pT_matchingEff"]->SetLineWidth(2) ; pT_matchingEff[j]["pT_matchingEff"]->SetMarkerStyle(3) ;
    pT_matchingEff[j]["pT_matchingEff"]->Draw("P") ;
    for (Int_t i=0; i<=1; i++) {
      gPad->SetLogx(i) ;
      gPad->GetLogx() == 0 ? logX = "" : logX = "_logx" ;
      effPlot->SaveAs(TString::Format( "plots/%s/%s%s.png", dir.Data(), pT_matchingEff[j]["pT_matchingEff"]->GetName(), logX.Data() )) ;
    } gPad->SetLogx(0) ;
    //
    pT_newSoftMuonEff[j]["pT_newSoftMuonEff"]->SetLineWidth(2) ; pT_newSoftMuonEff[j]["pT_newSoftMuonEff"]->SetMarkerStyle(3) ;
    pT_newSoftMuonEff[j]["pT_newSoftMuonEff"]->Draw("P") ;
    for (Int_t i=0; i<=1; i++) {
      gPad->SetLogx(i) ;
      gPad->GetLogx() == 0 ? logX = "" : logX = "_logx" ;
      effPlot->SaveAs(TString::Format( "plots/%s/%s%s.png", dir.Data(), pT_newSoftMuonEff[j]["pT_newSoftMuonEff"]->GetName(), logX.Data() )) ;
    } gPad->SetLogx(0) ;
  }

  for (Int_t i = 0; i < 5; i++) {
    nVtx_newSoftMuonEff[i]["nVtx_newSoftMuonEff"]->SetLineWidth(2) ; nVtx_newSoftMuonEff[i]["nVtx_newSoftMuonEff"]->SetMarkerStyle(3) ;
    nVtx_newSoftMuonEff[i]["nVtx_newSoftMuonEff"]->Draw("P") ;
    effPlot->SaveAs(TString::Format( "plots/%s/%s.png", dir.Data(), nVtx_newSoftMuonEff[i]["nVtx_newSoftMuonEff"]->GetName() )) ;
  }

}

// ------------ method called when starting to processes a run  ------------
/*
void 
HLTEffAnalyzer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
HLTEffAnalyzer::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
HLTEffAnalyzer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
HLTEffAnalyzer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
HLTEffAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(HLTEffAnalyzer);
