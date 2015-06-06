import FWCore.ParameterSet.Config as cms

process = cms.Process('NTUPLE')

process.options = cms.untracked.PSet(
        wantSummary = cms.untracked.bool(True)
	#,SkipEvent = cms.untracked.vstring('ProductNotFound')
)
# import of standard configurations
process.load('FWCore/MessageService/MessageLogger_cfi')
process.MessageLogger.suppressInfo = cms.untracked.vstring( "mkcands" )
process.MessageLogger.suppressWarning = cms.untracked.vstring( "mkcands" )
process.MessageLogger.cerr.FwkReport.reportEvery = 1

#MC = False
MC = True
if MC :
        #official = False
        official = True

MCMotherId = 511 # 511 B0 (=anti-B0), 531 Bs0
#MCMotherId = 531
if MCMotherId == 511 :
    MCExclusiveDecay = True
elif MCMotherId == 531 :
    MCExclusiveDecay = False

# Input source
process.source = cms.Source("PoolSource",
                            skipEvents = cms.untracked.uint32( 0 ), #with 11976 Processing run: 201707 lumi: 281 event: 383901681
                            fileNames = cms.untracked.vstring()
)

if (not MC) :
    sourceFiles = cms.untracked.vstring(
            # Sanjay
            #'file:PYTHIA6_Bd2Psi2SKpi_TuneZ2star_8TeV_cff_py_RAW2DIGI_L1Reco_RECO.root'
            # dataset C
            '/store/data/Run2012C/MuOniaParked/AOD/22Jan2013-v1/30000/1E71D761-D870-E211-9343-00215E25A5E2.root'
    )
