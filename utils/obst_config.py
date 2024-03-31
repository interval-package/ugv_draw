orange_color = (204/255, 137/255, 99/255)
blue_color = (89/255, 117/255, 164/255)
red_color = (255/255, 127/255, 127/255)


obst_cir_red = {
    "radius": 0.15,
    "facecolor": red_color, 
    "edgecolor": 'black'
}

obst_cir_gray = {
    "radius": 0.15,
    "facecolor": red_color, 
    "edgecolor": 'black'
}


obst_rect_cargo_width0 = 0.365
obst_rect_cargo_height0 = 0.525
obst_rect_cargo0 = {
    "xy": (3.5+0.1-obst_rect_cargo_width0*0.5, -5+1.4+obst_rect_cargo_height0/2-obst_rect_cargo_height0*0.5), 
    "width": obst_rect_cargo_width0, "height": obst_rect_cargo_height0,
    "facecolor": orange_color, 
    "edgecolor": 'black'
}

obst_rect_cargo_width1 = 0.365
obst_rect_cargo_height1 = 0.525
obst_rect_cargo1 = {
    "xy": (3.5+0.1-obst_rect_cargo_width1*0.5, -5+1.4-obst_rect_cargo_height1/2-obst_rect_cargo_height1*0.5), 
    "width": obst_rect_cargo_width1, "height": obst_rect_cargo_height1,
    "facecolor": orange_color, 
    "edgecolor": 'black'
}

obst_rect_cargo_width2 = 0.3
obst_rect_cargo_height2 = 0.6
obst_rect_cargo2 = {
    "xy": (3.5+0.6+0.15+0.1-obst_rect_cargo_width2*0.5, -5+5.5*0.6-0.1-obst_rect_cargo_height2*0.5), 
    "width": obst_rect_cargo_width2, "height": obst_rect_cargo_height2,
    "facecolor": orange_color, 
    "edgecolor": 'black'
}

obst_rect_cargo_width3 = 0.75
obst_rect_cargo_height3 = 0.3
obst_rect_cargo3 = {
    "xy": (3.5-3.5*0.6+0.6-obst_rect_cargo_width3*0.5, -5+14*0.6-obst_rect_cargo_height3*0.5), 
    "width": obst_rect_cargo_width3, "height": obst_rect_cargo_height3,
    "facecolor": orange_color, 
    "edgecolor": 'black'
}

obst_rect_cargo_width4 = 1.3
obst_rect_cargo_height4 = 0.3
obst_rect_cargo4 = {
    "xy": (3.5-3.5*0.6-1.2-obst_rect_cargo_width4*0.5, -5+14*0.6-obst_rect_cargo_height4*0.5), 
    "width": obst_rect_cargo_width4, "height": obst_rect_cargo_height4,
    "facecolor": orange_color, 
    "edgecolor": 'black'
}

obst_rect_shelf = {
    "xy": (-1.3, 2.2), "width": 0.8, "height": 1,
    "facecolor": 'green', 
    "edgecolor": 'black',
    "alpha": 0.8
}
