import os

from PyLooper.hep.cms.dataset.CMSDataset import CMSDataset
from PyLooper.hep.root.TFile import TFile

# ____________________________________________________________________________________________________________________________________________ ||
input_dir           = "/Users/lucien/CMS/ztoll-ml/Data/"
tree_path_in_file   = "LiteTree"

# ____________________________________________________________________________________________________________________________________________ ||
ZJetsToLL_LO_MLM = CMSDataset(
    "ZJetsToLL_LO_MLM",
    [TFile(os.path.join(input_dir,"2020-07-09_MuonTreeProducer.root"),tree_path_in_file,),],
    xs = 1.,
    sumw = 1.,
    plot_name = "ZJetsToLL_LO_MLM",
    )

ZJetsToLL_LO_MLM.branches = [
        "Muon_Pt",
        "Muon_Eta",
        "Muon_Phi",
        "Muon_GenPt",
        "Muon_GenEta",
        "Muon_GenPhi",
        "Muon_GenMass",
        ]