elif MC :
        if MCMotherId == 511 :
                if (not official) :
                        sourceFiles = cms.untracked.vstring(
                                # CRAB 
                                # private
                                #'file:/lustre/cms/store/group/cristella/Bd2Psi2SKpi-PHSP/MC_generation/141028_153606/merge/MC_Bd2Psi2SKpi_first111.root'
                                #'file:/lustre/cms/store/group/cristella/Bd2Psi2SKpi-PHSP/MC_generation/141028_153606/merge/MC_Bd2Psi2SKpi_1of2.root'
                                'file:/lustre/cms/store/group/cristella/Bd2Psi2SKpi-PHSP/MC_generation/141028_153606/merge/MC_Bd2Psi2SKpi.root'
                        )
                else :
                        sourceFiles = cms.untracked.vstring(
                                # offcial MC
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/00448020-25C4-E411-8D01-008CFA052A88.root',	
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/5AE5AE39-28C4-E411-9098-00266CFEFC38.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/A879FCE0-BFC3-E411-B78A-00266CFE7ADC.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/0637E61B-48C4-E411-BCB2-C4346BB28750.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/5E04151D-48C4-E411-A8C0-C4346BC076D0.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/A8A8F6C9-A8C3-E411-905A-6CC2173BC1D0.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/0AE361B0-A1C3-E411-AF9A-00266CFEFE1C.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/600063BF-9BC3-E411-AC48-00266CFFBF34.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/B0D2C91F-C6C3-E411-A468-00266CFF0ACC.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/0C90DA2C-9EC3-E411-A7B7-AC162DABAF78.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/6046D79D-2FC4-E411-B82A-00266CFFBCFC.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/B8D9ACDC-39C4-E411-80F4-00266CFFBF50.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/10CB4FC5-C9C3-E411-8421-008CFA052A88.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/6095427E-C7C3-E411-A635-6CC2173BB810.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/BAE3DAAD-38C4-E411-9DAF-00266CFFC980.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/14FDEDB4-A1C3-E411-B7EA-00266CFF0ACC.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/6212816F-3BC4-E411-9E47-00266CFFCAF0.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/BC34EB4F-EDC3-E411-9904-00266CFFCA1C.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/1CBB34C9-A8C3-E411-B0C6-C4346BC808B8.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/62179E9E-AEC3-E411-AFBB-008CFA052A88.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/C0F93096-33C4-E411-979E-00266CFFC980.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/20CF17F6-34C4-E411-8AD0-00266CFF0ACC.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/64E6F32C-C2C3-E411-A4ED-00266CFF0ACC.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/C211B5B9-A9C3-E411-AE4C-6CC2173BBEC0.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/222D8CA0-A7C3-E411-B77A-00266CFEFCE8.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/669215ED-02C6-E411-9951-00266CFFBF38.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/C29431E0-C4C3-E411-9C17-C4346BBF3E78.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/2232D902-ADC3-E411-A423-00266CFE6404.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/66B15C4A-C4C3-E411-B4C9-C4346BBF3E78.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/C8187CD8-3DC4-E411-BEDE-008CFA105EFC.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/244E8B4C-B1C3-E411-A630-008CFA0527CC.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/66D6B41B-9EC3-E411-99C3-6CC2173BB810.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/CE574DC3-C9C3-E411-8F26-00266CFFBF4C.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/2A1734A0-2BC4-E411-831B-00266CFF0ACC.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/6ACA30DA-3DC4-E411-B849-6CC2173BB820.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/CEB978AB-2BC4-E411-8FAE-AC162DABAF78.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/2A5193B6-E5C3-E411-B0AC-00266CFFBC38.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/6CA4F380-BCC3-E411-A08D-00266CFEFCE8.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/CEDACC05-16C4-E411-A8A4-00266CFFC550.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/2CDCD5EF-02C6-E411-9703-008CFA05206C.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/70BD3ABE-B6C3-E411-8B63-00266CFFBDAC.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/D0B947FF-BBC3-E411-BAE6-AC162DABAF78.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/300CC650-CBC3-E411-AD9C-C4346BC84780.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/720878DF-37C4-E411-844A-00266CFFC980.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/D0D2882D-DEC3-E411-BB80-6CC2173BC2E0.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/304FBEC0-B6C3-E411-9691-00266CFFC948.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/74C202CB-BAC3-E411-990E-AC162DABAF78.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/D27EB2B0-A1C3-E411-8415-00266CF82C98.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/3258550E-C7C3-E411-9B1A-00266CFFBF90.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/76757474-B3C3-E411-B009-008CFA052A88.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/D4011C85-BBC3-E411-A944-6CC2173BC2E0.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/34C80250-B1C3-E411-8B5D-00266CFE6404.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/7824B34B-32C4-E411-B74E-00266CFF0ACC.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/D47700A5-B9C3-E411-B27D-00266CFFCAF0.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/382480B4-2DC4-E411-A733-00266CFFBCFC.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/7866B903-03C6-E411-94B5-00266CFEFE70.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/D4830D7A-3EC4-E411-A498-008CFA105EFC.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/3E2DF3C3-C9C3-E411-AA1A-00266CFEFCE8.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/7AF5837C-35C4-E411-A601-AC162DABAF78.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/D6281850-CBC3-E411-A140-6CC2173BC7B0.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/3E7C0A93-BCC3-E411-95C9-00266CFFBEB4.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/8067216C-C2C3-E411-A72E-00266CFE6404.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/D88732F8-B1C3-E411-AF21-00266CFE6404.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/3EAC064E-C6C3-E411-A606-00266CFE7ADC.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/828F2CC2-AFC3-E411-A710-00266CFFBF90.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/DACA84DF-37C4-E411-8065-6CC2173BC7B0.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/3ECB44EE-B4C3-E411-AA4C-00266CFFCB7C.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/8ABADE21-E8C3-E411-A0BF-00266CFFCA1C.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/DC5910F3-34C4-E411-9340-00266CFFC980.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/3ED647FB-B2C3-E411-B755-008CFA052A88.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/906F7204-FDC3-E411-9EF8-00266CFFBEB4.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/DC66ECDC-39C4-E411-80E4-00266CFFBF50.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/425D3D8A-C1C3-E411-A4E9-00266CFFC9C4.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/928B32CD-9CC3-E411-AC4B-6CC2173BB810.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/DE150DEE-ACC3-E411-9A96-00266CFFBF50.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/42EBEEA2-E6C3-E411-8BC5-008CFA052A88.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/9434A1AF-9BC3-E411-89FE-00266CFFCA1C.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/E019C075-B2C3-E411-9A20-008CFA052A88.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/44DFCAEE-B4C3-E411-96B8-00266CFFBF94.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/98A9909D-2BC4-E411-8E92-6CC2173BC7B0.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/E02AAEC3-32C4-E411-BD24-00266CFF0ACC.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/46384706-C1C3-E411-887A-00266CFF0ACC.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/98CD61E6-ACC3-E411-BE1A-00266CFEFCE8.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/E0C8BB4A-C4C3-E411-9C3A-6CC2173BC7B0.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/485DE1CE-AAC3-E411-A595-00266CFFBF90.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/9A7D6CE8-B1C3-E411-BF1C-008CFA0527CC.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/E0D425EE-02C6-E411-B115-6CC2173BBED0.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/4ABDCA17-C6C3-E411-A0B9-6CC2173BB810.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/9C5188BF-B6C3-E411-951B-AC162DACB208.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/E6C4F686-3BC4-E411-B340-00266CFFC044.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/502B51E6-ACC3-E411-9DC2-C4346BBF3E78.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/A0015EDD-AFC3-E411-B2F8-00266CFFBEB4.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/E84F3AD8-BFC3-E411-8A08-008CFA0527CC.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/528732E8-ACC3-E411-B367-00266CFF0ACC.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/A01E5DA1-A7C3-E411-852D-00266CFFCA1C.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/F6B50DDB-C0C3-E411-89EE-00266CFFCA1C.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/52B3E4EF-C6C3-E411-8D60-6CC2173BB810.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/A0450ED9-BFC3-E411-A6F7-00266CFF0ACC.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/F6BD7B40-3AC4-E411-A343-00266CFF0ACC.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/56735BC2-AFC3-E411-90D2-6CC2173BBEC0.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/A61DF3A8-B9C3-E411-B53C-C4346BC7AAE0.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/5A7A64C1-C9C3-E411-99C8-C4346BC808B8.root',
                                'file:/lustre/cms/store/mc/Summer12DR53X/BdToPsi2SKPi_MSEL5_TuneZ2star_8TeV-pythia6/AODSIM/PU_RD2_START53_V19F-v1/10000/A8203BEC-BFC3-E411-BCE7-00266CFFC948.root'
                        )
        elif MCMotherId == 531 :
                sourceFiles = cms.untracked.vstring(
                # Bs
                '/store/mc/Summer12_DR53X/BsToPsiMuMu_2MuPtEtaFilter_8TeV-pythia6-evtgen/AODSIM/PU_S10_START53_V7A-v1/0000/005DE3B0-FDDC-E111-9812-00266CFFC198.root',
                '/store/mc/Summer12_DR53X/BsToPsiMuMu_2MuPtEtaFilter_8TeV-pythia6-evtgen/AODSIM/PU_S10_START53_V7A-v1/0000/0090EB21-15DD-E111-9BE2-0017A4770800.root',
                '/store/mc/Summer12_DR53X/BsToPsiMuMu_2MuPtEtaFilter_8TeV-pythia6-evtgen/AODSIM/PU_S10_START53_V7A-v1/0000/00A0B7F6-98DF-E111-866D-00266CFFC13C.root',
                '/store/mc/Summer12_DR53X/BsToPsiMuMu_2MuPtEtaFilter_8TeV-pythia6-evtgen/AODSIM/PU_S10_START53_V7A-v1/0000/00A0B7F6-98DF-E111-866D-00266CFFC13C.root',
                '/store/mc/Summer12_DR53X/BsToPsiMuMu_2MuPtEtaFilter_8TeV-pythia6-evtgen/AODSIM/PU_S10_START53_V7A-v1/0000/00A0B7F6-98DF-E111-866D-00266CFFC13C.root',
                '/store/mc/Summer12_DR53X/BsToPsiMuMu_2MuPtEtaFilter_8TeV-pythia6-evtgen/AODSIM/PU_S10_START53_V7A-v1/0000/00A0B7F6-98DF-E111-866D-00266CFFC13C.root',
                '/store/mc/Summer12_DR53X/BsToPsiMuMu_2MuPtEtaFilter_8TeV-pythia6-evtgen/AODSIM/PU_S10_START53_V7A-v1/0000/00A0B7F6-98DF-E111-866D-00266CFFC13C.root',
                '/store/mc/Summer12_DR53X/BsToPsiMuMu_2MuPtEtaFilter_8TeV-pythia6-evtgen/AODSIM/PU_S10_START53_V7A-v1/0000/00A0B7F6-98DF-E111-866D-00266CFFC13C.root',
                '/store/mc/Summer12_DR53X/BsToPsiMuMu_2MuPtEtaFilter_8TeV-pythia6-evtgen/AODSIM/PU_S10_START53_V7A-v1/0000/0213D14A-4CE0-E111-AC17-1CC1DE056080.root',
                '/store/mc/Summer12_DR53X/BsToPsiMuMu_2MuPtEtaFilter_8TeV-pythia6-evtgen/AODSIM/PU_S10_START53_V7A-v1/0000/0239D053-E7DF-E111-96FB-00266CFFBF90.root'
            )

