import random
import math
import msvcrt
import sys
import time
from queue import Queue, Empty
import threading

import arcade

import pymunk

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
TITLE = 'pymunk 範例 (以arcade實作)'

global_space = pymunk.Space()
global_space.gravity = (0.0, -900.0)

BALL_COLORS = (arcade.color.WINDSOR_TAN,
               arcade.color.VIVID_VIOLET,
               arcade.color.ULTRAMARINE_BLUE,
               arcade.color.TANGELO,
               arcade.color.UFO_GREEN,
               )

class PymunkCircle:
    def __init__(self,):
        # pymunk part
        self.mass = 1
        self.radius = random.randrange(10,30)
        self.moment = pymunk.moment_for_circle(self.mass, 0, self.radius)
        self.body = pymunk.Body(self.mass, self.moment)
        x = random.randint(120, 380)
        self.body.position = x, 550
        self.physics_shape = pymunk.Circle(self.body, self.radius)
        self.physics_shape.friction = 0.8
        global_space.add(self.body, self.physics_shape)
        
        ### arcade part
        
        self.shape_element = arcade.ShapeElementList()
        # circle
        ball_color = random.choice(BALL_COLORS)
        #s = arcade.create_ellipse_filled(0, 0, self.radius, self.radius, ball_color)
        s = arcade.create_ellipse_filled_with_colors(0, 0, self.radius, self.radius,
                                            ball_color, arcade.color.UNMELLOW_YELLOW)
        self.shape_element.append(s)
        
        # dot
        #s = arcade.create_ellipse_filled(self.radius-6 , 0, 2, 2, arcade.color.WHITE)
        #self.shape_element.append(s)
        s = arcade.create_ellipse_filled(self.radius-8 , 8, 2, 4, arcade.color.UNMELLOW_YELLOW, tilt_angle=30)
        self.shape_element.append(s)

        
    def draw(self):
        self.shape_element.center_x = self.body.position.x
        self.shape_element.center_y = self.body.position.y
        self.shape_element.angle = math.degrees(self.body.angle)
        self.shape_element.draw()
        



class PymunkStaticLine:
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
        
    
    



class PymunkGame(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, TITLE)
        self.set_update_rate(1/60)
        self.ball_list = []
        self.line_list = []

        self.cmd_queue = Queue()
        
    def setup(self):
        line1 = PymunkStaticLine((400,200),(100,300))
        self.line_list.append(line1)
        line2 = PymunkStaticLine((100,50),(50,100))
        self.line_list.append(line2)
        
        b = PymunkCircle()
        b.body.position = (300,150)
        joint = pymunk.PinJoint(b.body, line1.body, (0,0) , (0,0))
        joint.distance = 150
        global_space.add(joint)
        self.ball_list.append(b)
        
        #arcade.schedule(self.add_circle, 2)
        
        
        arcade.schedule(self.handle_stdin, 0.5)
        t = threading.Thread(target=self.stdin_thread)
        t.daemon = True
        t.start()
        
    
    def on_draw(self):
        arcade.start_render()
        
        for b in self.ball_list:
            b.draw()
            
        for li in self.line_list:
            #print('line: ', li.shape_element.center_x, li.shape_element.center_y)
            li.draw()
    
    def on_update(self, dt):
        global_space.step(dt)
    
    def on_key_press(self, symbol, mod):
        if symbol == arcade.key.ESCAPE:
            self.close()
            
    def add_circle(self):
        for i in range(5):        
            p = PymunkCircle()
            self.ball_list.append(p)

    def stdin_thread(self):
        
        print('begin ')
        print('\n')
        print('4t>>> ', end='')
        while True:
             try:
                line = sys.stdin.readline()
                self.cmd_queue.put(line)
                time.sleep(0.5)
             except RuntimeError as e :
                 print('請按上方執行或STOP按鈕')
                 return

           

    def handle_stdin(self, dt):
        try:
            line = self.cmd_queue.get(block=False)
        except Empty:
            return
        
        try:
            if '=' in line:
                exec(line)
            else:
                r = eval(line)
                if r:
                    print(r)
            #print('Got: ', line[:-1], '---')
        
        except Exception as e:
            print(e)
        finally:
            print('4t>>> ', end='') 
        

if __name__ == '__main__' :
    win = PymunkGame()
    win.setup()
    arcade.run()
    
