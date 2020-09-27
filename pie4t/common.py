import arcade
### default win size

WIN_WIDTH = 500
WIN_HEIGHT = 800

###

WIN_MIN_WIDTH = 300
WIN_MIN_HEIGHT = 300
WIN_MAX_WIDTH = 1600
WIN_MAX_HEIGHT = 1000


TITLE = '物理碰撞模擬'

DT_UPDATE = 1/50
DT_SPLIT_NUM = 4
DT_SPLIT = DT_UPDATE / DT_SPLIT_NUM





GRAVITY = [0, -800]
DENSITY = 0.01
FRICTION = 0.5
ELASTICITY = 0.3






VELOCITY_LIMIT = 1000


RECYCLE_Y_MAX_MUL = 3
RECYCLE_Y_MIN_MUL = -1
RECYCLE_X_MAX_MUL = 2
RECYCLE_X_MIN_MUL = -1

SEG_THICKNESS = 6


#assist
ASSIST_MARK_PERIOD = 0.5


#shape
SHAPE_COLORS = (arcade.color.WINDSOR_TAN,
               arcade.color.VIVID_VIOLET,
               arcade.color.ULTRAMARINE_BLUE,
               arcade.color.TANGELO,
               arcade.color.AO,
               )

CIRCLE_RADIUS_MAX = 40
CIRCLE_RADIUS_MIN = 15

BOX_WIDTH_MAX = 80
BOX_WIDTH_MIN = 20

BOX_ELASTICITY = 0.5
BOX_FRICTION = 0.3
# collision type
COLLITYPE_DEFAULT = 0

COLLITYPE_HOLE = 5
COLLITYPE_SEGMENT = 9

# filter category
CATE_SEGMENT = 0b00000001
CATE_CIRCLE =  0b00000010
CATE_BOX =     0b00000100

### common var
is_engine_created = False

# stage is a physics engine
stage = None
物理舞台 = None