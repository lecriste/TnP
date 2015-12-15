import FWCore.ParameterSet.Config as cms

process = cms.Process("TagProbe")

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.source = cms.Source("PoolSource", 
    fileNames = cms.untracked.vstring(),
)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000000) ) # 3' for 1k vents on Run2015C, 2.5MB in 20' for 10k events, 90MB in 26h for 1M events on Run2015C   


process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("Configuration.StandardSequences.Reconstruction_cff")

import os
if   "CMSSW_5_3_" in os.environ['CMSSW_VERSION']:
    process.GlobalTag.globaltag = cms.string('GR_R_53_V7::All')
    process.source.fileNames = [
        '/store/data/Run2012C/MuOnia/AOD/PromptReco-v1/000/198/208/B0C8994D-2CC7-E111-B04E-0025901D6288.root',
        '/store/data/Run2012C/MuOnia/AOD/PromptReco-v1/000/198/208/76FB8276-3AC7-E111-A52E-001D09F297EF.root',
        '/store/data/Run2012C/MuOnia/AOD/PromptReco-v1/000/198/208/76E299E2-2FC7-E111-B2CC-001D09F28F25.root',
        '/store/data/Run2012C/MuOnia/AOD/PromptReco-v1/000/198/208/5C0AD4DE-4AC7-E111-9C14-001D09F23A20.root',
        '/store/data/Run2012C/MuOnia/AOD/PromptReco-v1/000/198/208/4E4682A9-30C7-E111-9A8C-003048F1C420.root',
        '/store/data/Run2012C/MuOnia/AOD/PromptReco-v1/000/198/208/3669603F-2FC7-E111-8935-003048D2BE06.root',
        '/store/data/Run2012C/MuOnia/AOD/PromptReco-v1/000/198/208/0E9130E2-2FC7-E111-9494-001D09F26509.root',
        '/store/data/Run2012C/MuOnia/AOD/PromptReco-v1/000/198/208/02CA3FBC-2DC7-E111-9CA1-003048D2BB90.root',
    ]
elif "CMSSW_5_2_" in os.environ['CMSSW_VERSION']:
    process.GlobalTag.globaltag = cms.string('GR_P_V39_AN1::All')
    process.source.fileNames = [
        '/store/data/Run2012A/MuOnia/AOD/PromptReco-v1/000/191/226/645E9BE9-FC87-E111-9D30-5404A63886C5.root',
        '/store/data/Run2012A/MuOnia/AOD/PromptReco-v1/000/191/226/60C36C17-0188-E111-8B3D-5404A638868F.root',
        '/store/data/Run2012A/MuOnia/AOD/PromptReco-v1/000/191/226/5E384785-F087-E111-A8CB-BCAEC518FF80.root',
        '/store/data/Run2012A/MuOnia/AOD/PromptReco-v1/000/191/226/5C605E9F-F887-E111-A540-00237DDC5CB0.root',
        '/store/data/Run2012A/MuOnia/AOD/PromptReco-v1/000/191/226/5C0DCA92-CE87-E111-A539-5404A63886C6.root',
        '/store/data/Run2012A/MuOnia/AOD/PromptReco-v1/000/191/226/5A856F46-1888-E111-A3A5-BCAEC5329700.root',
        '/store/data/Run2012A/MuOnia/AOD/PromptReco-v1/000/191/226/5271187F-DF87-E111-ADDB-BCAEC518FF7C.root',
    ]
