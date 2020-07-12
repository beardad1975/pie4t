from time import time

import arcade
from pymunk.vec2d import Vec2d
from . import common

class DotMark:
    def __init__(self, x=0, y=0):
        self.enabled = False

        self.x = x
        self.y = y

        self.timestamp = time()
        

    def lazy_setup(self):
        self.shape_list = arcade.ShapeElementList()
        
        s = arcade.create_ellipse(0, 0 , 20, 20, (255,255,255,120))
        self.shape_list.append(s)

        vs = arcade.create_rectangle(0,0, 3, 20, arcade.color.BLACK )
        hs = arcade.create_rectangle(0,0, 20, 3, arcade.color.BLACK )
        self.shape_list.append(vs)
        self.shape_list.append(hs)

    def update_pos(self, x, y):
        self.x = x
        self.y = y
        self.timestamp = time()
        self.enabled = True
        

    def draw(self):
        if self.enabled:
            if time() - self.timestamp < common.ASSIST_MARK_PERIOD:
                self.shape_list.center_x = self.x
                self.shape_list.center_y = self.y
                self.shape_list.angle = 0 # no rotation
                self.shape_list.draw()
            else: # expired
                self.enabled = False


class SegmentAssist:
    def __init__(self):
        self.enabled = False

        self.first_point_x = 0
        self.first_point_y = 0
        #self.mouse_x = 0
        #self.mouse_y = 0
         
        

    def lazy_setup(self):
        #self.shape_list = arcade.ShapeElementList()
        pass

    def click_first(self, x, y ):
        self.first_point_x = x
        self.first_point_y = y
        #self.mouse_x = x
        #self.mouse_y = y
        self.enabled = True
        #common.stage.dot_mark.update_pos(x, y)

    def cancel_first(self):
        self.enabled= False
        #common.stage.dot_mark.enabled = False

    def click_second(self, x, y ):
        # add segment
        
        fx = self.first_point_x
        fy = self.first_point_y
        
        if not (fx == x and fy == y):
            common.stage.新增線段((fx,fy),(x, y), common.SEG_THICKNESS)
            self.enabled = False
        else:
            print('segment too short')
        

    # def update_mouse_pos(self, x, y):
    #     self.mouse_x = x
    #     self.mouse_y = y

    def draw(self):
        if self.enabled :
            fx = self.first_point_x
            fy = self.first_point_y
            mx = common.stage.mouse_x
            my = common.stage.mouse_y
            arcade.draw_line(fx, fy, mx, my,arcade.color.GREEN ,common.SEG_THICKNESS)

class ArrowAssist:
    def __init__(self):
        #self.mode_turn_on = False # turn on by user
        self.enabled = False  # drawing
        #self.vector = 0
        self.start_x = 0
        self.start_y = 0
        # self.mouse_x = 0
        # self.mouse_y = 0


    def start(self, pos=None):
        #if self.mode_turn_on :


        if pos is None :
            self.start_x = common.stage.mouse_x
            self.start_y = common.stage.mouse_y
        else:
            pos = Vec2d(pos)
            self.start_x = pos.x
            self.start_y = pos.y
            

        self.enabled = True

    # def update_mouse_pos(self, x, y):
    #     if self.mode_turn_on and self.enabled:
    #         self.mouse_x = x
    #         self.mouse_y = y

    def launch(self):
        if self.enabled:
            self.enabled = False




    def lazy_setup(self):
        pass

    def draw(self):
        if self.enabled :
            sx = self.start_x
            sy = self.start_y
            mx = common.stage.mouse_x
            my = common.stage.mouse_y

            if self.vector.length > 40:
                line_v = self.vector
                line_v.length -= 30

                # line
                arcade.draw_line(sx, sy, sx + line_v.x, sy + line_v.y,
                            arcade.color.RED ,common.SEG_THICKNESS*3)
                # triangle
            

                left_v = self.vector
                left_v.length -= 30
                left_v.angle_degrees += 5

                right_v = self.vector
                right_v.length -= 30
                right_v.angle_degrees -= 5

                

                arcade.draw_triangle_filled(mx, my,
                    sx + left_v.x, sy + left_v.y,
                    sx + right_v.x, sy + right_v.y,
                    arcade.color.RED
                )

            
            

    @property
    def vector(self):
            sx = self.start_x
            sy = self.start_y
            mx = common.stage.mouse_x
            my = common.stage.mouse_y
            return Vec2d(mx - sx, my - sy)

    @property
    def start_pos(self):
        return Vec2d(self.start_x, self.start_y)



  

            

