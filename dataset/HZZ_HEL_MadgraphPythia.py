import os

from PyLooper.hep.cms.dataset.CMSDataset import CMSDataset
from PyLooper.hep.root.TFile import TFile

# ____________________________________________________________________________________________________________________________________________ ||
input_dir           = "/cmsuf/data/store/user/t2/users/klo/MLHEP/LiteTree/210115_mg_hzz_hel_v2/"
tree_path_in_file   = "LiteTree"

# ____________________________________________________________________________________________________________________________________________ ||
sample_dict = {}
for f in os.listdir(input_dir):
    if ".root" not in f: continue
    param_str = f.replace(".root","")
    sample_dict[param_str] = CMSDataset(
        "HZZ_CWW_"+param_str,
        [TFile(os.path.join(input_dir,f),tree_path_in_file,),],
        xs = 1.,
        sumw = 1.,
        isMC = True,
        isSignal = True,
        plot_name = "HZZ_CWW_"+"%4.4f"%float(param_str),
        )
    sample_dict[param_str].param = float(param_str)
    sample_dict[param_str].branches = [
        "Muon_Pt",
        "Muon_Eta",
        "Muon_Phi",
        "Electron_Pt",
        "Electron_Eta",
        "Electron_Phi",
        ]
