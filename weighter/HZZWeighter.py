import numpy as np
import pickle,os,awkward,uproot_methods

from PyLooper.common.Module import Module

class HZZWeighter(Module):
    def analyze(self,data,dataset,cfg):
        cfg.collector.event_weight = np.ones(data["mass4l"].shape[0]) * data["passedFullSelection"]
