import random
import math

import pymunk
from pymunk.vec2d import Vec2d
import arcade

from . import common
from .common import SHAPE_COLORS
from .physics_common import PhysicsCommon


class Circle(PhysicsCommon):
    def __init__(self, 半徑=None):
        # pymunk part
        #self.density = 1
        self.lazy_setup_done = False
        self.type_ = '圓球'

        self.phy_body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        self.phy_body.velocity_func = self.limit_velocity
        self.phy_body.position_func = self.limit_position
      

        if 半徑 is not None :
            self.radius = round(max(半徑, 4),0)
            
        else:
            self.radius = random.randrange(common.CIRCLE_RADIUS_MIN,
                            common.CIRCLE_RADIUS_MAX)
            

        self.phy_shape = pymunk.Circle(self.phy_body, self.radius)

        # if 位置 is not None:
        #     self.phy_body.position = 位置
        # else:
        #     x = random.randint(120, 380)
        #     self.phy_body.position = x, 550

        win_width = common.stage.win_width
        win_height = common.stage.win_height
        x = random.randint(int(win_width*0.25), int(win_width*0.75))
        y = random.randint(int(win_height*0.7), int(win_height*0.9))
        self.phy_body.position = x , y

        self.phy_shape.density = common.DENSITY
        self.phy_shape.friction = common.FRICTION
        self.phy_shape.elasticity = common.ELASTICITY
        # keep referene to self in shape. For delete
        self.phy_shape.obj = self
        self.phy_shape.filter = pymunk.ShapeFilter(categories=common.CATE_CIRCLE)

        #self.moment = pymunk.moment_for_circle(self.mass, 0, self.radius)
        #self.body = pymunk.Body(self.mass, self.moment)

        #self.physics_shape = pymunk.Circle(self.body, self.radius)
        #self.physics_shape.friction = 0.8
        common.stage.space.add(self.phy_body, self.phy_shape)
        
        if common.stage.is_engine_running:
            self.lazy_setup()
            self.lazy_setup_done = True





    def lazy_setup(self):
        ### arcade part
        if not self.lazy_setup_done:
            #print('do circle lazy setup')
            self.ball_color = random.choice(SHAPE_COLORS)

            #  two shape element for different body type           
            self.dynamic_shape_element = arcade.ShapeElementList()
            self.kinematic_shape_element = arcade.ShapeElementList()  

            self.make_dynamic_shape()
            self.make_kinematic_shape()

            if self.物理反應 :
                self.current_shape_element = self.dynamic_shape_element
            else :
                self.current_shape_element = self.kinematic_shape_element
            
            
    def make_dynamic_shape(self):
            # dynamic  circle

            #s = arcade.create_ellipse_filled(0, 0, self.radius, self.radius, ball_color)
            s = arcade.create_ellipse_filled_with_colors(0, 0, self.radius, self.radius,
                                        self.ball_color, arcade.color.UNMELLOW_YELLOW)
            self.dynamic_shape_element.append(s)
            # dot
            s_radius = int(self.radius * 0.15)
            s = arcade.create_ellipse_filled(self.radius-s_radius*2 , 0, s_radius, s_radius, arcade.color.WHITE)
            self.dynamic_shape_element.append(s)

    def make_kinematic_shape(self):
            # dynamic  circle

            #s = arcade.create_ellipse_filled(0, 0, self.radius, self.radius, ball_color)
            s = arcade.create_ellipse_filled_with_colors(0, 0, self.radius, self.radius,
                                        arcade.color.GRAY, arcade.color.UNMELLOW_YELLOW)
            self.kinematic_shape_element.append(s)
            # dot
            s_radius = int(self.radius * 0.15)
            s = arcade.create_ellipse_filled(self.radius-s_radius*2 , 0, s_radius, s_radius, arcade.color.WHITE)
            self.kinematic_shape_element.append(s)

    def __repr__(self):
        t = self.type_
        r = self.phy_shape.radius
        a = self.phy_shape.area
        d = self.phy_shape.density
        m = self.phy_shape.mass
        f = self.phy_shape.friction
        e = self.phy_shape.elasticity
        x = self.phy_body.position.x
        y = self.phy_body.position.y

        return f'[{t}]半徑{r:.0f}, 面積{a:.1f}, 密度{d:.2f}, 質量{m:.1f},\n' \
               f'     摩擦{f:.1f}, 彈性{e:.1f}, x座標{x:.0f}, y座標{y:.0f}\n'


    def draw(self):
        self.current_shape_element.center_x = self.phy_body.position.x
        self.current_shape_element.center_y = self.phy_body.position.y
        self.current_shape_element.angle = math.degrees(self.phy_body.angle)
        self.current_shape_element.draw()


    ### circle property
    @property
    def 半徑(self):
        return self.phy_shape.radius


