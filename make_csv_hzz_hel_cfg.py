from PyLooper.common.Dataset import Dataset
from PyLooper.common.Collector import Collector

from PyLooper.stat.Hist1D import Hist1D
from PyLooper.hep.plotter.Plotter import Plotter
from PyLooper.hep.plotter.Plot import Plot

from dataset.ZZ_HEL_MadgraphPythia import ZZ
from dataset.EFTHZZ_HEL_MadgraphPythia import sample_dict
from dataset.SMHZZ_HEL_MadgraphPythia import ggH 
from weighter.HZZWeighter import HZZWeighter
from producer.HZZ_CSVProducer import CSVProducer

verbose = True
nblock = 1024
ngrid = 100
entrysteps = nblock*ngrid
namedecode = "utf-8" 

dataset_list = [ggH,ZZ,] + list(sample_dict.values())
merged_dataset_list = []

for d in dataset_list:
    d.lumi = 130*1000

collector = Collector(
    output_path = "./output/2021_01_18_make_csv_HZZ_HEL_cfg/",
    )
collector.csv_filename = "train.npy"
collector.array_dict = {}

modules = [
    HZZWeighter("EventWeighter"),
    CSVProducer("CSVProducer"),
    ]