process.PoolSource.fileNames = sourceFiles ;


process.source.inputCommands = cms.untracked.vstring(
        "keep *",
        "drop L1GlobalTriggerObjectMapRecord_hltL1GtObjectMap__RECO",
        "drop *_MEtoEDMConverter_*_*"
	)

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32( 150000 ) # 256Kb in 2' for 100 events, 1Mb in 7' for 1k events, 6Mb in 50' for 8650 events, 100Mb in 14h for 150k events, 1.4Gb in 4 days for 1.2M events of official MC
        #input = cms.untracked.int32( 1000 ) # 310Kb in 3' for 1k events of private MC
        #input = cms.untracked.int32( 100 ) # = 20Mb in 2h for 15k events, 2Mb in 10' for 1k events of Run2012C/MuOniaParked/AOD/22Jan2013-v1
	#input = cms.untracked.int32( 1000 ) # = 3Mb for 6546 events, 85Kb for 100, 800kb for 1k events of BsToPsiMuMu
	#input = cms.untracked.int32( 24000 ) # = 870Kb # timeout after 24500 for Run2012A/MuOnia
	#input = cms.untracked.int32( -1 ) # = 5718Kb # timeout after 3700 for Run2012A/MuOnia
	)

#Output size of CRAB jobs ~200MB usually works well. (max 300-500 Mb according to Cesare) 

