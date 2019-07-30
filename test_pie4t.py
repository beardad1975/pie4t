import unittest

import pie4t, pyglet, pymunk
import wrapper

from math import radians, degrees, pi


class TestPie4tInit(unittest.TestCase):
    # def setUp(self):
    #     self.engine = pie4t.Engine()
    #     self.box = self.engine.add_box()

    def test_物理引擎_engine_factory(self):
        stage = pie4t.物理引擎()
        self.assertTrue(isinstance(stage, pie4t.Engine))

    def test_width_and_height_params(self):
        width = 200
        height = 300
        self.engine = pie4t.Engine(width=width, height=height)
        self.assertEqual(self.engine.config.WINDOW_WIDTH, width)
        self.assertEqual(self.engine.config.WINDOW_HEIGHT, height)

    def test_舞台寬_and_舞台高_params(self):
        width = 550
        height = 240
        self.engine = pie4t.Engine(舞台寬=width, 舞台高=height)
        self.assertEqual(self.engine.config.WINDOW_WIDTH, width)
        self.assertEqual(self.engine.config.WINDOW_HEIGHT, height)        

    def test_window_width_and_height(self):
        width = 700
        height = 200        
        self.engine = pie4t.Engine(width=width, height=height)

        def update(dt):
            pyglet.app.exit()

        pyglet.clock.schedule_interval(update, 0.1)
        self.engine.run()

        self.assertEqual(self.engine.window.width, width)
        self.assertEqual(self.engine.window.height, height)

class TestPie4tSetup(unittest.TestCase):
    def setUp(self):
        self.stage = pie4t.Engine()

    def test_get_and_set_gravity(self):
        g = (0, -500)
        self.stage.gravity = g
        self.assertEqual(self.stage.space.gravity, g)
        self.assertEqual(self.stage.gravity, g)

    def test_get_and_set_重力(self):
        g = (0, -500)
        self.stage.重力 = g
        self.assertEqual(self.stage.space.gravity, g)
        self.assertEqual(self.stage.重力, g)

    def test_get_and_set_default_friction(self):
        fr = 0.8
        self.stage.default_friction = fr
        self.assertEqual(self.stage.config.FRICTION, fr)
        self.assertEqual(self.stage.default_friction, fr)

    def test_get_and_set_預設摩擦(self):
        fr = 0.8
        self.stage.預設摩擦 = fr
        self.assertEqual(self.stage.config.FRICTION, fr)
        self.assertEqual(self.stage.預設摩擦, fr)

    def test_get_and_set_default_elasticity(self):
        e = 0.9
        self.stage.default_elasticity = e
        self.assertEqual(self.stage.config.ELASTICITY, e)
        self.assertEqual(self.stage.default_elasticity, e)

    def test_get_and_set_預設彈性(self):
        e = 0.9
        self.stage.預設彈性 = e
        self.assertEqual(self.stage.config.ELASTICITY, e)
        self.assertEqual(self.stage.預設彈性, e)

    def test_get_and_set_default_density(self):
        d = 10
        self.stage.default_density = d
        self.assertEqual(self.stage.config.DENSITY, d)
        self.assertEqual(self.stage.default_density, d)

    def test_get_and_set_預設密度(self):
        d = 10
        self.stage.預設密度 = d
        self.assertEqual(self.stage.config.DENSITY, d)
        self.assertEqual(self.stage.預設密度, d)

