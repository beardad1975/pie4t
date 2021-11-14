import pymunk
import arcade

from . import common


class Segment:
    def __init__(self, a, b, 寬=None):
        self.is_lazy_setup = False



        # pymunk part
        self.a = a
        self.b = b

        if 寬 is not None:
            self.thickness = 寬
        else:
            self.thickness = common.SEG_THICKNESS

        self.phy_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.phy_body.position = a
        a_b_delta = (b[0] - a[0], b[1]-a[1])
        self.phy_shape = pymunk.Segment(self.phy_body,(0,0), a_b_delta, 
                                self.thickness//2)
        self.phy_shape.friction = 1
        self.phy_shape.elasticity = 1
        self.phy_shape.collision_type = common.COLLITYPE_SEGMENT

        self.phy_shape.filter = pymunk.ShapeFilter(categories=common.CATE_SEGMENT)

        self.phy_shape.obj = self

        common.stage.space.add(self.phy_body)
        common.stage.space.add(self.phy_shape)
        
        if common.stage.is_engine_running:
            self.lazy_setup()
            common.stage.is_engine_running = True

    def lazy_setup(self):
        if not self.is_lazy_setup:
            #arcade part
            self.shape_element = arcade.ShapeElementList()
            a = self.a
            b = self.b
            self.line_shape = arcade.create_line(a[0], a[1], b[0], b[1],
                     arcade.color.YELLOW_ORANGE, self.thickness)
            self.is_lazy_setup = True

    def draw(self):
        self.line_shape.draw()
        
    