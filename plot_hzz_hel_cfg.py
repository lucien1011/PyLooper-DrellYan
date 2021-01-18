from PyLooper.common.Dataset import Dataset
from PyLooper.common.Collector import Collector

from PyLooper.stat.Hist1D import Hist1D
from PyLooper.hep.plotter.Plotter import Plotter
from PyLooper.hep.plotter.Plot import Plot

from dataset.ZZ_HEL_MadgraphPythia import ZZ
from dataset.EFTHZZ_HEL_MadgraphPythia import sample_dict
from dataset.SMHZZ_HEL_MadgraphPythia import ggH 
from weighter.HZZWeighter import HZZWeighter

verbose = True
nblock = 1024
ngrid = 100
entrysteps = nblock*ngrid
namedecode = "utf-8" 

dataset_list = [
        ggH,
        ZZ,
        sample_dict["0.010927157057048276"],
        sample_dict["0.0509606966591849"],
        sample_dict["0.11241494661692496"],
        sample_dict["0.15202925850976992"],
        sample_dict["0.19807022744383446"],
        ]
merged_dataset_list = []

for d in dataset_list:
    d.lumi = 130*1000.

collector = Collector(
    output_path = "./output/2021_01_16_plot_HZZ_HEL_cfg/",
    )

plots = [
        Plot("mass4l",lambda data,dataset,cfg: data["mass4l"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(60,80.,200.),),
        Plot("massZ1",lambda data,dataset,cfg: data["massZ1"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(60,0.,120.),),
        Plot("massZ2",lambda data,dataset,cfg: data["massZ2"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(60,0.,120.),),
        Plot("pTL1",lambda data,dataset,cfg: data["pTL1"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(50,0.,100.),),
        Plot("pTL2",lambda data,dataset,cfg: data["pTL2"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(30,0.,60.),),
        Plot("pTL3",lambda data,dataset,cfg: data["pTL3"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(30,0.,60.),),
        Plot("pTL4",lambda data,dataset,cfg: data["pTL4"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(20,0.,40.),),
        Plot("cosTheta1",lambda data,dataset,cfg: data["cosTheta1"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(20,-1.,1.),),
        Plot("cosTheta2",lambda data,dataset,cfg: data["cosTheta2"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(20,-1.,1.),),
        Plot("cosThetaStar",lambda data,dataset,cfg: data["cosThetaStar"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(20,-1.,1.),),
        Plot("Phi",lambda data,dataset,cfg: data["Phi"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(20,-4.,4.),),
        Plot("Phi1",lambda data,dataset,cfg: data["Phi1"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(20,-4.,4.),),
    ]

modules = [
    HZZWeighter("EventWeighter"),
    Plotter("Plot",),
    ]
