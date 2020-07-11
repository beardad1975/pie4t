from inspect import signature
import sys, time

import arcade
import pymunk
import pyperclip
import pyglet

from . import common
from .common import COLLITYPE_DEFAULT, COLLITYPE_HOLE 

from .repl import Repl
from .circle import Circle
from .segment import Segment
from .assist import DotMark

import __main__

class PhysicsEngine(arcade.Window, Repl):
    
    def __init__(self, 寬=common.WIDTH, 
                       高=common.HEIGHT, 
                       title=common.TITLE):
        # check module level default physics engine
        
        common.stage = self
        common.物理舞台 = self        
        common.is_engine_created = True
        __main__.stage = self
        __main__.物理舞台 = self

        

        self.win_width = 寬 if 寬 > common.MIN_WIDTH else common.MIN_WIDTH
        self.win_height = 高 if 高 > common.MIN_HEIGHT else common.MIN_HEIGHT

        print('stage size: ', self.win_width, self.win_height)
        __main__.中央座標 = (self.win_width, self.win_height//2)

        self.title = title
        self.set_update_rate(common.DT_UPDATE)
        self.circle_list = []
        self.segment_list = []
        self.is_engine_running = False

        # status line
        self.font =  ('C:/Windows/Fonts/msjh.ttc','arial')
        self.status_x = 0
        self.status_y = 0

        # pymunk space
        self.space = pymunk.Space()
        self.space.gravity = common.GRAVITY
        self.sleep_time_threshold = 1
        
        # info 
        # self.info = {}
        # self.info['gravity_x'] = 0
        # self.info['gravity_y'] = 0 
        # self.info['mouse_x'] = 0
        # self.info['mouse_y'] = 0
        # self.info['obj_num'] = 0
        # self.info_text = ''
        #self.info_update()

        # infomation update (can't to fast because text create burden)
        #arcade.schedule(self.info_update, 0.4)


        # assist
        self.dot_mark = DotMark()

        hole_handler = self.space.add_collision_handler(COLLITYPE_DEFAULT,
                COLLITYPE_HOLE)



        hole_handler.begin = self.hole_begin_callback
        hole_handler.pre_solve = self.hole_pre_solve_callback
        hole_handler.post_solve = self.hole_post_solve_callback
        hole_handler.separate = self.hole_separate_callback




        # custom event handler ref
        self.user_mouse_press_handler = lambda x, y: print('default mouse press')

        print(f"建立物理舞台(寬{self.win_width}x高{self.win_height})")

    # def info_update(self, dt=0):
    #     self.info['gravity_x'] = int(self.space.gravity.x)
    #     self.info['gravity_y'] = int(self.space.gravity.y) 
    #     self.info['obj_num'] = self.object_num

    #     gx = self.info['gravity_x']
    #     gy = self.info['gravity_y']
    #     mx = self.info['mouse_x']
    #     my = self.info['mouse_y']
    #     obj_num = self.info['obj_num']
    #     self.info_text = f'重力[{gx},{gy}] 滑鼠[{mx},{my}] 物體數:{obj_num} ' 
    #     print(self.info_text)      


    def hole_begin_callback(self, arbiter, space, data):
        #print('begin res ', arbiter.restitution)

        #print('begin ', end='')
        #shape, _ = arbiter.shapes
        #self.移除(shape.obj)
        #return False
        return True

    def hole_pre_solve_callback(self, arbiter, space, data):
        #arbiter.restitution = 1
        print('pre solve sur v ', arbiter.surface_velocity)
        #print('begin friction', arbiter.is_first_contact)
        #arbiter.friction = 0
        #print('pre_solve ', end='')

        #return False
        return True

    def hole_post_solve_callback(self, arbiter, space, data):
        #print('post_solve ', end='')
        #return True
        pass

    def hole_separate_callback(self, arbiter, space, data):
        #print('separate removal ', arbiter.is_removal)
        #return True
        pass

    def lazy_setup(self):
        super().__init__(self.win_width, self.win_height, self.title)

        #print('do engine lazy setup')
        for i in self.circle_list:
            i.lazy_setup()
        
        for i in self.segment_list:
            i.lazy_setup()

        # assist 
        self.dot_mark.lazy_setup()



    def setup_pinball_layout(self):
        
        self.add_segment((488,696),(473,754), 3)
        self.add_segment((473,754), (437,775), 3)
        self.add_segment((437,775), (390,790), 3)

        self.add_segment((426,30),(426,660),3)

        # 隔板
        for i in range(6):
            self.add_segment((60+i*60,120),(60+i*60,220),3)

        

        
        self.add_segment((11,70),(358,47),3)
        # self.add_line()

        # self.add_line()

        # self.add_line()

        # self.add_line()

        # self.add_line()


    def setup_wall_around(self):
        thick = 10
        #self.新增線段( (thick,25), (self.win_width-thick,25), thick)
        self.add_segment( (thick,self.win_height-thick), (self.win_width-thick,self.win_height-thick),thick)
        self.add_segment( (thick,25), (thick,self.win_height-thick),thick)
        self.add_segment( (self.win_width-thick,25), (self.win_width-thick,self.win_height-thick),thick)

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
        #self.setup_pinball_layout()
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
            
        for li in self.segment_list:
            #print('line: ', li.shape_element.center_x, li.shape_element.center_y)
            li.draw()


        # draw assist
        self.dot_mark.draw()

        # draw status line
        #gx = int(self.space.gravity.x)
        #gy = int(self.space.gravity.y)


        #arcade.draw_text(self.info_text, 0, 0, 
        #                    arcade.csscolor.WHITE, 14, font_name=self.font)
    
    def on_update(self, dt):
        # physics engine 
        #print('dt:', dt)
        for i in range(common.DT_SPLIT_NUM):
            self.space.step(common.DT_SPLIT)


        # step_dt = 1/200.
        # x = 0
        # while x < dt:
            
        #     x += step_dt
        #     self.space.step(step_dt)


    def on_key_press(self, symbol, mod):
        if symbol == arcade.key.ESCAPE:
            self.close()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_RIGHT:
            #mx = self.info['mouse_x']
            #my = self.info['mouse_y']
            cor_text = f'[{x},{y}]'
            pyperclip.copy(cor_text)
            print('複製座標 '+ cor_text)            
                      
            self.dot_mark.update_pos(x, y)
            
        elif button == arcade.MOUSE_BUTTON_LEFT:
            # call user define handlers
            self.user_mouse_press_handler(x, y)
        

        
        

    def on_mouse_motion(self, x, y, dx, dy):
        
        #self.info['mouse_x'] = x
        #self.info['mouse_y'] = y
        pass



    ### add object

    def add_segment(self,*args, **kwargs):
        s = Segment(*args, **kwargs)
        self.segment_list.append(s)
        return s

    新增線段 = add_segment


    def 新增圓球(self, *args, **kwargs):
        c = Circle(*args, **kwargs)
        self.circle_list.append(c)
        return c

    def 移除(self, obj):
        # remove shape and body from space
        self.space.remove(obj.phy_shape)
        self.space.remove(obj.phy_body)
        if isinstance(obj, Circle):
            self.circle_list.remove(obj)
            del obj.dynamic_shape_element
            del obj.kinematic_shape_element
            
        del obj.phy_shape
        del obj.phy_body
        del obj


    ### property
    @property
    def gravity(self):
        return self.space.gravity

    @gravity.setter
    def gravity(self, value):
        self.space.gravity = value 

    @property
    def 重力(self):
        return self.space.gravity

    @重力.setter
    def 重力(self, value):
        self.space.gravity = value 

    @property
    def object_num(self):
        num = len(self.circle_list) 
        return num

    @property
    def 物體數量(self):
        num = len(self.circle_list) 
        return num

  