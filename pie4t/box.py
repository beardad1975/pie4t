import random
import math

import pymunk
from pymunk.vec2d import Vec2d
import arcade

from . import common
from .common import SHAPE_COLORS
from .physics_common import PhysicsCommon

class Box(PhysicsCommon):
    def __init__(self, 寬=None, 高=None):
        # pymunk part
        #self.density = 1
        self.lazy_setup_done = False
        self.type_ = '方塊'

        self.phy_body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        self.phy_body.velocity_func = self.limit_velocity
        self.phy_body.position_func = self.limit_position
      

        if 寬 is not None :
            self.box_width = round(max(寬, 4),0)
        else:
            self.box_width = random.randrange(common.BOX_WIDTH_MIN,
                                common.BOX_WIDTH_MAX)

        if 高 is not None :
            self.box_height = round(max(高, 4),0)
        else:
            self.box_height = random.randrange(common.BOX_WIDTH_MIN,
                                common.BOX_WIDTH_MAX)


        self.phy_shape = pymunk.Poly.create_box(self.phy_body, 
                                (self.box_width, self.box_height), radius=0)


        win_width = common.stage.win_width
        win_height = common.stage.win_height
        x = random.randint(int(win_width*0.25), int(win_width*0.75))
        y = random.randint(int(win_height*0.7), int(win_height*0.9))
        self.phy_body.position = x , y

        self.phy_shape.density = common.DENSITY
        self.phy_shape.friction = common.BOX_FRICTION
        self.phy_shape.elasticity = common.BOX_ELASTICITY
        # keep referene to self in shape. For delete
        self.phy_shape.obj = self
        self.phy_shape.filter = pymunk.ShapeFilter(categories=common.CATE_BOX)

        common.stage.space.add(self.phy_body, self.phy_shape)
        
        if common.stage.is_engine_running:
            self.lazy_setup()
            self.lazy_setup_done = True


    def lazy_setup(self):
        ### arcade part
        if not self.lazy_setup_done:
            #print('do circle lazy setup')
            self.box_color = random.choice(SHAPE_COLORS)

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
            
            s = arcade.create_rectangle_filled(0, 0, self.box_width, self.box_height,
                                        self.box_color)
            self.dynamic_shape_element.append(s)

            r = self.box_color[0]+50
            r = r if r <=255 else 255
            g = self.box_color[1]+50
            g = g if g <=255 else 255
            b = self.box_color[2]+50
            b = b if b <=255 else 255

            border_color = (r, g, b)

            s = arcade.create_rectangle(0, 0, self.box_width, self.box_height,
                                        border_color, 3, filled=False)
            self.dynamic_shape_element.append(s)
            
            s = arcade.create_rectangle_filled(int(self.box_width*0.35), 0, 
                    3, int(self.box_height*0.8),
                                        border_color)
            self.dynamic_shape_element.append(s)
            
            

    def make_kinematic_shape(self):
            # dynamic  circle

            
            s = arcade.create_rectangle_filled(0, 0, self.box_width, self.box_height,
                                        arcade.color.GRAY)
            self.kinematic_shape_element.append(s)

            s = arcade.create_rectangle(0, 0, self.box_width, self.box_height,
                                        arcade.color.LAVENDER_GRAY, 3, filled=False)
            self.kinematic_shape_element.append(s)
            
            s = arcade.create_rectangle_filled(int(self.box_width*0.35), 0, 
                    3, int(self.box_height*0.8),
                                        arcade.color.LAVENDER_GRAY)
            self.kinematic_shape_element.append(s)

            
    def __repr__(self):
        # l = round(self.box_length, 1)
        # w = round(self.box_width, 1)
        # d = round(self.phy_shape.density, 1)
        # m = round(self.phy_shape.mass, 1)
        # f = self.phy_shape.friction
        # e = self.phy_shape.elasticity

        # return f'方塊 <長{l},寬{w},密度{d},質量{m},摩擦{f},彈性{e}>'

        t = self.type_
        w = self.box_width
        h = self.box_height
        a = self.phy_shape.area
        d = self.phy_shape.density
        m = self.phy_shape.mass
        f = self.phy_shape.friction
        e = self.phy_shape.elasticity
        x = self.phy_body.position.x
        y = self.phy_body.position.y

        return f'[{t}]寬{w:.0f}, 高{h:.0f}, 面積{a:.0f}, 密度{d:.2f}, 質量{m:.1f},\n' \
               f'     摩擦{f:.1f}, 彈性{e:.1f}, x座標{x:.0f}, y座標{y:.0f}\n'



    def draw(self):
        self.current_shape_element.center_x = self.phy_body.position.x
        self.current_shape_element.center_y = self.phy_body.position.y
        self.current_shape_element.angle = math.degrees(self.phy_body.angle)
        self.current_shape_element.draw()




