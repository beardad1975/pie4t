import unittest

import pie4t, pyglet

from math import radians, degrees


class TestPie4tBasic(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()