process.load('Configuration.Geometry.GeometryIdeal_cff') # 53x

process.load("Configuration.StandardSequences.GeometryExtended_cff") # from Lucia
process.load("Configuration.StandardSequences.Reconstruction_cff") # from Lucia

process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.GlobalTag.globaltag = 'FT_53_V6_AN3::All'
process.GlobalTag.globaltag = 'START53_V19F::All'
#process.GlobalTag.globaltag = 'START53_V7C::All'


process.load('Configuration/EventContent/EventContent_cff')
#
#  Load common sequences
#
process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskAlgoTrigConfig_cff')
process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskTechTrigConfig_cff')
process.load('HLTrigger/HLTfilters/hltLevel1GTSeed_cfi')

####################################################################################
##################################good collisions############################################
    
#### 44x
#process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
#                                                      vertexCollection = cms.InputTag('offlinePrimaryVertices'),
#                                                      minimumNDOF = cms.uint32(4) ,
#                                                      maxAbsZ = cms.double(24),
#                                                      maxd0 = cms.double(2)
#                                           )

## 53x                                    
pvSelection = cms.PSet(
        minNdof = cms.double( 4. )
        , maxZ    = cms.double( 24. )
        , maxRho  = cms.double( 2. )
)

process.goodOfflinePrimaryVertices = cms.EDFilter("PrimaryVertexObjectFilter", # checks for fake PVs automatically
                                                  filterParams = pvSelection,
                                                  filter       = cms.bool( False ), # use only as producer
                                                  src          = cms.InputTag( 'offlinePrimaryVertices' )
                                          )

process.primaryVertexFilter = process.goodOfflinePrimaryVertices.clone( filter = True )


process.noscraping = cms.EDFilter("FilterOutScraping",
                                  applyfilter = cms.untracked.bool(True),
                                  debugOn = cms.untracked.bool(False),
                                  #debugOn = cms.untracked.bool(True),
                                  numtrack = cms.untracked.uint32(10),
                                  thresh = cms.untracked.double(0.25)
                          )


# PAT Layer 0+1
process.load("PhysicsTools.PatAlgos.patSequences_cff")
process.load("PhysicsTools.PatAlgos.cleaningLayer1.genericTrackCleaner_cfi")
process.cleanPatTracks.checkOverlaps.muons.requireNoOverlaps = cms.bool(False)
process.cleanPatTracks.checkOverlaps.electrons.requireNoOverlaps = cms.bool(False)
from PhysicsTools.PatAlgos.producersLayer1.muonProducer_cfi import *
patMuons.embedTrack = cms.bool(True)
patMuons.embedPickyMuon = cms.bool(False)
patMuons.embedTpfmsMuon = cms.bool(False)

# Prune generated particles to muons and their parents
process.genMuons = cms.EDProducer("GenParticlePruner",
                                  src = cms.InputTag("genParticles"),
                                  select = cms.vstring(
                                          "drop  *  ",                     # this is the default
                                          "++keep abs(pdgId) = 13",        # keep muons and their parents
                                          "drop pdgId == 21 && status = 2" # remove intermediate qcd spam carrying no flavour info
                                  )
 )



process.load("MuonAnalysis.MuonAssociators.patMuonsWithTrigger_cff")
from MuonAnalysis.MuonAssociators.patMuonsWithTrigger_cff import  addMCinfo, useExistingPATMuons, useL1MatchingWindowForSinglets, changeTriggerProcessName, switchOffAmbiguityResolution, addDiMuonTriggers
    # with some customization
if MC:
        addMCinfo(process)
        # since we match inner tracks, keep the matching tight and make it one-to-one
        process.muonMatch.maxDeltaR = 0.05
        process.muonMatch.resolveByMatchQuality = True

