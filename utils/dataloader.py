import pickle
import pandas as pd
import numpy as np
from typing import List, Literal, Union
import os

path_indoor = "data/indoor/results_2403"

path_outside = "data/outside/results"

path_base_res = path_outside

path_results = [name for name in os.listdir(path_base_res) if name.endswith("ADP")]

headers_csv = ["action_delta_v_normal","action_w","action_v",
               "step","ego_x","action_delat_v","ego_w","ego_v",
               "action_delta_w","action_delta_w_normal","ego_y",
               "t","ego_theta"]

def preload_tab(tar_file:Union[int, str]):
    if isinstance(tar_file, int):
        tar_file = path_results[tar_file]
    data_file = os.path.join(path_base_res, tar_file, "results0.csv")
    assert os.path.exists(data_file), "No such data"
    tab = pd.read_csv(data_file)
    return tab

def process_scene_traj(tab: pd.DataFrame):
    header = ["t", "step", "ego_x", "ego_w", "ego_v", "ego_y", "ego_theta"]
    return tab[header]

def process_tab_disp(tab=None):
    if tab is None:
        tab = preload_tab(0)

    header_filtered = [head for head in headers_csv if not head.startswith("action")]

    return tab[header_filtered]

if __name__ == "__main__":
    pass
