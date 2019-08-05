'''
    进程处理
'''
import os
from multiprocessing import Process

def childpocess(name):
    print(name + "----" + str(os.getpid()))

if __name__ == "__main__":
    print(os.getpid())  # 获取当前进程
    p = Process(target=childpocess, args=('test',))
    print("开启子进程。。。。。。")
    p.start()  #开启子进程的任务
    p.join()    #等子进程结束后在运行后面的代码
    print("child process end")




