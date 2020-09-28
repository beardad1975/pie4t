import sys
import threading
from queue import Queue, Empty 
import time
import code

import arcade
import pie4t
from . import common

import __main__
from __main__ import __dict__ as main_dict

class Repl:
    """  Repl main and readline thread """
    def start_repl(self): 
        self.cmd_queue = Queue()
        self.is_cmd_completed = True

        self.console = code.InteractiveConsole(locals=main_dict,filename='輸入')   
        
        arcade.schedule(self.handle_repl, 0.2)
        t = threading.Thread(target=self.readline_thread)
        common.repl_thread = t
        t.daemon = True
        t.start()  

    def readline_thread(self):
        print('物理模擬開始 ')
        print('\n')
        print('>>> ', end='')
        while True:
             try:
                line = sys.stdin.readline()
                self.cmd_queue.put(line)
                time.sleep(0.2)
             except RuntimeError as e :
                 print('請按上方紅STOP按鈕重啟互動環境')
                 return

    def handle_repl(self, dt):
        try:
            line = self.cmd_queue.get(block=False)
        except Empty:
            return

        # strip enter  or  leading white space
        line = line.rstrip()
        if self.is_cmd_completed: line = line.lstrip()


        if self.console.push(line):
            # not complele
            print('... ', end='')
            self.is_cmd_completed = False
        else:
            # complete
            print('>>> ', end='')
            self.is_cmd_completed = True

        # try:
        #     if '=' in line:
        #         #exec(line)
        #         exec(line, main_dict)
        #     else:
        #         #r = eval(line)
        #         r = eval(line, main_dict)
        #         if r:
        #             print(r)
        #     #print('Got: ', line[:-1], '---')
        
        # except Exception as e:
        #     print(e)
        # finally:
        #     print('4t>>> ', end='') 