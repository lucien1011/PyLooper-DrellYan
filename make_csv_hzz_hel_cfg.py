from PyLooper.common.Dataset import Dataset
from PyLooper.common.Collector import Collector

from PyLooper.stat.Hist1D import Hist1D
from PyLooper.hep.plotter.Plotter import Plotter
from PyLooper.hep.plotter.Plot import Plot

from dataset.HZZ_HEL_MadgraphPythia import sample_dict
from weighter.HZZWeighter import HZZWeighter
from producer.CSVProducer import CSVProducer

verbose = True
nblock = 1024
ngrid = 100
entrysteps = nblock*ngrid
namedecode = "utf-8"

dataset_list = sample_dict.values()
merged_dataset_list = []

collector = Collector(
    output_path = "./output/2021_01_16_make_csv_hzz_hel_cfg/",
    )
collector.csv_filename = "train.npy"
collector.array_dict = {}

modules = [
    HZZWeighter("EventWeighter"),
    CSVProducer("CSVProducer"),
    ]
