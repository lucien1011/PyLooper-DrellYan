import os

from PyLooper.hep.cms.dataset.CMSDataset import CMSDataset
from PyLooper.hep.root.TFile import TFile

# ____________________________________________________________________________________________________________________________________________ ||
input_dir           = "/cmsuf/data/store/user/t2/users/klo/MLHEP/LiteTree/210117_mg_zz_hel/"
tree_path_in_file   = "LiteTree"
sumw                = 100*5000

# ____________________________________________________________________________________________________________________________________________ ||
ZZ = CMSDataset(
    "ZZ",
    [TFile(os.path.join(input_dir,f),tree_path_in_file,) for f in os.listdir(input_dir) if ".root" in f],
    xs = 1.256,
    sumw = sumw,
    isMC = True,
    plot_name = "ZZ",
    )
ZZ.param = -1.
ZZ.branches = [
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
