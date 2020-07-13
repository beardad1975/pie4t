from inspect import signature
import sys, time, json, os

import arcade
import pymunk
import pyperclip
import pyglet

from . import common
from .common import COLLITYPE_DEFAULT, COLLITYPE_HOLE 

from .repl import Repl
from .circle import Circle
from .box import Box
from .segment import Segment
from .assist import (DotMark, SegmentAddAssist, ArrowAssist,
                        SegmentRemoveAssist, CoordinateAssist,  )

import __main__

class PhysicsEngine(arcade.Window, Repl):
    
    def __init__(self, 寬=common.WIDTH, 
                       高=common.HEIGHT, 
                       title=common.TITLE):
        # check module level default physics engine
        
        common.stage = self
        common.舞台 = self        
        common.is_engine_created = True
        __main__.stage = self
        __main__.舞台 = self
        __main__.key = arcade.key

        self.pause_simulate = False 
        self.slow_simulate = False

        self.win_width = 寬 if 寬 > common.MIN_WIDTH else common.MIN_WIDTH
        self.win_height = 高 if 高 > common.MIN_HEIGHT else common.MIN_HEIGHT

        #print('stage size: ', self.win_width, self.win_height)
        __main__.中央座標 = (self.win_width, self.win_height//2)

        self.title = title
        self.set_update_rate(common.DT_UPDATE)
        self.circle_list = []
        self.poly_list = []
        self.segment_list = []
        self.is_engine_running = False

        

        # status line
        self.font =  ('C:/Windows/Fonts/msjh.ttc','arial')

        self.terrain_filename = __main__.__file__ + '.地形'

        # retain mouse postion while mouse motion event
        self.mouse_x = 0
        self.mouse_y = 0

        # pymunk space
        self.space = pymunk.Space()
        self.space.gravity = common.GRAVITY
        self.sleep_time_threshold = 1
        
        self.obj_filter = pymunk.ShapeFilter(
                    mask=common.CATE_CIRCLE | common.CATE_BOX)

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
        self.seg_add_assist = SegmentAddAssist()
        self.seg_remove_assist = SegmentRemoveAssist()
        self.arrow_assist = ArrowAssist()
        self.coor_assist = CoordinateAssist()

        hole_handler = self.space.add_collision_handler(COLLITYPE_DEFAULT,
                COLLITYPE_HOLE)



        hole_handler.begin = self.hole_begin_callback
        hole_handler.pre_solve = self.hole_pre_solve_callback
        hole_handler.post_solve = self.hole_post_solve_callback
        hole_handler.separate = self.hole_separate_callback




        # custom event handler 
        self.user_mouse_press_handler = None
        self.user_mouse_release_handler = None
        self.user_key_press_handler = None
        self.user_key_release_handler = None
        self.user_arrow_launch_handler = None
        self.user_mouse_drag_handler = None
        self.user_object_click_handler = None
        # self.user_mouse_press_handler = lambda x, y :  None
        # self.user_mouse_release_handler = lambda x, y: None
        # self.user_key_press_handler = lambda key: None
        # self.user_key_release_handler = lambda key: None
        # self.user_arrow_launch_handler = lambda vector,start_pos :  None

        print(f"建立舞台(寬{self.win_width}x高{self.win_height})")

        if not self.load_terrain():
            #default terrain
            self.新增線段((50, 50),(self.win_width-50, 50),6)
            print('使用預設地形')

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

        for i in self.poly_list:
            i.lazy_setup()

        for i in self.segment_list:
            i.lazy_setup()

        # assist 
        self.dot_mark.lazy_setup()
        self.coor_assist.lazy_setup()
        



    # def setup_pinball_layout(self):
        
    #     self.add_segment((488,696),(473,754), 3)
    #     self.add_segment((473,754), (437,775), 3)
    #     self.add_segment((437,775), (390,790), 3)

    #     self.add_segment((426,30),(426,660),3)

    #     # 隔板
    #     for i in range(6):
    #         self.add_segment((60+i*60,120),(60+i*60,220),3)

        

        
    #     self.add_segment((11,70),(358,47),3)
        # self.add_line()

        # self.add_line()

        # self.add_line()

        # self.add_line()

        # self.add_line()


    # def setup_wall_around(self):
    #     thick = 10
    #     #self.新增線段( (thick,25), (self.win_width-thick,25), thick)
    #     self.add_segment( (thick,self.win_height-thick), (self.win_width-thick,self.win_height-thick),thick)
    #     self.add_segment( (thick,25), (thick,self.win_height-thick),thick)
    #     self.add_segment( (self.win_width-thick,25), (self.win_width-thick,self.win_height-thick),thick)

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
        #self.setup_wall_around()
        #self.setup_pinball_layout()
        self.lazy_setup()
        self.collect_user_event_handlers()
        self.start_repl()

        

        # try cursor
        #cur = self.get_system_mouse_cursor('crosshair')
        #cur = self.get_system_mouse_cursor('help')
        # set cursor to default
        #cur = self.get_system_mouse_cursor('help')
        self.set_mouse_cursor(None)

        self.is_engine_running = True

        #load terrain file (right after is_engine_running flag)



        arcade.run()    


    def save_terrain(self):
        terrain_list = []
        for s in self.segment_list:
            tmp = [s.a, s.b, s.thickness]
            terrain_list.append(tmp)
            
        
        with open(self.terrain_filename, 'w', encoding='utf-8') as f:
            json.dump(terrain_list, f)
            
        #print('save terrain')


    def load_terrain(self):
        try:
            with open(self.terrain_filename, 'r', encoding='utf-8') as f:
                terrain_list = json.load(f)
        except FileNotFoundError:
            #print('找不到地形檔')
            return False
            
        else:
            self.segment_list = []
            for item in terrain_list:
                self.新增線段(item[0], item[1], item[2])
            print('地形載入完成')
            return True

    載入地形 = load_terrain

    def collect_user_event_handlers(self):
        # if hasattr(__main__, 'on_mouse_press'):
        #     # check number of parameters
        #     sig = signature(__main__.on_mouse_press)
        #     if len(sig.parameters) == 4:
        #          # parameters: x, y, button, modifiers
        #         self.user_mouse_press_handler = __main__.on_mouse_ress
        #         print( 'handler registed: on_mouse_press' )
        #     else:
        #         print('handler error: on_mouse_press needs  4 parameters')
        #         sys.exit()

        if hasattr(__main__, '按下滑鼠時'):
            # check number of parameters
            sig = signature(__main__.按下滑鼠時)
            if len(sig.parameters) == 2:
                 # parameters: x, y, button, modifiers
                self.user_mouse_press_handler = __main__.按下滑鼠時
                print( '登錄事件函式：按下滑鼠時' )
            else:
                print('事件函式錯誤: 按下滑鼠時 需要2個參數')
                sys.exit()

        if hasattr(__main__, '拖曳滑鼠時'):
            # check number of parameters
            sig = signature(__main__.拖曳滑鼠時)
            if len(sig.parameters) == 4:
                 # parameters: x, y, button, modifiers
                self.user_mouse_drag_handler = __main__.拖曳滑鼠時
                print( '登錄事件函式：拖曳滑鼠時' )
            else:
                print('事件函式錯誤: 拖曳滑鼠時 需要4個參數')
                sys.exit()



        if hasattr(__main__, '放開滑鼠時'):
            # check number of parameters
            sig = signature(__main__.放開滑鼠時)
            if len(sig.parameters) == 2:
                 # parameters: x, y, button, modifiers
                self.user_mouse_release_handler = __main__.放開滑鼠時
                print( '登錄事件函式：放開滑鼠時' )
            else:
                print('事件函式錯誤: 放開滑鼠時 需要2個參數')
                sys.exit()

        if hasattr(__main__, '點擊物體時'):
            # check number of parameters
            sig = signature(__main__.點擊物體時)
            if len(sig.parameters) == 3:
                 # parameters: x, y, button, modifiers
                self.user_object_click_handler = __main__.點擊物體時
                print( '登錄事件函式：點擊物體時' )
            else:
                print('事件函式錯誤: 點擊物體時 需要3個參數')
                sys.exit()



        if hasattr(__main__, '按下鍵盤時'):
            # check number of parameters
            sig = signature(__main__.按下鍵盤時)
            if len(sig.parameters) == 1:
                 # parameters: x, y, button, modifiers
                self.user_key_press_handler = __main__.按下鍵盤時
                print( '登錄事件函式：按下鍵盤時' )
            else:
                print('事件函式錯誤: 按下鍵盤時 需要1個參數')
                sys.exit()

        if hasattr(__main__, '放開鍵盤時'):
            # check number of parameters
            sig = signature(__main__.放開鍵盤時)
            if len(sig.parameters) == 1:
                 # parameters: x, y, button, modifiers
                self.user_key_release_handler = __main__.放開鍵盤時
                print( '登錄事件函式：放開鍵盤時' )
            else:
                print('事件函式錯誤: 放開鍵盤時 需要1個參數')
                sys.exit()

        if hasattr(__main__, '箭頭發射時'):
            # check number of parameters
            sig = signature(__main__.箭頭發射時)
            if len(sig.parameters) == 2:
                 # parameters: x, y, button, modifiers
                self.user_arrow_launch_handler = __main__.箭頭發射時
                print( '登錄事件函式：箭頭發射時' )
            else:
                print('事件函式錯誤: 箭頭發射時 需要2個參數')
                sys.exit()

    ### event

    def on_draw(self):
        arcade.start_render()
        
        self.coor_assist.draw()

        for b in self.circle_list:
            b.draw()
            
        for p in self.poly_list:
            p.draw()

        for li in self.segment_list:
            #print('line: ', li.shape_element.center_x, li.shape_element.center_y)
            li.draw()


        # draw assist
        self.dot_mark.draw()
        self.seg_add_assist.draw()
        self.seg_remove_assist.draw()
        self.arrow_assist.draw()
        
        # draw status line
        #gx = int(self.space.gravity.x)
        #gy = int(self.space.gravity.y)

        if self.seg_add_assist.enabled:
            arcade.draw_text('新增地形(滑鼠右鍵)', 0, 0, 
                            arcade.csscolor.WHITE, 14, font_name=self.font)
        elif self.seg_remove_assist.enabled:
            arcade.draw_text('移除地形(滑鼠右鍵)', 0, 0, 
                            arcade.csscolor.WHITE, 14, font_name=self.font)
    
    def on_update(self, dt):
        # physics engine 
        #print('dt:', dt)
        if not self.pause_simulate:
            if not self.slow_simulate:
                for i in range(common.DT_SPLIT_NUM):
                    self.space.step(common.DT_SPLIT)
            else: # slow mode
                for i in range(common.DT_SPLIT_NUM // 4):
                    self.space.step(common.DT_SPLIT)


        # step_dt = 1/200.
        # x = 0
        # while x < dt:
            
        #     x += step_dt
        #     self.space.step(step_dt)


    def on_key_press(self, symbol, mod):
        if symbol == arcade.key.ESCAPE:
            self.close()
        elif symbol in (arcade.key.LCTRL, arcade.key.RCTRL):
            self.seg_add_assist.enable()
            #self.seg_remove_assist.disable()
        elif symbol in (arcade.key.LALT, arcade.key.RALT):
            self.seg_remove_assist.enable()
            #self.seg_add_assist.disable()
        elif symbol == arcade.key.TAB :
            self.coor_assist.enable()
        elif not self.模擬暫停 and self.user_key_press_handler :
            self.user_key_press_handler(symbol)

    def on_key_release(self, symbol, mod):
        if symbol in (arcade.key.LCTRL, arcade.key.RCTRL):
            #print('ctrl released')
            self.seg_add_assist.disable()
        elif symbol in (arcade.key.LALT, arcade.key.RALT):
            self.seg_remove_assist.disable()
        elif symbol == arcade.key.TAB :
            self.coor_assist.disable()
        elif not self.模擬暫停 and self.user_key_release_handler:
            self.user_key_release_handler(symbol)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_RIGHT:
            if modifiers & arcade.key.MOD_CTRL:
                if self.seg_add_assist.enabled:
                    self.seg_add_assist.click(x, y)
                
                    #print('click first')
                # else: # do second point
                #     self.seg_add_assist.click_second(x, y)
                #     fx = self.seg_add_assist.first_point_x
                #     fy = self.seg_add_assist.first_point_y
                #     seg_text = "A點 = [{},{}]\nB點 = [{},{}]\n新增線段(A點, B點, 寬=4)\n"
                #     seg_text = seg_text.format(fx,fy, x, y)
                #     pyperclip.copy(seg_text)
                #     print('複製線段程式')
            elif modifiers & arcade.key.MOD_ALT:
                if self.seg_remove_assist.enabled:
                    self.seg_remove_assist.click(x, y)
            else : # no ctrl pressed
                cor_text = f'[{x},{y}]'
                pyperclip.copy(cor_text)
                print('複製座標 '+ cor_text)
                self.dot_mark.update_pos(x, y)   

        elif button == arcade.MOUSE_BUTTON_LEFT and not self.模擬暫停:
            if self.user_mouse_press_handler:
            # call user define handlers
                self.user_mouse_press_handler(x, y)

            if self.user_object_click_handler:
                query = common.stage.space.point_query_nearest((x,y), 0, self.obj_filter)
                if query:
                    self.user_object_click_handler(x, y, query.shape.obj)


    def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            if not self.模擬暫停 and self.user_mouse_drag_handler:
                self.user_mouse_drag_handler(x, y, dx, dy)


    def on_mouse_motion(self, x, y, dx, dy):
        
        # segment assist
        self.mouse_x = x
        self.mouse_y = y

        if self.seg_remove_assist.enabled:
            self.seg_remove_assist.update_hover(x, y)

        # if self.seg_add_assist.enabled:
        #     self.seg_add_assist.update_mouse_pos(x, y)

    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            # check if arrow assist need launch
            if self.arrow_assist.enabled:
                self.arrow_assist.launch()
                vector = self.arrow_assist.vector
                start_pos = self.arrow_assist.start_pos
                print('start_pos: ', start_pos)
                self.user_arrow_launch_handler(vector, start_pos)

            # call user define handlers
            if not self.模擬暫停 and self.user_mouse_release_handler:
                self.user_mouse_release_handler(x, y)
         
                        
                

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

    def 新增方塊(self, *args, **kwargs):
        b = Box(*args, **kwargs)
        self.poly_list.append(b)
        return b

    def 移除(self, obj):

        try:

            if isinstance(obj, Segment):
                self.space.remove(obj.phy_shape)
                self.segment_list.remove(obj)
                del obj.shape_element
                del obj.phy_shape
                del obj.phy_body
                del obj
            else: 
            # remove shape and body from space
                self.space.remove(obj.phy_shape)
                self.space.remove(obj.phy_body)
                if isinstance(obj, Circle):
                    self.circle_list.remove(obj)
                    del obj.dynamic_shape_element
                    del obj.kinematic_shape_element
                
                if isinstance(obj, Box):
                    self.poly_list.remove(obj)
                    del obj.dynamic_shape_element
                    del obj.kinematic_shape_element

                del obj.phy_shape
                del obj.phy_body
                del obj
        except AttributeError:
            print('移除物體不存在')        

    ### assist
    def 箭頭開始(self, *args, **kwargs):
        self.arrow_assist.start(*args, **kwargs)


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
        num = len(self.circle_list) + len(self.poly_list) 
        return num

    @property
    def 物體數量(self):
        num = len(self.circle_list) + len(self.poly_list) 
        return num


    @property
    def 模擬暫停(self):
        return self.pause_simulate

    @模擬暫停.setter
    def 模擬暫停(self, value):
        if value :
            self.pause_simulate = True
        else:
            self.pause_simulate = False 

    @property
    def 慢動作(self):
        return self.slow_simulate

    @慢動作.setter
    def 慢動作(self, value):
        if value:
            self.slow_simulate = True
        else:
            self.slow_simulate = False
  
    # @property
    # def 箭頭開始(self):
    #     return self.arrow_assist.enabled

    # @箭頭開始.setter
    # def 箭頭開始(self, value):
    #     if value:
    #         self.arrow_assist.enabled = True
    #     else:
    #         self.arrow_assist.enabled = False