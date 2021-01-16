import numpy as np
import pickle,os,awkward,uproot_methods

from PyLooper.common.Module import Module

class DYToLLWeighter(Module):
    def analyze(self,data,dataset,cfg):
        nlep2_idx = data["Muon_Pt"].count() >= 2
        cfg.collector.mu_pt = data["Muon_Pt"][nlep2_idx]
        cfg.collector.mu_eta = data["Muon_Eta"][nlep2_idx]
        cfg.collector.mu_phi = data["Muon_Phi"][nlep2_idx]

        cfg.collector.mu_vec1 = uproot_methods.classes.TLorentzVector.PtEtaPhiMassLorentzVectorArray(cfg.collector.mu_pt[:,0],cfg.collector.mu_eta[:,0],cfg.collector.mu_phi[:,0],0.,)
        cfg.collector.mu_vec2 = uproot_methods.classes.TLorentzVector.PtEtaPhiMassLorentzVectorArray(cfg.collector.mu_pt[:,1],cfg.collector.mu_eta[:,1],cfg.collector.mu_phi[:,1],0.,)

        cfg.collector.mll = (cfg.collector.mu_vec1 + cfg.collector.mu_vec2).mass 
        cfg.collector.event_weight = np.ones(cfg.collector.mu_pt.shape[0])