elif "CMSSW_7_4_" in os.environ['CMSSW_VERSION']:
    process.GlobalTag.globaltag = cms.string('GR_P_V56::All')
    process.source.fileNames = [
        # 50 ns
        #'/store/data/Run2015B/Charmonium/AOD/PromptReco-v1/000/251/164/00000/56BA3AC3-A226-E511-98BB-02163E0133B5.root',
	#'/store/data/Run2015B/Charmonium/AOD/PromptReco-v1/000/251/167/00000/FED37D13-A826-E511-8641-02163E01386E.root',
	#'/store/data/Run2015B/Charmonium/AOD/PromptReco-v1/000/251/168/00000/1602316B-CF26-E511-BCBA-02163E011BF3.root',
	#'/store/data/Run2015B/Charmonium/AOD/PromptReco-v1/000/251/168/00000/86456DCF-D026-E511-A8E2-02163E011D37.root',
        #'/store/data/Run2015B/Charmonium/AOD/PromptReco-v1/000/251/162/00000/E855BF93-4227-E511-8207-02163E011976.root',
        #'/store/data/Run2015B/Charmonium/AOD/PromptReco-v1/000/251/244/00000/4ADDEB99-6727-E511-BEF2-02163E011955.root',
        #'/store/data/Run2015B/Charmonium/AOD/PromptReco-v1/000/251/244/00000/C6DB3E01-8327-E511-B696-02163E0139CF.root',
        #'/store/data/Run2015B/Charmonium/AOD/PromptReco-v1/000/251/244/00000/FC4B5FE2-8A27-E511-A0DD-02163E014729.root',
        #'/store/data/Run2015B/Charmonium/AOD/PromptReco-v1/000/251/251/00000/7097B2BC-8E27-E511-80E1-02163E0138B3.root',
        #'/store/data/Run2015B/Charmonium/AOD/PromptReco-v1/000/251/252/00000/0067F5A4-9A27-E511-B904-02163E01267F.root',
        #'/store/data/Run2015B/Charmonium/AOD/PromptReco-v1/000/251/252/00000/642ACBD2-A127-E511-A59E-02163E0123F1.root',
        #'/store/data/Run2015B/Charmonium/AOD/PromptReco-v1/000/251/252/00000/F24C3492-9627-E511-AEC5-02163E011C7F.root'
        # 25 ns
        # redirector: root://eoscms.cern.ch/ ;   global redirector: root://cms-xrd-global.cern.ch/ ;   european redirector: root://xrootd-cms.infn.it// ;   US redirector: root://cmsxrootd.fnal.gov/ 
	#'/store/data/Run2015D/Charmonium/AOD/PromptReco-v3/000/257/822/00000/00B0174E-0869-E511-82B8-02163E01469D.root',
        #'/store/data/Run2015D/Charmonium/AOD/PromptReco-v3/000/256/629/00000/3475D421-065F-E511-9389-02163E011D45.root',
        # dataset C
        #'/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/253/888/00000/5668060A-0941-E511-A433-02163E014523.root', # 0 events
        #'/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/253/890/00000/D0DD2762-0941-E511-8D68-02163E014481.root', # 0 events
        #'/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/253/944/00000/CC59B3BC-3C41-E511-850A-02163E014405.root', # 0 events
        #'/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/253/952/00000/AAB10CDC-4241-E511-B200-02163E0140E9.root', # 0 events
        #'/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/253/954/00000/08A34D9A-4441-E511-B733-02163E014331.root', # 0 events
        #'/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/094/00000/00D975CA-2C46-E511-8D41-02163E014229.root', # 0 events
        #'/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/096/00000/60E94939-5C45-E511-A45F-02163E014555.root', # 0 events
        #'/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/212/00000/C4B4E9F1-BA45-E511-A0C9-02163E0140F8.root', # 0 events
        #'/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/219/00000/8229ACBC-C345-E511-8D7D-02163E0140F8.root', # 0 events
        #'/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/226/00000/42D98650-4545-E511-A6B3-02163E014128.root', # 0 events
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/227/00000/2AAF5B25-9C45-E511-88E0-02163E014636.root', 
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/229/00000/9CD00F16-EB45-E511-9414-02163E013565.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/231/00000/462E71A3-6345-E511-AC60-02163E0133C0.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/232/00000/C6507137-8245-E511-85AB-02163E014510.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/251/00000/9238F0DC-3546-E511-8F87-02163E012460.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/279/00000/FEB2DE57-A545-E511-A5E4-02163E01298B.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/280/00000/3ADD7E2F-A445-E511-B561-02163E01478E.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/282/00000/B04DCE4A-A845-E511-BC98-02163E011DF7.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/283/00000/8A0E2867-DD45-E511-99C6-02163E0141E8.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/284/00000/822D271E-3E45-E511-BFFF-02163E0138DE.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/285/00000/723CC112-1946-E511-8A21-02163E013860.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/289/00000/E095B7BE-FA45-E511-8EC0-02163E014258.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/290/00000/68741B2F-F745-E511-9F6A-02163E0137FC.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/292/00000/FECD67F6-CB45-E511-B661-02163E01391B.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/293/00000/B270069F-2346-E511-B7AF-02163E011A21.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/294/00000/868D358C-5D45-E511-8458-02163E01457C.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/306/00000/9687B35B-EC45-E511-B603-02163E0135DD.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/307/00000/82442455-3E45-E511-A5F4-02163E014683.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/308/00000/C2DF0ABD-3C45-E511-BDE9-02163E01374E.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/309/00000/641EAFAF-BF45-E511-A1E1-02163E011A21.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/313/00000/64FCC821-CE45-E511-8DF4-02163E0144A6.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/314/00000/A61220F6-0846-E511-AFE9-02163E01299C.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/315/00000/12663589-2346-E511-AD2A-02163E01250A.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/317/00000/BC1B83AC-E945-E511-8B9D-02163E0129E7.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/318/00000/E83C84D9-BE45-E511-A660-02163E011D96.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/319/00000/5C66B233-3E46-E511-8E9B-02163E013831.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/332/00000/5C445947-0F46-E511-A775-02163E0145AD.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/340/00000/20DA6081-AB45-E511-AA37-02163E013932.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/341/00000/5402E77D-9A45-E511-B04D-02163E011DB6.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/342/00000/F0943C6E-9445-E511-9D11-02163E014588.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/349/00000/369C82FE-1046-E511-9DBE-02163E01338E.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/362/00000/681F3297-4046-E511-B82B-02163E0121D5.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/367/00000/7C532C87-4046-E511-9E59-02163E0138DE.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/368/00000/C2C12F5C-4546-E511-99F1-02163E014300.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/380/00000/BED1BE0F-5B46-E511-9E51-02163E012460.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/416/00000/96F61819-8746-E511-8C62-02163E01455F.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/437/00000/B6D554FD-8A46-E511-91A2-02163E013591.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/450/00000/C47E9931-9246-E511-A9C5-02163E0144AE.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/451/00000/0018573A-9246-E511-9AF3-02163E0133EC.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/453/00000/4CC7FB60-9446-E511-9EF8-02163E012155.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/454/00000/32237FFA-9446-E511-9A1B-02163E013816.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/456/00000/C8FB008B-9646-E511-89E4-02163E01469B.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/457/00000/A4308B49-9746-E511-B008-02163E01340A.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/458/00000/4E0B3629-9C46-E511-B994-02163E013723.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/459/00000/76B13945-D646-E511-8B7E-02163E0138DE.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/500/00000/6405BBD0-D246-E511-BF19-02163E014541.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/511/00000/32B3994D-D846-E511-864D-02163E013497.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/512/00000/6A0C6AD0-2547-E511-8B9B-02163E0136DB.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/513/00000/385AE0BE-D746-E511-A62D-02163E01479A.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/530/00000/6E12F204-0F47-E511-8082-02163E011851.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/532/00000/2C26AB3A-1C47-E511-8E62-02163E01470C.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/602/00000/CA93D054-A347-E511-9102-02163E0143CC.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/607/00000/FE6A5737-BB47-E511-B71D-02163E013958.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/608/00000/707AABC2-BD48-E511-86F4-02163E01267F.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/712/00000/92855E71-CF48-E511-8EB0-02163E012BA2.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/768/00000/3EA12D26-1049-E511-81E5-02163E014642.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/769/00000/8CBD7CF5-1849-E511-8D66-02163E0133CA.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/780/00000/E61D74A1-2949-E511-B5A9-02163E0121D5.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/785/00000/70BA055C-3E49-E511-9F83-02163E014717.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/790/00000/1E96E0E6-DA49-E511-A085-02163E011DBA.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/790/00000/20E9A637-B549-E511-AA58-02163E011A50.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/790/00000/309EBFAE-D349-E511-B366-02163E014125.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/790/00000/602E9016-C249-E511-84EB-02163E01559C.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/790/00000/64476921-CB49-E511-A948-02163E0129EE.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/790/00000/6C0A4392-D849-E511-B13B-02163E01266D.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/790/00000/94E81D99-D249-E511-94C1-02163E012647.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/790/00000/A497C6D2-B849-E511-8077-02163E01339E.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/790/00000/A6B9BCFF-D049-E511-A1CC-02163E013765.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/790/00000/A8401D68-D449-E511-89D8-02163E014360.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/790/00000/B0CF8495-D549-E511-8D10-02163E0143C8.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/790/00000/BE46CBA7-CF49-E511-9D19-02163E014200.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/790/00000/D83D6F9F-E149-E511-AE1C-02163E011E88.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/824/00000/1ED25134-354A-E511-AEB7-02163E013441.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/128F6535-324B-E511-AACD-02163E011D21.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/16D16F3F-324B-E511-B5CE-02163E011DFD.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/1A095A2D-324B-E511-B23D-02163E013558.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/3897AC4B-334B-E511-BF13-02163E01456D.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/3A524439-324B-E511-A28C-02163E011F5D.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/408EB52B-324B-E511-A245-02163E011B6A.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/540E9233-324B-E511-BBA5-02163E01248D.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/5463DD38-324B-E511-B45B-02163E011AC9.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/5EA0C43C-324B-E511-AD87-02163E0143D3.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/60B9232C-324B-E511-B49F-02163E0121C9.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/6AAF522F-324B-E511-AC33-02163E01357D.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/70611F32-324B-E511-9B94-02163E0120FF.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/72A10CF3-324B-E511-903C-02163E0140DC.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/760AA435-324B-E511-A9CE-02163E01186D.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/7691622C-324B-E511-9B31-02163E011DCA.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/76B1EB78-324B-E511-9E37-02163E012303.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/9E0A042B-324B-E511-9199-02163E01380A.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/AA5B162F-324B-E511-B0DC-02163E0135B0.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/B07F5732-324B-E511-8AC4-02163E0154D3.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/B677EC3F-324B-E511-B82B-02163E01282E.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/B803CF2D-384B-E511-BC3D-02163E01389C.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/BA8D8F32-324B-E511-B9FB-02163E0135D4.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/BC01484A-324B-E511-9BC0-02163E011F24.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/C0E4A730-324B-E511-90E3-02163E01343E.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/C8B37FB9-404B-E511-93C9-02163E014761.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/CC6CB539-324B-E511-9697-02163E011A41.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/D49FC93A-324B-E511-BD5A-02163E01364B.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/E0AC833A-324B-E511-9EEC-02163E014761.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/E6FB6332-324B-E511-AAC6-02163E0145BB.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/E8FDA438-324B-E511-ABFA-02163E01466E.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/EAF0A12D-324B-E511-8361-02163E0137E3.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/833/00000/F21A5D2C-324B-E511-8E32-02163E014796.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/852/00000/E46424F0-974B-E511-B5E2-02163E01213D.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/879/00000/20B268F2-9F4B-E511-A359-02163E0143AA.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/879/00000/F8E352F9-9F4B-E511-88EB-02163E015541.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/905/00000/18F65DA6-BA4B-E511-A2DB-02163E01279E.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/905/00000/1CD21CAD-BA4B-E511-A566-02163E0143A2.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/905/00000/204135A9-BA4B-E511-82FE-02163E011E91.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/905/00000/26E685A3-BA4B-E511-8A82-02163E012ABA.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/906/00000/1CBD178C-CD4B-E511-B61D-02163E014291.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/907/00000/C4A55346-E24B-E511-80E3-02163E013463.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/913/00000/00716CF9-EB4B-E511-BEA7-02163E0136EE.root',
        '/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/914/00000/FCED70C1-EC4B-E511-9676-02163E0142B5.root'
        ]
