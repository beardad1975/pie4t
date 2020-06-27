import random
import math

import pymunk
import arcade

from . import common

BALL_COLORS = (arcade.color.WINDSOR_TAN,
               arcade.color.VIVID_VIOLET,
               arcade.color.ULTRAMARINE_BLUE,
               arcade.color.TANGELO,
               arcade.color.UFO_GREEN,
               )

class Circle:
    def __init__(self,):
        # pymunk part
        #self.density = 1
        self.is_lazy_setup = False

        self.pe_body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)

        self.radius = random.randrange(10,30)
        self.pe_shape = pymunk.Circle(self.pe_body, self.radius)
        self.pe_shape.density = 10
        self.pe_shape.friction = 0.5
        self.pe_shape.elasticity = 0.5

        #self.moment = pymunk.moment_for_circle(self.mass, 0, self.radius)
        #self.body = pymunk.Body(self.mass, self.moment)
        x = random.randint(120, 380)
        self.pe_body.position = x, 550
        #self.physics_shape = pymunk.Circle(self.body, self.radius)
        #self.physics_shape.friction = 0.8
        common.stage.space.add(self.pe_body, self.pe_shape)
        
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
            s = arcade.create_ellipse_filled(self.radius-8 , 8, 2, 4, arcade.color.UNMELLOW_YELLOW, tilt_angle=30)
            self.shape_element.append(s)
        
    def draw(self):
        self.shape_element.center_x = self.pe_body.position.x
        self.shape_element.center_y = self.pe_body.position.y
        self.shape_element.angle = math.degrees(self.pe_body.angle)
        self.shape_element.draw()
        