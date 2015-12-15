////////////////////////////////
//
//written by Ilse Kraetschmer
//last updated on 19th August 2013
//
////////////////////////////////
//change for combination of tracks

// C/C++
#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <sstream>
#include <vector>
#include <limits>
// Root
#include "TFile.h"
#include "TROOT.h"
#include "TStyle.h"
#include "TH2.h"
#include "TDirectory.h"
#include "TCanvas.h"
#include "TPad.h"
#include "TGraph.h"
#include "TIterator.h"
#include "TObject.h"
#include "TKey.h"
#include "TText.h"
#include "TPaveText.h"
#include "TString.h"
#include "TLatex.h"
#include "TGraphAsymmErrors.h"
#include "TMath.h"


// Return opened root file (or 0 on fail)
TFile* open(std::string filename) {
    TFile* file = new TFile(filename.c_str());
    if ((!file)||(file->IsZombie())) {
        std::cerr <<"File "<<filename<<" is bad" <<std::endl;
        return 0;
    }
    return file;
}

// Change to a subdirectory
// Return: directory (or 0 on fail)
TDirectory* cd(TDirectory* indir,std::string subdir)
{
    TDirectory* outdir = dynamic_cast<TDirectory*>(indir->Get(subdir.c_str()));
    if (!outdir) {
        std::cerr <<"\nDirectory "<<subdir <<" not found" <<std::endl;
        return 0;
    }
    return outdir;
}

// comparison to 0
bool isZero(double a) { return fabs(a)<1E-301; }

// Struct to store efficiency values
struct storage{
    double var; double var_low; double var_high;
    double eff; double eff_low; double eff_high;
    // Resets every member
    void null() {
        var = 0.0; var_low = 0.0; var_high = 0.0;
        eff = 0.0; eff_low = 0.0; eff_high = 0.0;
    }
    void print() {
        std::cout <<"var = " <<var <<" + " <<var_high <<" - " <<var_low <<"\n"
                  <<"eff = " <<eff <<" + " <<eff_high <<" - " <<eff_low <<"\n"
                  <<std::endl;
    }
    void setEff(double e, double low, double high) {
        eff = e; eff_low = low; eff_high = high;
    }
    void setVar(double meanVar, double v_low, double v_high) {
        var = meanVar; var_low = v_low; var_high = v_high;
    }
};