else: raise RuntimeError, "Unknown CMSSW version %s" % os.environ['CMSSW_VERSION']



## ==== Fast Filters ====
process.goodVertexFilter = cms.EDFilter("VertexSelector",
    src = cms.InputTag("offlinePrimaryVertices"),
    cut = cms.string("!isFake && ndof > 4 && abs(z) <= 25 && position.Rho <= 2"),
    filter = cms.bool(True),
)
process.noScraping = cms.EDFilter("FilterOutScraping",
    applyfilter = cms.untracked.bool(True),
    debugOn = cms.untracked.bool(False), ## Or 'True' to get some per-event info
    numtrack = cms.untracked.uint32(10),
    thresh = cms.untracked.double(0.25)
)
process.fastFilter = cms.Sequence(process.goodVertexFilter + process.noScraping)

process.load("HLTrigger.HLTfilters.triggerResultsFilter_cfi")
process.triggerResultsFilter.triggerConditions = cms.vstring( 'HLT_Mu*_L2Mu*' )
process.triggerResultsFilter.l1tResults = ''
process.triggerResultsFilter.throw = True
process.triggerResultsFilter.hltResults = cms.InputTag( "TriggerResults", "", "HLT" )
#process.HLTMu   = process.triggerResultsFilter.clone(triggerConditions = ['HLT_Mu*_L2Mu*'])
#process.HLTBoth = process.triggerResultsFilter.clone(triggerConditions = ['HLT_Mu*_L2Mu*', 'HLT_Mu*_Track*_Jpsi*'])
process.HLTMu   = process.triggerResultsFilter.clone(triggerConditions = [ 'HLT_Mu*_L2Mu*', 'HLT_Mu*' ]) # for Mu8 test
process.HLTBoth = process.triggerResultsFilter.clone(triggerConditions = [ 'HLT_Mu*_L2Mu*', 'HLT_Mu*_Track*_Jpsi*', 'HLT_Mu*' ]) # for Mu8 test
process.HLTBoth_withDimuon = process.triggerResultsFilter.clone(triggerConditions = [ 'HLT_Mu*_L2Mu*', 'HLT_Mu*_Track*_Jpsi*', 'HLT_Mu*', 'HLT_Dimuon*' ])

