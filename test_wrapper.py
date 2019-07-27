import unittest

import pie4t



class TestWrapperClass(unittest.TestCase):
    def setUp(self):
        self.engine = pie4t.Engine()
        self.box = self.engine.add_box()

    def test_mass(self):
        m = 500
        self.box.mass = m
        self.assertEqual(self.box.body.mass, m)
