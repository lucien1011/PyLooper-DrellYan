import numpy as np
import pickle,os,awkward

from PyLooper.common.Module import Module

class CSVProducer(Module):
    def analyze(self,data,dataset,cfg):
        arr = np.concatenate(
                [
                    np.expand_dims(data["mass4l"],axis=1),
                    np.broadcast_to(dataset.mass,(cfg.collector.mu_pt.shape[0],1)),
                ],
                axis=1,
                )
        cfg.collector.array_dict[dataset.name] = arr

    def end(self,dataset,cfg):
        out_path = os.path.join(cfg.collector.output_path,dataset.name+"_"+cfg.collector.csv_filename)
        with open(out_path,"wb") as f: np.save(f,cfg.collector.array_dict[dataset.name])

    def sumup(self,cfg):
        out_arr = np.concatenate([np.load(os.path.join(cfg.collector.output_path,fname)) for fname in os.listdir(cfg.collector.output_path)])
        out_path = os.path.join(cfg.collector.output_path,cfg.collector.csv_filename)
        with open(out_path,"wb") as f: np.save(f,out_arr)