##    __  __                       
##   |  \/  |_   _  ___  _ __  ___ 
##   | |\/| | | | |/ _ \| '_ \/ __|
##   | |  | | |_| | (_) | | | \__ \
##   |_|  |_|\__,_|\___/|_| |_|___/
##                                 
## ==== Merge CaloMuons and Tracks into the collection of reco::Muons  ====
from RecoMuon.MuonIdentification.calomuons_cfi import calomuons;
process.mergedMuons = cms.EDProducer("CaloMuonMerger",
    mergeTracks = cms.bool(True),
    mergeCaloMuons = cms.bool(False), # AOD
    muons     = cms.InputTag("muons"), 
    caloMuons = cms.InputTag("calomuons"),
    tracks    = cms.InputTag("generalTracks"),
    minCaloCompatibility = calomuons.minCaloCompatibility,
    ## Apply some minimal pt cut
    muonsCut     = cms.string("track.isNonnull && pt > 2"),
    caloMuonsCut = cms.string("pt > 2"),
    tracksCut    = cms.string("pt > 2"),
)

## ==== Trigger matching
process.load("MuonAnalysis.MuonAssociators.patMuonsWithTrigger_cff")
## with some customization
#process.muonMatchHLTL2.maxDeltaR = 0.3 # Zoltan tuning - it was 0.5 # present in Zmumu
#process.muonMatchHLTL3.maxDeltaR = 0.1 # present in Zmumu
from MuonAnalysis.MuonAssociators.patMuonsWithTrigger_cff import *
changeRecoMuonInput(process, "mergedMuons")
#useExtendedL1Match(process) 
#addHLTL1Passthrough(process)

from MuonAnalysis.TagAndProbe.common_variables_cff import *
process.load("MuonAnalysis.TagAndProbe.common_modules_cff")

process.tagMuons = cms.EDFilter("PATMuonSelector",
    src = cms.InputTag("patMuonsWithTrigger"),
    cut = cms.string("(isGlobalMuon || numberOfMatchedStations > 1) && pt > 7.5 && !triggerObjectMatchesByCollection('hltL3MuonCandidates').empty()"),
)

process.oneTag  = cms.EDFilter("CandViewCountFilter", src = cms.InputTag("tagMuons"), minNumber = cms.uint32(1))

process.probeMuons = cms.EDFilter("PATMuonSelector",
    src = cms.InputTag("patMuonsWithTrigger"),
    #cut = cms.string("track.isNonnull && (!triggerObjectMatchesByCollection('hltMuTrackJpsiEffCtfTrackCands').empty() || !triggerObjectMatchesByCollection('hltMuTrackJpsiCtfTrackCands').empty() || !triggerObjectMatchesByCollection('hltL2MuonCandidates').empty())"),
    cut = cms.string("track.isNonnull && !triggerObjectMatchesByCollection('hltTracksIter').empty()"),
    #cut = cms.string("") # for Mu8 test
    #cut = cms.string("track.isNonnull && !triggerObjectMatchesByCollection('hltL2MuonCandidates').empty()"),
)

process.tpPairs = cms.EDProducer("CandViewShallowCloneCombiner",
    cut = cms.string('2.8 < mass < 3.4 && abs(daughter(0).vz - daughter(1).vz) < 1'),
    decay = cms.string('tagMuons@+ probeMuons@-')
)
process.onePair = cms.EDFilter("CandViewCountFilter", src = cms.InputTag("tpPairs"), minNumber = cms.uint32(1))

from MuonAnalysis.TagAndProbe.muon.tag_probe_muon_extraIso_cff import ExtraIsolationVariables

process.tpTree = cms.EDAnalyzer("TagProbeFitTreeProducer",
    # choice of tag and probe pairs, and arbitration
    tagProbePairs = cms.InputTag("tpPairs"),
    arbitration   = cms.string("None"),
    # probe variables: all useful ones
    variables = cms.PSet(
        AllVariables,
        ExtraIsolationVariables,
        dxyBS = cms.InputTag("muonDxyPVdzmin","dxyBS"),
        dxyPVdzmin = cms.InputTag("muonDxyPVdzmin","dxyPVdzmin"),
        dzPV = cms.InputTag("muonDxyPVdzmin","dzPV"),
        nSplitTk  = cms.InputTag("splitTrackTagger"),
    ),
    flags = cms.PSet(
       TrackQualityFlags,
       MuonIDFlags,
       HighPtTriggerFlags,
       HighPtTriggerFlagsDebug,
       LowPtTriggerFlagsPhysics,
       LowPtTriggerFlagsEfficienciesProbe,
       Acc_JPsi = cms.string("(abs(eta) <= 1.3 && pt > 3.3) || (1.3 < abs(eta) <= 2.2 && p > 2.9) || (2.2 < abs(eta) <= 2.4  && pt > 0.8)"),
    ),
    tagVariables = cms.PSet(
        KinematicVariables, 
        nVertices = cms.InputTag("nverticesModule"),
        l1rate = cms.InputTag("l1rate"),
        bx     = cms.InputTag("l1rate","bx"),
    ),
    tagFlags = cms.PSet(
        HighPtTriggerFlags,
        HighPtTriggerFlagsDebug,
        LowPtTriggerFlagsPhysics,
        LowPtTriggerFlagsEfficienciesTag,
    ),
    pairVariables = cms.PSet(
        pt = cms.string("pt"),
        dphiVtxTimesQ = cms.InputTag("tagProbeSeparation", "dphiVtxTimesQ"),
        drM1          = cms.InputTag("tagProbeSeparation", "drM1"),
        dphiM1        = cms.InputTag("tagProbeSeparation", "dphiM1"),
        distM1        = cms.InputTag("tagProbeSeparation", "distM1"),
        drM2          = cms.InputTag("tagProbeSeparation", "drM2"),
        dphiM2        = cms.InputTag("tagProbeSeparation", "dphiM2"),
        distM2        = cms.InputTag("tagProbeSeparation", "distM2"),
        drVtx         = cms.InputTag("tagProbeSeparation", "drVtx"),
        dz            = cms.string("daughter(0).vz - daughter(1).vz"),
        probeMultiplicity = cms.InputTag("probeMultiplicity"),
    ),
    pairFlags = cms.PSet(),
    isMC           = cms.bool(False),
    addRunLumiInfo = cms.bool(True),
    allProbes = cms.InputTag("probeMuons"), # was missing
)


