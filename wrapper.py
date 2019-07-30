import math


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

    @property
    def 位置(self):
        return self.body.position

    @位置.setter
    def 位置(self, p):
        self.body.position = p

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
    def force(self):
        return self.body.force

    @force.setter
    def force(self, f):
        self.body.force = f

    @property
    def 力(self):
        return self.body.force

    @力.setter
    def 力(self, f):
        self.body.force = f

    @property
    def degree(self):
        return math.degrees(self.body.angle)

    @degree.setter
    def degree(self, d):
        self.body.angle = math.radians(d)

    @property
    def 角度(self):
        return math.degrees(self.body.angle)

    @角度.setter
    def 角度(self, d):
        self.body.angle = math.radians(d)

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


    #@property
    #def density(self):
    #    return self.shape.density

    #@density.setter
    #def density(self, d):
    #    self.shape.density = d

    #@property
    #def 密度(self):
    #    return self.shape.density

    #@密度.setter
    #def 密度(self, d):
    #    self.shape.density = d

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
