MC = False
MC = True

mode_25ns = False # for 50ns
#mode_25ns = True

RunC = True
RunC = False
RunDv3 = True
RunDv3 = False
RunDv4 = True
#RunDv4 = False


from CRABClient.UserUtilities import config
config = config()

config.section_('General')
# MC
if MC:
	if (not mode_25ns):
	        #config.General.requestName = 'TnP_MC_request'
	        #config.General.requestName = 'TnP_MC_request_standardCfg'
	        #config.General.requestName = 'TnP_fullMC_request'
	        #config.General.requestName = 'TnP_fullMC_Mu8'
	        #config.General.requestName = 'TnP_fullMC_standardCfg_withL2Filter'
                #config.General.requestName = 'TnP_fullMC_standardCfg_withCorrectL2Filter'
	        #config.General.requestName = 'TnP_fullMC_standardCfg_withCorrectGenMuons'
	        #config.General.requestName = 'TnP_fullMC_OniaTriggersFlags'
		#config.General.requestName = 'TnP_50nsFirst47ipb_vertexingTriggersFlags'
		#config.General.requestName = 'TnP_fullMC_vertexingTriggersFlags_withMCMatch'
                config.General.requestName = 'TnP_fullMC_withAllTagVars'
	else:
		config.General.requestName = 'TnP_fullMC_25ns'
# Data
else:
	if (not mode_25ns):
	        #config.General.requestName = 'Jpsi_tree'
	        #config.General.requestName = 'Jpsi_tree_Mu8'
	        #config.General.requestName = 'TnP_full50nsData_standardCfg_withL2Filter'
	        #config.General.requestName = 'TnP_last50nsRun_standardCfg_withL2Filter'
	        #config.General.requestName = 'TnP_last50nsRun_standardCfg_withCorrectL2Filter'
	        #config.General.requestName = 'TnP_50nsFirst47ipb_OniaTriggersFlags'
		config.General.requestName = 'TnP_50nsFirst47ipb_vertexingTriggersFlags'
	else:
		if (RunC):
			config.General.requestName = 'TnP_RunC_25ns'
		elif (RunDv3):
			config.General.requestName = 'TnP_RunDv3_25ns'
		elif (RunDv4):
			config.General.requestName = 'TnP_RunDv4_25ns'

config.General.transferOutputs = True
config.General.transferLogs = False

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
# MC
if MC:
	config.JobType.psetName = '../tp_from_aod_simple_MC.py'
# Data
else:
	config.JobType.psetName = '../tp_from_aod_simple_Data.py'

#config.JobType.outputFiles = ['tnpJpsi_MC.root']

config.section_('Data')
# MC
if MC:
	if (not mode_25ns):
	        #config.Data.inputDataset = '/JpsiToMuMu_JPsiPt7_13TeV-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/AODSIM'
                #config.Data.inputDataset = '/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1/AODSIM' # INVALID
	        #config.Data.allowNonValidInputDataset = True
		config.Data.inputDataset = '/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v2/AODSIM'
	else:
		config.Data.inputDataset = '/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/AODSIM' 

# Data
else:
	if (not mode_25ns):
		config.Data.inputDataset = '/Charmonium/Run2015B-PromptReco-v1/AOD'
	        #config.Data.inputDataset = '/Charmonium/Run2015C-PromptReco-v1/AOD'
	else:
		if (RunC):
			config.Data.inputDataset = '/Charmonium/Run2015C-PromptReco-v1/AOD'
		elif (RunDv3):
			config.Data.inputDataset = '/Charmonium/Run2015D-PromptReco-v3/AOD'
		elif (RunDv4):
			config.Data.inputDataset = '/Charmonium/Run2015D-PromptReco-v4/AOD'


config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
if MC:
	config.Data.unitsPerJob = 17 # for full official MC
else:
	if (not mode_25ns):
		config.Data.unitsPerJob = 1
	        #config.Data.lumiMask = 'Cert_181530-183126_HI7TeV_PromptReco_Collisions11_JSON.txt' # 47/pb
		config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Cert_246908-251883_13TeV_PromptReco_Collisions15_JSON_MuonPhys_v2.txt' # 47/pb
	        #config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Cert_246908-255031_13TeV_PromptReco_Collisions15_50ns_JSON_MuonPhys_v2.txt' # 77.34/pb 
	else:
		config.Data.unitsPerJob = 1
		if (RunDv3):
			config.Data.unitsPerJob = 2
		elif (RunDv4):
			config.Data.unitsPerJob = 3
	        config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_MuonPhys.txt' # 2.59/fb


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