process.load("MuonAnalysis.TagAndProbe.muon.tag_probe_muon_extraIso_cfi")

process.tnpSimpleSequence = cms.Sequence(
    process.tagMuons +
    process.oneTag     +
    process.probeMuons +
    process.tpPairs    +
    process.onePair    +
    process.muonDxyPVdzmin +
    process.nverticesModule +
    process.tagProbeSeparation +
    process.computeCorrectedIso +
    process.probeMultiplicity + 
    process.splitTrackTagger +
    process.l1rate +
    process.tpTree
)

process.tagAndProbe = cms.Path( 
    process.fastFilter +
    process.HLTBoth    +
    process.mergedMuons                 *
    process.patMuonsWithTriggerSequence *
    process.tnpSimpleSequence
)

# OnePair tree for vertexing filter efficiency
process.tpTreeOnePair = process.tpTree.clone(
   arbitration   = "OnePair",
   # a few L1,L2,L3 variables in Ilse's file
   pairVariables = cms.PSet(
        process.tpTree.pairVariables,
        rapidity      = cms.string("rapidity"),
        absrapidity   = cms.string("abs(rapidity)"),
        prescaled     = cms.InputTag("tagProbeSeparation", "prescaled"),
        VtxProb       = cms.InputTag("tagProbeSeparation", "VtxProb"),
        #VtxCosPA      = cms.InputTag("tagProbeSeparation", "VtxCosPA"),
        VtxLxySig     = cms.InputTag("tagProbeSeparation", "VtxLxySig"),
        VtxLxy        = cms.InputTag("tagProbeSeparation", "VtxLxy"),
        #VtxL3d        = cms.InputTag("tagProbeSeparation", "VtxL3d"),
        DCA           = cms.InputTag("tagProbeSeparation", "DCA"),
        ),
)

process.tnpSimpleSequenceOnePair = cms.Sequence(
    process.tagMuons +
    process.probeMuons +
    process.tpPairs    +
    process.muonDxyPVdzmin +
    process.nverticesModule    +
    process.tagProbeSeparation +
    process.computeCorrectedIso +
    process.splitTrackTagger + 
    process.l1rate +
    process.tpTreeOnePair
)

process.tagAndProbeOnePair = cms.Path( 
    process.fastFilter +
    process.HLTBoth_withDimuon    +
    process.mergedMuons                 *
    process.patMuonsWithTriggerSequence *
    process.tnpSimpleSequenceOnePair
)


##    _____               _    _             
##   |_   _| __ __ _  ___| | _(_)_ __   __ _ 
##     | || '__/ _` |/ __| |/ / | '_ \ / _` |
##     | || | | (_| | (__|   <| | | | | (_| |
##     |_||_|  \__,_|\___|_|\_\_|_| |_|\__, |
##                                     |___/ 

## Then make another collection for standalone muons, using standalone track to define the 4-momentum
process.muonsSta = cms.EDProducer("RedefineMuonP4FromTrack",
    src   = cms.InputTag("muons"),
    track = cms.string("outer"),
)
## Match to trigger, to measure the efficiency of HLT tracking
from PhysicsTools.PatAlgos.tools.helpers import *
process.patMuonsWithTriggerSequenceSta = cloneProcessingSnippet(process, process.patMuonsWithTriggerSequence, "Sta")
process.muonMatchHLTL2Sta.maxDeltaR = 0.5
process.muonMatchHLTL3Sta.maxDeltaR = 0.5
massSearchReplaceAnyInputTag(process.patMuonsWithTriggerSequenceSta, "mergedMuons", "muonsSta")

## Define probes and T&P pairs
process.probeMuonsSta = cms.EDFilter("PATMuonSelector",
    src = cms.InputTag("patMuonsWithTriggerSta"),
    cut = cms.string("outerTrack.isNonnull && !triggerObjectMatchesByCollection('hltL2MuonCandidates').empty()"), 
)
process.tpPairsSta = process.tpPairs.clone(decay = "tagMuons@+ probeMuonsSta@-", cut = "2 < mass < 5")

process.onePairSta = cms.EDFilter("CandViewCountFilter", src = cms.InputTag("tpPairsSta"), minNumber = cms.uint32(1))

process.staToTkMatch.maxDeltaR     = 0.3
process.staToTkMatch.maxDeltaPtRel = 2.
process.staToTkMatchNoJPsi.maxDeltaR     = 0.3
process.staToTkMatchNoJPsi.maxDeltaPtRel = 2.

process.load("MuonAnalysis.TagAndProbe.tracking_reco_info_cff")

