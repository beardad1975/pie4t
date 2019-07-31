import sys
from random import choice, randint, random
from inspect import signature

import pyglet
from pyglet.window import key
import pymunk
import pymunk.pyglet_util

from wrapper import BodyShapeWrapper



options = pymunk.pyglet_util.DrawOptions()
toplevel = sys.modules["__main__"]


class Config:
    def __init__(self, width, height):
        # customizable
        self.WINDOW_WIDTH = 600 if width is None else width
        self.WINDOW_HEIGHT = 600 if height is None else height   
        self.FRICTION = 0.5 
        self.ELASTICITY = 0.8
        self.DT = 0.02
        #used internally
        self.DENSITY = 1
        self.GRAVITY = (0, 0)  
        self.SIZE = (20, 20)
        self.RANDOM_RADIUS_RANGE = (10,40) 
        self.RANDOM_VELOCITY_RANGE = (-300, 300)
        self.RANDOM_X_RANGE = (int(self.WINDOW_WIDTH*0.4), int(self.WINDOW_WIDTH*0.6))
        self.RANDOM_Y_RANGE = (int(self.WINDOW_HEIGHT*0.4), int(self.WINDOW_HEIGHT*0.6))
        self.WALL_THICKNESS = 10 
    


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

    def random(self):
        c = choice(['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'white'])
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

    def add_circle(self, radius=None, 半徑=None, static=False, 固定=False, kinematic=False):
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

        circle_shape.density = self.config.DENSITY
        circle_shape.friction = self.config.FRICTION
        circle_shape.elasticity = self.config.ELASTICITY
        
        circle_shape.color = color.random()

        temp_x = randint(*self.config.RANDOM_X_RANGE)
        temp_y = randint(*self.config.RANDOM_Y_RANGE)
        circle_body.position = (temp_x, temp_y)

        circle_body.velocity = (randint(*self.config.RANDOM_VELOCITY_RANGE),
                                randint(*self.config.RANDOM_VELOCITY_RANGE)
                                )

        self.space.add(circle_body, circle_shape)
        return  BodyShapeWrapper(circle_body, circle_shape)

    def 新增圓形(self, **kwargs):
        return self.add_circle(**kwargs)

    def add_box(self,size=None,大小=None, static=False, 固定=False,kinematic=False):
        if static or 固定 :
            box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        elif kinematic:
            box_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        else:
            box_body = pymunk.Body(body_type=pymunk.Body.DYNAMIC) 

        size = 大小 if 大小 is not None else size
        size = size if size is not None else self.config.SIZE
        if type(size) is not tuple and  type(size) is not list:
            raise BoxException('新增方塊錯誤','大小要2個數字組合')

        if size[0] <= 0 or size[1] <= 0:
            raise BoxException('新增方塊錯誤','大小值沒有大於0')
        box_shape = pymunk.Poly.create_box(box_body, size)

        box_shape.density = self.config.DENSITY
        box_shape.friction = self.config.FRICTION
        box_shape.elasticity = self.config.ELASTICITY
        
        box_shape.color = color.random()     
        


        x = randint(*self.config.RANDOM_X_RANGE)
        y = randint(*self.config.RANDOM_Y_RANGE)
        box_body.position = (x, y)

        box_body.angle = 3.1416 * random()

        box_body.velocity = ( randint(*self.config.RANDOM_VELOCITY_RANGE),
                              randint(*self.config.RANDOM_VELOCITY_RANGE) )

        self.space.add(box_body, box_shape)
        return  BodyShapeWrapper(box_body, box_shape)

    def 新增方塊(self, **kwargs):
        return self.add_box(**kwargs)

    def make_borders(self):
        self.make_one_border( (0,0), (self.config.WINDOW_WIDTH,0))
        self.make_one_border( (0,self.config.WINDOW_HEIGHT), (self.config.WINDOW_WIDTH,self.config.WINDOW_HEIGHT))
        self.make_one_border( (0,0), (0,self.config.WINDOW_HEIGHT))
        self.make_one_border( (self.config.WINDOW_WIDTH,0), (self.config.WINDOW_WIDTH,self.config.WINDOW_HEIGHT))

    def 產生邊界(self):
        self.make_borders()

    def make_one_border(self, a, b):
        wall_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        wall_shape = pymunk.Segment(wall_body, a,b,self.config.WALL_THICKNESS)
        wall_shape.friction = self.config.FRICTION
        wall_shape.elasticity = self.config.ELASTICITY
        wall_body.position = 0, 0
        self.space.add(wall_shape)

    
    def on_draw(self):
        self.window.clear()
        self.draw()

    def draw(self):
        self.space.debug_draw(options)


    def default_update(self, dt):
        small_dt = dt / 4
        for i in range(4):
            self.space.step(small_dt)


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

        self.check_event_handler_params()

        self.window = pyglet.window.Window(self.config.WINDOW_WIDTH,
                                            self.config.WINDOW_HEIGHT, 
                                            resizable=False)        
        
        self.on_draw = self.window.event(self.on_draw)
        
    
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

        if hasattr(toplevel,"update"):
            pyglet.clock.schedule_interval(toplevel.update, self.config.DT)
        else:
            pyglet.clock.schedule_interval(self.default_update, self.config.DT)
        pyglet.app.run()

    def 開始模擬(self):
        self.run()

物理引擎 = Engine


