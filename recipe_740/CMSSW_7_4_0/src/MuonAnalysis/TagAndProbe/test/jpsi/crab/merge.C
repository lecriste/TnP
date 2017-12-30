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

  //FILE *fp = fopen( TString::Format("./%s.root",outputFile.Data()), "r" );
  //TFile *fp = TFile::Open( TString::Format("./%s.root",outputFile.Data()), "r" );
  //TFile *fp = new TFile(TString::Format("./%s.root",outputFile.Data()), "recreate");

  //TChain *chain = new TChain("mkcands/Z_data","");
  //TChain *chain = new TChain("tpTree/fitter_tree","");
  //TChain *chainSta = new TChain("tpTreeSta/fitter_tree","");

  //TTree::SetMaxTreeSize(250000000000); // for TChain

  TString eos = "/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select" ;

  //TString prefix = "/eos/cms/store/group/phys_muon/lecriste/TnP/Charmonium/crab_TnP_last50nsRun_standardCfg_withL2Filter/150922_224126/" ;
  //TString prefix = "/eos/cms/store/group/phys_muon/lecriste/TnP/Charmonium/crab_TnP_full50nsData_standardCfg_withL2Filter/150921_075028/" ;
  //TString prefix = "/eos/cms/store/group/phys_muon/lecriste/TnP/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/crab_TnP_fullMC_standardCfg_withCorrectL2Filter/151016_215636/" ;
  //TString prefix = "/eos/cms/store/group/phys_muon/lecriste/TnP/Charmonium/crab_TnP_50nsFirst47ipb_standardCfg_withCorrectL2Filter/151018_154048/" ;
  //TString prefix = "/eos/cms/store/group/phys_muon/lecriste/TnP/Charmonium/crab_TnP_50nsFirst47ipb_OniaTriggersFlags/151024_112308/" ;
  //TString prefix = "/eos/cms/store/group/phys_muon/lecriste/TnP/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/crab_TnP_fullMC_OniaTriggersFlags/151023_225039/" ;
  //TString prefix = "/eos/cms/store/group/phys_muon/lecriste/TnP/Charmonium/crab_TnP_50nsFirst47ipb_vertexingTriggersFlags/151103_171444/" ;
  //TString prefix = "/eos/cms/store/group/phys_muon/lecriste/TnP/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/crab_TnP_fullMC_vertexingTriggersFlags_withMCMatch/151104_183446/" ;
  //TString prefix = "/eos/cms/store/group/phys_muon/lecriste/TnP/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/crab_TnP_fullMC25ns/151126_113230/" ;
  //TString prefix = "/eos/cms/store/group/phys_muon/lecriste/TnP/Charmonium/crab_TnP_RunDv3_25ns/151126_165735/" ; TString dir = "crab_TnP_RunDv3_25ns";
  //TString prefix = "/eos/cms/store/group/phys_muon/lecriste/TnP/Charmonium/crab_TnP_RunDv4_25ns/151126_170321/" ; TString dir = "crab_TnP_RunDv4_25ns";
  //TString prefix = "/eos/cms/store/group/phys_muon/lecriste/TnP/Charmonium/crab_TnP_RunC_25ns/151126_160437/" ; TString dir = "crab_TnP_RunC_25ns";
  //TString prefix = "/eos/cms/store/group/phys_muon/lecriste/TnP/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/crab_TnP_fullMC_withAllTagVars/151211_174215/" ; TString dir = "crab_TnP_fullMC_withAllTagVars";
  //TString prefix = "/eos/cms/store/group/phys_muon/lecriste/TnP/Charmonium/crab_TnP_RunC_25ns_noPairVtxInfo/160108_111956/" ; TString dir = "crab_TnP_RunC_25ns_noPairVtxInfo";
  //TString dir = "crab_TnP_RunC_25ns_noPairVtxInfo"; TString task = "160108_111956" ;
  //TString prefix = "/eos/cms/store/group/phys_muon/lecriste/TnP/Charmonium/crab_TnP_RunDv3_25ns_noPairVtxInfo/160108_132823/" ; TString dir = "crab_TnP_RunDv3_25ns_noPairVtxInfo";
  TString dir = "crab_TnP_RunDv3_25ns_noPairVtxInfo"; TString task = "160108_132823" ;
  //TString prefix = "/eos/cms/store/group/phys_muon/lecriste/TnP/Charmonium/crab_TnP_RunDv4_25ns_noPairVtxInfo/160109_223454/" ; TString dir = "crab_TnP_RunDv4_25ns_noPairVtxInfo";
  //TString dir = "crab_TnP_RunDv4_25ns_noPairVtxInfo"; TString task = "160109_223454" ;
  //TString prefix = "/eos/cms/store/group/phys_muon/lecriste/TnP/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/crab_TnP_fullMC_25ns_withAllTagVars/160201_100551/" ; TString dir = "crab_TnP_fullMC_25ns_withAllTagVars";
  //TString prefix = "/eos/cms/store/group/phys_muon/lecriste/TnP/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/crab_TnP_fullMC_25ns_addingMu25/160208_174353/" ;
  //TString dir = "crab_TnP_fullMC_25ns_addingMu25"; TString task = "160208_174353" ;
  //TString prefix = "/eos/cms/store/group/phys_muon/lecriste/TnP/Charmonium/crab_TnP_RunC_25ns_addingMu25/160208_171741/" ; TString dir = "crab_TnP_RunC_25ns_addingMu25"; 
  //TString prefix = "/eos/cms/store/group/phys_muon/lecriste/TnP/Charmonium/crab_TnP_RunDv3_25ns_addingMu25/160208_171839/" ; TString dir = "crab_TnP_RunDv3_25ns_addingMu25";
  //TString prefix = "/eos/cms/store/group/phys_muon/lecriste/TnP/Charmonium/crab_TnP_RunDv4_25ns_addingMu25/160208_171916/" ; TString dir = "crab_TnP_RunDv4_25ns_addingMu25";
  // Mu8
  //TString prefix = "/eos/cms/store/group/phys_muon/lecriste/TnP/DoubleMuon/crab_TnP_RunC_25ns_Mu8/160129_082727/" ; TString dir = "crab_TnP_RunC_25ns_Mu8";
  //TString prefix = "/eos/cms/store/group/phys_muon/lecriste/TnP/DoubleMuon/crab_TnP_RunDv4_25ns_Mu8/160129_081627/" ; TString dir = "crab_TnP_RunDv4_25ns_Mu8";
  //TString prefix = "/eos/cms/store/group/phys_muon/lecriste/TnP/DoubleMuon/crab_TnP_RunDv3_25ns_Mu8_v2/160131_233829/" ; TString dir = "crab_TnP_RunDv3_25ns_Mu8_v2";

  //TString rootPrefix = "root://eoscms.cern.ch/"+prefix ;

  TString prefix = "";
  TString inputFile = "";
  if (dir.Contains("MC")) {
    prefix = "/store/group/phys_muon/lecriste/TnP/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8";
    inputFile = "tnpJPsi_officialBPHMC";
  } else {
   prefix = "/store/group/phys_muon/lecriste/TnP/Charmonium"; 
   inputFile = "tnpJPsi_Data"; }
  
  TString rootPrefix = "root://eoscms.cern.ch/"+prefix+"/"+dir+"/"+task+"/" ;

  //TString outputFile = "full50nsRun" ;
  //TString outputFile = "last50nsRun" ;
  TString outputFile = inputFile ;
  
  for (Int_t i=2; i<=5; i++) {
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
    /*
    TString intermediateFile = outputFile + "_" + path + ".root" ;
    TString intermediateLog = "hadd_" + path + "_log.txt" ;
    //gSystem->Exec(TString::Format("hadd -f -k -v 1 %s %s%s/%s*.root > %s", intermediateFile.Data(), prefix.Data(), path.Data(), inputFile.Data(), intermediateLog.Data())) ;
    // for eos
    //gSystem->Exec(TString::Format("%s ls %s%s/ | grep .root | awk '{ printf \"%s%s/\"; print }' | xargs hadd -f -k -v 1 %s > %s", eos.Data(), rootPrefix.Data(), path.Data(), rootPrefix.Data(), path.Data(), intermediateFile.Data(), intermediateLog.Data() )) ;
    gSystem->Exec(TString::Format("%s ls %s%s/ | grep .root | awk '{ printf \"%s%s/\"; print }' | xargs hadd -f -k -v 1 %s/%s > %s/%s", eos.Data(), rootPrefix.Data(), path.Data(), rootPrefix.Data(), path.Data(), dir.Data(), intermediateFile.Data(), dir.Data(), intermediateLog.Data() )) ;
    */
    TString subdir = dir+"/"+path;
    gSystem->mkdir(subdir, false);
    for (Int_t j=0; j<=9; j++) {
      TString intermediateFile = outputFile + "_" + path + "_" + TString::Itoa(j,10) + ".root" ;
      TString intermediateLog = "hadd_" + path + "_" + TString::Itoa(j,10) + "_log.txt" ;
      gSystem->Exec(TString::Format("%s ls %s%s/ | grep %d.root | awk '{ printf \"%s%s/\"; print}' | xargs hadd -f -k -v 1 %s/%s > %s/%s", eos.Data(), rootPrefix.Data(), path.Data(), j, rootPrefix.Data(), path.Data(), subdir.Data(), intermediateFile.Data(), subdir.Data(), intermediateLog.Data() )) ;
    }
    gSystem->Exec(TString::Format("hadd -f -k -v 1 %s/%s_%s.root %s/%s_%s_*.root > %s/hadd_%s_log.txt", dir.Data(), outputFile.Data(), path.Data(), subdir.Data(), outputFile.Data(), path.Data(), dir.Data(), path.Data())) ;

  }

  //fp->mkdir("tpTree")->cd();
  //chain->Merge( TString::Format("./%s.root",outputFile.Data()) ); // last used
  //fp->mkdir("tpTreeSta")->cd();
  //chainSta->Merge( TString::Format("./%s.root",outputFile.Data()) );

  //fp->Close();


  // with hadd command
  //gSystem->Exec(TString::Format("hadd -f -k -v 1 %s.root %s_000*.root > hadd_log.txt", outputFile.Data(), outputFile.Data())) ;
  //gSystem->Exec(TString::Format("hadd -f -k -v 1 %s/%s.root %s/%s_000*.root > %s/hadd_log.txt", dir.Data(), outputFile.Data(), dir.Data(), outputFile.Data(), dir.Data())) ;
  gSystem->Exec(TString::Format("hadd -f -k -v 1 %s/%s.root %s/%s_000*.root > %s/hadd_log.txt", dir.Data(), outputFile.Data(), dir.Data(), outputFile.Data(), dir.Data())) ;

  return 0 ;
}
