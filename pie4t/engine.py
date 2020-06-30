from inspect import signature
import sys

import arcade
import pymunk
import pyperclip
import pyglet

from . import common
from .repl import Repl
from .circle import Circle
from .line import StaticLine

import __main__

class PhysicsEngine(arcade.Window, Repl):
    
    def __init__(self, width=common.WIDTH, 
                       height=common.HEIGHT, 
                       title=common.TITLE):
        # check module level default physics engine
        
        common.stage = self
        common.物理舞台 = self        
        common.is_engine_created = True
        __main__.stage = self
        __main__.物理舞台 = self



        self.win_width = width
        self.win_height = height

        __main__.中央座標 = (width//2, height//2)

        self.title = title
        self.set_update_rate(common.UPDATE_DT)
        self.circle_list = []
        self.line_list = []
        self.is_engine_running = False

        # status line
        self.font =  ('C:/Windows/Fonts/msjh.ttc','arial')
        self.status_x = 0
        self.status_y = 0

        # pymunk space
        self.space = pymunk.Space()
        self.space.gravity = common.GRAVITY
        self.sleep_time_threshold = 1
        

        # custom event handler ref
        self.user_mouse_press_handler = lambda x, y, button, modifiers: print('default mouse press')

        print(f"建立物理舞台(寬{self.win_width}x高{self.win_height})")

    def lazy_setup(self):
        super().__init__(self.win_width, self.win_height, self.title)

        print('do engine lazy setup')
        for i in self.circle_list:
            i.lazy_setup()
        
        for i in self.line_list:
            i.lazy_setup()



    def setup_wall_around(self):
        thick = 10
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
        self.collect_user_event_handlers()
        self.start_repl()

        

        self.is_engine_running = True
        arcade.run()    


    def collect_user_event_handlers(self):
        if hasattr(__main__, 'on_mouse_press'):
            # check number of parameters
            sig = signature(__main__.on_mouse_press)
            if len(sig.parameters) == 4:
                 # parameters: x, y, button, modifiers
                self.user_mouse_press_handler = __main__.on_mouse_ress
                print( 'handler registed: on_mouse_press' )
            else:
                print('handler error: on_mouse_press needs  4 parameters')
                sys.exit()

        if hasattr(__main__, '按下滑鼠時'):
            # check number of parameters
            sig = signature(__main__.按下滑鼠時)
            if len(sig.parameters) == 2:
                 # parameters: x, y, button, modifiers
                self.user_mouse_press_handler = __main__.按下滑鼠時
                print( '登錄處理函式：按下滑鼠時' )
            else:
                print('處理函式錯誤: 按下滑鼠時 需要2個參數')
                sys.exit()


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
        # physics engine 
        self.space.step(common.QUARTER_DT)
        self.space.step(common.QUARTER_DT)
        self.space.step(common.QUARTER_DT)
        self.space.step(common.QUARTER_DT)
    
    def on_key_press(self, symbol, mod):
        if symbol == arcade.key.ESCAPE:
            self.close()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_RIGHT:
            cor_text = f'({self.status_x},{self.status_y})'
            pyperclip.copy(cor_text)
            print('複製座標 '+ cor_text)
        elif button == arcade.MOUSE_BUTTON_LEFT:
            # call user define handler
            self.user_mouse_press_handler(x, y)
        

        
        

    def on_mouse_motion(self, x, y, dx, dy):
        
        self.status_x = x
        self.status_y = y



    ### add object

    def add_line(self, a, b, thickness=3):
        line = StaticLine(a,b,thickness)
        self.line_list.append(line)

    def 新增圓球(self, *args, **kwargs):
        c = Circle(*args, **kwargs)
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