addDiMuonTriggers(process)
useExistingPATMuons(process,'cleanPatMuons',addL1Info=False)
changeTriggerProcessName(process, 'HLT')
switchOffAmbiguityResolution(process) # Switch off ambiguity resolution: allow multiple reco muons to match to the same trigger muon
useL1MatchingWindowForSinglets(process)

process.muonL1Info.maxDeltaR     = 0.3
process.muonL1Info.fallbackToME1 = True
process.muonMatchHLTL1.maxDeltaR     = 0.3
process.muonMatchHLTL1.fallbackToME1 = True
process.muonMatchHLTL2.maxDeltaR = 0.3
process.muonMatchHLTL2.maxDPtRel = 10.0
process.muonMatchHLTL3.maxDeltaR = 0.1
process.muonMatchHLTL3.maxDPtRel = 10.0
process.muonMatchHLTCtfTrack.maxDeltaR = 0.1
process.muonMatchHLTCtfTrack.maxDPtRel = 10.0
process.muonMatchHLTTrackMu.maxDeltaR = 0.1
process.muonMatchHLTTrackMu.maxDPtRel = 10.0

from PhysicsTools.PatAlgos.tools.trackTools import *
######## adding tracks refitted with different mass
from RecoTracker.TrackProducer.TrackRefitters_cff import *
from TrackingTools.MaterialEffects.RungeKuttaTrackerPropagator_cfi import *
#process.RungeKuttaTrackerPropagatorForMuons = TrackingTools.MaterialEffects.RungeKuttaTrackerPropagator_cfi.RungeKuttaTrackerPropagator.clone( Mass = cms.double(0.10565837), ComponentName = cms.string('RungeKuttaTrackerPropagatorForMuons') )
#process.refittedGeneralTracksMuon = RecoTracker.TrackProducer.TrackRefitter_cfi.TrackRefitter.clone( Propagator = "RungeKuttaTrackerPropagatorForMuons" )
process.RungeKuttaTrackerPropagatorForPions = TrackingTools.MaterialEffects.RungeKuttaTrackerPropagator_cfi.RungeKuttaTrackerPropagator.clone( Mass = cms.double(0.13957), ComponentName = cms.string('RungeKuttaTrackerPropagatorForPions') )
process.refittedGeneralTracksPion = RecoTracker.TrackProducer.TrackRefitter_cfi.TrackRefitter.clone( Propagator = "RungeKuttaTrackerPropagatorForPions" )
makeTrackCandidates( process,                                # patAODTrackCands
                     label = 'TrackCands',                   # output collection will be 'allLayer0TrackCands', 'allLayer1TrackCands', 'selectedLayer1TrackCands'
                     tracks = cms.InputTag('generalTracks'), # input track collection
                     #tracks = cms.InputTag('refittedGeneralTracksMuon'), # input track collection               // AP changed from generalTracks
                     #tracks = cms.InputTag('refittedGeneralTracksPion'), # input track collection               // AP changed from generalTracks
                     #particleType = 'mu+',                   # particle type (for assigning a mass)
                     particleType = 'pi+',                   # particle type (for assigning a mass)
                     preselection = 'pt > 0.35',              # preselection cut on candidates. Only methods of 'reco::Candidate' are available
                     selection = 'pt > 0.35',                 # Selection on PAT Layer 1 objects ('selectedLayer1TrackCands')
                     #selection = 'p < 0.7',                 # Selection on PAT Layer 1 objects ('selectedLayer1TrackCands')
                     isolation = {},                         # Isolations to use ('source':deltaR; set to {} for None)
                     isoDeposits = [],
                     mcAs = None                           # Replicate MC match as the one used for Muons
             );                                    # you can specify more than one collection for this

l1cands = getattr(process, 'patTrackCands')
l1cands.addGenMatch = False

######## adding tracks refitted with Kaon mass
#process.RungeKuttaTrackerPropagator.Mass = cms.double(0.493677)
process.RungeKuttaTrackerPropagatorForKaons = TrackingTools.MaterialEffects.RungeKuttaTrackerPropagator_cfi.RungeKuttaTrackerPropagator.clone(
        Mass = cms.double(0.493677), ComponentName = cms.string('RungeKuttaTrackerPropagatorForKaons') )
