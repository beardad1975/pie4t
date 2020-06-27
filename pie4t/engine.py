import arcade
import pymunk


from . import common
from .repl import Repl
from .circle import Circle



class PhysicsEngine(arcade.Window, Repl):
    
    def __init__(self, width=common.DEFAULT_WIDTH, 
                       height=common.DEFAULT_HEIGHT, 
                       title=common.DEFAULT_TITLE):
        # check module level default physics engine
        common.stage = self
        common.舞台 = self        
        common.is_engine_created = True

        self.win_width = width
        self.win_height = height
        self.title = title
        self.set_update_rate(1/60)
        self.circle_list = []
        self.segment_list = []
        self.is_engine_running = False

        # pymunk space
        self.space = pymunk.Space()
        self.space.gravity = common.DEFAULT_GRAVITY

    def lazy_setup(self):
        super().__init__(self.win_width, self.win_height, self.title)

        print('do engine lazy setup')
        for i in self.circle_list:
            i.lazy_setup()
        

    @property
    def object_num(self):
        num = len(self.circle_list) + len(self.segment_list)
        return num

    def setup(self):
        pass
        #line1 = StaticLine((400,200),(100,300))
        #self.line_list.append(line1)
        #line2 = StaticLine((100,50),(50,100))
        #self.line_list.append(line2)
        
        #b = Circle()
        #b.body.position = (300,150)
        #joint = pymunk.PinJoint(b.body, line1.body, (0,0) , (0,0))
        #joint.distance = 150
        #global_space.add(joint)
        #self.ball_list.append(b)
        
        #arcade.schedule(self.add_circle, 2)
        
    def simulate(self):
        self.lazy_setup()
        self.start_repl()

        

        self.is_engine_running = True
        arcade.run()    
    
    def on_draw(self):
        arcade.start_render()
        
        for b in self.circle_list:
            b.draw()
            
        for li in self.segment_list:
            #print('line: ', li.shape_element.center_x, li.shape_element.center_y)
            li.draw()
    
    def on_update(self, dt):
        self.space.step(dt)
    
    def on_key_press(self, symbol, mod):
        if symbol == arcade.key.ESCAPE:
            self.close()
            
    def add_circle(self):
        c = Circle()
        self.circle_list.append(c)
        return c