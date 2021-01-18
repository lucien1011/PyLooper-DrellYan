import os

from PyLooper.hep.cms.dataset.CMSDataset import CMSDataset
from PyLooper.hep.root.TFile import TFile

# ____________________________________________________________________________________________________________________________________________ ||
input_dir           = "/cmsuf/data/store/user/t2/users/klo/MLHEP/LiteTree/210115_mg_hzz_hel_v2/"
tree_path_in_file   = "LiteTree"
sumw                = 100000

# ____________________________________________________________________________________________________________________________________________ ||
ggH = CMSDataset(
    "Higgs",
    [TFile(os.path.join(input_dir,"0.002312241433103379.root"),tree_path_in_file,)],
    xs = 48.52*0.0002768,
    sumw = sumw,
    isMC = True,
    plot_name = "SM Higgs",
    )
ggH.param = 0.0
ggH.branches = [
    "mass4l",
    "massZ1",
    "massZ2",
    "pT4l",
    "rapidity4l",
    "pTZ1",
    "pTZ2",
    "pTL1",
    "pTL2",
    "pTL3",
    "pTL4",
    "cosTheta1",
    "cosTheta2",
    "cosThetaStar",
    "Phi",
    "Phi1",
    "passedFullSelection",
    ]