process.refittedGeneralTracksKaon = RecoTracker.TrackProducer.TrackRefitter_cfi.TrackRefitter.clone( Propagator = "RungeKuttaTrackerPropagatorForKaons" )
###################################################
makeTrackCandidates( process,                                        # patAODTrackCands
                     label = 'TrackKaonCands',                       # output collection will be 'allLayer0TrackCands', 'allLayer1TrackCands', 'selectedLayer1TrackCands'
                     #tracks = cms.InputTag('refittedGeneralTracksKaon'), # input track collection               // AP changed from generalTracks
                     tracks = cms.InputTag('generalTracks'), # input track collection               // AP changed from generalTracks
                     particleType = 'K+',                            # particle type (for assigning a mass)  // AP changed from pi to K
                     #particleType = 'pi+',                            # particle type (for assigning a mass)  // AP changed from pi to K
                     #particleType = 'mu+',                            # particle type (for assigning a mass)  // AP changed from pi to K
                     preselection = 'pt > 0.35',                      # preselection cut on candidates. Only methods of 'reco::Candidate' are available
                     selection = 'pt > 0.35',                         # Selection on PAT Layer 1 objects ('selectedLayer1TrackCands')
                     #selection = 'p < 0.7',                         # Selection on PAT Layer 1 objects ('selectedLayer1TrackCands')
                     isolation = {},                                 # Isolations to use ('source':deltaR; set to {} for None)
                     isoDeposits = [],
                     #mcAs = 'muon'                                   # Replicate MC match as the one used for Muons # AP "=None"  ??
                     mcAs = None                                    # Replicate MC match as the one used for Muons
             );                                                      # you can specify more than one collection for this

l1cands = getattr(process, 'patTrackKaonCands')
l1cands.addGenMatch = False

process.load("RecoTracker.DeDx.dedxHarmonic2_cfi")
process.dedxHarmonic2Kaon = RecoTracker.DeDx.dedxHarmonic2_cfi.dedxHarmonic2.clone (
        tracks = 'refittedGeneralTracksKaon',
        trajectoryTrackAssociation = 'refittedGeneralTracksKaon'
)
# dE/dx hits
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")
#process.load("RecoTracker.TrackProducer.TrackRefitters_cff") #already imported above
#process.TrackRefitter.src = 'generalTracks'
#process.TrackRefitter.src = 'refittedGeneralTracksPion'

#process.dedxHitInfo = cms.EDProducer("HSCPDeDxInfoProducer",
#                                     #tracks = cms.InputTag("TrackRefitter"),
#                                     #trajectoryTrackAssociation = cms.InputTag("TrackRefitter"),
#                                     tracks = cms.InputTag("refittedGeneralTracksPion"),
#                                     trajectoryTrackAssociation = cms.InputTag("refittedGeneralTracksPion"),
#                                     
#                                     UseStrip  = cms.bool(True),
#                                     UsePixel  = cms.bool(True),
#                                     MeVperADCStrip = cms.double(3.61e-06*265),
#                                     MeVperADCPixel = cms.double(3.61e-06),
#                                     
#                                     UseCalibration = cms.bool(False),
#                                     calibrationPath = cms.string("/afs/cern.ch/user/q/querten/workspace/public/dEdx/CMSSW_5_2_4/src/dEdx/ppGridProject/Gains.root"),
#                                     ShapeTest = cms.bool(True),
#                             )
#
#process.dedxHitInfoKaon = cms.EDProducer("HSCPDeDxInfoProducer",
#                                         tracks = cms.InputTag("refittedGeneralTracksKaon"),
#                                         trajectoryTrackAssociation = cms.InputTag("refittedGeneralTracksKaon"),
#                                         
#                                         UseStrip  = cms.bool(True),
#                                         UsePixel  = cms.bool(True),
#                                         MeVperADCStrip = cms.double(3.61e-06*265),
#                                         MeVperADCPixel = cms.double(3.61e-06),
#                                         
#                                         UseCalibration = cms.bool(False),
#                                         calibrationPath = cms.string("/afs/cern.ch/user/q/querten/workspace/public/dEdx/CMSSW_5_2_4/src/dEdx/ppGridProject/Gains.root"),
#                                         ShapeTest = cms.bool(True),
#                                 )


#process.PATfilter = cms.EDFilter("X3872FilterPAT")
process.PATfilter = cms.EDFilter("Z4430FilterPAT")

