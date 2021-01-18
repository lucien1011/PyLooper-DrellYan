import numpy as np
import pickle,os,awkward

from PyLooper.common.Module import Module

class CSVProducer(Module):
    def analyze(self,data,dataset,cfg):
        data_shape0 = data["mass4l"].shape[0]
        arr = np.concatenate(
                [
                    np.expand_dims(data["mass4l"],axis=1),
                    np.expand_dims(data["massZ1"],axis=1),
                    np.expand_dims(data["massZ2"],axis=1),
                    np.expand_dims(data["pT4l"],axis=1),
                    np.expand_dims(data["rapidity4l"],axis=1),
                    np.expand_dims(data["pTZ1"],axis=1),
                    np.expand_dims(data["pTZ2"],axis=1),
                    np.expand_dims(data["pTL1"],axis=1),
                    np.expand_dims(data["pTL2"],axis=1),
                    np.expand_dims(data["pTL3"],axis=1),
                    np.expand_dims(data["pTL4"],axis=1),
                    np.expand_dims(data["cosTheta1"],axis=1),
                    np.expand_dims(data["cosTheta2"],axis=1),
                    np.expand_dims(data["cosThetaStar"],axis=1),
                    np.expand_dims(data["Phi"],axis=1),
                    np.expand_dims(data["Phi1"],axis=1),
                    np.broadcast_to(dataset.param,(data_shape0,1)),
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
