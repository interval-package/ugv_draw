import matplotlib.pyplot as plt
import seaborn as sns

from utils.obst_config import obst_cir_red, obst_cir_gray, \
    obst_rect_cargo0, obst_rect_cargo1, obst_rect_cargo2, obst_rect_cargo3, obst_rect_cargo4,\
    obst_rect_shelf

# sns.set_style("whitegrid")
sns.set_style("darkgrid")

world_bound_x = [-2, 5]
world_bound_y = [-6, 4]

# order infomation

z_order_ugv = 10
z_order_obst = 8
z_order_road = 2
z_order_traj = 12

config_scene = {
    "world_bound_x": world_bound_x,
    "world_bound_y": world_bound_y,
    "obstacles": {
        "circles": [
            # dict(xy= (2.5, -3.6-0.3), **obst_cir_red),
            # dict(xy= (2.5, -3.6+0.3), **obst_cir_red),
            # dict(xy= (3.5+0.6+0.25, -0.8), **obst_cir_gray),
            # dict(xy= (3.5+0.6+0.25, 0.5), **obst_cir_gray),
            # dict(xy= (3.5+0.6+0.25, 1.5), **obst_cir_gray),
            # dict(xy= (3.5+0.6+0.25, 2.8), **obst_cir_gray),
            # dict(xy= (3.5, 3.4), **obst_cir_gray),
            # dict(xy= (2.5, 3.4), **obst_cir_gray),
        ],
        "rectangles": [
            dict(**obst_rect_cargo0),
            dict(**obst_rect_cargo1),
            dict(**obst_rect_cargo2),
            dict(**obst_rect_cargo3),
            dict(**obst_rect_cargo4),
            dict(**obst_rect_shelf),
        ]
    }
}

config_traj = {}

config_ugv = {
    "width": 0.5,
    "height": 0.6,
    "arrow_len": 0.35,
    "line_width": 2,
    "fill": True
}

config_road = {
    "width": 1.0,
    # radius for the turning point
    "radius": 0.3,
    # the point is the lower bound
    "point": (2.7+0.5, 1.7+0.5),
    "world_bound_x": [-2, 6],
    "world_bound_y": [-6, 4],
    "color": "green",
    "alpha": 0.1,
    # draw the border for the road
    "border": False,
}

config_legend = {

}