process.tpTreeSta = process.tpTree.clone(
    tagProbePairs = "tpPairsSta",
    #arbitration   = "OneProbe", # present in Zmumu
    variables = cms.PSet(
        KinematicVariables, 
        #StaOnlyVariables, # present in Zmumu
        ## track matching variables
        tk_deltaR     = cms.InputTag("staToTkMatch","deltaR"),
        tk_deltaEta   = cms.InputTag("staToTkMatch","deltaEta"),
        tk_deltaR_NoJPsi     = cms.InputTag("staToTkMatchNoJPsi","deltaR"),
        tk_deltaEta_NoJPsi   = cms.InputTag("staToTkMatchNoJPsi","deltaEta"),
        tk_deltaR_NoBestJPsi     = cms.InputTag("staToTkMatchNoBestJPsi","deltaR"),
        tk_deltaEta_NoBestJPsi   = cms.InputTag("staToTkMatchNoBestJPsi","deltaEta"),
    ),
    flags = cms.PSet(
        #Mu5_L2Mu3_Jpsi_L2 = LowPtTriggerFlagsEfficienciesProbe.Mu5_L2Mu3_Jpsi_L2,
        LowPtTriggerFlagsPhysics,
        LowPtTriggerFlagsEfficienciesProbe,
        outerValidHits = cms.string("outerTrack.numberOfValidHits > 0"),
        TM  = cms.string("isTrackerMuon"),
        Glb = cms.string("isGlobalMuon"),
        Tk  = cms.string("track.isNonnull"),
        #StaTkSameCharge = cms.string("outerTrack.isNonnull && innerTrack.isNonnull && (outerTrack.charge == innerTrack.charge)"), # present in Zmumu
    ),
    tagVariables = cms.PSet(
        KinematicVariables, 
        nVertices = cms.InputTag("nverticesModule"),
        #combRelIso = cms.string("(isolationR03.emEt + isolationR03.hadEt + isolationR03.sumPt)/pt"),
        #chargedHadIso04 = cms.string("pfIsolationR04().sumChargedHadronPt"),
        #neutralHadIso04 = cms.string("pfIsolationR04().sumNeutralHadronEt"),
        #photonIso04 = cms.string("pfIsolationR04().sumPhotonEt"),
        #combRelIsoPF04dBeta = IsolationVariables.combRelIsoPF04dBeta,
        #l1rate = cms.InputTag("l1rate"), # uncommented in "add bx information to data tree #18"
        #bx     = cms.InputTag("l1rate","bx"),
    ),
    tagFlags = cms.PSet(
        #Mu5_L2Mu3_Jpsi_MU = LowPtTriggerFlagsEfficienciesTag.Mu5_L2Mu3_Jpsi_MU,
        LowPtTriggerFlagsEfficienciesTag,
    ),
    pairVariables = cms.PSet(
        dz      = cms.string("daughter(0).vz - daughter(1).vz"),
        pt      = cms.string("pt"), 
        #
        dphiVtxTimesQ = cms.InputTag("tagProbeStaSeparation", "dphiVtxTimesQ"),
        drM1          = cms.InputTag("tagProbeStaSeparation", "drM1"),
        dphiM1        = cms.InputTag("tagProbeStaSeparation", "dphiM1"),
        distM1        = cms.InputTag("tagProbeStaSeparation", "distM1"),
        drM2          = cms.InputTag("tagProbeStaSeparation", "drM2"),
        dphiM2        = cms.InputTag("tagProbeStaSeparation", "dphiM2"),
        distM2        = cms.InputTag("tagProbeStaSeparation", "distM2"),
        drVtx         = cms.InputTag("tagProbeStaSeparation", "drVtx"),
        probeMultiplicity = cms.InputTag("probeStaMultiplicity"),
        #
        rapidity = cms.string("rapidity"),
        deltaR   = cms.string("deltaR(daughter(0).eta, daughter(0).phi, daughter(1).eta, daughter(1).phi)"), 
        ),
    pairFlags     = cms.PSet(),
    allProbes     = "probeMuonsSta", # was missing w.r.t. MC
)

process.tnpSimpleSequenceSta = cms.Sequence(
    process.tagMuons +
    process.oneTag     +
    process.probeMuonsSta +
    process.tpPairsSta      +
    process.onePairSta      +
    process.nverticesModule +
    process.tagProbeStaSeparation +
    process.probeStaMultiplicity + 
    process.staToTkMatchSequenceJPsi +
    process.l1rate +
    process.tpTreeSta
)

## Add extra RECO-level info
if False:
    process.tnpSimpleSequenceSta.replace(process.tpTreeSta, process.tkClusterInfo+process.tpTreeSta)
    process.tpTreeSta.tagVariables.nClustersStrip = cms.InputTag("tkClusterInfo","siStripClusterCount")
    process.tpTreeSta.tagVariables.nClustersPixel = cms.InputTag("tkClusterInfo","siPixelClusterCount")
    process.tnpSimpleSequenceSta.replace(process.tpTreeSta, process.tkLogErrors+process.tpTreeSta)
    process.tpTreeSta.tagVariables.nLogErrFirst = cms.InputTag("tkLogErrors","firstStep")
    process.tpTreeSta.tagVariables.nLogErrPix   = cms.InputTag("tkLogErrors","pixelSteps")
    process.tpTreeSta.tagVariables.nLogErrAny   = cms.InputTag("tkLogErrors","anyStep")

