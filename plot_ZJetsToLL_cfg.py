from PyLooper.common.Dataset import Dataset
from PyLooper.common.Collector import Collector

from PyLooper.stat.Hist1D import Hist1D
from PyLooper.hep.plotter.Plotter import Plotter
from PyLooper.hep.plotter.Plot import Plot

from Dataset.ZJetsToLL_LO_MLM import ZJetsToLL_LO_MLM
from Weighter.EventWeighter import EventWeighter

verbose = True
nblock = 1024
ngrid = 100
entrysteps = nblock*ngrid
namedecode = "utf-8" 

dataset_list =  [ZJetsToLL_LO_MLM]
merged_dataset_list = []

collector = Collector(
    output_path = "./output/2020_12_07_plot_ZJetsToLL_cfg/",
    )

plots = [
        Plot("Pt_L1",lambda data,dataset,cfg: cfg.collector.mu_pt[:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,200.),),
        Plot("Pt_L2",lambda data,dataset,cfg: cfg.collector.mu_pt[:,1],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,100.),),
        Plot("Eta_L1",lambda data,dataset,cfg: cfg.collector.mu_eta[:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,-3.,3.),),
        Plot("Eta_L2",lambda data,dataset,cfg: cfg.collector.mu_eta[:,1],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,-3.,3.),),
        Plot("Phi_L1",lambda data,dataset,cfg: cfg.collector.mu_phi[:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,-3.,3.),),
        Plot("Phi_L2",lambda data,dataset,cfg: cfg.collector.mu_phi[:,1],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,-3.,3.),),

        Plot("GenPt_L1",lambda data,dataset,cfg: cfg.collector.mu_genpt[:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,200.),),
        Plot("GenPt_L2",lambda data,dataset,cfg: cfg.collector.mu_genpt[:,1],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,100.),),
        Plot("GenEta_L1",lambda data,dataset,cfg: cfg.collector.mu_geneta[:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,-3.,3.),),
        Plot("GenEta_L2",lambda data,dataset,cfg: cfg.collector.mu_geneta[:,1],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,-3.,3.),),
        Plot("GenPhi_L1",lambda data,dataset,cfg: cfg.collector.mu_genphi[:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,-3.,3.),),
        Plot("GenPhi_L2",lambda data,dataset,cfg: cfg.collector.mu_genphi[:,1],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,-3.,3.),),
        Plot("GenMass_L1",lambda data,dataset,cfg: cfg.collector.mu_genmass[:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,-3.,3.),),
        Plot("GenMass_L2",lambda data,dataset,cfg: cfg.collector.mu_genmass[:,1],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,-3.,3.),),
        
        Plot("PtRes_L1",lambda data,dataset,cfg: cfg.collector.mu_pt[:,0]/cfg.collector.mu_genpt[:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.9,1.1),),
        Plot("PtRes_L2",lambda data,dataset,cfg: cfg.collector.mu_pt[:,1]/cfg.collector.mu_genpt[:,1],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.9,1.1),),
        
        Plot("PtInvRes_L1",lambda data,dataset,cfg: cfg.collector.mu_genpt[:,0]/cfg.collector.mu_pt[:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.9,1.1),),
        Plot("PtInvRes_L2",lambda data,dataset,cfg: cfg.collector.mu_genpt[:,1]/cfg.collector.mu_pt[:,1],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.9,1.1),),

        Plot("EtaInvRes_L1",lambda data,dataset,cfg: cfg.collector.mu_geneta[:,0]/cfg.collector.mu_eta[:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.9,1.1),),
        Plot("EtaInvRes_L2",lambda data,dataset,cfg: cfg.collector.mu_geneta[:,1]/cfg.collector.mu_eta[:,1],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.9,1.1),),

        Plot("PhiInvRes_L1",lambda data,dataset,cfg: cfg.collector.mu_genphi[:,0]/cfg.collector.mu_phi[:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.9,1.1),),
        Plot("PhiInvRes_L2",lambda data,dataset,cfg: cfg.collector.mu_genphi[:,1]/cfg.collector.mu_phi[:,1],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.9,1.1),),

    ]

modules = [
    EventWeighter("EventWeighter"),
    Plotter("Plot",),
    ]
