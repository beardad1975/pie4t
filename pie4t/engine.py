import arcade
import pymunk
import pyperclip
import pyglet

from . import common
from .repl import Repl
from .circle import Circle
from .line import StaticLine


class PhysicsEngine(arcade.Window, Repl):
    
    def __init__(self, width=common.DEFAULT_WIDTH, 
                       height=common.DEFAULT_HEIGHT, 
                       title=common.DEFAULT_TITLE):
        # check module level default physics engine
        
        common.stage = self
        common.物理舞台 = self        
        common.is_engine_created = True
        import __main__
        __main__.stage = self
        __main__.物理舞台 = self

        self.win_width = width
        self.win_height = height
        self.title = title
        self.set_update_rate(1/60)
        self.circle_list = []
        self.line_list = []
        self.is_engine_running = False

        # status line
        self.font =  ('C:/Windows/Fonts/msjh.ttc','arial')
        self.status_x = 0
        self.status_y = 0

        # pymunk space
        self.space = pymunk.Space()
        self.space.gravity = common.DEFAULT_GRAVITY

        print("建立物理舞台")

    def lazy_setup(self):
        super().__init__(self.win_width, self.win_height, self.title)

        print('do engine lazy setup')
        for i in self.circle_list:
            i.lazy_setup()
        
        for i in self.line_list:
            i.lazy_setup()



    def setup_wall_around(self):
        thick = 8
        self.add_line( (thick,25), (self.win_width-thick,25), thick)
        self.add_line( (thick,self.win_height-thick), (self.win_width-thick,self.win_height-thick),thick)
        self.add_line( (thick,25), (thick,self.win_height-thick),thick)
        self.add_line( (self.win_width-thick,25), (self.win_width-thick,self.win_height-thick),thick)

        # pass
        # line1 = StaticLine((400,200),(100,300))
        # self.line_list.append(line1)
        # line2 = StaticLine((100,50),(50,100))
        # self.line_list.append(line2)
        
        # b = Circle()
        # b.phy_body.position = (300,150)
        # joint = pymunk.PinJoint(b.phy_body, line1.phy_body, (0,0) , (0,0))
        # joint.distance = 150
        # common.stage.space.add(joint)
        # self.circle_list.append(b)
        
        #arcade.schedule(self.add_circle, 2)
        
    def simulate(self):
        self.setup_wall_around()
        self.lazy_setup()
        self.start_repl()

        

        self.is_engine_running = True
        arcade.run()    

    ### event

    def on_draw(self):
        arcade.start_render()
        
        for b in self.circle_list:
            b.draw()
            
        for li in self.line_list:
            #print('line: ', li.shape_element.center_x, li.shape_element.center_y)
            li.draw()

        # draw status line
        gx = int(self.space.gravity.x)
        gy = int(self.space.gravity.y)

        text = f'滑鼠右鍵複製座標  重力({gx},{gy})  ' 
        arcade.draw_text(text, 0, 0, arcade.csscolor.WHITE, 14, font_name=self.font)
    
    def on_update(self, dt):
        self.space.step(dt)
    
    def on_key_press(self, symbol, mod):
        if symbol == arcade.key.ESCAPE:
            self.close()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_RIGHT:
            cor_text = f'({self.status_x},{self.status_y})'
            pyperclip.copy(cor_text)
            print('複製座標 '+ cor_text)

    def on_mouse_motion(self, x, y, dx, dy):
        
        self.status_x = x
        self.status_y = y



    ### add object

    def add_line(self, a, b, thickness=3):
        line = StaticLine(a,b,thickness)
        self.line_list.append(line)

    def add_circle(self):
        c = Circle()
        self.circle_list.append(c)
        return c

    ### property
    @property
    def gravity(self):
        return self.space.gravity

    @gravity.setter
    def gravity(self, g):
        self.space.gravity = g 

    @property
    def 重力(self):
        return self.space.gravity

    @重力.setter
    def 重力(self, g):
        self.space.gravity = g 

    @property
    def object_num(self):
        num = len(self.circle_list) 
        return num

    @property
    def 物件數量(self):
        num = len(self.circle_list) 
        return num