//////////////////////////////////////////////
//MAIN FUNCTION
//////////////////////////////////////////////
void createPtRootFiles() {
  gROOT->SetStyle("Plain");
  gStyle->SetTitleBorderSize(0);
  gStyle->SetTitleOffset(1.25,"X") ;
  gStyle->SetTitleOffset(1.2,"Y") ;

  // code set up so that MC file is split in different files for abseta bins
  //const std::string effName[] = {"Loose2012", "Soft2012", "newSoft2012", "Tight2012", "Dimuon10_L1L2"}; 
  TString effName[] = {"Loose2012", "Soft2012", "newSoft2012", "Tight2012", "Dimuon10_L1L2", "Dimuon16_L1L2", "L3_wrt_Dimuon10_L1L2", "L3_wrt_Dimuon16_L1L2", "Dimuon16_Jpsi_wrt_Dimuon6_Jpsi_NoVertexing", "Dimuon10_Jpsi_Barrel_wrt_Dimuon0er16_Jpsi_NoVertexing"};
  const int nEff = sizeof(effName)/sizeof(effName[0]);
  vector<TString> triggers = {"_Mu7p5_Track2_Jpsi"} ; 
  vector<TString> trigL3 = {""} ;
  //
  vector< pair<TString, vector<TString>> > eff_triggers ;
  for (uint iEff=0; iEff<nEff; ++iEff)
    if ( !(effName[iEff].Contains("L3") || effName[iEff].Contains("Vertexing")) )
      eff_triggers.push_back( make_pair(effName[iEff],triggers) ) ;
    else
      eff_triggers.push_back( make_pair(effName[iEff],trigL3) ) ;

  // Name of samples: data and MC
  const std::string effSampleName[] = {"MC", "DATA"};
  //const std::string effSampleName[] = {"MC", "MC"};
  //const std::string effSampleName[] = {"MC"};
  //const std::string effSampleName[] = {"MC", "MC_Mu8"};
  //const std::string effSampleName[] = {"DATA"};
  const int nEffSample = sizeof(effSampleName)/sizeof(effSampleName[0]);

  // 2015
  //int iEff = 1; iEff = 4; iEff = 5; /*iEff = 6; iEff = 7; iEff = 8; iEff = 9; */ 
  // 2012
  //int iEff = 2;

  TString mode = ""; //mode = "25ns_";

  vector< double > bins1, bins2;
  vector< TString > bins2name;
  //for (int iEff=1; iEff<=1; ++iEff) {
  for (int iEff=4; iEff<=7; ++iEff) {

    // Name of trigger: Mu5_Track2, Mu7_Track7
    vector< vector<std::string> > trackName(nEffSample) ;
    if (effName[iEff].Contains("Dimuon6_Jpsi_NoVertexing")) {
      //const std::string trackName[nEffSample][1] = { {"Dimuon6_Jpsi_NoVertexing"},{"Dimuon6_Jpsi_NoVertexing"} };
      for (Int_t iEffSample = 0; iEffSample < nEffSample; iEffSample++)
	trackName[iEffSample].push_back("Dimuon6_Jpsi_NoVertexing");
    } else if (effName[iEff].Contains("Dimuon0er16_Jpsi_NoVertexing")) {
      //const std::string trackName[nEffSample][1] = { {"Dimuon0er16_Jpsi_NoVertexing"},{"Dimuon0er16_Jpsi_NoVertexing"} };
      for (Int_t iEffSample = 0; iEffSample < nEffSample; iEffSample++)
	trackName[iEffSample].push_back("Dimuon0er16_Jpsi_NoVertexing");
    } else
      for (Int_t iEffSample = 0; iEffSample < nEffSample; iEffSample++) {
	//trackName[iEffSample].push_back("");
	//if (effName[iEff].Contains("Soft2012")) {
	//const std::string trackName[nEffSample][] = {{"Mu5_Track2", "Mu7_Track7"},{"Mu5_Track2", "Mu7_Track7"}};
	//const std::string trackName[nEffSample][] = {{"Mu7p5_Track2", "Mu7p5_Track7"},{"Mu7p5_Track2", "Mu7p5_Track7"}};
	//const std::string trackName[nEffSample][] = {{"Mu8"}};
	//const std::string trackName[nEffSample][] = }{"Mu7p5_Track7"}};
	//const std::string trackName[nEffSample][1] = {{"Mu7p5_Track2"},{"Mu8"}};
	//const std::string trackName[nEffSample][1] = {{"Mu7p5_Track2"},{"Mu7p5_Track2"}};
	trackName[iEffSample].push_back("Mu7p5_Track2");
      }
    
    //const int nTrack = sizeof(trackName[0])/sizeof(trackName[0][0]);
    const int nTrack = trackName[0].size();
    cout <<"\nnTrack = " <<nTrack <<endl;
    
    // fill with Mu7p5_Track7 for pt > 9 GeV - former 7 GeV
    Float_t triggerTreshold = 999. ;
    if ( trackName[0][nTrack-1] ==  "Mu7_Track7")
      triggerTreshold = 7. ;
    
    //Declare bins according to efficiency
    // pt_abseta
    //double bins1[] = {2.0, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.5, 5.0, 6.0, 8.0, 10.0, 20.0}; TString var1name = "pT" ;
    //double bins1[] = {2.0, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.5, 5.0, 6.0, 8.0, 10.0, 15.0, 20.0, 30.0, 40.0}; TString var1name = "pT" ;
    //double bins1[] = {2.0, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.5, 5.0, 6.0, 8.0, 10.0, 15.0, 20.0}; TString var1name = "pT" ;
    //double bins1[] = {2.0, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.5, 5.0, 5.5, 6.0, 7.0, 9.0, 11.0, 14.0, 17.0, 20.0}; TString var1name = "pT" ;
    //double bins1[] = {10, 20, 25, 30, 35, 40, 50, 60, 90, 140, 300, 500}; TString var1name = "pT" ;
    //double bins1[] = {2.0, 2.5, 3.0, 3.5, 4.0, 4.75, 5.5, 7.5, 10.0, 20.0, 40.0}; TString var1name = "pT" ;
    bins1.clear();
    if (!effName[iEff].Contains("Vertexing")) {
      bins1.push_back(2.0); bins1.push_back(2.5); bins1.push_back(3.0); bins1.push_back(3.5); bins1.push_back(4.0); bins1.push_back(4.75); bins1.push_back(5.5); bins1.push_back(7.5); bins1.push_back(10.0); bins1.push_back(20.0); bins1.push_back(40.0); 
    } 
    else {
      if (!effName[iEff].Contains("Dimuon16"))
	bins1.push_back(10.0);
      bins1.push_back(16.0); bins1.push_back(20.0); bins1.push_back(40.0);
    } TString var1name = "pT" ;

    //std::string bins2name[] = {"0to2p4"};
    //TString bins2name[] = {"0to2p5"}; double bins2[] = {0, 2.5}; TString var2name = "abseta" ; // does not matter since we always look at only one abseta bin // ? 
    //TString bins2name[] = {"0to0p9","0p9to1p2","1p2to2p1","2p1to2p4"}; double bins2[] = {0., 0.9, 1.2, 2.1, 2.4};
    bins2.clear(); bins2name.clear();
    bins2.push_back(0.); bins2.push_back(0.9); bins2.push_back(1.2);
    bins2name.push_back("0to0p9"); bins2name.push_back("0p9to1p2");
    if (!effName[iEff].Contains("Dimuon10")) {
      bins2.push_back(2.1); bins2.push_back(2.4);
      bins2name.push_back("1p2to2p1"); bins2name.push_back("2p1to2p4");
    } else {
      bins2.push_back(1.6);
      bins2name.push_back("1p2to1p6");
    } TString var2name = "abseta" ;

    //
    // plateau
    //double bins2[] = {8, 20}; TString bins2name[] = {"8to20"}; TString var2name = "pT" ;
    // turn-on
    //double bins2[] = {3, 5}; TString bins2name[] = {"3to5"}; TString var2name = "pT" ;
    //
    //double bins1[] = {0., 0.9, 1.2, 2.1, 2.4}; TString bins1name[] = {"0to0p9","0p9to1p2","1p2to2p1","2p1to2p4"}; TString var1name = "eta" ; 

    //const int nBins1 = sizeof(bins1)/sizeof(bins1[0]) -1;
    const int nBins1 = bins1.size() -1;
    //const int nBins2 = sizeof(bins2)/sizeof(bins2[0]) -1;
    const int nBins2 = bins2.size() -1;

    TString binnedVars = "_pt_abseta" ;
    //binnedVars = "_plateau" ;
    //binnedVars = "_ptTurnOn" ;
    binnedVars = "_pt_abseta_notSeparated" ;
    //binnedVars = "_pt_abseta_seagull" ; //binnedVars = "_pt_abseta_cowboy" ;
    if (effName[iEff].Contains("Vertexing"))
      binnedVars.ReplaceAll("abseta","absrapidity");
    // give number of abseta bin
    //int abseta = 2;
    int abseta = (!binnedVars.Contains("plateau") && !binnedVars.Contains("ptTurnOn")) ? nBins2 : nBins1 ;


    //input files
    //std::stringstream datafile, mcfile;
    TString inputfile[nEffSample] ;
    std::string path = "/afs/cern.ch/work/l/lecriste/TnP/recipe_740/CMSSW_7_4_0/src/MuonAnalysis/TagAndProbe/test/jpsi/fitTreeAnalyzer" ;
    //datafile <<"/scratch/ikratsch/TnP2012/MuonPOG/official6March2014/changedMass/multiplicity/TnP_MuonID_data_all_" <<eff_triggers[iEff].first <<"_pt_abseta" <<abseta <<"_multiplicity.root";

    for (int iEffSample = 0; iEffSample < nEffSample; iEffSample++)
      if ( effSampleName[iEffSample] == "DATA" ) {
	//inputfile[iEffSample] = TString::Format("%s/TnP_MuonID__data_246908-251883_JSON_MuonPhys_v2__%s%s.root", path.c_str(), eff_triggers[iEff].first.c_str(), binnedVars.Data()) ;
	//inputfile[iEffSample] = TString::Format("%s/TnP_MuonID__data_246908-251883_JSON_MuonPhys_v2__%s%s.root", path.c_str(), eff_triggers[iEff].first.c_str(), binnedVars.Data()) ;
	//inputfile[iEffSample] = TString::Format("%s/TnP_MuonID__data_246908-251883_JSON_MuonPhys_v2__%s%s.root", path.c_str(), effName[1].Data(), binnedVars.Data()) ;
	//inputfile[iEffSample] = TString::Format("%s/TnP_MuonID__data_all__%s%s.root", path.c_str(), effName[1].Data(), binnedVars.Data()) ;
	inputfile[iEffSample] = TString::Format("%s/TnP_MuonID__data_%s_%s%s.root", path.c_str(), mode.Data(), effName[1].Data(), binnedVars.Data()) ;
	//inputfile[iEffSample] = TString::Format("%s/TnP_MuonID__data_all_%s_%s%s.root", path.c_str(), mode.Data(), effName[1].Data(), binnedVars.Data()) ;
	if (effName[iEff].Contains("Vertexing"))
	  inputfile[iEffSample] = TString::Format("%s/TnP_Vertexing__data_246908-251883_JSON_MuonPhys_v2_%s.root", path.c_str(), binnedVars.Data()) ;
	//inputfile[iEffSample] = TString::Format("%s/TnP_MuonID__data_246908-255031_JSON_MuonPhys_v2__%s%s.root", path.c_str(), eff_triggers[iEff].first.c_str(), binnedVars.Data()) ;
      }
      else if ( effSampleName[iEffSample] == "MC" ) { 
	//inputfile[iEffSample] = TString::Format("%s/TnP_MuonID_signal_mc_%s%s_fullMC_allBins.root", path,eff_triggers[iEff].first,binnedVars) ;
	//inputfile[iEffSample] = TString::Format("%s/TnP_MuonID__signal_mc__%s%s_30M.root", path.c_str(), eff_triggers[iEff].first.c_str(), binnedVars.Data()) ;
	//inputfile[iEffSample] = TString::Format("%s/TnP_MuonID__signal_mc__%s%s.root", path.c_str(), effName[1].Data(), binnedVars.Data()) ;
	inputfile[iEffSample] = TString::Format("%s/TnP_MuonID__signal_mc_%s_%s%s.root", path.c_str(), mode.Data(), effName[1].Data(), binnedVars.Data()) ;
	//inputfile[iEffSample] = TString::Format("%s/TnP_MuonID__signal_mc__%s%s_30M.root", path.c_str(), effName[1].Data(), binnedVars.Data()) ;
	if (effName[iEff].Contains("Vertexing"))
	  inputfile[iEffSample] = TString::Format("%s/TnP_Vertexing__signal_mc_%s.root", path.c_str(), binnedVars.Data()) ;
	//inputfile[iEffSample] = TString::Format("%s/TnP_MuonID__signal_mc__%s%s_Mu8.root", path.c_str(), eff_triggers[iEff].first.c_str(), binnedVars.Data()) ;
      }
      else if ( effSampleName[iEffSample] == "MC_Mu8" ) { 
	inputfile[iEffSample] = TString::Format("%s/TnP_MuonID__signal_mc__%s%s_Mu8.root", path.c_str(), eff_triggers[iEff].first.Data(), binnedVars.Data()) ;
      }
    //output file
    std::stringstream outputfile;
    //outputfile <<"/scratch/ikratsch/TnP2012/MuonPOG/official6March2014/changedMass/multiplicity/MuonID_" <<eff_triggers[iEff].first <<binnedVars <<abseta <<"_2012_multiplicity.root";
    //outputfile <<path <<"/MuonID_" <<eff_triggers[iEff].first <<binnedVars <<".root";
    if (nEffSample < 2)
      outputfile <<"./MuonID_" <<eff_triggers[iEff].first <<"_" <<mode <<binnedVars <<".root";
    else 
      outputfile <<"./MuonID_" <<eff_triggers[iEff].first <<"_" <<mode <<binnedVars <<"__" <<effSampleName[0] <<"_vs_" <<effSampleName[1] <<".root";
    TFile *output = new TFile(outputfile.str().c_str(),"RECREATE");


    // structure to store values
    storage values[nEffSample][nTrack][nBins1+1][nBins2+1];

    // initialize storage
    for(int iEffSample = 0; iEffSample < nEffSample; iEffSample++){
      for(int iTrack = 0; iTrack < nTrack; iTrack++){
	for (int iBins1 = 0; iBins1 < nBins1 +1; iBins1++){
	  for (int iBins2 = 0; iBins2 < nBins2 +1; iBins2++){
	    values[iEffSample][iTrack][iBins1][iBins2].null();
	  } //iBins1
	} //iBins2
      }//iTrack
    } //iEffSample


    for (int iEffSample = 0; iEffSample < nEffSample; iEffSample++) {
      
      // open input files
      TFile *file;
      /*
	if (iEffSample == 0)
	file = open( datafile.str().c_str() );
	else
	file = open( mcfile.str().c_str() );
      */
      file = open( inputfile[iEffSample].Data() );
      cout <<"\nSuccessfully opened "<<effSampleName[iEffSample] <<" file:\n" <<inputfile[iEffSample].Data() <<"\n" <<endl;
      if (!file) return;
      
      // Jump to tpTree
      TDirectory* dir_tpTree = 0;
      if ( !inputfile[iEffSample].Contains("Vertexing") )
	dir_tpTree = cd(file,"tpTree");
      else
	dir_tpTree = cd(file,"tpTreeOnePair");
      if (!dir_tpTree) continue;

      TString x_y[] = {"pt_abseta","abseta_pt"};
      if ( effName[iEff].Contains("NoVertexing") ) {
	x_y[0] = "pair_pt_pair_absrapidity"; x_y[1] = "pair_absrapidity_pair_pt"; }
      TH2F *myTH2[] = {0,0};

      //std::string plot[nBins2] ;
      //TString titleX[nBins2], titleY[nBins2] ;
      vector< std::string > plot(nBins2) ;
      vector< TString > titleX(nBins2), titleY(nBins2) ;
      // Jump to next directory
      for (int iTrack = 0; iTrack < nTrack; iTrack++) {

	std::stringstream directory;
	if ( !binnedVars.Contains("plateau") ) {
	  if ( trackName[iEffSample][iTrack] != "Mu8" ) {
	    if ( !inputfile[iEffSample].Contains("Vertexing") ) {
	      //directory <<eff_triggers[iEff].first <<"_pt_abseta_" <<trackName[iEffSample][iTrack] <<"_Jpsi";
	      directory <<eff_triggers[iEff].first <<binnedVars <<eff_triggers[iEff].second[0] ;
	    } else
	      directory <<eff_triggers[iEff].first ;
	  } else
	    directory <<eff_triggers[iEff].first <<binnedVars <<eff_triggers[iEff].second[0]; 
	} else {
	  if ( iTrack != nTrack-1 ) continue;
	  directory <<eff_triggers[iEff].first <<binnedVars ;
	}

	// directory <<"Soft_pt_abseta";
	TDirectory* dir_run = cd( dir_tpTree, directory.str().c_str() );
	if (!dir_run) continue;
	else cout <<"cd to " <<directory.str().c_str() <<" dir" <<endl ;
	// Jump to fit directory
	TDirectory* dir_fit_eff = cd(dir_run,"fit_eff_plots");
	if (!dir_fit_eff) return;
	// cout <<"Found fit directory" <<endl;
	  
	//if(iEffSample==0)
	//inter <<"pt_PLOT_abseta_bin" <<abseta <<"_&_" <<trackName[iTrack] <<"_Jpsi_TK_pass_&_tag_" <<trackName[iTrack] <<"_Jpsi_MU_pass";
	//else
	//inter <<"pt_PLOT_" <<trackName[iTrack] <<"_Jpsi_TK_pass_&_tag_" <<trackName[iTrack] <<"_Jpsi_MU_pass";
	//inter <<"pt_PLOT_abseta_bin" <<abseta;
	//inter <<"pt_PLOT";
	  
	// 2D
	for (Int_t i=0; i<2; ++i) {
	  TString name2D = x_y[i];
	  if (effName[iEff].Contains("Soft2012"))
	    name2D.Append("_PLOT__pair_drM1_0p5to10_and_pair_probeMultiplicity_0p5to1p5_and_"+ trackName[iEffSample][iTrack] +"_Jpsi_TK_pass_and_tag_"+ trackName[iEffSample][iTrack] +"_Jpsi_MU_pass");
	  else if ( effName[iEff].EqualTo("Dimuon10_L1L2") )
	    name2D.Append("_PLOT__dB_-0p3to0p3_and_dzPV_-20to20_and_pair_drM1_0p5to10_and_pair_probeMultiplicity_0p5to1p5_and_tag_abseta_0to1p6_and_"+ trackName[iEffSample][iTrack] +"_Jpsi_TK_pass_and_TMOST_pass_and_Track_HP_pass_and_tag_"+ trackName[iEffSample][iTrack] +"_Jpsi_MU_pass");
	  else if ( effName[iEff].EqualTo("Dimuon16_L1L2") )
	    name2D.Append("_PLOT__dB_-0p3to0p3_and_dzPV_-20to20_and_pair_drM1_0p5to10_and_pair_probeMultiplicity_0p5to1p5_and_tag_pt_10to1000_and_"+ trackName[iEffSample][iTrack] +"_Jpsi_TK_pass_and_TMOST_pass_and_Track_HP_pass_and_tag_"+ trackName[iEffSample][iTrack] +"_Jpsi_MU_pass");
	  else if ( effName[iEff].EqualTo("L3_wrt_Dimuon10_L1L2") )
	    name2D.Append("_PLOT__dB_-0p3to0p3_and_dzPV_-20to20_and_pair_drM1_0p5to10_and_pair_probeMultiplicity_0p5to1p5_and_Dimuon10_L1L2_pass_and_TMOST_pass_and_Track_HP_pass_and_tag_Mu7p5_L2Mu2_Jpsi_MU_pass");
	  else if ( effName[iEff].EqualTo("L3_wrt_Dimuon16_L1L2") )
	    name2D.Append("_PLOT__dB_-0p3to0p3_and_dzPV_-20to20_and_pair_drM1_0p5to10_and_pair_probeMultiplicity_0p5to1p5_and_tag_pt_10to1000_and_Dimuon16_L1L2_pass_and_TMOST_pass_and_Track_HP_pass_and_tag_Mu7p5_L2Mu2_Jpsi_MU_pass");
	  else if ( effName[iEff].Contains("NoVertexing") ) 
	    name2D.Append("_PLOT__pair_probeMultiplicity_0p5to1p5_and_"+ trackName[iEffSample][iTrack] +"_pass_and_tag_"+ trackName[iEffSample][iTrack] +"_pass");
	
	  if ( binnedVars.Contains("notSeparated") )
	    name2D.ReplaceAll("pair_drM1_0p5to10_and_","") ;

	  TCanvas* c2D = dynamic_cast<TCanvas*> (dir_fit_eff->Get( name2D ));
	  if (!c2D) cout <<"No " <<name2D <<" in \"" <<dir_fit_eff->GetName() <<"\" dir in " <<effSampleName[iEffSample] <<" file!" <<endl;
	  else {
	    myTH2[i] = dynamic_cast<TH2F*> (c2D->FindObject( c2D->GetName() ));
	    if (!myTH2[i]) cout <<"No " <<c2D->GetName() <<" in TCanvas " <<name2D <<endl;
	    else {
	      //myTH2[i]->SetTitle( c2D->GetName() );
	      myTH2[i]->SetName( TString(effSampleName[iEffSample]+"__"+x_y[i]) ); }
	  }
	}

	for(int iBins2 = 0; iBins2 < nBins2; iBins2++) {
	    
	  cout <<"\n" <<effSampleName[iEffSample] <<endl;
	    
	  std::stringstream inter;
	  if ( !binnedVars.Contains("plateau") && !binnedVars.Contains("ptTurnOn") )
	    if ( abseta > 2 ) {
	      if ( trackName[iEffSample][iTrack] != "Mu8" ) {
		if (eff_triggers[iEff].first.Contains("L3"))
		  inter <<"pt_PLOT__abseta_" <<bins2name[iBins2] <<"_and_" <<eff_triggers[iEff-2].first <<"_pass_and_TMOST_pass_and_Track_HP_pass_and_tag_" <<"Mu7p5_L2Mu2" <<"_Jpsi_MU_pass" ;
		else if (eff_triggers[iEff].first.Contains("L1L2"))
		  inter <<"pt_PLOT__abseta_" <<bins2name[iBins2] <<"_and_" <<trackName[iEffSample][iTrack] <<"_Jpsi_TK_pass_and_TMOST_pass_and_Track_HP_pass_and_tag_" <<trackName[iEffSample][iTrack] <<"_Jpsi_MU_pass" ;
		else if (eff_triggers[iEff].first.Contains("Vertexing")) 
		  inter <<"pair_pt_PLOT__pair_absrapidity_" <<bins2name[iBins2] <<"_and_" <<trackName[iEffSample][iTrack] <<"_pass_and_tag_" <<trackName[iEffSample][iTrack] <<"_pass" ;
		else 
		  inter <<"pt_PLOT__abseta_" <<bins2name[iBins2] <<"_and_" <<trackName[iEffSample][iTrack] <<"_Jpsi_TK_pass_and_tag_" <<trackName[iEffSample][iTrack] <<"_Jpsi_MU_pass" ;

	      } else 
		inter <<"pt_PLOT__abseta_" <<bins2name[iBins2] <<"_and_tag_" <<trackName[iEffSample][iTrack] <<"_pass" ;
	    } else
	      inter <<"pt_PLOT__" <<trackName[iEffSample][iTrack] <<"_Jpsi_TK_pass_and_tag_" <<trackName[iEffSample][iTrack] <<"_Jpsi_MU_pass" ;
	  else
	    if (trackName[iEffSample][iTrack] != "Mu8")
	      inter <<"abseta_PLOT__" <<trackName[iEffSample][iTrack] <<"_Jpsi_TK_pass_and_tag_" <<trackName[iEffSample][iTrack] <<"_Jpsi_MU_pass" ;
	    else if (trackName[iEffSample][iTrack] == "Mu8")
	      inter <<"abseta_PLOT__tag_" <<trackName[iEffSample][iTrack] <<"_pass" ;
	      
	  plot[iBins2] = inter.str() ;
	    
	  cout <<plot[iBins2].c_str() <<endl;
	  TCanvas *c = dynamic_cast<TCanvas*> (dir_fit_eff->Get( plot[iBins2].c_str() ));
	  if (!c) {
	    cout <<"No " <<plot[iBins2].c_str() <<" in " <<effSampleName[iEffSample] <<" file!" <<endl;
	    continue ;
	  }
	  TGraphAsymmErrors *tGraph = dynamic_cast<TGraphAsymmErrors*> (c->FindObject("hxy_fit_eff")) ;
	  titleX[iBins2] = tGraph->GetXaxis()->GetTitle() ;
	  titleY[iBins2] = tGraph->GetYaxis()->GetTitle() ;
	  //check if there are values in PLOT
	  int N = tGraph->GetN();
	  if (N == 0) {
	    cout <<"No values in " <<plot[iBins2].c_str() <<endl;
	    continue; }
	  
	  if (nBins1+1 > N) {
	    cout <<"nBins1+1 (= " <<nBins1+1 <<") is > #points in the TGraph (=" <<N <<")! Please check your bins1 array" <<endl;
	    //continue;
	  }
	  //for (int iPoint = 0; iPoint < nBins1; iPoint++) {
	  for(int iPoint = 0; iPoint < nBins1 +1; iPoint++) {
	      
	    //get values from plot
	    double x = 0, y = 0;
	    double z = tGraph->GetPoint(iPoint, x, y);
	    double err_high = tGraph->GetErrorYhigh(iPoint), err_low = tGraph->GetErrorYlow(iPoint);
	    double var_high = tGraph->GetErrorXhigh(iPoint), var_low = tGraph->GetErrorXlow(iPoint);
	    //if(err_high > 0.05) {err_high = err_low; cout <<"changed high error" <<endl;}
	    //if(err_low > 0.05) {err_low = err_high; cout <<"changed low error" <<endl;}
	    //if(iEffSample==1 && err_high > 0.05) {err_high = err_low; cout <<"changed MC high error" <<endl;}
	    if (y + err_high > 1) err_high = 1 - y;
	      
	    //store values
	    for (int s = 0; s < nBins1 +1; s++) {
	      if (x > bins1[s] && x < bins1[s+1]) {
		values[iEffSample][iTrack][s][iBins2].setEff(y, err_low, err_high);
		values[iEffSample][iTrack][s][iBins2].setVar(x, var_low, var_high);
		cout <<"Bin"<<s <<". " <<trackName[iEffSample][iTrack] <<": eff = " <<values[iEffSample][iTrack][s][iBins2].eff
		     <<" low = " <<values[iEffSample][iTrack][s][iBins2].eff_low <<" high = " <<values[iEffSample][iTrack][s][iBins2].eff_high
		     <<", " <<var1name <<" = " <<values[iEffSample][iTrack][s][iBins2].var <<endl;
		break;
	      }
	    }//s
 
	  } //iPoint
	} //iBins2
      } // iTrack
	
      cout <<endl ;

      for(int iBins2 = 0; iBins2 < nBins2; iBins2++) {

	//create TGraphAsymmErrors to store graph
	TGraphAsymmErrors *graph = new TGraphAsymmErrors();

	TString name = effSampleName[iEffSample];
	name.Append("__"+var2name+"_"+bins2name[iBins2]) ;
	cout <<"\n" <<name <<endl;

	graph->SetName(name);
	graph->SetTitle(plot[iBins2].c_str());
	int points = 0;

	for(int iBins1 = 0; iBins1 < nBins1; iBins1++) {
	  //for(int iBins1 = 0; iBins1 < nBins1 +1; iBins1++) {

	  // fill TGraphsAsymmErrors
	  // fill with Mu5_Track2 for pt < 9 GeV - former 7 GeV
	  //if (!isZero(values[iEffSample][0][iBins1][iBins2].eff)) {
	  if ( ((!binnedVars.Contains("plateau") && !binnedVars.Contains("ptTurnOn")) ? bins1[iBins1] : bins2[iBins2]) < triggerTreshold && !isZero(values[iEffSample][0][iBins1][iBins2].eff)) {
	    //if ((abseta == 0 && bins1[iBins1] >= 3.5) || (abseta == 1 && bins1[iBins1] >= 2.5) || (abseta == 2 && bins1[iBins1] >= 2.0)) {
	    if ((abseta == 0 && bins1[iBins1] >= 3.5) || (abseta == 1 && bins1[iBins1] >= 2.5) || (abseta >= 2 && bins1[iBins1] >= 2.0)) {
	      // only tight
	      //if((abseta == 0 && bins1[iBins1] >= 3.5) || (abseta == 1 && bins1[iBins1] >= 3.0) || (abseta == 2 && bins1[iBins1] >= 2.0)){
	      graph->SetPoint(points, values[iEffSample][0][iBins1][iBins2].var, values[iEffSample][0][iBins1][iBins2].eff);
	      graph->SetPointError(points,
				   values[iEffSample][0][iBins1][iBins2].var_low, values[iEffSample][0][iBins1][iBins2].var_high,
				   values[iEffSample][0][iBins1][iBins2].eff_low, values[iEffSample][0][iBins1][iBins2].eff_high);
	      cout <<eff_triggers[iEff].first <<" " <<effSampleName[iEffSample] <<" " <<trackName[iEffSample][0] <<" " <<points <<" ptbin = "  <<iBins1
		   <<" mean = " <<values[iEffSample][0][iBins1][iBins2].var <<" eff = " <<values[iEffSample][0][iBins1][iBins2].eff
		   <<" low = " <<values[iEffSample][0][iBins1][iBins2].eff_low <<" high = " <<values[iEffSample][0][iBins1][iBins2].eff_high
		   <<endl;
	      points++;
	      // }
	    }
	  }
	  // fill with Mu7p5_Track7 for pt > 9 GeV - former 7 GeV
	  else if( ((!binnedVars.Contains("plateau") && !binnedVars.Contains("ptTurnOn")) ? bins1[iBins1] : bins2[iBins2]) >= triggerTreshold && !isZero(values[iEffSample][1][iBins1][iBins2].eff)) {
	    graph->SetPoint(points, values[iEffSample][1][iBins1][iBins2].var, values[iEffSample][1][iBins1][iBins2].eff);
	    graph->SetPointError(points,
				 values[iEffSample][1][iBins1][iBins2].var_low, values[iEffSample][1][iBins1][iBins2].var_high,
				 values[iEffSample][1][iBins1][iBins2].eff_low, values[iEffSample][1][iBins1][iBins2].eff_high);
	    cout <<eff_triggers[iEff].first <<" " <<effSampleName[iEffSample] <<" " <<trackName[iEffSample][nTrack-1] <<" " <<points <<" ptbin = "  <<iBins1
		 <<" mean = " <<values[iEffSample][1][iBins1][iBins2].var <<" eff = " <<values[iEffSample][1][iBins1][iBins2].eff
		 <<" low = " <<values[iEffSample][1][iBins1][iBins2].eff_low <<" high = " <<values[iEffSample][1][iBins1][iBins2].eff_high
		 <<endl;
	    points++;
	  }

	} // iBins1

	graph->SetMarkerStyle(8);
	graph->Draw("ALP") ;
	graph->GetXaxis()->SetTitle( titleX[iBins2] ) ;
	graph->GetYaxis()->SetTitle( titleY[iBins2] ) ;
	output->cd();
	graph->Write();

      } // iBins2
      for (Int_t i=0; i<2; ++i)
	if (myTH2[i])
	  myTH2[i]->Write();
    } // iEffSample
    //output->Close() ;

    // overlay
    TString prefix = "../" ;
    prefix = "/afs/cern.ch/work/l/lecriste/www/TnP/" ;
    TString uploadFile = "index.php" ;
    //output = TFile::Open(output->GetName()) ;
    //cout <<"after open" <<endl ;
    if ( nEffSample > 1 ) {
      TGraphAsymmErrors *overlay[nEffSample] ;
      TCanvas *overlayC = new TCanvas("overlayC","overlay Canvas",800,600) ;
      for (int iBins2 = 0; iBins2 < nBins2; iBins2++) {
	output->cd();
	overlay[0] = (TGraphAsymmErrors*)output->Get(effSampleName[0]+"__abseta_"+bins2name[iBins2]) ;
	overlay[nEffSample-1] = (TGraphAsymmErrors*)output->Get(effSampleName[1]+"__abseta_"+bins2name[iBins2]) ;
	if ( overlay[0] ) {
	  overlay[0]->Draw("AP") ;
	  overlay[0]->SetMinimum( 0. ) ;
	  overlay[0]->SetMaximum( 1.1 ) ;
	} else cout <<"\nNo " <<effSampleName[0]+"__abseta_"+bins2name[iBins2] <<" TGraphAsymmErrors found!" <<endl ; 
	if ( overlay[nEffSample-1] ) {
	  overlay[nEffSample-1]->Draw("Psame") ;
	} else cout <<"\nNo " <<effSampleName[1]+"__abseta_"+bins2name[iBins2] <<" TGraphAsymmErrors found!" <<endl ;

	for (Int_t i=0; i<2; i++) {
	  overlay[i]->SetTitle( effSampleName[i]+"__abseta_"+bins2name[iBins2] );
	  overlay[i]->SetMarkerColor(i+1) ; overlay[i]->SetLineColor(i+1) ; overlay[i]->SetFillColor(0) ;
	  overlay[i]->GetXaxis()->SetMoreLogLabels();
	  overlay[i]->GetXaxis()->SetRangeUser(bins1[0],bins1[nBins1]);
	}

	//TString dir = prefix+"plots/mc/tpTree/"+eff_triggers[iEff].first+"/" ;
	TString dir = prefix+"plots/mc/50ns/tpTree/"+eff_triggers[iEff].first+"/" ;
	if (mode.Contains("25ns"))
	  dir.ReplaceAll("50ns","25ns") ;
	if ( inputfile[0].Contains("30M") || inputfile[1].Contains("30M"))
	  dir.ReplaceAll("/tpTree","/30M/tpTree") ;
	if ( effName[iEff].Contains("Vertexing") )
	  dir.ReplaceAll("tpTree","tpTreeOnePair") ;
	dir.ReplaceAll("/_","/") ;

	gSystem->mkdir(dir, true);
	if ( prefix.EqualTo("/afs/cern.ch/work/l/lecriste/www/TnP/") )
	  gSystem->CopyFile(prefix+uploadFile, dir+uploadFile, true);

	dir.Append( binnedVars+"/" ); dir.ReplaceAll("/_","/") ;
	gSystem->mkdir(dir, true);
	if ( prefix.EqualTo("/afs/cern.ch/work/l/lecriste/www/TnP/") )
	  gSystem->CopyFile(prefix+uploadFile, dir+uploadFile, true);

	dir.Append( eff_triggers[iEff].second[0]+"/" ); dir.ReplaceAll("/_","/") ;
	gSystem->mkdir(dir, true);
	if ( prefix.EqualTo("/afs/cern.ch/work/l/lecriste/www/TnP/") )
	  gSystem->CopyFile(prefix+uploadFile, dir+uploadFile, true);

	dir.Append( "overlay/" );
	gSystem->mkdir(dir, true);
	if ( prefix.EqualTo("/afs/cern.ch/work/l/lecriste/www/TnP/") )
	  gSystem->CopyFile(prefix+uploadFile, dir+uploadFile, true);

	dir.Append( effSampleName[nEffSample-1]+"/" );
	gSystem->mkdir(dir, true);
	if ( prefix.EqualTo("/afs/cern.ch/work/l/lecriste/www/TnP/") )
	  gSystem->CopyFile(prefix+uploadFile, dir+uploadFile, true);
 
	overlayC->SetLogx();
	overlayC->SetGrid() ; 
	gPad->BuildLegend(0.5, 0.12, 0.88, 0.32) ;
	overlayC->SaveAs( dir+bins2name[iBins2]+".png") ;
      }
    }
  
    TFile *data_yield_file = TFile::Open("../TnP_yield_Charmonium_PromptReco_50ns_first47ipb.root") ;
    //
    // ratio: DATA/MC
    if ( nEffSample > 1 ) {

      Int_t dataIdx = 1, noDataIdx = 0;
      for (int iEffSample = 0; iEffSample < nEffSample; iEffSample++)
	if ( effSampleName[iEffSample] == "DATA" ) {
	  dataIdx = iEffSample ;
	  noDataIdx = nEffSample-1-dataIdx ;
	}

      //TString dir = prefix+"plots/mc/tpTree/"+eff_triggers[iEff].first+"/" ;
      TString dir = prefix+"plots/mc/50ns/tpTree/"+eff_triggers[iEff].first+"/" ;
      if (mode.Contains("25ns"))
	dir.ReplaceAll("50ns","25ns") ;
      if ( inputfile[0].Contains("30M") || inputfile[1].Contains("30M"))
	dir.ReplaceAll("/tpTree","/30M/tpTree") ;
      if ( effName[iEff].Contains("Vertexing") )
	dir.ReplaceAll("tpTree","tpTreeOnePair") ;
      dir.ReplaceAll("/_","/") ;
      
      gSystem->mkdir(dir, true);
      if ( prefix.EqualTo("/afs/cern.ch/work/l/lecriste/www/TnP/") )
	gSystem->CopyFile(prefix+uploadFile, dir+uploadFile, true);
      
      dir.Append( binnedVars+"/" ); dir.ReplaceAll("/_","/") ;
      gSystem->mkdir(dir, true);
      if ( prefix.EqualTo("/afs/cern.ch/work/l/lecriste/www/TnP/") )
	gSystem->CopyFile(prefix+uploadFile, dir+uploadFile, true);
      
      dir.Append( eff_triggers[iEff].second[0]+"/" ); dir.ReplaceAll("/_","/") ;
      gSystem->mkdir(dir, true);
      if ( prefix.EqualTo("/afs/cern.ch/work/l/lecriste/www/TnP/") )
	gSystem->CopyFile(prefix+uploadFile, dir+uploadFile, true);
      
      dir.Append( "ratio/" );
      gSystem->mkdir(dir, true);
      if ( prefix.EqualTo("/afs/cern.ch/work/l/lecriste/www/TnP/") )
	gSystem->CopyFile(prefix+uploadFile, dir+uploadFile, true);
      
      dir.Append( effSampleName[nEffSample-1]+"/" );
      gSystem->mkdir(dir, true);
      if ( prefix.EqualTo("/afs/cern.ch/work/l/lecriste/www/TnP/") )
	gSystem->CopyFile(prefix+uploadFile, dir+uploadFile, true);
      
      gSystem->mkdir(dir+"fit/", true);
      if ( prefix.EqualTo("/afs/cern.ch/work/l/lecriste/www/TnP/") )
	gSystem->CopyFile(prefix+uploadFile, dir+"fit/"+uploadFile, true);
      
      for (int iBins2 = 0; iBins2 < nBins2; iBins2++) {
	TGraph *data_yield = (TGraph*)data_yield_file->Get("pT_yields_Mu7p5_Track2__abseta"+bins2name[iBins2]) ;
	if (data_yield == 0)
	  cout <<"No \"" <<"pT_yields_Mu7p5_Track2__abseta"+bins2name[iBins2] <<"\" TGraph found in file \"" <<data_yield_file->GetName() <<"\"" <<endl ;

	cout <<"\nRATIO and DIFF for " <<bins2name[iBins2] <<endl;
      	
	TGraphAsymmErrors *ratio = new TGraphAsymmErrors();
	ratio->SetTitle("Ratio "+effSampleName[dataIdx]+"/"+effSampleName[noDataIdx]+" for |#eta(#mu)| from"+bins2name[iBins2]+";muon p_{T} [GeV]");
	TCanvas* ratioC = 0; TCanvas* ratioFitC = 0 ; 
	//
	TGraphAsymmErrors *diff = new TGraphAsymmErrors();
	diff->SetTitle("Difference "+effSampleName[dataIdx]+" - "+effSampleName[noDataIdx]+" for |#eta(#mu)| from"+bins2name[iBins2]+";muon p_{T} [GeV]");
	TCanvas* diffC = 0 ; 

	int pointsRatio = 0, pointsDiff = 0;
	vector <vector <double>> eff_ratio(nBins1), eff_diff(nBins1) ;
	eff_ratio.resize(nBins1) ; eff_diff.resize(nBins1) ;
	for (int iBins1 = 0; iBins1 < nBins1; iBins1++) {
	  //for (int iBins1 = 0; iBins1 < nBins1 +1; iBins1++) {
	  
	  // compute ratio and diff
	  eff_ratio[iBins1].resize(4,0) ; eff_diff[iBins1].resize(4,1) ;
	  
	  if (bins1[iBins1] < triggerTreshold && !isZero(values[noDataIdx][0][iBins1][iBins2].eff)) { // 7 GeV
	    //if ((abseta == 0 && bins1[iBins1] >= 3.5) || (abseta == 1 && bins1[iBins1] >= 2.5) || (abseta == 2 && bins1[iBins1] >= 2.0)) {
	    if ((abseta == 0 && bins1[iBins1] >= 3.5) || (abseta == 1 && bins1[iBins1] >= 2.5) || (abseta >= 2 && bins1[iBins1] >= 2.0)) {
	      // only tight
	      //if((abseta == 0 && bins1[iBins1] >= 3.5) || (abseta == 1 && bins1[iBins1] >= 3.0) || (abseta == 2 && bins1[iBins1] >= 2.0)) {
	      // RATIO
	      eff_ratio[iBins1][1] = values[dataIdx][0][iBins1][iBins2].eff / values[noDataIdx][0][iBins1][iBins2].eff;
	      eff_ratio[iBins1][2] = eff_ratio[iBins1][1] *
		TMath::Sqrt(TMath::Power(values[dataIdx][0][iBins1][iBins2].eff_low/values[dataIdx][0][iBins1][iBins2].eff,2)
			    + TMath::Power(values[noDataIdx][0][iBins1][iBins2].eff_low/values[noDataIdx][0][iBins1][iBins2].eff,2));
	      eff_ratio[iBins1][3] = eff_ratio[iBins1][1] *
		TMath::Sqrt(TMath::Power(values[dataIdx][0][iBins1][iBins2].eff_high/values[dataIdx][0][iBins1][iBins2].eff,2)
			    + TMath::Power(values[noDataIdx][0][iBins1][iBins2].eff_high/values[noDataIdx][0][iBins1][iBins2].eff,2));
	      // DIFF
	      eff_diff[iBins1][1] = values[dataIdx][0][iBins1][iBins2].eff - values[noDataIdx][0][iBins1][iBins2].eff;
	      eff_diff[iBins1][2] = 
		TMath::Sqrt(TMath::Power(values[dataIdx][0][iBins1][iBins2].eff_low,2)
			    + TMath::Power(values[noDataIdx][0][iBins1][iBins2].eff_low,2));
	      eff_diff[iBins1][3] =
		TMath::Sqrt(TMath::Power(values[dataIdx][0][iBins1][iBins2].eff_high,2)
			    + TMath::Power(values[noDataIdx][0][iBins1][iBins2].eff_high,2));
	      // MEAN
	      eff_ratio[iBins1][0] = (values[dataIdx][0][iBins1][iBins2].var + values[noDataIdx][0][iBins1][iBins2].var)/2;
	      eff_diff[iBins1][0] = (values[dataIdx][0][iBins1][iBins2].var + values[noDataIdx][0][iBins1][iBins2].var)/2;
	      //
	      // }
	    }
	  }
	  else if (bins1[iBins1] >= triggerTreshold && !isZero(values[noDataIdx][1][iBins1][iBins2].eff)) { // 7 GeV
	    // RATIO
	    eff_ratio[iBins1][1] = values[dataIdx][1][iBins1][iBins2].eff / values[noDataIdx][1][iBins1][iBins2].eff;
	    eff_ratio[iBins1][2] = eff_ratio[iBins1][1] *
	      TMath::Sqrt(TMath::Power(values[dataIdx][1][iBins1][iBins2].eff_low/values[dataIdx][1][iBins1][iBins2].eff,2)
			  + TMath::Power(values[noDataIdx][1][iBins1][iBins2].eff_low/values[noDataIdx][1][iBins1][iBins2].eff,2));
	    eff_ratio[iBins1][3] = eff_ratio[iBins1][1] *
	      TMath::Sqrt(TMath::Power(values[dataIdx][1][iBins1][iBins2].eff_high/values[dataIdx][1][iBins1][iBins2].eff,2)
			  + TMath::Power(values[noDataIdx][1][iBins1][iBins2].eff_high/values[noDataIdx][1][iBins1][iBins2].eff,2));
	    // DIFF
	    eff_diff[iBins1][1] = values[dataIdx][1][iBins1][iBins2].eff - values[noDataIdx][1][iBins1][iBins2].eff;
	    eff_diff[iBins1][2] = 
	      TMath::Sqrt(TMath::Power(values[dataIdx][1][iBins1][iBins2].eff_low,2)
			  + TMath::Power(values[noDataIdx][1][iBins1][iBins2].eff_low,2));
	    eff_diff[iBins1][3] =
	      TMath::Sqrt(TMath::Power(values[dataIdx][1][iBins1][iBins2].eff_high,2)
			  + TMath::Power(values[noDataIdx][1][iBins1][iBins2].eff_high,2));
	    // MEAN
	    eff_ratio[iBins1][0] = (values[dataIdx][1][iBins1][iBins2].var + values[noDataIdx][1][iBins1][iBins2].var)/2;
	    eff_diff[iBins1][0] = (values[dataIdx][1][iBins1][iBins2].var + values[noDataIdx][1][iBins1][iBins2].var)/2;
	  }
	  
	  
	  double x_high = 0, x_low = 0;
	  for (int i = 0; i < nBins1; i++) {
	    if ((bins1[i] <= eff_ratio[iBins1][0]) && (bins1[i+1] >= eff_ratio[iBins1][0])){
	      //cout <<"found bin: " <<bins1[i] <<" " <<bins1[i+1] <<endl;
	      x_low = eff_ratio[iBins1][0] - bins1[i];
	      x_high = - eff_ratio[iBins1][0] + bins1[i+1];
	    }
	  }
	  //cout <<x_low <<" " <<x_high <<" " <<eff_ratio[iBins1][0] <<endl;
	  
	  //fill TGraphsAsymmErrors
	  if (!TMath::IsNaN(eff_ratio[iBins1][1]) && eff_ratio[iBins1][1]!=0) {
	    ratio->SetPoint(pointsRatio, eff_ratio[iBins1][0], eff_ratio[iBins1][1]);
	    ratio->SetPointError(pointsRatio, TMath::Abs(x_low), TMath::Abs(x_high), eff_ratio[iBins1][2], eff_ratio[iBins1][3]);
	    pointsRatio++;
	    
	    //cout <<eff_triggers[iEff].first <<" etabin = "  <<iBins1 <<" mean = " <<eff_ratio[iBins1][0]
	    //          <<" eff = " <<eff_ratio[iBins1][1] <<" low = " <<eff_ratio[iBins1][2] <<" high = " <<eff_ratio[iBins1][3]
	    //          <<endl;
	    diff->SetPoint(pointsDiff, eff_ratio[iBins1][0], eff_diff[iBins1][1]);
	    diff->SetPointError(pointsDiff, TMath::Abs(x_low), TMath::Abs(x_high), eff_diff[iBins1][2], eff_diff[iBins1][3]);
	    
	    pointsDiff++;
	  }
	  cout.precision(3);
	  //cout <<"Only Mu5_Track2 is shown. Be careful with ratios." <<endl;
	  cout <<" & " <<bins1[iBins1] <<" $ < p_T < $ " <<bins1[iBins1+1] <<" & $"
	       <<fixed <<values[dataIdx][0][iBins1][iBins2].eff <<"^{+"
	       <<values[dataIdx][0][iBins1][iBins2].eff_high <<"}_{-"
	       <<values[dataIdx][0][iBins1][iBins2].eff_low <<"}$ & $"
	       <<values[noDataIdx][0][iBins1][iBins2].eff <<"^{+"
	       <<values[noDataIdx][0][iBins1][iBins2].eff_high <<"}_{-"
	       <<values[noDataIdx][0][iBins1][iBins2].eff_low <<"}$ & $"
	    // RATIO
	       <<eff_ratio[iBins1][1] <<"^{+"
	       <<eff_ratio[iBins1][3] <<"}_{-"
	       <<eff_ratio[iBins1][2] <<"}$\\" <<endl
	    // DIFF
	       <<eff_diff[iBins1][1] <<"^{+"
	       <<eff_diff[iBins1][3] <<"}_{-"
	       <<eff_diff[iBins1][2] <<"}$\\" <<endl ;
	  
	} //iBins1
	
	// my layout
	cout <<"\n| pT bins |" ;
	cout <<"\n| Ratio |" ;
	cout <<"\n| Diff |\n" <<endl ;
	Int_t row_bins = 6 ;
	for (int iRow = 0; iRow < nBins1/row_bins +1; iRow++) {
	  for (int iBins1 = 0+(row_bins*iRow); iBins1 < (row_bins*(iRow+1) > nBins1 ? nBins1 : row_bins*(iRow+1)); iBins1++)
	    cout <<TString::Format("|     %4.3g < pT < %-4.3g       ",bins1[iBins1], bins1[iBins1+1]) ;
	  cout <<endl;
	  for (int iBins1 = 0+(row_bins*iRow); iBins1 < (row_bins*(iRow+1) > nBins1 ? nBins1 : row_bins*(iRow+1)); iBins1++) 
	    cout <<TString::Format("|  %.3f^{+%-6.2g}_{-%-6.2g} ", eff_ratio[iBins1][1], eff_ratio[iBins1][3], eff_ratio[iBins1][2]) ; 
	  cout <<endl;
	  for (int iBins1 = 0+(row_bins*iRow); iBins1 < (row_bins*(iRow+1) > nBins1 ? nBins1 : row_bins*(iRow+1)); iBins1++) 
	    cout <<TString::Format("| %+.3f^{+%-6.2g}_{-%-6.2g} ", eff_diff[iBins1][1], eff_diff[iBins1][3], eff_diff[iBins1][2]) ; 
	  cout <<endl ;
	  cout <<endl ;
	}
	
	
	ratio->SetMarkerStyle(8); diff->SetMarkerStyle(8);
	TString ratioName = "ratio_"+bins2name[iBins2], diffName = "diff_"+bins2name[iBins2] ;
	ratio->SetName( ratioName ) ;  diff->SetName( diffName ) ;
	output->cd();
	ratio->Write(); diff->Write();
	
	Int_t nx = 1, ny = 2 ;
	// RATIO
	ratioC = new TCanvas(ratioName,ratioName,nx*800,ny*600) ; ratioC->Divide(nx,ny);
	ratioC->cd(1) ;
	ratio->Draw("ALP") ;
	if (effSampleName[nEffSample-1] != "MC_Mu8") {
	  ratio->SetMinimum( 0.5 ) ; //0.6
	  ratio->SetMaximum( 1.5 ) ; //1.1
	} else { 
	  ratio->SetMinimum( 0.85 ) ;
	  ratio->SetMaximum( 1.15 ) ;
	}
	ratio->GetXaxis()->SetMoreLogLabels();
	ratio->GetXaxis()->SetRangeUser(bins1[0],bins1[nBins1]);
	gPad->SetGrid() ;
	//
	if (!effName[iEff].Contains("Vertexing")) {
	  gPad->SetLogx() ;
	  ratioC->cd(2) ;
	  if (data_yield) {
	    data_yield->Draw("ALP") ;
	    data_yield->GetXaxis()->SetRangeUser(bins1[0],bins1[nBins1]);
	    gPad->SetLogx() ;
	    gPad->SetGrid() ;
	  }
	}
	//ratioC->SaveAs( TString::Format("../plots/ratio/27oct/"+eff_triggers[iEff].first+"/%s.png", ratioName.Data()) ) ;
	//
	// DIFF
	diffC = new TCanvas(diffName,diffName,nx*800,ny*600) ; diffC->Divide(nx,ny);
	diffC->cd(1) ;
	diff->Draw("ALP") ;
	diff->SetMinimum( ratio->GetMinimum() - 1 ) ;
	diff->SetMaximum( ratio->GetMaximum() - 1 ) ;
	diff->GetXaxis()->SetMoreLogLabels();
	diff->GetXaxis()->SetRangeUser(bins1[0],bins1[nBins1]);
	gPad->SetGrid() ;
	if (!effName[iEff].Contains("Vertexing")) {
	  gPad->SetLogx() ;
	  diffC->cd(2) ;
	  if (data_yield) {
	    data_yield->Draw("ALP") ;
	    data_yield->GetXaxis()->SetRangeUser(bins1[0],bins1[nBins1]);
	    gPad->SetLogx() ;
	    gPad->SetGrid() ;
	  }
	}
	//diffC->SaveAs( TString::Format("../plots/ratio/27oct/"+eff_triggers[iEff].first+"/%s.png", diffName.Data()) ) ;

 
	ratioC->SaveAs( dir+ratioName+".png") ;
	diffC->SaveAs( dir+diffName+".png") ;

	// fit
	ratioFitC = new TCanvas(ratioName.Append("_fit"),ratioName,800,600) ;
	ratio->Draw("ALP") ;
	ratio->Fit("pol0");
	if (ratio->GetFunction("pol0")) ratio->GetFunction("pol0")->SetLineColor(kRed);
	gStyle->SetOptFit(111);
	TPaveStats *st = (TPaveStats*)ratio->GetListOfFunctions()->FindObject("stats");
	if (st) {
	  st->SetX1NDC(0.5); st->SetX2NDC(0.9); 
	  st->SetY1NDC(0.7); st->SetY2NDC(0.9); } 
	gPad->SetLogx() ;
	gPad->SetGrid() ;
	ratioFitC->SaveAs( dir+"fit/"+ratioName+".png") ;

      } //iBins2

    } // nEffSample > 1

  } // for (int iEff=6; iEff<=7; ++iEff) 
    
} //void

