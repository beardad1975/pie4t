
from . import common
from .engine import PhysicsEngine

物理引擎 = PhysicsEngine

__all__ = [ 
            'add_circle', '新增圓球', '物理引擎',
            'simulate', '模擬主迴圈', '移除',
            'add_segment','新增線段','add_box','新增方塊',



            ]



######## top level function

def add_circle(*args, **kwargs):
    if not common.is_engine_created:
        PhysicsEngine()
    return common.stage.新增圓球(*args, **kwargs)

新增圓球 = add_circle


def add_box(*args, **kwargs):
    if not common.is_engine_created:
        PhysicsEngine()
    return common.stage.新增方塊(*args, **kwargs)

新增方塊 = add_box

def add_segment(*args, **kwargs):
    if not common.is_engine_created:
        PhysicsEngine()
    return common.stage.新增線段(*args, **kwargs)

新增線段 = add_segment



def 移除(obj):
    if not common.is_engine_created:
        PhysicsEngine()
    return common.stage.移除(obj)



def simulate():
    if not common.is_engine_created:
        PhysicsEngine()

    common.stage.simulate()


模擬主迴圈 = simulate

開始模擬 = simulate

#def module_init():
    # module reference
    #__main__.pie4t_module = sys.modules['pie4t']

    ## check batch mode
    # had __file__ and import pie4t in files
    # if hasattr(__main__ , '__file__') and __main__.__file__.endswith('py'):
    #     #print('has __file__')
    #     try:
    #         with open(__main__.__file__, encoding='utf8') as f:
    #             lines = f.readlines()
    #             for i in lines:
    #                 if 'import' in i and 'pie4t' in i:
    #                     __main__.pie4t_module.is_batch_mode = True
                        
    #                     print(__file__, ': is batch mode,')
    #                     break
    #     except FileNotFoundError:
    #         pass

    # create game win
    #__main__.pie4t_module.game_win = PhysicsEngine()
    #__main__.pie4t_module.is_initialized = True

### module init

#module_init()



if __name__ == '__main__' :
    pass
    