process.mkcands = cms.EDAnalyzer("MuMuPiKPAT",
                                 HLTriggerResults = cms.untracked.InputTag("TriggerResults","","HLT"),
                                 inputGEN  = cms.untracked.InputTag("genParticles"),
                                 VtxSample   = cms.untracked.string('offlinePrimaryVertices'),
                                 SameSign = cms.untracked.bool(False),
                                 DoMonteCarloTree = cms.untracked.bool( MC ),
                                 MonteCarloParticleId = cms.untracked.int32(20443),
                                 MonteCarloExclusiveDecay = cms.untracked.bool( MCExclusiveDecay ),
                                 MonteCarloMotherId = cms.untracked.int32( MCMotherId ), 
                                 MonteCarloDaughtersN = cms.untracked.int32( 3 ), # 3 for exclusive B0->psi'KPi
                                 #
                                 DoMuMuMassConstraint = cms.untracked.bool(True),
                                 #SkipJPsi = cms.untracked.bool(True),
                                 SkipJPsi = cms.untracked.bool(False),
                                 SkipPsi2S = cms.untracked.bool(False),
                                 MinNumMuPixHits = cms.untracked.int32(1),
                                 MinNumMuSiHits = cms.untracked.int32(8),
                                 MaxMuNormChi2 = cms.untracked.double(7),
                                 MaxMuD0 = cms.untracked.double(10.0),
                                 sharedFraction = cms.untracked.double(0.5),

                                 MinJPsiMass = cms.untracked.double(2.9), 
                                 MaxJPsiMass = cms.untracked.double(3.3), 
                                 MinPsiPrimeMass = cms.untracked.double(3.55), 
                                 MaxPsiPrimeMass = cms.untracked.double(3.8), 

                                 MinNumTrSiHits = cms.untracked.int32(4),
                                 MinTrPt = cms.untracked.double(0.350),
                                 Chi2NDF_Track =  cms.untracked.double(7.0),
				 # Delta R
				 MaxMuMuTrackDR = cms.untracked.double(1.5), 
                                 MaxB0CandTrackDR = cms.untracked.double(1.5),   
                                 UseB0Dr = cms.untracked.bool(True),            

                                 MinMuMuPiKMass = cms.untracked.double(4.8),
                                 MaxMuMuPiKMass = cms.untracked.double(5.6),

                                 resolvePileUpAmbiguity = cms.untracked.bool(True),
                                 addMuMulessPrimaryVertex = cms.untracked.bool(True),
                                 #addMuMulessPrimaryVertex = cms.untracked.bool(False),
                                 addB0lessPrimaryVertex = cms.untracked.bool(True),
                                 #Debug_Output = cms.untracked.bool(True),
                                 ##
                                 ##  use the correct trigger path
                                 ##
                                 TriggersForMatching = cms.untracked.vstring(
                                         # 2012 displaced J/psi = Alessandra
                                         #"HLT_DoubleMu4_Jpsi_Displaced_v9", "HLT_DoubleMu4_Jpsi_Displaced_v10", "HLT_DoubleMu4_Jpsi_Displaced_v11", "HLT_DoubleMu4_Jpsi_Displaced_v12",
                                         # Lucia
                                         # 2010
                                         #"HLT_DoubleMu3_Quarkonium_v1", "HLT_DoubleMu3_Quarkonium_v2",
                                         #"HLT_Dimuon6p5_Barrel_PsiPrime_v1",
                                         # 2011
                                         #"HLT_Dimuon7_PsiPrime_v1", "HLT_Dimuon7_PsiPrime_v2", "HLT_Dimuon7_PsiPrime_v3", "HLT_Dimuon7_PsiPrime_v4", "HLT_Dimuon7_PsiPrime_v5",
                                         #"HLT_Dimuon9_PsiPrime_v1", "HLT_Dimuon9_PsiPrime_v4", "HLT_Dimuon9_PsiPrime_v5",
                                         #"HLT_Dimuon11_PsiPrime_v1", "HLT_Dimuon11_PsiPrime_v4", "HLT_Dimuon11_PsiPrime_v5",
                                         # inclusive psi(2S)
                                         #"HLT_Dimuon0_PsiPrime_v3", "HLT_Dimuon0_PsiPrime_v4", "HLT_Dimuon0_PsiPrime_v5", "HLT_Dimuon0_PsiPrime_v6",
                                         "HLT_Dimuon5_PsiPrime_v3", "HLT_Dimuon5_PsiPrime_v4", "HLT_Dimuon5_PsiPrime_v5", "HLT_Dimuon5_PsiPrime_v6"
                                         #"HLT_Dimuon7_PsiPrime_v1", "HLT_Dimuon7_PsiPrime_v2", "HLT_Dimuon7_PsiPrime_v3", "HLT_Dimuon9_PsiPrime_v9",
                                         #"HLT_DoubleMu3p5_LowMass_Displaced_v3", "HLT_DoubleMu3p5_LowMass_Displaced_v4", "HLT_DoubleMu3p5_LowMass_Displaced_v5", "HLT_DoubleMu3p5_LowMass_Displaced_v6"
                                 ),
                                FiltersForMatching = cms.untracked.vstring(
                                        # Alessandra
                                        #"hltDisplacedmumuFilterDoubleMu4Jpsi", "hltDisplacedmumuFilterDoubleMu4Jpsi", "hltDisplacedmumuFilterDoubleMu4Jpsi", "hltDisplacedmumuFilterDoubleMu4Jpsi"
                                        # Kay
                                        "hltVertexmumuFilterDimuon5PsiPrime", "hltVertexmumuFilterDimuon5PsiPrime", "hltVertexmumuFilterDimuon5PsiPrime", "hltVertexmumuFilterDimuon5PsiPrime"#, "hltVertexmumuFilterDimuon7PsiPrime", "hltVertexmumuFilterDimuon7PsiPrime", "hltVertexmumuFilterDimuon7PsiPrime", "hltVertexmumuFilterDimuon7PsiPrime"                               
                                        #hltDoubleMu4JpsiDisplacedL3Filtered         
                                )
                                 
                                 
                         )


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('set_below.root')
)
if (not MC) :
    process.TFileService.fileName = cms.string('MuOniaRun2012C_25Apr_MuMuPiPiPAT_ntpl.root')
