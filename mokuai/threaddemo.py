'''
    线程
    threading()模块
'''
import threading
import time


def loop():
    print("thread %s is running",threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print("thread %s is running", threading.current_thread().name)
thread = threading.Thread(target=loop,name="threadloop")
thread.start()
thread.join()
print('thread %s ended.' % threading.current_thread().name)


