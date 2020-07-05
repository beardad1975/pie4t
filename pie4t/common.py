
### default

WIDTH = 600
HEIGHT = 600
TITLE = '遊戲物理引擎'

UPDATE_DT = 1/50

QUARTER_DT = UPDATE_DT / 4


GRAVITY = (0, -900)
DENSITY = 1
FRICTION = 0.5
ELASTICITY = 0.95


# collision type
COLLITYPE_DEFAULT = 0

COLLITYPE_HOLE = 5
COLLITYPE_LINE = 9



### common var
is_engine_created = False

# stage is a physics engine
stage = None
物理舞台 = None