if False: # turn on for tracking efficiency from RECO/AOD + earlyGeneralTracks
    process.tracksNoMuonSeeded = cms.EDFilter("TrackSelector",
      src = cms.InputTag("generalTracks"),
      cut = cms.string(" || ".join("isAlgoInMask('%s')" % a for a in [
                    'initialStep', 'lowPtTripletStep', 'pixelPairStep', 'detachedTripletStep',
                    'mixedTripletStep', 'pixelLessStep', 'tobTecStep', 'jetCoreRegionalStep' ] ) )
    )
    process.pCutTracks0 = process.pCutTracks.clone(src = 'tracksNoMuonSeeded')
    process.tkTracks0 = process.tkTracks.clone(src = 'pCutTracks0')
    process.tkTracksNoJPsi0 = process.tkTracksNoJPsi.clone(src = 'tkTracks0')
    process.tkTracksNoBestJPsi0 = process.tkTracksNoBestJPsi.clone(src = 'tkTracks0')
    process.preTkMatchSequenceJPsi.replace(
            process.tkTracksNoJPsi, process.tkTracksNoJPsi +
            process.tracksNoMuonSeeded + process.pCutTracks0 + process.tkTracks0 + process.tkTracksNoJPsi0 +process.tkTracksNoBestJPsi0
    )
    process.staToTkMatch0 = process.staToTkMatch.clone(matched = 'tkTracks0')
    process.staToTkMatchNoJPsi0 = process.staToTkMatchNoJPsi.clone(matched = 'tkTracksNoJPsi0')
    process.staToTkMatchNoBestJPsi0 = process.staToTkMatchNoBestJPsi.clone(matched = 'tkTracksNoJPsi0')
    process.staToTkMatchSequenceJPsi.replace( process.staToTkMatch, process.staToTkMatch + process.staToTkMatch0 )
    process.staToTkMatchSequenceJPsi.replace( process.staToTkMatchNoJPsi, process.staToTkMatchNoJPsi + process.staToTkMatchNoJPsi0 )
    process.staToTkMatchSequenceJPsi.replace( process.staToTkMatchNoBestJPsi, process.staToTkMatchNoBestJPsi + process.staToTkMatchNoBestJPsi0 )
    process.tpTreeSta.variables.tk0_deltaR     = cms.InputTag("staToTkMatch0","deltaR")
    process.tpTreeSta.variables.tk0_deltaEta   = cms.InputTag("staToTkMatch0","deltaEta")
    process.tpTreeSta.variables.tk0_deltaR_NoJPsi   = cms.InputTag("staToTkMatchNoJPsi0","deltaR")
    process.tpTreeSta.variables.tk0_deltaEta_NoJPsi = cms.InputTag("staToTkMatchNoJPsi0","deltaEta")
    process.tpTreeSta.variables.tk0_deltaR_NoBestJPsi   = cms.InputTag("staToTkMatchNoBestJPsi0","deltaR")
    process.tpTreeSta.variables.tk0_deltaEta_NoBestJPsi = cms.InputTag("staToTkMatchNoBestJPsi0","deltaEta")

process.tagAndProbeSta = cms.Path( 
    process.fastFilter +
    process.HLTMu      +
    process.muonsSta                       +
    process.patMuonsWithTriggerSequenceSta +
    process.tnpSimpleSequenceSta
)


if False: # turn on for tracking efficiency using L1 seeds
    process.probeL1 = cms.EDFilter("CandViewSelector",
        src = cms.InputTag("l1extraParticles"),
        cut = cms.string("pt >= 2 && abs(eta) < 2.4"),
    )
    process.tpPairsTkL1 = process.tpPairs.clone(decay = "tagMuons@+ probeL1@-", cut = 'mass > 2')
    process.l1ToTkMatch    = process.staToTkMatch.clone(src = "probeL1", srcTrack="none")
    process.l1ToTkMatchNoJPsi = process.staToTkMatchNoJPsi.clone(src = "probeL1", srcTrack="none")
    process.l1ToTkMatchNoBestJPsi = process.staToTkMatchNoBestJPsi.clone(src = "probeL1", srcTrack="none")
    process.l1ToTkMatch0    = process.staToTkMatch0.clone(src = "probeL1", srcTrack="none")
    process.l1ToTkMatchNoJPsi0 = process.staToTkMatchNoJPsi0.clone(src = "probeL1", srcTrack="none")
    process.l1ToTkMatchNoBestJPsi0 = process.staToTkMatchNoBestJPsi0.clone(src = "probeL1", srcTrack="none")
    process.tpTreeL1 = process.tpTreeSta.clone(
        tagProbePairs = "tpPairsTkL1",
        arbitration   = "OneProbe",
        variables = cms.PSet(
            KinematicVariables,
            bx = cms.string("bx"),
            quality = cms.string("gmtMuonCand.quality"),
            ## track matching variables
            tk_deltaR     = cms.InputTag("l1ToTkMatch","deltaR"),
            tk_deltaEta   = cms.InputTag("l1ToTkMatch","deltaEta"),
            tk_deltaR_NoJPsi   = cms.InputTag("l1ToTkMatchNoJPsi","deltaR"),
            tk_deltaEta_NoJPsi = cms.InputTag("l1ToTkMatchNoJPsi","deltaEta"),
            tk_deltaR_NoBestJPsi   = cms.InputTag("l1ToTkMatchNoBestJPsi","deltaR"),
            tk_deltaEta_NoBestJPsi = cms.InputTag("l1ToTkMatchNoBestJPsi","deltaEta"),
            ## track matching variables (early general tracks)
            tk0_deltaR     = cms.InputTag("l1ToTkMatch0","deltaR"),
            tk0_deltaEta   = cms.InputTag("l1ToTkMatch0","deltaEta"),
            tk0_deltaR_NoJPsi   = cms.InputTag("l1ToTkMatchNoJPsi0","deltaR"),
            tk0_deltaEta_NoJPsi = cms.InputTag("l1ToTkMatchNoJPsi0","deltaEta"),
            tk0_deltaR_NoBestJPsi   = cms.InputTag("l1ToTkMatchNoBestJPsi0","deltaR"),
            tk0_deltaEta_NoBestJPsi = cms.InputTag("l1ToTkMatchNoBestJPsi0","deltaEta"),
        ),
        flags = cms.PSet(
        ),
        tagVariables = cms.PSet(
            pt = cms.string("pt"),
            eta = cms.string("eta"),
            phi = cms.string("phi"),
            nVertices   = cms.InputTag("nverticesModule"),
	    #ERICA:to check if for the JPsi is valid
            #combRelIso = cms.string("(isolationR03.emEt + isolationR03.hadEt + isolationR03.sumPt)/pt"),
            #chargedHadIso04 = cms.string("pfIsolationR04().sumChargedHadronPt"),
            #neutralHadIso04 = cms.string("pfIsolationR04().sumNeutralHadronEt"),
            #photonIso04 = cms.string("pfIsolationR04().sumPhotonEt"),
            #combRelIsoPF04dBeta = IsolationVariables.combRelIsoPF04dBeta,
        ),
        pairVariables = cms.PSet(
            #nJets30 = cms.InputTag("njets30ModuleSta"),
            pt      = cms.string("pt"),
            rapidity = cms.string("rapidity"),
            deltaR   = cms.string("deltaR(daughter(0).eta, daughter(0).phi, daughter(1).eta, daughter(1).phi)"),
        ),
        pairFlags = cms.PSet(),
        allProbes     = cms.InputTag("probeL1"),
    )
    process.tagAndProbeTkL1 = cms.Path(
        process.fastFilter +
        process.probeL1 +
        process.tpPairsTkL1 +
        process.preTkMatchSequenceJPsi +
        process.l1ToTkMatch + process.l1ToTkMatchNoJPsi + process.l1ToTkMatchNoBestJPsi +
        process.l1ToTkMatch0 + process.l1ToTkMatchNoJPsi0 + process.l1ToTkMatchNoBestJPsi0 +
	#process.nverticesModule + process.l1rate + # added in "add bx information to data tree #18"
        process.tpTreeL1
    )

