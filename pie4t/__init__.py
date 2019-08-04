import sys
from random import choice, randint, random
from inspect import signature
import math

import pyglet
from pyglet.window import key
import pymunk
import pymunk.pyglet_util

from pie4t.wrapper import BodyShapeWrapper



options = pymunk.pyglet_util.DrawOptions()
toplevel = sys.modules["__main__"]


class Config:
    def __init__(self, width, height):
        # customizable
        self.WINDOW_WIDTH = 640 if width is None else width
        self.WINDOW_HEIGHT = 480 if height is None else height   
        self.FRICTION = 0.5 
        self.ELASTICITY = 0.8
        self.DT = 0.02
        #used internally
        self.DENSITY = 1
        self.GRAVITY = (0, 0)
        self.X = self.WINDOW_WIDTH // 2
        self.Y = self.WINDOW_HEIGHT // 2
        self.SIZE = (40, 40)
        self.SIZE_WIDTH = 20
        self.SIZE_HEIGHT = 20
        self.RANDOM_RADIUS_RANGE = (10,40) 
        self.RANDOM_VELOCITY_RANGE = (-300, 300)
        self.RANDOM_X_RANGE = (int(self.WINDOW_WIDTH*0.4), int(self.WINDOW_WIDTH*0.6))
        self.RANDOM_Y_RANGE = (int(self.WINDOW_HEIGHT*0.4), int(self.WINDOW_HEIGHT*0.6))
        self.RAMDOM_SIZE_RANGE = (10, 60)
        self.WALL_THICKNESS = 10 

        #garbge collect bound
        self.RIGHT_GC_BOUND = self.WINDOW_WIDTH + 1000
        self.LEFT_GC_BOUND = -1000
        self.TOP_GC_BOUND = self.WINDOW_HEIGHT + 1000
        self.BOTTOM_GC_BOUND = -1000    


class Color:
    red = (255,0,0,255)
    orange =  (255,165,0,255)
    yellow = (255,255,0,255)
    green = (0,255,0,255)
    blue = (0,0,255,255)
    cyan = (0,255,255,255)
    purple = (255,0,255,255)
    white = (255,255,255,255)
    black = (0, 0, 0, 0)
    gray = (120, 120, 120, 255) 

    def random(self):
        c = choice(['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple'])
        return getattr(self, c)

color = Color()


class Pie4tBaseException(ValueError): pass
class CircleException(Pie4tBaseException):pass
class BoxException(Pie4tBaseException):pass
class EventException(Pie4tBaseException):pass

