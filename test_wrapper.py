import unittest

import pie4t

from math import radians, degrees


class TestWrapperClass(unittest.TestCase):
    def setUp(self):
        self.engine = pie4t.Engine()
        self.box = self.engine.add_box()

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

    def test_set_and_get_force(self):
        f = (10, -200)
        self.box.force = f
        self.assertEqual(f, self.box.body.force)
        self.assertEqual(self.box.force, f)

    def test_set_and_get_力(self):
        f = (10, -200)
        self.box.力 = f
        self.assertEqual(f, self.box.body.force)
        self.assertEqual(self.box.力, f)

    def test_set_and_get_degree(self):
        d = 180
        self.box.degree = d
        self.assertEqual( radians(d), self.box.body.angle)
        self.assertEqual(self.box.degree, d)

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

    def test_set_and_get_density(self):
        d = 90
        self.box.density = d
        self.assertEqual( d, self.box.shape.density)
        self.assertEqual(self.box.density, d)


if __name__ == '__main__':
    unittest.main()