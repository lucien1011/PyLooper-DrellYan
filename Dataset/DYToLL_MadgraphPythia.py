import os

from PyLooper.hep.cms.dataset.CMSDataset import CMSDataset
from PyLooper.hep.root.TFile import TFile

# ____________________________________________________________________________________________________________________________________________ ||
input_dir           = "/Users/lucien/CMS/ztoll-ml/Data/201210_mg_dyll/"
tree_path_in_file   = "LiteTree"

# ____________________________________________________________________________________________________________________________________________ ||
sample_dict = {}
for f in os.listdir(input_dir):
    mass_str = f.replace(".root","")
    sample_dict[mass_str] = CMSDataset(
        "DYToLL_M"+mass_str,
        [TFile(os.path.join(input_dir,f),tree_path_in_file,),],
        xs = 1.,
        sumw = 1.,
        plot_name = "DYToLL_M"+mass_str,
        )
    sample_dict[mass_str].mass = float(mass_str)
    sample_dict[mass_str].branches = [
        "Muon_Pt",
        "Muon_Eta",
        "Muon_Phi",
        "Muon_GenPt",
        "Muon_GenEta",
        "Muon_GenPhi",
        "Muon_GenMass",
        ]
