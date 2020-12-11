import numpy as np
import pickle,os,awkward

from PyLooper.common.Module import Module

class EventWeighter(Module):
    def analyze(self,data,dataset,cfg):
        nlep2_idx = data["Muon_Pt"].count() >= 2
        cfg.collector.mu_pt = data["Muon_Pt"][nlep2_idx]
        cfg.collector.mu_eta = data["Muon_Eta"][nlep2_idx]
        cfg.collector.mu_phi = data["Muon_Phi"][nlep2_idx]
        
        cfg.collector.mu_genpt = data["Muon_GenPt"][nlep2_idx]
        cfg.collector.mu_geneta = data["Muon_GenEta"][nlep2_idx]
        cfg.collector.mu_genphi = data["Muon_GenPhi"][nlep2_idx]
        cfg.collector.mu_genmass = data["Muon_GenMass"][nlep2_idx]

        cfg.collector.event_weight = np.ones(cfg.collector.mu_pt.shape[0])
