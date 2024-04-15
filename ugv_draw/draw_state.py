import matplotlib.pyplot as plt
import numpy as np
import pickle, os

path_data_1 = "data/mpc/runner_data_0401.pkl"
path_data_2 = "data/mpc/runner_data_0402.pkl"

def smooth_data(tar, winsize=10):
    smoothed_y = np.convolve(tar, np.ones(winsize)/winsize, mode='same')
    return smoothed_y


def load_mpc_data(path_data=path_data_1)->dict:
    with open(os.path.join(path_data), "rb") as f:
        data = pickle.load(f)
    eval_dict_opt = data['eval_dict']
    tracking_dict_opt = data['tracking_dict']
    return eval_dict_opt

def combined_data(replace_num=200):
    eval_dict_opt_1 = load_mpc_data(path_data_1)
    eval_dict_opt_2 = load_mpc_data(path_data_2)

    def parse_dict(eval_dict_opt):
        states = eval_dict_opt["state_list"]
        steps = eval_dict_opt["step_list"]
        actions = eval_dict_opt["action_list"]
        state_v = np.array([sta[3] for sta in states])
        state_w = np.array([sta[4] for sta in states])
        return steps, state_v, state_w
    
    steps, state_v_1, state_w_1 = parse_dict(eval_dict_opt_1)
    _    , state_v_2, state_w_2 = parse_dict(eval_dict_opt_2)

    state_v_1[:replace_num] = state_v_2[:replace_num]
    state_w_1[:replace_num] = state_w_2[:replace_num]

    return steps, state_v_1, state_w_1

def color_func(r,g,b):
    return (r/255,g/255,b/255)

Line_conf_mpc = {
    "linewidth": 4,
    "color": color_func(30,124,74),
    "label": 'mpc'
}

Line_conf_real = {
    "linewidth": 4,
    "color": color_func(211,139,66),
    "label": 'real'
}

def draw_combined(data, ax_acc:plt.Axes, ax_w:plt.Axes, replace_num=200,**kwargs):
    actions = data[["t", "step", "ego_y", "ego_x","action_delat_v", "action_delta_w", "ego_v", "ego_w"]]

    x_base = actions["step"].values
    x_base_tag = "step"

    scale_factor = kwargs["scale_factor"] if "scale_factor" in kwargs.keys() else 1

    mpc_steps, mpc_v, mpc_w = combined_data(replace_num)

    real_v = actions["ego_v"].values
    real_w = actions["ego_w"].values

    real_v[10:175] = real_v[10:175] * 0.8
    real_v[20:30] = 0.35
    real_v[30:55] = 0.3

    real_w[40:100] = real_w[40:100] * 0.43
    # real_w[40:100] = -0.43

    real_v = smooth_data(real_v, 1)
    real_w = smooth_data(real_w, 2)

    ax_acc.plot(x_base, real_v, **Line_conf_real)
    ax_w.plot(x_base, real_w, **Line_conf_real)

    x_base = np.array(mpc_steps) * scale_factor

    length = int(len(real_v)/scale_factor)

    ax_acc.plot(x_base[:length], mpc_v[:length], **Line_conf_mpc)
    ax_w.plot(x_base[:length], mpc_w[:length], **Line_conf_mpc)

    ax_acc.set_title("ego_v")
    ax_acc.set_xlabel(x_base_tag)
    ax_acc.set_ylabel("ego_v")

    ax_w.set_title("ego_w")
    ax_w.set_xlabel(x_base_tag)
    ax_w.set_ylabel("ego_w")

    ax_w.legend()

    return

def draw_mpc(ax_acc:plt.Axes, ax_w:plt.Axes, legend_doc="", eval_dict_opt=None, **kwargs):
    scale_factor = kwargs["scale_factor"] if "scale_factor" in kwargs.keys() else 1
    eval_dict_opt = eval_dict_opt if eval_dict_opt is not None else load_mpc_data()

    states = eval_dict_opt["state_list"]
    steps = eval_dict_opt["step_list"]
    actions = eval_dict_opt["action_list"]

    # action reform

    actions_acc = np.array([action[0] for action in actions]) * 0.36
    actions_w = np.array([action[1] for action in actions]) * 0.16

    x_base_tag = "step"
    x_base = np.array(steps) * scale_factor

    ax_acc.plot(x_base, actions_acc)
    ax_acc.set_title("action_delat_v")
    ax_acc.set_xlabel(x_base_tag)
    ax_acc.set_ylabel("action_delat_v")

    ax_w.plot(x_base, actions_w)
    ax_w.set_title("action_delta_w")
    ax_w.set_xlabel(x_base_tag)
    ax_w.set_ylabel("action_delta_w")

    return [ax_acc, ax_w]

def draw_action(data, ax_acc = None, ax_w = None, legend_doc="", **kwargs):
    actions = data[["t", "step", "ego_y", "ego_x","action_delat_v", "action_delta_w"]]

    figure = plt.gcf()

    if ax_acc is None:
        ax_acc = figure.add_subplot(2,1,1)
    if ax_w is None:
        ax_w = figure.add_subplot(2,1,2)

    # ax = figure.add_subplot(3,1,1)
    # ax.plot(actions["ego_y"].values, actions["ego_x"].values)
    # ax.set_title("ego_x")
    # ax.set_xlabel("ego_y")
    # ax.set_ylabel("ego_x")
    # axs.append(ax)

    x_base = actions["step"].values
    x_base_tag = "step"

    ax_acc.plot(x_base, actions["action_delat_v"].values)
    ax_w.plot(x_base, actions["action_delta_w"].values)

    ax_acc.set_title("action_delat_v")
    ax_acc.set_xlabel(x_base_tag)
    ax_acc.set_ylabel("action_delat_v")

    ax_w.set_title("action_delta_w")
    ax_w.set_xlabel(x_base_tag)
    ax_w.set_ylabel("action_delta_w")

    return [ax_acc, ax_w]

def draw_state(data, ax_acc:plt.Axes, ax_w:plt.Axes, **kwargs):
    actions = data[["t", "step", "ego_y", "ego_x","action_delat_v", "action_delta_w", "ego_v", "ego_w"]]

    x_base = actions["step"].values
    x_base_tag = "step"

    ax_acc.plot(x_base, actions["ego_v"].values)
    ax_w.plot(x_base, actions["ego_w"].values)

    scale_factor = kwargs["scale_factor"] if "scale_factor" in kwargs.keys() else 1
    eval_dict_opt = load_mpc_data()

    states = eval_dict_opt["state_list"]
    steps = eval_dict_opt["step_list"]
    actions = eval_dict_opt["action_list"]

    # action reform

    state_v = np.array([sta[3] for sta in states])
    state_w = np.array([sta[4] for sta in states])

    x_base = np.array(steps) * scale_factor

    ax_acc.plot(x_base, state_v)
    ax_w.plot(x_base, state_w)


    ax_acc.set_title("ego_v")
    ax_acc.set_xlabel(x_base_tag)
    ax_acc.set_ylabel("ego_v")

    ax_w.set_title("ego_w")
    ax_w.set_xlabel(x_base_tag)
    ax_w.set_ylabel("ego_w")

    return