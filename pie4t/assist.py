from time import time

import arcade
from . import common

class DotMark:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.radius = 20
        self.circle_color = (255,255,255,90)
        self.cross_line_width = 3
        self.cross_line_height = 10
        self.cross_color = arcade.color.YELLOW
        self.timestamp = time()
        self.enable = False

    def lazy_setup(self):
        self.shape_list = arcade.ShapeElementList()
        
        s = arcade.create_ellipse(0, 0 , 20, 20, (255,255,255,90))
        self.shape_list.append(s)

        vs = arcade.create_rectangle(0,0, 3, 20, arcade.color.YELLOW )
        hs = arcade.create_rectangle(0,0, 20, 3, arcade.color.YELLOW )
        self.shape_list.append(vs)
        self.shape_list.append(hs)

    def update_pos(self, x, y):
        self.x = x
        self.y = y
        self.timestamp = time()
        self.enable = True
        

    def draw(self):
        if self.enable:
            if time() - self.timestamp < common.ASSIST_MARK_PERIOD:
                self.shape_list.center_x = self.x
                self.shape_list.center_y = self.y
                self.shape_list.angle = 0 # no rotation
                self.shape_list.draw()
            else: # expired
                self.enable = False