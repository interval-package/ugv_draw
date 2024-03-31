import matplotlib.pyplot as plt
import numpy as np


def draw_action(data, ax_acc = None, ax_w = None):
    actions = data[["t", "step", "ego_y", "ego_x","action_delat_v", "action_delta_w"]]

    figure = plt.gcf()
    axs = []

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

    x_base = actions["ego_y"].values
    x_base_tag = "ego_y"


    ax_acc.plot(x_base, actions["action_delat_v"].values)
    ax_acc.set_title("action_delat_v")
    ax_acc.set_xlabel(x_base_tag)
    ax_acc.set_ylabel("action_delat_v")
    axs.append(ax_acc)


    ax_w.plot(x_base, actions["action_delta_w"].values)
    ax_w.set_title("action_delta_w")
    ax_w.set_xlabel(x_base_tag)
    ax_w.set_ylabel("action_delta_w")
    axs.append(ax_w)

    return np.array(axs)
