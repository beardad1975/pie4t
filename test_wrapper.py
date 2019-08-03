import unittest

import pie4t

from math import radians, degrees


class TestWrapperClass(unittest.TestCase):
    def setUp(self):
        self.stage = pie4t.Engine()
        self.box = self.stage.add_box()

    def test_set_and_get_mass(self):
        m = 500
        self.box.mass = m
        self.assertEqual(m, self.box.body.mass)
        self.assertEqual(self.box.mass, m)

    def test_set_and_get_質量(self):
        m = 500
        self.box.質量 = m
        self.assertEqual(m, self.box.body.mass)
        self.assertEqual(self.box.質量, m)        

    def test_set_and_get_moment(self):
        mo = 1699
        self.box.moment = mo
        self.assertEqual(mo, self.box.body.moment)
        self.assertEqual(self.box.moment, mo)

    def test_set_and_get_轉動慣量(self):
        mo = 1699
        self.box.轉動慣量 = mo
        self.assertEqual(mo, self.box.body.moment)
        self.assertEqual(self.box.轉動慣量, mo)


    def test_set_and_get_position(self):
        pos = (10, 20)
        self.box.position = pos
        self.assertEqual(pos, self.box.body.position)
        self.assertEqual(self.box.position, pos)

    def test_set_and_get_位置(self):
        pos = (10, 20)
        self.box.位置 = pos
        self.assertEqual(pos, self.box.body.position)
        self.assertEqual(self.box.位置, pos)

    def test_set_and_get_position_x(self):
        x  = 700
        self.box.position_x = x
        self.assertEqual(self.box.body.position.x , x)
        self.assertEqual(self.box.position_x, x)

    def test_set_and_get_位置x(self):
        x  = -100
        self.box.位置x = x
        self.assertEqual(self.box.body.position.x , x)
        self.assertEqual(self.box.位置x, x)

    def test_set_and_get_position_y(self):
        y  = 700
        self.box.position_y = y
        self.assertEqual(self.box.body.position.y , y)
        self.assertEqual(self.box.position_y, y)

    def test_set_and_get_位置y(self):
        y  = -100
        self.box.位置y = y
        self.assertEqual(self.box.body.position.y , y)
        self.assertEqual(self.box.位置y, y)


    def test_set_and_get_velocity(self):
        v = (10, -200)
        self.box.velocity = v
        self.assertEqual(v, self.box.body.velocity)
        self.assertEqual(self.box.velocity, v)

    def test_set_and_get_速度(self):
        v = (10, -200)
        self.box.速度 = v
        self.assertEqual(v, self.box.body.velocity)
        self.assertEqual(self.box.速度, v)

    def test_set_and_get_velocity_x(self):
        velocity_x = 100
        self.box.velocity_x = velocity_x
        self.assertEqual(self.box.body.velocity.x, velocity_x)
        self.assertEqual(self.box.velocity_x, velocity_x)

    def test_set_and_get_速度x(self):
        velocity_x = 100
        self.box.速度x = velocity_x
        self.assertEqual(self.box.body.velocity.x, velocity_x)
        self.assertEqual(self.box.速度x, velocity_x)

    def test_set_and_get_velocity_y(self):
        velocity_y = 190
        self.box.velocity_y = velocity_y
        self.assertEqual(self.box.body.velocity.y, velocity_y)
        self.assertEqual(self.box.velocity_y, velocity_y)

    def test_set_and_get_速度y(self):
        velocity_y = -100
        self.box.速度y = velocity_y
        self.assertEqual(self.box.body.velocity.y, velocity_y)
        self.assertEqual(self.box.速度y, velocity_y)

    def test_set_and_get_force(self):
        f = (10, -200)
        self.box.force = f
        self.assertEqual(f, self.box.body.force)
        self.assertEqual(self.box.force, f)

    # def test_set_and_get_施力(self):
    #     f = (10, -200)
    #     self.box.施力 = f
    #     self.assertEqual(f, self.box.body.force)
    #     self.assertEqual(self.box.施力, f)

    # def test_set_and_get_force_x(self):
    #     f_x = 1999
    #     self.box.force_x = f_x
    #     self.assertEqual(self.box.force.x, f_x)
    #     self.assertEqual(self.box.force_x, f_x)

    def test_set_and_get_angle(self):
        d = 180
        self.box.angle = d
        self.assertEqual( radians(d), self.box.body.angle)
        self.assertEqual(self.box.angle, d)

    def test_set_and_get_角度(self):
        d = 180
        self.box.角度 = d
        self.assertEqual( radians(d), self.box.body.angle)
        self.assertEqual(self.box.角度, d)

    def test_set_and_get_angular_velocity_degree(self):
        av = 90
        self.box.angular_velocity_degree = av
        self.assertEqual( radians(av), self.box.body.angular_velocity)
        self.assertEqual(self.box.angular_velocity_degree, av)

    def test_set_and_get_角速度(self):
        av = 90
        self.box.角速度 = av
        self.assertEqual( radians(av), self.box.body.angular_velocity)
        self.assertEqual(self.box.角速度, av)

    def test_set_and_get_torque(self):
        t = 90
        self.box.torque = t
        self.assertEqual( t, self.box.body.torque)
        self.assertEqual(self.box.torque, t)

    def test_set_and_get_力矩(self):
        t = 90
        self.box.力矩 = t
        self.assertEqual( t, self.box.body.torque)
        self.assertEqual(self.box.力矩, t)

    # def test_set_and_get_density(self):
    #     d = 90
    #     self.box.density = d
    #     self.assertEqual( d, self.box.shape.density)
    #     self.assertEqual(self.box.density, d)

    # def test_set_and_get_密度(self):
    #     d = 90
    #     self.box.密度 = d
    #     self.assertEqual( d, self.box.shape.density)
    #     self.assertEqual(self.box.密度, d)

    def test_set_and_get_elasticity(self):
        e = 0.9
        self.box.elasticity = e
        self.assertEqual( e, self.box.shape.elasticity)
        self.assertEqual(self.box.elasticity, e)

    def test_set_and_get_彈性(self):
        e = 0.9
        self.box.彈性 = e
        self.assertEqual( e, self.box.shape.elasticity)
        self.assertEqual(self.box.彈性, e)

    def test_set_and_get_friction(self):
        f = 0.9
        self.box.friction = f
        self.assertEqual( f, self.box.shape.friction)
        self.assertEqual(self.box.friction, f)

    def test_set_and_get_摩擦(self):
        f = 0.9
        self.box.摩擦 = f
        self.assertEqual( f, self.box.shape.friction)
        self.assertEqual(self.box.摩擦, f)

    def test_set_and_get_color(self):
        c = (128, 128, 255, 255) 
        self.box.color = c
        self.assertEqual( c, self.box.shape.color)
        self.assertEqual(self.box.color, c)

    def test_set_and_get_顏色(self):
        c = (128, 128, 255, 255) 
        self.box.顏色 = c
        self.assertEqual( c, self.box.shape.color)
        self.assertEqual(self.box.顏色, c)

    def test_get_area(self):
        box2 = self.stage.add_box(width=5, height=10)
        self.assertEqual(box2.area, 5*10)


if __name__ == '__main__':
    unittest.main()