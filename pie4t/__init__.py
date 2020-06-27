
from . import common
from .engine import PhysicsEngine

物理引擎 = PhysicsEngine

__all__ = [ 
            'add_circle', '新增圓球',
            'simulate','開始模擬','mainloop','主迴圈',



            ]



######## top level function

def add_circle():
    if not common.is_engine_created:
        PhysicsEngine()
    return common.stage.add_circle()

新增圓球 = add_circle





def mainloop():
    if not common.is_engine_created:
        PhysicsEngine()

    common.stage.simulate()

simulate = mainloop
主迴圈 = mainloop
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
    
