from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)   #进程池对象，4表示最多同时跑4个进程
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))  #开启子进程
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()  #对pool调用join()会等待所有的进程调用完毕，调用join()之前必须先调用close()方法，调用close()后就不能继续添加新的process
    print('All subprocesses done.')