elif MC :
    if MCMotherId == 511 :
            if (not official) :
                    process.TFileService.fileName = cms.string('BdToPsiKpi_18Mar_MuMuPiKPAT_ntpl.root')
            else :
                    process.TFileService.fileName = cms.string('officialBdToPsiKpi_18Mar_MuMuPiKPAT_ntpl.root')
    elif MCMotherId == 531 :
        process.TFileService.fileName = cms.string('BsToPsiMuMu_03Mar_MuMuPiKPAT_ntpl.root')


# turn off MC matching for the process
from PhysicsTools.PatAlgos.tools.coreTools import *
# old: removeMCMatching(process, ['All'], outputInProcess = False)
removeMCMatching(process,['All'],"",None,[])

process.patDefaultSequence.remove(process.patJetCorrFactors)
process.patDefaultSequence.remove(process.patJetCharge)
process.patDefaultSequence.remove(process.patJetPartonMatch)
process.patDefaultSequence.remove(process.patJetGenJetMatch)
process.patDefaultSequence.remove(process.patJetPartons)
## error in 5_3_22, so removing it
#process.patDefaultSequence.remove(process.patJetPartonAssociation)
process.patDefaultSequence.remove(process.patJetFlavourAssociation)
process.patDefaultSequence.remove(process.patJets)
## error in 53x, so removing it
#process.patDefaultSequence.remove(process.metJESCorAK5CaloJet)
#process.patDefaultSequence.remove(process.metJESCorAK5CaloJetMuons)
process.patDefaultSequence.remove(process.patMETs)
process.patDefaultSequence.remove(process.selectedPatJets)
process.patDefaultSequence.remove(process.cleanPatJets)
process.patDefaultSequence.remove(process.countPatJets)

process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('onia2MuMuPAT.root'),
                               outputCommands = cms.untracked.vstring('drop *',
                                                #'keep *_genMuons_*_Onia2MuMuPAT',                      # generated muons and parents
                                                'keep patMuons_patMuonsWithTrigger_*_NTUPLE',    # All PAT muons including general tracks and matches to triggers
                                                              )
                       )

process.filter = cms.Sequence(
        process.goodOfflinePrimaryVertices
        + process.primaryVertexFilter
        + process.noscraping
)
#44x process.filter = cms.Sequence(process.primaryVertexFilter+process.noscraping)

process.ntup = cms.Path(
        #process.refittedGeneralTracksPion *
        #process.refittedGeneralTracksMuon *
        #process.refittedGeneralTracksKaon *
        #process.offlineBeamSpot * process.TrackRefitter * process.dedxHitInfo
        #process.dedxHarmonic2Kaon * 
        process.offlineBeamSpot #* process.dedxHitInfo
        * process.filter
        * process.patDefaultSequence
        * process.patMuonsWithTriggerSequence
        * process.PATfilter
        * process.mkcands
)

process.schedule = cms.Schedule(process.ntup)

# rsync -vut --existing test/crab/runMuMuPiKPAT_dataOrMC_03Mar.py cristella@cmssusy.ba.infn.it:/cmshome/cristella/work/Z_analysis/exclusive/clean_14ott/CMSSW_5_3_22/src/UserCode/MuMuPiKPAT/test/crab/runMuMuPiKPAT_dataOrMC_03Mar.py

