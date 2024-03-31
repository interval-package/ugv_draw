import matplotlib.pyplot as plt
import matplotlib.patches as pat
import numpy as np
import pandas as pd
from utils.draw_config import config_scene, config_road, config_traj, z_order_obst, z_order_road, z_order_traj
from ugv_draw.draw_legend import draw_scene_legend
from typing import List, Dict


def draw_scene(ax:plt.Axes = None, config=config_scene):
    if ax is None:
        ax = plt.gcf().add_subplot(1,1,1)

    ax.set_xlim(*config["world_bound_x"])
    ax.set_ylim(*config["world_bound_y"])
    ax.set_xticks(np.arange(*config["world_bound_x"]))
    ax.set_yticks(np.arange(*config["world_bound_y"]))

    ax.grid(visible=True, which="both", axis="both")
    ax.set_aspect("equal")

    # draw obstacles
    obses = config["obstacles"]
    # draw circle obstacles
    list_circle:List[pat.Circle] = []
    obses_c: List[Dict] = obses["circles"]
    for obst in obses_c:
        cir = pat.Circle(zorder=z_order_obst, **obst)
        ax.add_patch(cir)
        list_circle.append(cir)

    # draw rect obstacles
    list_rectangle:List[pat.Rectangle] = []
    obses_r: List[Dict] = obses["rectangles"]
    for obst in obses_r:
        rect = pat.Rectangle(zorder=z_order_obst, **obst)
        ax.add_patch(rect)
        list_circle.append(rect)

    obstacle_info = {
        "circles": list_circle,
        "rectangle": list_rectangle
    }

    info = {
        "obstacles": obstacle_info
    }
    
    return ax, info 

def draw_road(ax:plt.Axes, config=config_road):
    width  = config["width"]
    radius = config["radius"]
    point  = config["point"]
    y_l = config["world_bound_y"][0]
    x_l = config["world_bound_x"][0]
    p_up = (point[0], y_l)
    p_left = (x_l, point[1])

    # first draw patch

    style_config = {
        "facecolor":config["color"], 
        # "edgecolor": "none", 
        "alpha":config["alpha"], 
        "fill":True,
        # "z_order": z_order_road
    }

    body_up = pat.Rectangle(p_up, width=width, height=point[1] - y_l - radius, 
                            **style_config)
    body_left = pat.Rectangle(p_left, width=point[0] - x_l - radius, height=width, 
                              **style_config)
    body_turn = pat.Wedge((point[0]-radius, point[1]-radius), 
                          r=width+radius, width=width,
                          theta1=0, theta2=90, **style_config)

    patchs:pat.Patch = [body_up, body_turn, body_left]

    for patch in patchs:
        patch.set_zorder(z_order_road)
        ax.add_patch(patch)

    info = {
        "road_body": patchs
    }

    if config["border"]:
        # make lines
        pass

    return ax, info

def draw_traj(ax:plt.Axes, traj_data, config=None):

    ego_x = traj_data["ego_x"].values
    ego_y = traj_data["ego_y"].values
    ego_phi = traj_data["ego_theta"].values
    t = traj_data["t"].values
    downsampling_ratio = 10
    downsampling_x = ego_x[::downsampling_ratio]
    downsampling_y = ego_y[::downsampling_ratio]
    traj_sca = ax.scatter(downsampling_x, downsampling_y, s=120, zorder=z_order_traj, 
                          cmap=plt.cm.plasma, c=np.arange(len(downsampling_x))*0.5)
    # traj_sca.set_zorder(z_order_traj)
    # plt.colorbar(traj_sca)
    ## add legend
    plt.colorbar(traj_sca, ax=ax, label="Time (s)")
    
    from ugv_draw.ugv_patch import UGV_patch
    t_list = [50, 100, 170, 270, 380, 620, 700, 800]
    for t in t_list:
        robot_tmp = UGV_patch(ax, ego_x[t], ego_y[t],  ego_phi[t], "green")

    info = {
        "traj": traj_sca
    }
    return ax, info

def draw_sub_legend(ax:plt.Axes):
    ax2 = ax.inset_axes([-0.05,0.0,0.5,0.5])
    # fill ax2 using lightgray
    ax2.set_facecolor('None')
    # 加边框
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax2.grid(False)
    # set xticks
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax.tick_params(axis='both', which='both', bottom=False, top=False, left=False, right=False)
    # ax2.axis('off')
    draw_scene_legend(ax2)
    return
