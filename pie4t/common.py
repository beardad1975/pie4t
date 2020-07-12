import arcade
### default

WIDTH = 600
HEIGHT = 600

MIN_WIDTH = 200
MIN_HEIGHT = 200

TITLE = '遊戲物理引擎'

DT_UPDATE = 1/50
DT_SPLIT_NUM = 4
DT_SPLIT = DT_UPDATE / DT_SPLIT_NUM





GRAVITY = [0, -800]
DENSITY = 0.001
FRICTION = 0.5
ELASTICITY = 0.95






VELOCITY_LIMIT = 1000

POSITION_Y_MAX = HEIGHT * 4
POSITION_Y_MIN = HEIGHT * -1
POSITION_X_MAX = WIDTH * 2
POSITION_X_MIN = WIDTH * -1

SEG_THICKNESS = 4


#assist
ASSIST_MARK_PERIOD = 5


#shape
SHAPE_COLORS = (arcade.color.WINDSOR_TAN,
               arcade.color.VIVID_VIOLET,
               arcade.color.ULTRAMARINE_BLUE,
               arcade.color.TANGELO,
               arcade.color.AO,
               )

CIRCLE_RADIUS_MAX = 30
CIRCLE_RADIUS_MIN = 10

BOX_WIDTH_MAX = 60
BOX_WIDTH_MIN = 20

BOX_ELASTICITY = 0.5
BOX_FRICTION = 0.3
# collision type
COLLITYPE_DEFAULT = 0

COLLITYPE_HOLE = 5
COLLITYPE_SEGMENT = 9



### common var
is_engine_created = False

# stage is a physics engine
stage = None
物理舞台 = None