##    _____     _          ____       _            
##   |  ___|_ _| | _____  |  _ \ __ _| |_ ___  ___ 
##   | |_ / _` | |/ / _ \ | |_) / _` | __/ _ \/ __|
##   |  _| (_| |   <  __/ |  _ < (_| | ||  __/\__ \
##   |_|  \__,_|_|\_\___| |_| \_\__,_|\__\___||___/
##                                                 
##       
#process.load("MuonAnalysis.TagAndProbe.fakerate_all_cff")
#
#process.fakeRateJetPlusProbeTree = process.tpTree.clone(
#    tagProbePairs = 'jetPlusProbe',
#    arbitration   = 'None',
#    tagVariables = process.JetPlusProbeTagVariables,
#    tagFlags = cms.PSet(),
#    pairVariables = cms.PSet(deltaPhi = cms.string("deltaPhi(daughter(0).phi, daughter(1).phi)")),
#    pairFlags     = cms.PSet(),
#    isMC = False, # MC matches not in place for FR yet
#)
#process.fakeRateWPlusProbeTree = process.tpTree.clone(
#    tagProbePairs = 'wPlusProbe',
#    arbitration   = 'None',
#    tagVariables = process.WPlusProbeTagVariables,
#    tagFlags = cms.PSet(),
#    pairVariables = cms.PSet(),
#    pairFlags     = cms.PSet(SameSign = cms.string('daughter(0).daughter(0).charge == daughter(1).charge')),
#    isMC = False, # MC matches not in place for FR yet
#)
#process.fakeRateZPlusProbeTree = process.tpTree.clone(
#    tagProbePairs = 'zPlusProbe',
#    arbitration   = 'None',
#    tagVariables  = process.ZPlusProbeTagVariables,
#    tagFlags      = cms.PSet(),
#    pairVariables = cms.PSet(),
#    pairFlags     = cms.PSet(),
#    isMC = False, # MC matches not in place for FR yet
#)
#
#process.fakeRateJetPlusProbe = cms.Path(
#    process.fastFilter +
#    process.mergedMuons * process.patMuonsWithTriggerSequence +
#    process.tagMuons + process.probeMuons + process.extraProbeVariablesSeq +
#    process.jetPlusProbeSequence +
#    process.fakeRateJetPlusProbeTree
#)
#process.fakeRateWPlusProbe = cms.Path(
#    process.fastFilter +
#    process.mergedMuons * process.patMuonsWithTriggerSequence +
#    process.tagMuons + process.probeMuons + process.extraProbeVariablesSeq +
#    process.wPlusProbeSequence +
#    process.fakeRateWPlusProbeTree
#)
#process.fakeRateZPlusProbe = cms.Path(
#    process.fastFilter +
#    process.mergedMuons * process.patMuonsWithTriggerSequence +
#    process.tagMuons + process.probeMuons + process.extraProbeVariablesSeq +
#    process.zPlusProbeSequence +
#    process.fakeRateZPlusProbeTree
#)

process.schedule = cms.Schedule(
   process.tagAndProbe,
   process.tagAndProbeSta,
   process.tagAndProbeOnePair,
   #process.tagAndProbeTkL1
   #process.fakeRateJetPlusProbe,
   #process.fakeRateWPlusProbe,
   #process.fakeRateZPlusProbe,
)


process.RandomNumberGeneratorService.tkTracksNoJPsi      = cms.PSet( initialSeed = cms.untracked.uint32(81) )
process.RandomNumberGeneratorService.tkTracksNoJPsi0      = cms.PSet( initialSeed = cms.untracked.uint32(81) )
process.RandomNumberGeneratorService.tkTracksNoBestJPsi  = cms.PSet( initialSeed = cms.untracked.uint32(81) )
process.RandomNumberGeneratorService.tkTracksNoBestJPsi0  = cms.PSet( initialSeed = cms.untracked.uint32(81) )

process.TFileService = cms.Service("TFileService", fileName = cms.string("tnpJPsi_Data.root"))