class TestPie4tdegree(unittest.TestCase):
    def setUp(self):
        self.stage = pie4t.Engine()

    def test_set_radius(self):
        r = 5
        circle = self.stage.add_circle(radius=r)
        self.assertEqual(circle.shape.area, pi * r * r)

    def test_set_半徑(self):
        r = 9
        circle = self.stage.add_circle(半徑=r)
        self.assertEqual(circle.shape.area, pi * r * r)

    def test_radius_not_bigger_than_0(self):
        with self.assertRaises(pie4t.CircleException):
            self.circle = self.stage.add_circle(radius=0)

        with self.assertRaises(pie4t.CircleException):
            self.circle = self.stage.add_circle(radius=-5)

    def test_半徑_not_bigger_than_0(self):
        with self.assertRaises(pie4t.CircleException):
            self.circle = self.stage.add_circle(半徑=0)

        with self.assertRaises(pie4t.CircleException):
            self.circle = self.stage.add_circle(半徑=-5)

    def test_default_body_type(self):
        circle = self.stage.add_circle()
        self.assertIs(circle.body.body_type, pymunk.Body.DYNAMIC)

    def test_set_static(self):
        circle = self.stage.add_circle(static=False)
        self.assertIs(circle.body.body_type, pymunk.Body.DYNAMIC)

        circle = self.stage.add_circle(static=True)
        self.assertIs(circle.body.body_type, pymunk.Body.STATIC)

    def test_set_固定(self):
        circle = self.stage.add_circle(固定=False)
        self.assertIs(circle.body.body_type, pymunk.Body.DYNAMIC)

        circle = self.stage.add_circle(固定=True)
        self.assertIs(circle.body.body_type, pymunk.Body.STATIC)

    def test_set_kinematic(self):
        circle = self.stage.add_circle(kinematic=False)
        self.assertIs(circle.body.body_type, pymunk.Body.DYNAMIC)

        circle = self.stage.add_circle(kinematic=True)
        self.assertIs(circle.body.body_type, pymunk.Body.KINEMATIC)

    def test_新增圓形(self):
        circle = self.stage.新增圓形()
        self.assertIsInstance(circle.shape, pymunk.Circle)
        self.assertIsInstance(circle, wrapper.BodyShapeWrapper)

class TestPie4tBox(unittest.TestCase):
    def setUp(self):
        self.stage = pie4t.Engine()

    def test_set_size(self):
        width = 3
        height = 7
        box = self.stage.add_box(size=(width, height)) 
        self.assertEqual(box.shape.area, width * height)

    def test_set_大小(self):
        width = 3
        height = 7
        box = self.stage.add_box(大小=(width, height)) 
        self.assertEqual(box.shape.area, width * height)

    def test_size_not_bigger_than_0(self):
        with self.assertRaises(pie4t.BoxException):
            self.stage.add_box(size=[0, 5])

        with self.assertRaises(pie4t.BoxException):
            self.stage.add_box(size=[8, 0])

        with self.assertRaises(pie4t.BoxException):
            self.stage.add_box(size=[-5, 5])

        with self.assertRaises(pie4t.BoxException):
            self.stage.add_box(size=[1, -1])

    def test_大小_not_bigger_than_0(self):
        with self.assertRaises(pie4t.BoxException):
            self.stage.add_box(大小=[0, 5])

        with self.assertRaises(pie4t.BoxException):
            self.stage.add_box(大小=[8, 0])

        with self.assertRaises(pie4t.BoxException):
            self.stage.add_box(大小=[-5, 5])

        with self.assertRaises(pie4t.BoxException):
            self.stage.add_box(大小=[1, -1])

    def test_set_static(self):
        box = self.stage.add_box(static=False)
        self.assertIs(box.body.body_type, pymunk.Body.DYNAMIC)

        box = self.stage.add_box(static=True)
        self.assertIs(box.body.body_type, pymunk.Body.STATIC)

    def test_set_固定(self):
        box = self.stage.add_box(固定=False)
        self.assertIs(box.body.body_type, pymunk.Body.DYNAMIC)

        box = self.stage.add_box(固定=True)
        self.assertIs(box.body.body_type, pymunk.Body.STATIC)

    def test_set_kinematic(self):
        box = self.stage.add_box(kinematic=False)
        self.assertIs(box.body.body_type, pymunk.Body.DYNAMIC)

        box = self.stage.add_box(kinematic=True)
        self.assertIs(box.body.body_type, pymunk.Body.KINEMATIC)

    def test_新增方塊(self):
        box = self.stage.新增方塊()
        self.assertIsInstance(box.shape, pymunk.Poly)
        self.assertIsInstance(box, wrapper.BodyShapeWrapper)

# class TestPie4tEventHandler(unittest.TestCase):
#     def setUp(self):
#         self.stage = pie4t.Engine()

#     def test_on_mouse_press_params_mismatch(self):
#         def on_mouse_press(x,y):
#             pass


#         with self.assertRaises(pie4t.EventException):
#             self.stage.run()

if __name__ == '__main__':
    unittest.main()