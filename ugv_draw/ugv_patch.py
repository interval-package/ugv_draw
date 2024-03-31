import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as pat
from utils.draw_config import config_ugv, z_order_ugv
from typing import Dict, List, Union

facecolor = 'lightgray'
class UGV_patch:

    def __init__(self, ax:plt.Axes, x = 0, y = 0, theta = np.pi/2, color="blue", config:Dict = config_ugv, **kwargs) -> None:
        # init at center
        self.ax = ax
        self.x = x
        self.y = y
        self.theta = theta
        self.width = config["width"]
        self.height = config["height"]
        self.arrow_len = config["arrow_len"]
        self.line_width = config["line_width"]
        self.color = color
        self.fill = config["fill"]
        self.init = kwargs.get("init", False)
        self.z_order_ugv = z_order_ugv
        if self.init:
            self.z_order_ugv += 1

        rotate_angle = (self.theta - self.theta_error)/np.pi * 180

        # self.cir = pat.Circle((x, y), 0,facecolor='gray', edgecolor='black')
        self.body = pat.Rectangle((x - self.width/2, y - self.height/2), 
                                  width=self.width, height=self.height,
                                  angle=rotate_angle,
                                  fill=self.fill,
                                  facecolor = facecolor,
                                  rotation_point="center",
                                  edgecolor='none'
                                  )
        self.body.set_zorder(self.z_order_ugv+0.2)
        self.body_line:List[plt.Line2D] = [ax.plot([], [], "black", linewidth=self.line_width)[0] for i in range(2)]
        for line in self.body_line:
            line.set_zorder(self.z_order_ugv+0.5)

        match_angle = np.arctan(self.width/self.height)/np.pi*180
        body_radius = np.sqrt(np.square(self.width) + np.square(self.height))/2

        self.match_angle = match_angle
        self.body_radius = body_radius
        if self.fill:
            self.head = pat.Wedge((x, y), r=body_radius,
                                # angle=rotate_angle,
                                theta1 = 90 - match_angle + rotate_angle, theta2 = 90 + match_angle + rotate_angle,
                                facecolor = color,
                                edgecolor='black', linewidth=self.line_width)

            self.tail = pat.Wedge((x, y), r=body_radius, 
                                # angle=rotate_angle,
                                theta1 = 270 - match_angle + rotate_angle, theta2 = 270 + match_angle + rotate_angle,
                                facecolor = facecolor,
                                edgecolor='black', linewidth=self.line_width)
        else:
            self.head = pat.Arc((x, y), width=body_radius, height=body_radius,
                                angle=rotate_angle,
                                theta1 = 90 - match_angle, theta2 = 90 + match_angle,
                                edgecolor=color, linewidth=self.line_width)

            self.tail = pat.Arc((x, y), width=body_radius, height=body_radius,
                                angle=rotate_angle,
                                theta1 = 270 - match_angle, theta2 = 270 + match_angle,
                                edgecolor=color, linewidth=self.line_width)
        
        self.head.set_zorder(self.z_order_ugv+0.1)
        self.tail.set_zorder(self.z_order_ugv+0.1)
            
        self.arrow = ax.plot([], [], color, linewidth=self.line_width)[0]
        self.arrow.set_zorder(self.z_order_ugv+0.5)
        self.spwan()
        self.set_to_ax()
        pass

    # the sub this to match rotation condition
    theta_error = np.pi/2

    def set_to_ax(self):
        self.ax.add_patch(self.body)
        self.ax.add_patch(self.head)
        self.ax.add_patch(self.tail)
        return self.ax

    def set_body_line(self):
        # self.body.get_verts()
        phi = self.theta_error - self.theta
        rotation_matrix = np.array([[np.cos(phi), -np.sin(phi)],
                                    [np.sin(phi), np.cos(phi)]])
        x1, x2, y1, y2 = -self.width/2, self.width/2, -self.height/2, self.height/2
        origin_mat = np.array([[x1, y1], [x1, y2], [x2, y1], [x2, y2]])
        # rotate
        mat = origin_mat @ rotation_matrix  + np.array([[self.x, self.y]]).repeat(4, 0)
        mat = mat.T
        for i in range(2):
            self.body_line[i].set_data(mat[0, 2*i:2*i+2], mat[1, 2*i:2*i+2])
        return self.body_line

    def set_arrow(self, x, y, theta):
        self.arrow.set_data([x, x + np.cos(theta) * self.arrow_len], [y, y + np.sin(theta) * self.arrow_len])
        return self.arrow

    def spwan(self):
        rotate_angle = (self.theta - self.theta_error)/np.pi * 180
        def patch_rotate_arc(patch: pat.Arc):
            patch.set_center((self.x, self.y))
            patch.set_angle(rotate_angle)

        self.body.set_xy((self.x - self.width/2, self.y - self.height/2))
        self.body.set_angle(rotate_angle)
        self.set_body_line()
        if self.fill:
            self.head.set_theta1(90 - self.match_angle + rotate_angle)
            self.head.set_theta2(90 + self.match_angle + rotate_angle)
            self.head.set_center((self.x, self.y))
            self.tail.set_theta1(270 - self.match_angle + rotate_angle)
            self.tail.set_theta2(270 + self.match_angle + rotate_angle)
            self.tail.set_center((self.x, self.y))
        else:
            patch_rotate_arc(self.head)
            patch_rotate_arc(self.tail)

        self.set_arrow(self.x, self.y, self.theta)
        return self

    def move_to(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta
        return self.spwan()

    def move(self, dx, dy, dtheta):
        self.x = self.x + dx
        self.y = self.y + dy
        self.theta = self.theta + dtheta
        return self.spwan()

