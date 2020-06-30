import random
import math

import pymunk
import arcade

from . import common

BALL_COLORS = (arcade.color.WINDSOR_TAN,
               arcade.color.VIVID_VIOLET,
               arcade.color.ULTRAMARINE_BLUE,
               arcade.color.TANGELO,
               arcade.color.AO,
               )

class Circle:
    def __init__(self, 半徑=None):
        # pymunk part
        #self.density = 1
        self.is_lazy_setup = False

        self.phy_body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)

        if 半徑 is not None:
            self.radius = 半徑
            self.phy_shape = pymunk.Circle(self.phy_body, self.radius)
        else:
            self.radius = random.randrange(10,30)
            self.phy_shape = pymunk.Circle(self.phy_body, self.radius)

        # if 位置 is not None:
        #     self.phy_body.position = 位置
        # else:
        #     x = random.randint(120, 380)
        #     self.phy_body.position = x, 550
        x = random.randint(120, 380)
        self.phy_body.position = x, 550

        self.phy_shape.density = common.DENSITY
        self.phy_shape.friction = common.FRICTION
        self.phy_shape.elasticity = common.ELASTICITY

        #self.moment = pymunk.moment_for_circle(self.mass, 0, self.radius)
        #self.body = pymunk.Body(self.mass, self.moment)

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

    def __repr__(self):
        r = round(self.phy_shape.radius, 1)
        d = round(self.phy_shape.density, 1)
        m = round(self.phy_shape.mass, 1)
        f = self.phy_shape.friction
        e = self.phy_shape.elasticity

        return f'圓球 <半徑{r},密度{d},質量{m},摩擦{f},彈性{e}>'


    def draw(self):
        self.shape_element.center_x = self.phy_body.position.x
        self.shape_element.center_y = self.phy_body.position.y
        self.shape_element.angle = math.degrees(self.phy_body.angle)
        self.shape_element.draw()

    ### circle property
    @property
    def 半徑(self):
        return self.phy_shape.radius

    ### rigid body property
    @property
    def 質量(self):
        return self.phy_shape.mass

    @質量.setter
    def 質量(self, value):
        if value <= 0:
            print("質量須大於0")
        else:
            self.phy_shape.mass = value 

    @property
    def 密度(self):
        return self.phy_shape.density

    @密度.setter
    def 密度(self, value):
        if value <= 0:
            print("密度須大於0")
        else:
            self.phy_shape.density = value   

    #read only
    @property
    def 半徑(self):
        return self.phy_shape.radius

    @property
    def 位置(self):
        return self.phy_body.position

    @位置.setter
    def 位置(self, value):
        self.phy_body.position = value
    
    @property
    def 摩擦(self):
        return self.phy_shape.friction

    @摩擦.setter
    def 摩擦(self, value):
        if value < 0:
            print("摩擦係數須大於等於0")
        else:
            self.phy_shape.friction = value 

    @property
    def 彈性(self):
        return self.phy_shape.elasticity

    @彈性.setter
    def 彈性(self, value):
        if value < 0 or value > 1:
            print("彈性係數須在0到1之間")
        else:
            self.phy_shape.elasticity = value    

