import math
import pymunk

class BodyShapeWrapper:
    def __init__(self, body, shape):
        self.body = body
        self.shape = shape

    @property
    def mass(self):
        return self.body.mass

    @mass.setter
    def mass(self, m):
        self.body.mass = m

    @property
    def 質量(self):
        return self.body.mass

    @質量.setter
    def 質量(self, m):
        self.body.mass = m

    @property
    def moment(self):
        return self.body.moment

    @moment.setter
    def moment(self, mo):
        self.body.moment = mo

    @property
    def 轉動慣量(self):
        return self.body.moment

    @轉動慣量.setter
    def 轉動慣量(self, mo):
        self.body.moment = mo

    @property
    def position(self):
        return self.body.position

    @position.setter
    def position(self, p):
        self.body.position = p
        if self.body.body_type is pymunk.Body.STATIC:
            self.body.space.reindex_static()

    @property
    def 位置(self):
        return self.body.position

    @位置.setter
    def 位置(self, p):
        self.body.position = p
        if self.body.body_type is pymunk.Body.STATIC:
            self.body.space.reindex_static()

    @property
    def position_x(self):
        return self.body.position.x

    @position_x.setter
    def position_x(self, x):
        ori_y = self.body.position.y
        self.body.position = (x, ori_y)
        if self.body.body_type is pymunk.Body.STATIC:
            self.body.space.reindex_static()

    @property
    def 位置x(self):
        return self.body.position.x

    @位置x.setter
    def 位置x(self, x):
        ori_y = self.body.position.y
        self.body.position = (x, ori_y)
        if self.body.body_type is pymunk.Body.STATIC:
            self.body.space.reindex_static()


    @property
    def position_y(self):
        return self.body.position.y

    @position_y.setter
    def position_y(self, y):
        ori_x = self.body.position.x
        self.body.position = (ori_x, y)
        if self.body.body_type is pymunk.Body.STATIC:
            self.body.space.reindex_static()

    @property
    def 位置y(self):
        return self.body.position.y

    @位置y.setter
    def 位置y(self, y):
        ori_x = self.body.position.x
        self.body.position = (ori_x, y)
        if self.body.body_type is pymunk.Body.STATIC:
            self.body.space.reindex_static()

    @property
    def velocity(self):
        return self.body.velocity

    @velocity.setter
    def velocity(self, v):
        self.body.velocity = v

    @property
    def 速度(self):
        return self.body.velocity

    @速度.setter
    def 速度(self, v):
        self.body.velocity = v

    @property
    def velocity_x(self):
        return self.body.velocity.x

    @velocity_x.setter
    def velocity_x(self, vel_x):
        ori_vel_y = self.body.velocity.y
        self.body.velocity = (vel_x, ori_vel_y)

    @property
    def 速度x(self):
        return self.body.velocity.x

    @速度x.setter
    def 速度x(self, vel_x):
        ori_vel_y = self.body.velocity.y
        self.body.velocity = (vel_x, ori_vel_y)

    @property
    def velocity_y(self):
        return self.body.velocity.y

    @velocity_y.setter
    def velocity_y(self, vel_y):
        ori_vel_x = self.body.velocity.x
        self.body.velocity = (ori_vel_x, vel_y)

    @property
    def 速度y(self):
        return self.body.velocity.y

    @速度y.setter
    def 速度y(self, vel_y):
        ori_vel_x = self.body.velocity.x
        self.body.velocity = (ori_vel_x, vel_y)



    @property
    def force(self):
        return self.body.force

    @force.setter
    def force(self, f):
        self.body.force = f

    # @property
    # def 施力(self):
    #     return self.body.force

    # @施力.setter
    # def 施力(self, f):
    #     self.body.force = f

    # @property
    # def force_x(self):
    #     return self.body.force.x

    # @force_x.setter
    # def force_x(self, f_x):
    #     ori_force_y = self.body.force.y
    #     self.body.force = (f_x, ori_force_y)

    # @property
    # def 施力x(self):
    #     return self.body.force.x

    # @施力x.setter
    # def 施力x(self, f_x):
    #     ori_force_y = self.body.force.y
    #     self.body.force = (f_x, ori_force_y)

    # @property
    # def force_y(self):
    #     return self.body.force.y

    # @force_y.setter
    # def force_y(self, f_y):
    #     ori_force_x = self.body.force.x
    #     self.body.force = (ori_force_x, f_y)

    # @property
    # def 施力y(self):
    #     return self.body.force.y

    # @施力y.setter
    # def 施力y(self, f_y):
    #     ori_force_x = self.body.force.x
    #     self.body.force = (ori_force_x, f_y)

    # angle use degree , not radian
    @property
    def angle(self):
        return math.degrees(self.body.angle)

    @angle.setter
    def angle(self, d):
        self.body.angle = math.radians(d)
        if self.body.body_type is pymunk.Body.STATIC:
            self.body.space.reindex_static()

    @property
    def 角度(self):
        return math.degrees(self.body.angle)

    @角度.setter
    def 角度(self, d):
        self.body.angle = math.radians(d)
        if self.body.body_type is pymunk.Body.STATIC:
            self.body.space.reindex_static()

    @property
    def angular_velocity_degree(self):
        return math.degrees(self.body.angular_velocity)

    @angular_velocity_degree.setter
    def angular_velocity_degree(self, av):
        self.body.angular_velocity = math.radians(av)

    @property
    def 角速度(self):
        return math.degrees(self.body.angular_velocity)

    @角速度.setter
    def 角速度(self, av):
        self.body.angular_velocity = math.radians(av)

    @property
    def torque(self):
        return self.body.torque

    @torque.setter
    def torque(self, t):
        self.body.torque = t

    @property
    def 力矩(self):
        return self.body.torque

    @力矩.setter
    def 力矩(self, t):
        self.body.torque = t

    @property
    def area(self):
        return self.shape.area

    @property
    def 面積(self):
        return self.shape.area


    @property
    def elasticity(self):
        return self.shape.elasticity

    @elasticity.setter
    def elasticity(self, e):
        self.shape.elasticity = e

    @property
    def 彈性(self):
        return self.shape.elasticity

    @彈性.setter
    def 彈性(self, e):
        self.shape.elasticity = e

    @property
    def friction(self):
        return self.shape.friction

    @friction.setter
    def friction(self, f):
        self.shape.friction = f

    @property
    def 摩擦(self):
        return self.shape.friction

    @摩擦.setter
    def 摩擦(self, f):
        self.shape.friction = f

    @property
    def color(self):
        return self.shape.color

    @color.setter
    def color(self, c):
        self.shape.color = c

    @property
    def 顏色(self):
        return self.shape.color

    @顏色.setter
    def 顏色(self, c):
        self.shape.color = c

    def apply_impulse(self, imp_x=None, imp_y=None, 衝量x=None, 衝量y=None):
        #print( 衝量x)
        tmp_imp_x = 衝量x if 衝量x is not None else imp_x
        tmp_imp_x = tmp_imp_x if tmp_imp_x is not None else 0
        tmp_imp_y = 衝量y if 衝量y is not None else imp_y
        tmp_imp_y = tmp_imp_y if tmp_imp_y is not None else 0 

        self.body.apply_impulse_at_world_point( (tmp_imp_x, tmp_imp_y,),
                                                self.body.position
                                                )   

    def 施加衝量(self, *args, **kwargs):
        #print(kwargs)
        self.apply_impulse(*args, **kwargs)