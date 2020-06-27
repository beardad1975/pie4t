import random
import math

import pymunk
import arcade

from . import common

BALL_COLORS = (arcade.color.WINDSOR_TAN,
               arcade.color.VIVID_VIOLET,
               arcade.color.ULTRAMARINE_BLUE,
               arcade.color.TANGELO,
               arcade.color.GREEN,
               )

class Circle:
    def __init__(self,):
        # pymunk part
        #self.density = 1
        self.is_lazy_setup = False

        self.phy_body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)

        self.radius = random.randrange(10,30)
        self.phy_shape = pymunk.Circle(self.phy_body, self.radius)
        self.phy_shape.density = common.DEFAULT_DENSITY
        self.phy_shape.friction = common.DEFAULT_FRICTION
        self.phy_shape.elasticity = common.DEFAULT_ELASTICITY

        #self.moment = pymunk.moment_for_circle(self.mass, 0, self.radius)
        #self.body = pymunk.Body(self.mass, self.moment)
        x = random.randint(120, 380)
        self.phy_body.position = x, 550
        #self.physics_shape = pymunk.Circle(self.body, self.radius)
        #self.physics_shape.friction = 0.8
        common.stage.space.add(self.phy_body, self.phy_shape)
        
        if common.stage.is_engine_running:
            self.lazy_setup()
            self.is_lazy_setup = True

    def lazy_setup(self):
        ### arcade part
        if not self.is_lazy_setup:
            print('do circle lazy setup')
            self.shape_element = arcade.ShapeElementList()
            # circle
            ball_color = random.choice(BALL_COLORS)
            #s = arcade.create_ellipse_filled(0, 0, self.radius, self.radius, ball_color)
            s = arcade.create_ellipse_filled_with_colors(0, 0, self.radius, self.radius,
                                                ball_color, arcade.color.UNMELLOW_YELLOW)
            self.shape_element.append(s)
            
            # dot
            #s = arcade.create_ellipse_filled(self.radius-6 , 0, 2, 2, arcade.color.WHITE)
            #self.shape_element.append(s)
            s_radius = int(self.radius * 0.15)
            s = arcade.create_ellipse_filled(self.radius-s_radius*2 , 0, s_radius, s_radius, arcade.color.WHITE)
            self.shape_element.append(s)
        
    def draw(self):
        self.shape_element.center_x = self.phy_body.position.x
        self.shape_element.center_y = self.phy_body.position.y
        self.shape_element.angle = math.degrees(self.phy_body.angle)
        self.shape_element.draw()
        