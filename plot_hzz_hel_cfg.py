from PyLooper.common.Dataset import Dataset
from PyLooper.common.Collector import Collector

from PyLooper.stat.Hist1D import Hist1D
from PyLooper.hep.plotter.Plotter import Plotter
from PyLooper.hep.plotter.Plot import Plot

from dataset.HZZ_HEL_MadgraphPythia import sample_dict
from weighter.HZZWeighter import HZZWeighter

verbose = True
nblock = 1024
ngrid = 100
entrysteps = nblock*ngrid
namedecode = "utf-8" 

dataset_list = [
        sample_dict["0.002312241433103379"],
        sample_dict["0.11241494661692496"],
        sample_dict["0.18344811555903712"],
        ]
merged_dataset_list = []

collector = Collector(
    output_path = "./output/2021_01_16_plot_HZZ_HEL_cfg/",
    )

plots = [
        Plot("mass4l",lambda data,dataset,cfg: data["mass4l"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(25,100.,150.),),
        Plot("massZ1",lambda data,dataset,cfg: data["massZ1"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(60,0.,120.),),
        Plot("massZ2",lambda data,dataset,cfg: data["massZ2"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(30,0.,60.),),
        Plot("pTL1",lambda data,dataset,cfg: data["pTL1"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(30,0.,60.),),
        Plot("pTL2",lambda data,dataset,cfg: data["pTL2"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(30,0.,60.),),
        Plot("pTL3",lambda data,dataset,cfg: data["pTL3"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(30,0.,60.),),
        Plot("pTL4",lambda data,dataset,cfg: data["pTL4"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(30,0.,60.),),
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
