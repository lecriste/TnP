#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <sstream>
#include <ctype.h>
#include <errno.h>
#include "TChain.h"
#include "TString.h"
//#include "TFile.h"

//gROOT->SetBatch(kTRUE);  // SERVE???????

// to be executed : root[0] .L merge.C ; root[1] main()

int main() {

  //TString path = "0000";
  //TString outputFile = "MuOniaParked_Run2012C_22Jan2013v1_MuMuPiKPAT";
  //TString outputFile = "official_BdToPsiKpi_18Mar_MuMuPiKPAT";
  //TString inputFile = "MuOniaRun2012C_25Apr_MuMuPiPiPAT_ntpl";
  TString inputFile = "tnpJPsi_officialBPHMC";
  TString outputFile = inputFile ;
  //TString outputFile = "MuOniaRun2012D_25Apr_MuMuPiPiPAT_ntpl" ;
  //FILE *fp = fopen( TString::Format("./%s.root",outputFile.Data()), "r" );
  //TFile *fp = TFile::Open( TString::Format("./%s.root",outputFile.Data()), "r" );
  //TFile *fp = new TFile(TString::Format("./%s.root",outputFile.Data()), "recreate");

  //TChain *chain = new TChain("mkcands/Z_data","");
  //TChain *chain = new TChain("tpTree/fitter_tree","");
  //TChain *chainSta = new TChain("tpTreeSta/fitter_tree","");

  //TTree::SetMaxTreeSize(250000000000); // for TChain

  for (Int_t i=0; i<=9; i++) {
    TString path = TString::Format("000%d",i);
    //TFile *fp = new TFile(TString::Format("./%s_%s.root",inputFile.Data(),path.Data()), "recreate");
    //fp->mkdir("tpTree")->cd(); // gives error
    //TString outputFile = "MuOniaParked_Run2012C_22Jan2013v1_MuMuPiKPAT_"+path+".root"; // moved above

    //FILE *fp = fopen("0000/MuOniaParked_Run2012C_22Jan2013v1_MuMuPiKPAT_0000.root","r");
    //FILE *fp = fopen( TString::Format("%s/%s",path.Data(),outputFile.Data()), "r" ); // moved above

    //TChain *chain = new TChain("mkcands/Z_data",""); // moved above

    //chain->Add("0000/BdToPsiKpi_18Mar_MuMuPiKPAT_ntpl_*.root");
    //chain->Add( TString::Format("%s/BdToPsiKpi_18Mar_MuMuPiKPAT_ntpl_*.root",path.Data()) );
    //chain->Add( TString::Format("%s/officialBdToPsiKpi_18Mar_MuMuPiKPAT_ntpl_*.root",path.Data()) );
    //chain->Add( TString::Format("%s/%s_%s*.root",path.Data(),outputFile.Data(),path.Data()) );
    //chain->Add( TString::Format("%s/%s_*.root",path.Data(),inputFile.Data()) ); // last used
    //chainSta->Add( TString::Format("%s/%s_*.root",path.Data(),outputFile.Data()) );

    //TTree::SetMaxTreeSize(30000000000); // moved above

    //chain->Merge("0000/MuOniaParked_Run2012C_22Jan2013v1_MuMuPiKPAT_0000.root");
    //chain->Merge( TString::Format("./%s_%s.root",outputFile.Data(),path.Data()) );
    //fp->Close();


    // with hadd command
    TString intermediateFile = outputFile + "_" + path + ".root" ;
    TString intermediateLog = "hadd_" + path + "_log.txt" ;
    TString prefix = "root://eoscms.cern.ch//eos/cms/store/group/phys_muon/lecriste/TnP/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/crab_TnP_fullMC_Mu8/150909_164454/" ;
    //gSystem->Exec(TString::Format("hadd -f -k -v 1 %s %s%s/%s*.root > %s", intermediateFile.Data(), prefix.Data(), path.Data(), inputFile.Data(), intermediateLog.Data())) ;
    // for eos
    TString eos = "/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select" ;
    gSystem->Exec(TString::Format("%s ls %s%s/ | grep .root | awk '{ printf \"%s%s/\"; print }' | xargs hadd -f -k -v 1 %s > %s", eos.Data(), prefix.Data(), path.Data(), prefix.Data(), path.Data(), intermediateFile.Data(), intermediateLog.Data() )) ;

  }

  //fp->mkdir("tpTree")->cd();
  //chain->Merge( TString::Format("./%s.root",outputFile.Data()) ); // last used
  //fp->mkdir("tpTreeSta")->cd();
  //chainSta->Merge( TString::Format("./%s.root",outputFile.Data()) );

  //fp->Close();


  // with hadd command
  gSystem->Exec(TString::Format("hadd -f -k -v 1 %s.root %s*.root > hadd_log.txt", outputFile.Data(), outputFile.Data())) ;

  return 0 ;
}
