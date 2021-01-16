from PyLooper.common.Dataset import Dataset
from PyLooper.common.Collector import Collector

from PyLooper.stat.Hist1D import Hist1D
from PyLooper.hep.plotter.Plotter import Plotter
from PyLooper.hep.plotter.Plot import Plot

from dataset.HZZ_HEL_MadgraphPythia import sample_dict
from weighter.EventWeighter import EventWeighter

verbose = True
nblock = 1024
ngrid = 100
entrysteps = nblock*ngrid
namedecode = "utf-8" 

dataset_list = [
        sample_dict["0.007207126964764954"],
        sample_dict["0.11519407215005831"],
        sample_dict["0.19386708765359545"],
        ]
merged_dataset_list = []

collector = Collector(
    output_path = "./output/2021_01_16_plot_HZZ_HEL_cfg/",
    )

plots = [
        Plot("Pt_L1",lambda data,dataset,cfg: cfg.collector.mu_pt[:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,200.),),
        Plot("Pt_L2",lambda data,dataset,cfg: cfg.collector.mu_pt[:,1],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,100.),),
        Plot("Eta_L1",lambda data,dataset,cfg: cfg.collector.mu_eta[:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,-3.,3.),),
        Plot("Eta_L2",lambda data,dataset,cfg: cfg.collector.mu_eta[:,1],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,-3.,3.),),
        Plot("Phi_L1",lambda data,dataset,cfg: cfg.collector.mu_phi[:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,-3.,3.),),
        Plot("Phi_L2",lambda data,dataset,cfg: cfg.collector.mu_phi[:,1],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,-3.,3.),),

    ]

modules = [
    EventWeighter("EventWeighter"),
    Plotter("Plot",),
    ]
