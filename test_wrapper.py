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

    def test_set_and_get_moment(self):
        mo = 1699
        self.box.moment = mo
        self.assertEqual(mo, self.box.body.moment)
        self.assertEqual(self.box.moment, mo)

    def test_set_and_get_position(self):
        pos = (10, 20)
        self.box.position = pos
        self.assertEqual(pos, self.box.body.position)
        self.assertEqual(self.box.position, pos)

    def test_set_and_get_velocity(self):
        v = (10, -200)
        self.box.velocity = v
        self.assertEqual(v, self.box.body.velocity)
        self.assertEqual(self.box.velocity, v)

    def test_set_and_get_force(self):
        f = (10, -200)
        self.box.force = f
        self.assertEqual(f, self.box.body.force)
        self.assertEqual(self.box.force, f)

    def test_set_and_get_degree(self):
        d = 180
        self.box.degree = d
        self.assertEqual( radians(d), self.box.body.angle)
        self.assertEqual(self.box.degree, d)


if __name__ == '__main__':
    unittest.main()