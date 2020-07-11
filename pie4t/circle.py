import random
import math

import pymunk
from pymunk.vec2d import Vec2d
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
        self.lazy_setup_done = False

        self.phy_body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        self.phy_body.velocity_func = self.limit_velocity
        self.phy_body.position_func = self.limit_position
      

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

        #self.moment = pymunk.moment_for_circle(self.mass, 0, self.radius)
        #self.body = pymunk.Body(self.mass, self.moment)

        #self.physics_shape = pymunk.Circle(self.body, self.radius)
        #self.physics_shape.friction = 0.8
        common.stage.space.add(self.phy_body, self.phy_shape)
        
        if common.stage.is_engine_running:
            self.lazy_setup()
            self.lazy_setup_done = True

    def limit_velocity(self, body, gravity, damping, dt):
        speeding = False
        l = body.velocity.length
        if l > common.VELOCITY_LIMIT:
            #print('found large velocity :', body.velocity)
            scale = common.VELOCITY_LIMIT / l
            body.velocity = body.velocity * scale
            speeding = True
            #print('fix to :', body.velocity)

        if not speeding :
            pymunk.Body.update_velocity(body, gravity, damping, dt)
        else:# speeding , no gravity
            pymunk.Body.update_velocity(body, (0,0), damping, dt)


    def limit_position(self, body, dt):
        # remove below lower bound
        pymunk.Body.update_position(body, dt)
        #print(body.position)
        x = body.position.x
        y = body.position.y
        if y < common.POSITION_Y_MIN :
            #print('exceed y min')
            #body.position = Vec2d(x, common.POSITION_Y_MAX)
            common.stage.移除(self)
            #print('remove: ', self)
        elif y > common.POSITION_Y_MAX:
            #body.position = Vec2d(x, common.POSITION_Y_MIN )
            common.stage.移除(self)
            #print('remove: ', self)
        elif x < common.POSITION_X_MIN :
            #print('exceed y min')
            #body.position = Vec2d(common.POSITION_X_MAX, y )
            common.stage.移除(self)
            #print('remove: ', self)
        elif x > common.POSITION_X_MAX:
            #body.position = Vec2d(common.POSITION_X_MIN, y ) 
            common.stage.移除(self)
            #print('remove: ', self)       

            #print('exceed y max')
            #print(body.position)
            #common.stage.移除(self)
            #print('remove: ', self)


    def lazy_setup(self):
        ### arcade part
        if not self.lazy_setup_done:
            #print('do circle lazy setup')
            self.ball_color = random.choice(BALL_COLORS)

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
        r = round(self.phy_shape.radius, 1)
        d = round(self.phy_shape.density, 1)
        m = round(self.phy_shape.mass, 1)
        f = self.phy_shape.friction
        e = self.phy_shape.elasticity

        return f'圓球 <半徑{r},密度{d},質量{m},摩擦{f},彈性{e}>'


    def draw(self):
        self.current_shape_element.center_x = self.phy_body.position.x
        self.current_shape_element.center_y = self.phy_body.position.y
        self.current_shape_element.angle = math.degrees(self.phy_body.angle)
        self.current_shape_element.draw()


    def 施加力量(self, force):
        self.phy_body.apply_force_at_local_point(force, (0,0))

    def 施加衝量(self, impulse):
        self.phy_body.apply_impulse_at_local_point(impulse, (0,0))


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
    def 速度(self):
        return self.phy_body.velocity

    @速度.setter
    def 速度(self, value):
        self.phy_body.velocity = value

    @property
    def 角度(self):
        return math.degrees(self.phy_body.angle)

    @角度.setter
    def 角度(self, value):
        self.phy_body.angle = math.radians(value)

    @property
    def 角速度(self):
        return math.degrees(self.phy_body.angular_velocity)

    @角速度.setter
    def 角速度(self, value):
        self.phy_body.angular_velocity = math.radians(value)


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

    @property
    def 物理反應(self):
        if self.phy_body.body_type == pymunk.Body.DYNAMIC:
            return True
        elif self.phy_body.body_type == pymunk.Body.KINEMATIC:
            return False

    @物理反應.setter
    def 物理反應(self, g):
        if g is True and self.phy_body.body_type ==  pymunk.Body.KINEMATIC:
            # change type to dynamic
            self.phy_body.body_type = pymunk.Body.DYNAMIC
            if common.stage.is_engine_running:
                self.current_shape_element = self.dynamic_shape_element
        elif  g is False and self.phy_body.body_type ==  pymunk.Body.DYNAMIC:
            # chang type to kinematic
            self.phy_body.body_type = pymunk.Body.KINEMATIC
            if common.stage.is_engine_running:
                self.current_shape_element = self.kinematic_shape_element

