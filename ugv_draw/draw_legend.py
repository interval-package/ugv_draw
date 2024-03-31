import matplotlib.pyplot as plt
import matplotlib.patches as pat
import numpy as np
import pandas as pd

from utils.draw_config import world_bound_x, world_bound_y
from utils.obst_config import obst_cir_red, obst_cir_gray, obst_rect_cargo1, obst_rect_shelf
from ugv_draw.ugv_patch import UGV_patch

def draw_scene_legend(ax: plt.Axes):
    ax.set_xlim((world_bound_x))
    ax.set_ylim((world_bound_y))


    x_len = world_bound_x[1] - world_bound_y[0]
    y_len = world_bound_y[1] - world_bound_y[0]

    legend_list = []

    x_pro = lambda px: world_bound_x[0] + x_len*px
    y_pro = lambda py: world_bound_y[0] + y_len*py

    radius = 0.03 * x_len
    padding_x = 0.1*x_len

    def legend_cir(x, y, cof:dict, doc):
        cof.copy()
        cof.pop("radius")
        obst = pat.Circle((x, y), radius, **cof)
        ax.text(x + padding_x + radius*2,  y, doc, va="center")
        # ax.add_patch(obst)
        legend_list.append(obst)

    def legend_rect(x, y, cof:dict, doc):
        cof = cof.copy()
        cof.pop("width")
        cof.pop("height")
        cof.pop("xy")
        obst = pat.Rectangle((x-radius, y-radius), radius*4, radius*2, **cof)
        ax.text(x + padding_x + radius*2,  y, doc, va="center")
        ax.add_patch(obst)
        legend_list.append(obst)

    y_list = [0.8, 0.65, 0.5, 0.35, 0.2]

    car_exp = UGV_patch(ax, x_pro(0.15), y_pro(y_list[0]), color="Green")
    ax.text(x_pro(0.15) + padding_x + radius*2,  y_pro(y_list[0]), "Ego robot", va="center")
    
    car_exp = UGV_patch(ax, x_pro(0.15), y_pro(y_list[1]), color="Red")
    ax.text(x_pro(0.15) + padding_x + radius*2,  y_pro(y_list[1]), "Obstacle robot", va="center")
    
    legend_cir(x_pro(0.15), y_pro(y_list[2]), obst_cir_gray, 'Obstacle cone ')
    legend_rect(x_pro(0.15), y_pro(y_list[3]), obst_rect_cargo1, "Obstacle box")
    legend_rect(x_pro(0.15), y_pro(y_list[4]), obst_rect_shelf, "Destination")

    return

if __name__ == "__main__":
    ax = plt.gca()
    draw_scene_legend(ax)
    pass