

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
    def torque(self):
        return self.body.torque

    @torque.setter
    def torque(self, t):
        self.body.torque = t
