from CRABClient.UserUtilities import config
config = config()

config.section_('General')
#config.General.requestName = 'Jpsi_tree'
#config.General.requestName = 'Jpsi_tree_Mu8'
#config.General.requestName = 'TnP_MC_request'
#config.General.requestName = 'TnP_MC_request_standardCfg'
#config.General.requestName = 'TnP_fullMC_request'
config.General.requestName = 'TnP_fullMC_Mu8'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../tp_from_aod_simple_MC.py'
#config.JobType.outputFiles = ['tnpJpsi_MC.root']

config.section_('Data')
#config.Data.inputDataset = '/JpsiToMuMu_JPsiPt7_13TeV-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/AODSIM'
#config.Data.inputDataset = '/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1/AODSIM' # INVALID
config.Data.inputDataset = '/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v2/AODSIM'
config.Data.allowNonValidInputDataset = True

config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
#config.Data.unitsPerJob = 1
config.Data.unitsPerJob = 17 # for full official MC
#config.Data.lumiMask = 'Cert_181530-183126_HI7TeV_PromptReco_Collisions11_JSON.txt'
config.Data.publication = False
#config.Data.outLFNDirBase = '/store/user/lecriste/TnP/'
config.Data.outLFNDirBase = '/store/group/phys_muon/lecriste/TnP/' # for CERN
#config.Data.ignoreLocality = True

config.section_('Site')
#config.Site.blacklist = ['T0', 'T1'] # T0 blacklisted by default
config.Site.blacklist = ['T1*']
#config.Site.blacklist = ['T1*','T2_DE_DESY','T2_CH_CSCS','T1_RU_JINR']

#config.Site.storageSite = 'T2_IT_Bari'
#config.Site.storageSite = 'T2_IT_Legnaro'
config.Site.storageSite = 'T2_CH_CERN'

