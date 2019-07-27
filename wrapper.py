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
    def position(self):
        return self.body.position

    @position.setter
    def position(self, p):
        self.body.position = p

    @property
    def velocity(self):
        return self.body.velocity

    @velocity.setter
    def velocity(self, v):
        self.body.velocity = v

    @property
    def force(self):
        return self.body.force

    @force.setter
    def force(self, f):
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
    def torque(self):
        return self.body.torque

    @torque.setter
    def torque(self, t):
        self.body.torque = t
