from time import time

import arcade
import pymunk
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


class SegmentAddAssist:
    def __init__(self):
        self._enabled = False
        self.first_clicked = False
        self.first_x = 0
        self.first_y = 0
        self.second_x = 0 
        self.second_y = 0
        self.dirty = False
         
    def enable(self):
        self._enabled = True
        self.first_clicked = False
        self.first_x = 0
        self.first_y = 0
        self.second_x = 0 
        self.second_y = 0
        self.dirty = False
        cur = common.stage.get_system_mouse_cursor('crosshair')
        common.stage.set_mouse_cursor(cur)
        common.stage.模擬暫停 = True        

    def disable(self):
        self._enabled = False
        common.stage.set_mouse_cursor(None)
        common.stage.模擬暫停 = False

        if self.dirty:
           common.stage.save_terrain()  

    @property
    def enabled(self):
        return self._enabled

    # def lazy_setup(self):
    #     #self.shape_list = arcade.ShapeElementList()
    #     pass

    def click(self, x, y):
        if not self.first_clicked:
            # first click
            self.first_x = x
            self.first_y = y
            self.first_clicked = True
        else: # second click
            self.second_x = x
            self.second_y = y
            self.first_clicked = False

            if not (self.first_x == self.second_x and self.first_y == self.second_y):
                common.stage.新增線段((self.first_x,self.first_y),
                                      (self.second_x, self.second_y),
                                       common.SEG_THICKNESS)
                self.dirty = True
                
    def draw(self):
        if self._enabled and self.first_clicked:
            fx = self.first_x
            fy = self.first_y
            mx = common.stage.mouse_x
            my = common.stage.mouse_y
            arcade.draw_line(fx, fy, mx, my,arcade.color.GREEN ,common.SEG_THICKNESS)


class SegmentRemoveAssist:
    def __init__(self):
        self._enabled = False
        self.dirty = False
        self.hover_segment = None
        self.seg_filter = pymunk.ShapeFilter(mask=common.CATE_SEGMENT)

    def enable(self):
        self._enabled = True
        self.dirty = False
        self.hover_segment = None
        cur = common.stage.get_system_mouse_cursor('help')
        common.stage.set_mouse_cursor(cur)
        common.stage.模擬暫停 = True        

    def disable(self):
        self._enabled = False
        common.stage.set_mouse_cursor(None)
        common.stage.模擬暫停 = False

        if self.dirty:
           common.stage.save_terrain()  

    @property
    def enabled(self):
        return self._enabled

    # def lazy_setup(self):
    #     #self.shape_list = arcade.ShapeElementList()
    #     pass

    def draw(self):
        if self._enabled:
            if self.hover_segment:
                a = self.hover_segment.a
                b = self.hover_segment.b
                thickness = self.hover_segment.thickness
                arcade.draw_line(a[0], a[1], b[0], b[1],
                     arcade.color.RED, thickness)

    def click(self, x, y):
        if self._enabled:
            if self.hover_segment:
                common.stage.移除(self.hover_segment)
                self.hover_segment = None
                self.dirty = True

    def update_hover(self,x, y):
        if self._enabled:
            query = common.stage.space.point_query_nearest((x,y), 0, self.seg_filter)
            if query:
                self.hover_segment = query.shape.obj
            else:
                self.hover_segment = None


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




    # def lazy_setup(self):
    #     pass

    def draw(self):
        if self.enabled :
            sx = self.start_x
            sy = self.start_y
            mx = common.stage.mouse_x
            my = common.stage.mouse_y
            length = self.vector.length
            #print("length: ",self.vector.length )
            if length > 40:
                line_v = self.vector
                line_v.length -= 30

                # line
                arcade.draw_line(sx, sy, sx + line_v.x, sy + line_v.y,
                            arcade.color.RED ,common.SEG_THICKNESS*3)
                # triangle
                #if length 
                if length < 500:
                    degree_delta =  15 - length / 50
                else:
                    degree_delta = 5
                

                left_v = self.vector
                left_v.length -= 30
                left_v.angle_degrees += degree_delta 

                right_v = self.vector
                right_v.length -= 30
                right_v.angle_degrees -= degree_delta 

                

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



class CoordinateAssist:
    def __init__(self):
        self._enabled = False
        self.shape_element = None
        self.coor_start = 0
        self.win_width = common.stage.win_width
        self.win_height = common.stage.win_height

        upper_bound = max(self.win_width, self.win_height)
        upper_bound = (upper_bound + 99) // 100 * 100 

        self.coor_end = upper_bound
        self.coor_step = 50
        self.label_step = 100

    def enable(self):
        self._enabled = True
        

    def disable(self):
        self._enabled = False
        

    @property
    def enabled(self):
        return self._enabled

    def lazy_setup(self):
        self.shape_element = arcade.ShapeElementList()
        i = 0
        for y in range(self.coor_start, self.coor_end + self.coor_step, self.coor_step):
            l = arcade.create_line(0, y, self.win_width ,y , arcade.color.ANTIQUE_BRONZE  , 1)
            self.shape_element.append(l)

            r = arcade.create_rectangle(0, y, 8, 3, arcade.color.WHITE_SMOKE)
            self.shape_element.append(r)
            

        # Draw the x labels.
        i = 0
        for x in range(self.coor_start, self.coor_end + self.coor_step, self.coor_step):
            l = arcade.create_line(x, 0, x ,self.win_height , arcade.color.ANTIQUE_BRONZE  , 1)
            self.shape_element.append(l)

            r = arcade.create_rectangle(x, 0, 3, 8, arcade.color.WHITE_SMOKE)
            self.shape_element.append(r)


    def draw(self):
        if self._enabled:
            self.shape_element.center_x = 0
            self.shape_element.center_y = 0
            self.shape_element.angle = 0
            self.shape_element.draw()
            i = 0
            for y in range(self.coor_start, self.coor_end + self.label_step, self.label_step):            
                arcade.draw_text(f"{y}", 5, y+3, arcade.color.WHITE_SMOKE, 12, anchor_x="left", anchor_y="center")
                i += 1

            i = 1
            for x in range(self.coor_start + self.label_step, self.coor_end + self.label_step, self.label_step):    
                arcade.draw_text( f"{x}" , x, 5, arcade.color.WHITE_SMOKE, 12, anchor_x="center", anchor_y="bottom")
                i += 1 

  

            

