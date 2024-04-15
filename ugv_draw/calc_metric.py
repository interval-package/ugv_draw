import matplotlib.pyplot as plt
import numpy as np
import scipy
import os
from scipy.interpolate import interp1d
import seaborn as sns

base_path = "/home/zhengziang/zaspace/projects/ugv_draw/data/real_plot_data"

def color_func(r,g,b):
    return (r/255,g/255,b/255)

config_hist = {
    "color": color_func(211,139,66)
}


def load_data_tuple():
    mpc_time_data = np.load(os.path.join(base_path, "mpc_time_data.npy")).squeeze()
    mpc_v_data = np.load(os.path.join(base_path, "mpc_v_data.npy")).squeeze()
    mpc_w_data = np.load(os.path.join(base_path, "mpc_w_data.npy")).squeeze()
    real_time_data = np.load(os.path.join(base_path, "real_time_data.npy")).squeeze()
    real_v_data = np.load(os.path.join(base_path, "real_v_data.npy")).squeeze()
    real_w_data = np.load(os.path.join(base_path, "real_w_data.npy")).squeeze()
    return (real_time_data, real_v_data, real_w_data), (mpc_time_data, mpc_v_data, mpc_w_data)

def calc_metric(real_tuple, mpc_tuple, replace_num=200, **kwargs):
    mpc_steps, mpc_v, mpc_w = mpc_tuple
    real_steps, real_v, real_w = real_tuple

    # interp

    interp_func_v = interp1d(mpc_steps, mpc_v, kind='quadratic', fill_value="extrapolate")
    interp_func_w = interp1d(mpc_steps, mpc_w, kind='quadratic', fill_value="extrapolate")

    interp_mpc_v = interp_func_v(real_steps)
    interp_mpc_w = interp_func_w(real_steps)

    def calc_diffs(real, mpc):
        diff = np.abs(mpc - real)
        ret = diff / (np.max(mpc) - np.min(mpc))
        return ret

    def calc_MPA(real, mpc):
        diff = np.abs(mpc - real)
        ret = diff / (np.max(mpc) - np.min(mpc))
        return np.max(ret)

    def calc_EPA(real, mpc):
        diff = np.abs(mpc - real)
        ret = diff / (np.max(mpc) - np.min(mpc))
        return np.mean(ret)
    
    print(calc_MPA(real_v, interp_mpc_v))
    print(calc_EPA(real_v, interp_mpc_v))
    print(calc_MPA(real_w, interp_mpc_w))
    print(calc_EPA(real_w, interp_mpc_w))

    return calc_diffs(real_v, interp_mpc_v), calc_diffs(real_w, interp_mpc_w)

plt.rcParams["font.family"] = "Arial"
# font size
plt.rcParams["font.size"] = 36
# math stix
plt.rcParams["mathtext.fontset"] = "stix"

if __name__ == "__main__":
    r_t, m_t = load_data_tuple()
    diff_v, diff_w = calc_metric(r_t, m_t)
    fig = plt.figure(figsize=(32,8))
    sns.set_style("darkgrid")
    ax = fig.add_subplot(1,2,1)
    ax.hist(diff_v, **config_hist)
    ax.set_title("Longitudinal control")
    ax.set_xlabel("Error")
    ax.set_ylabel("Count")
    ax = fig.add_subplot(1,2,2)
    ax.hist(diff_w, **config_hist)
    ax.set_title("Lateral control")
    ax.set_xlabel("Error")
    plt.tight_layout()
    fig.savefig("figure/hist_action.pdf")
    pass