class Engine:
    " physics impulse engine with pyglet and pymunk backended"

    def __init__(self, width=None, 舞台寬=None, height=None, 舞台高=None):
        width = 舞台寬 if 舞台寬 is not None else width
        height = 舞台高 if 舞台高 is not None else height
        self.config = Config(width, height)

        self.space = pymunk.Space()
        self.space.gravity = self.config.GRAVITY

        



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
    def gravity_x(self):
        return self.space.gravity.x

    @gravity_x.setter
    def gravity_x(self, g_x):
        ori_g_y = self.space.gravity.y
        self.space.gravity = (g_x, ori_g_y)  

    @property
    def 重力x(self):
        return self.space.gravity.x

    @重力x.setter
    def 重力x(self, g_x):
        ori_g_y = self.space.gravity.y
        self.space.gravity = (g_x, ori_g_y) 

    @property
    def gravity_y(self):
        return self.space.gravity.y

    @gravity_y.setter
    def gravity_y(self, g_y):
        ori_g_x = self.space.gravity.x
        self.space.gravity = (ori_g_x, g_y)  

    @property
    def 重力y(self):
        return self.space.gravity.y

    @重力y.setter
    def 重力y(self, g_y):
        ori_g_x = self.space.gravity.x
        self.space.gravity = (ori_g_x, g_y) 

    @property
    def default_friction(self):
        return self.config.FRICTION

    @default_friction.setter
    def default_friction(self, fr):
        self.config.FRICTION = fr 

    @property
    def 預設摩擦(self):
        return self.config.FRICTION

    @預設摩擦.setter
    def 預設摩擦(self, fr):
        self.config.FRICTION = fr

    @property
    def default_elasticity(self):
        return self.config.ELASTICITY

    @default_elasticity.setter
    def default_elasticity(self, e):
        self.config.ELASTICITY = e 

    @property
    def 預設彈性(self):
        return self.config.ELASTICITY

    @預設彈性.setter
    def 預設彈性(self, e):
        self.config.ELASTICITY = e 

    @property
    def default_density(self):
        return self.config.DENSITY

    @default_density.setter
    def default_density(self, d):
        self.config.DENSITY = d 

    @property
    def 預設密度(self):
        return self.config.DENSITY

    @預設密度.setter
    def 預設密度(self, d):
        self.config.DENSITY = d 

    @property
    def object_num(self):
        return len(self.space.shapes)

    @property
    def 物件數量(self):
        return len(self.space.shapes)
    

    def add_circle(self, position_x=None, position_y=None, 
                radius=None, static=False, kinematic=False,
                density=None, 密度=None,
                位置x=None, 位置y=None, 半徑=None, 
                固定=False, random_flag=False):
        if static or 固定 :
            circle_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        elif kinematic:
            circle_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        else:
            circle_body = pymunk.Body(body_type=pymunk.Body.DYNAMIC) 

        radius = 半徑 if 半徑 is not None else radius
        if radius is not None :
            if radius > 0:
                circle_shape = pymunk.Circle(circle_body, radius)
            else:
                raise CircleException('新增圓形錯誤','半徑值沒有大於0')
        else:
            circle_shape = pymunk.Circle(circle_body, randint(*self.config.RANDOM_RADIUS_RANGE))

        tmp_density = 密度 if 密度 is not None else density
        if tmp_density is None:
            tmp_density = self.config.DENSITY
        circle_shape.density = tmp_density
       
        circle_shape.friction = self.config.FRICTION
        circle_shape.elasticity = self.config.ELASTICITY
        
        circle_shape.color = color.random()

        tmp_x = 位置x if 位置x is not None else position_x
        if not random_flag:
            tmp_x = tmp_x if tmp_x is not None else self.config.X
        else:
            tmp_x = tmp_x if tmp_x is not None else randint(*self.config.RANDOM_X_RANGE)

        tmp_y = 位置y if 位置y is not None else position_y
        if not random_flag:
            tmp_y = tmp_y if tmp_y is not None else self.config.Y
        else:
            tmp_y = tmp_y if tmp_y is not None else randint(*self.config.RANDOM_Y_RANGE)

        circle_body.position = (tmp_x, tmp_y)

        if not random_flag:
            circle_body.velocity = (0, 0)
        else:
            circle_body.velocity = ( randint(*self.config.RANDOM_VELOCITY_RANGE),
                                randint(*self.config.RANDOM_VELOCITY_RANGE) )           

        self.space.add(circle_body, circle_shape)
        return  BodyShapeWrapper(circle_body, circle_shape)

    def 新增圓形(self, *args, **kwargs):
        return self.add_circle(*args, **kwargs)

    def add_random_circle(self, *args, **kwargs):
        kwargs['random_flag'] = True
        return self.add_circle(*args, **kwargs) 

    def 新增隨機圓形(self, *args, **kwargs):
        kwargs['random_flag'] = True
        return self.add_circle(*args, **kwargs) 

    def add_box(self, position_x=None, position_y=None, width=None,
                height=None, static=False, kinematic=False,
                density=None, 密度=None,
                位置x=None, 位置y=None, 寬=None, 高=None, 
                固定=False, random_flag=False):
        """add box in physics stage """

        if static or 固定 :
            box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        elif kinematic:
            box_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        else:
            box_body = pymunk.Body(body_type=pymunk.Body.DYNAMIC) 

        
        tmp_width = 寬 if 寬 is not None else width
        if not random_flag:
            tmp_width = tmp_width if tmp_width is not None else self.config.SIZE_WIDTH
        else:
            tmp_width = tmp_width if tmp_width is not None else randint(*self.config.RAMDOM_SIZE_RANGE)

        if tmp_width <= 0: raise BoxException('新增方塊錯誤','寬(width)要大於0')
        
        tmp_height = 高 if 高 is not None else height
        if not random_flag:
            tmp_height = tmp_height if tmp_height is not None else self.config.SIZE_HEIGHT
        else:
            tmp_height = tmp_height if tmp_height is not None else randint(*self.config.RAMDOM_SIZE_RANGE)

        if tmp_height <= 0: raise BoxException('新增方塊錯誤','高(height)要大於0')

        box_shape = pymunk.Poly.create_box(box_body, (tmp_width, tmp_height) )

        tmp_density = 密度 if 密度 is not None else density
        if tmp_density is None:
            tmp_density = self.config.DENSITY
        box_shape.density = tmp_density
        
        box_shape.friction = self.config.FRICTION
        box_shape.elasticity = self.config.ELASTICITY
        
        box_shape.color = color.random()     
        


        tmp_x = 位置x if 位置x is not None else position_x
        if not random_flag:
            tmp_x = tmp_x if tmp_x is not None else self.config.X
        else:
            tmp_x = tmp_x if tmp_x is not None else randint(*self.config.RANDOM_X_RANGE)

        tmp_y = 位置y if 位置y is not None else position_y
        if not random_flag:
            tmp_y = tmp_y if tmp_y is not None else self.config.Y
        else:
            tmp_y = tmp_y if tmp_y is not None else randint(*self.config.RANDOM_Y_RANGE)

        box_body.position = (tmp_x, tmp_y)

        if not random_flag:
            box_body.angle = 0
        else:
            box_body.angle = 3.1416 * 2 * random()

        if not random_flag:
            box_body.velocity = (0, 0)
        else:
            box_body.velocity = ( randint(*self.config.RANDOM_VELOCITY_RANGE),
                                randint(*self.config.RANDOM_VELOCITY_RANGE) )           

        self.space.add(box_body, box_shape)
        return  BodyShapeWrapper(box_body, box_shape)

    def 新增方塊(self, *args, **kwargs):
        return self.add_box(*args, **kwargs)

    def add_random_box(self, *args,  **kwargs):
        kwargs['random_flag'] = True
        return self.add_box(*args, **kwargs)                

    def 新增隨機方塊(self, *args, **kwargs):
        kwargs['random_flag'] = True
        return self.add_box(*args, **kwargs) 



    def make_borders(self):
        self.make_one_border( (0,0), (self.config.WINDOW_WIDTH,0))
        self.make_one_border( (0,self.config.WINDOW_HEIGHT), (self.config.WINDOW_WIDTH,self.config.WINDOW_HEIGHT))
        self.make_one_border( (0,0), (0,self.config.WINDOW_HEIGHT))
        self.make_one_border( (self.config.WINDOW_WIDTH,0), (self.config.WINDOW_WIDTH,self.config.WINDOW_HEIGHT))

    def 產生邊界(self):
        self.make_borders()

    def make_floor(self):
        start_pos = ( int(self.config.WINDOW_WIDTH * 0.1), 40)
        end_pos = (int(self.config.WINDOW_WIDTH * 0.9), 40)
        return self.make_one_border(start_pos, end_pos)

    def 產生地面(self):
        return self.make_floor()

    def make_one_border(self, a, b):
        wall_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        wall_shape = pymunk.Segment(wall_body, a,b,self.config.WALL_THICKNESS)
        wall_shape.friction = self.config.FRICTION
        wall_shape.elasticity = self.config.ELASTICITY
        wall_body.position = 0, 0
        self.space.add( wall_body,wall_shape)
        return BodyShapeWrapper(wall_body, wall_shape)
    
    def on_draw(self):
        self.window.clear()
        self.space.debug_draw(options)
        self.fps_display.draw()

        
    def engine_update(self, dt):
        small_dt = dt / 4
        for i in range(4):
            self.space.step(small_dt)

    def check_and_remove_out_of_gc_bound(self, dt):
        #print(len(self.space.bodies), len(self.space.shapes))
        for sh in self.space.shapes:
            x = sh.body.position.x
            y = sh.body.position.y
            if x > self.config.RIGHT_GC_BOUND or x < self.config.LEFT_GC_BOUND or \
               y > self.config.TOP_GC_BOUND or y < self.config.BOTTOM_GC_BOUND:
                self.space.remove(sh.body, sh)

    def check_event_handler_params(self):
        
        # 4 params for on_mouse_press
        #pyglet example: def on_mouse_press(x, y, button, modifiers):
        if hasattr(toplevel, "on_mouse_press"):
            sig = signature(toplevel.on_mouse_press)
            if len(sig.parameters) != 4 :
                raise EventException('事件處理函式錯誤', ' def on_mouse_press()函式 需要有4個參數')     
        
        if hasattr(toplevel, "當滑鼠被按下"):
            sig = signature(toplevel.當滑鼠被按下)
            if len(sig.parameters) != 4 :
                raise EventException('事件處理函式錯誤', ' def 當滑鼠被按下()函式 需要有4個參數')        

        # 6 params for on_mouse_drag
        #pyglet example: def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
        if hasattr(toplevel, "on_mouse_drag"):
            sig = signature(toplevel.on_mouse_drag)
            if len(sig.parameters) != 6 :
                raise EventException('事件處理函式錯誤', ' def on_mouse_drag()函式 需要有6個參數')     
        
        if hasattr(toplevel, "當滑鼠被拖曳"):
            sig = signature(toplevel.當滑鼠被拖曳)
            if len(sig.parameters) != 6 :
                raise EventException('事件處理函式錯誤', ' def 當滑鼠被拖曳()函式 需要有6個參數')

        # 4 params for on_mouse_release
        #pyglet example: def on_mouse_release(x, y, button, modifiers):
        if hasattr(toplevel, "on_mouse_release"):
            sig = signature(toplevel.on_mouse_release)
            if len(sig.parameters) != 4 :
                raise EventException('事件處理函式錯誤', ' def on_mouse_release()函式 需要有4個參數')     
        
        if hasattr(toplevel, "當滑鼠被放開"):
            sig = signature(toplevel.當滑鼠被放開)
            if len(sig.parameters) != 4 :
                raise EventException('事件處理函式錯誤', ' def 當滑鼠被放開()函式 需要有4個參數')

        # 2 params for on_key_press
        #pyglet example: def on_key_press(symbol, modifiers):
        if hasattr(toplevel, "on_key_press"):
            sig = signature(toplevel.on_key_press)
            if len(sig.parameters) != 2 :
                raise EventException('事件處理函式錯誤', ' def on_key_press()函式 需要有2個參數')     
        
        if hasattr(toplevel, "當鍵盤被按下"):
            sig = signature(toplevel.當鍵盤被按下)
            if len(sig.parameters) != 2 :
                raise EventException('事件處理函式錯誤', ' def 當鍵盤被按下()函式 需要有2個參數')

        # 2 params for on_key_release
        #pyglet example: def on_key_release(symbol, modifiers):
        if hasattr(toplevel, "on_key_release"):
            sig = signature(toplevel.on_key_release)
            if len(sig.parameters) != 2 :
                raise EventException('事件處理函式錯誤', ' def on_key_release()函式 需要有2個參數')     
        
        if hasattr(toplevel, "當鍵盤被放開"):
            sig = signature(toplevel.當鍵盤被放開)
            if len(sig.parameters) != 2 :
                raise EventException('事件處理函式錯誤', ' def 當鍵盤被放開()函式 需要有2個參數')

    def run(self):

        #self.check_event_handler_params()

        self.window = pyglet.window.Window(self.config.WINDOW_WIDTH,
                                            self.config.WINDOW_HEIGHT, 
                                            resizable=False)        
        
        self.on_draw = self.window.event(self.on_draw)

        self.fps_display = pyglet.window.FPSDisplay(window=self.window)
        
    
        if hasattr(toplevel, "當滑鼠被按下"):
            toplevel.當滑鼠被按下.__name__ = "on_mouse_press"
            toplevel.當滑鼠被按下 = self.window.event(toplevel.當滑鼠被按下)
        elif hasattr(toplevel, "on_mouse_press"):
            toplevel.on_mouse_press = self.window.event(toplevel.on_mouse_press)

        if hasattr(toplevel, "當滑鼠被拖曳"):
            toplevel.當滑鼠被拖曳.__name__ = "on_mouse_drag"
            toplevel.當滑鼠被拖曳 = self.window.event(toplevel.當滑鼠被拖曳)
        elif hasattr(toplevel, "on_mouse_drag"):
            toplevel.on_mouse_drag = self.window.event(toplevel.on_mouse_drag)

        if hasattr(toplevel, "當滑鼠被放開"):
            toplevel.當滑鼠被放開.__name__ = "on_mouse_release"
            toplevel.當滑鼠被放開 = self.window.event(toplevel.當滑鼠被放開)
        elif hasattr(toplevel, "on_mouse_release"):
            toplevel.on_mouse_release = self.window.event(toplevel.on_mouse_release)

        if hasattr(toplevel, "當鍵盤被按下"):
            toplevel.當鍵盤被按下.__name__ = "on_key_press"
            toplevel.當鍵盤被按下 = self.window.event(toplevel.當鍵盤被按下)
        elif hasattr(toplevel, "on_key_press"):
            toplevel.on_key_press = self.window.event(toplevel.on_key_press)            

        if hasattr(toplevel, "當鍵盤被放開"):
            toplevel.當鍵盤被放開.__name__ = "on_key_release"
            toplevel.當鍵盤被放開 = self.window.event(toplevel.當鍵盤被放開)
        elif hasattr(toplevel, "on_key_release"):
            toplevel.on_key_release = self.window.event(toplevel.on_key_release)            



        if hasattr(toplevel, "引擎定期更新"):
            pyglet.clock.schedule_interval(toplevel.引擎定期更新, self.config.DT)
        elif hasattr(toplevel,"engine_update"):
            pyglet.clock.schedule_interval(toplevel.update, self.config.DT)
        else:
            pyglet.clock.schedule_interval(self.engine_update, self.config.DT)

        if hasattr(toplevel, "更新"):
            pyglet.clock.schedule_interval(toplevel.更新, self.config.DT)
        elif hasattr(toplevel,"update"):
            pyglet.clock.schedule_interval(toplevel.update, self.config.DT)

        pyglet.clock.schedule_interval(self.check_and_remove_out_of_gc_bound, 2)


        pyglet.app.run()

    def 開始模擬(self):
        self.run()

物理引擎 = Engine


