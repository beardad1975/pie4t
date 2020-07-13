import random
import math

import pymunk
from pymunk.vec2d import Vec2d
import arcade

from . import common


class PhysicsCommon:
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

    def 施加力量(self, force):
        #self.phy_body.apply_force_at_world_point(force, (0,0))
        self.phy_body.force += force

    def 施加衝力(self, impulse):
        #self.phy_body.apply_impulse_at_world_point(impulse, (0,0))
        self.phy_body.velocity += impulse

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



