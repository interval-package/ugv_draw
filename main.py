from ugv_draw.draw_scene import draw_scene, draw_traj, draw_road, draw_sub_legend
from ugv_draw.ugv_patch import UGV_patch
from utils.dataloader import preload_tab, process_scene_traj
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.image as mpimg


plt.rcParams["font.family"] = "Arial"
# font size
plt.rcParams["font.size"] = 36
# math stix
plt.rcParams["mathtext.fontset"] = "stix"

def simple_main():
    data = preload_tab(0)
    data = process_scene_traj(data)

    figure = plt.figure(figsize=(16,16))
    ax = figure.add_subplot(1, 1, 1)

    robo_1 = UGV_patch(ax, 3.5, -5, np.pi/2, "green", init=True)
    robo_obst = UGV_patch(ax, 2.0, 2.8, np.pi, "red")
    # shadows
    
    draw_traj(ax, data)
    ax, info = draw_scene(ax)
    draw_road(ax=ax)
    draw_sub_legend(ax)

    ax.set_xlabel("$p_x$ (m)")
    ax.set_ylabel("$p_y$ (m)")
    # axis equal
    ax.set_aspect("equal")
    # set xticks
    ax.set_xticks(np.arange(-2, 5, 1))
    ax.set_yticks(np.arange(-5, 4, 1))

    x_list = [0.025, 0.58, 0.58, 0.868, 0.868, 0.868, 0.868, 0.75, 0.65]
    y_list = [0.205, 0.16, 0.22, 0.47, 0.59, 0.71, 0.83, 0.895, 0.895]
    for i in range(len(x_list)):
        x = x_list[i]
        y = y_list[i]
        ax2 = ax.inset_axes([x, y, 0.09,0.1])
        ax2.imshow(mpimg.imread("./cone.png"))
        ax2.axis("off")
    return ax

if __name__ == "__main__":
    simple_main()
    plt.tight_layout()
    plt.savefig("./temp.png", dpi=200)
    plt.savefig("./temp.pdf")
    pass
