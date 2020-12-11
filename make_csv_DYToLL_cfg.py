from PyLooper.common.Dataset import Dataset
from PyLooper.common.Collector import Collector

from PyLooper.stat.Hist1D import Hist1D
from PyLooper.hep.plotter.Plotter import Plotter
from PyLooper.hep.plotter.Plot import Plot

from Dataset.DYToLL_MadgraphPythia import sample_dict
from Weighter.EventWeighter import EventWeighter
from Producer.CSVProducer import CSVProducer

verbose = True
nblock = 1024
ngrid = 100
entrysteps = nblock*ngrid
namedecode = "utf-8"

dataset_list = sample_dict.values()
merged_dataset_list = []

collector = Collector(
    output_path = "./output/2020_12_11_make_csv_DYToLL_cfg/",
    )
collector.csv_filename = "train.npy"
collector.array_dict = {}

modules = [
    EventWeighter("EventWeighter"),
    CSVProducer("CSVProducer"),
    ]
