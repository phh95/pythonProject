# 面向对象编程来书写多线程实例

import threading
from threading import current_thread

class Mythread(threading.Thread):
    def run(self):
        print(current_thread().getName(),'start')
        print('run')
        print(current_thread().getName(),'stop')

t1 = Mythread()
t1.start()
t1.join()  # 调用 join() 就可以实现依赖——在线程 1 结束之后，再运行主程序的 end

print(current_thread().getName(),'end')