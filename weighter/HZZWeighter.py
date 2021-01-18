import numpy as np
import pickle,os,awkward,uproot_methods

from PyLooper.common.Module import Module

class HZZWeighter(Module):
    def analyze(self,data,dataset,cfg):
        data_shape0 = data["mass4l"].shape[0]
        cfg.collector.selection_weight = data["passedFullSelection"] * (data["mass4l"] > 118.) * (data["mass4l"] < 130.)
        cfg.collector.event_weight = np.ones(data_shape0) * cfg.collector.selection_weight * dataset.xs * dataset.lumi / dataset.sumw 
