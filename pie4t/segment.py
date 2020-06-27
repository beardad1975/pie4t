

class StaticLine:
    def __init__(self, a, b):
        # pymunk part
        self.a = a
        self.b = b
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = a
        a_b_delta = (b[0] - a[0], b[1]-a[1])
        self.physics_shape = pymunk.Segment(self.body,(0,0), a_b_delta, 3)
        self.physics_shape.friction = 0.8
        global_space.add(self.physics_shape)
        
        #arcade part
        self.shape_element = arcade.ShapeElementList()
        self.line_shape = arcade.create_line(a[0], a[1], b[0], b[1], arcade.color.YELLOW_ORANGE, 3)

        
    
    def draw(self):
        
        self.line_shape.draw()
        
    