'''
    多线程
'''
import threading

balance = 0
lock = threading.Lock()  #添加锁的实例

def changbalance(n):

    global  balance
    lock.acquire()  #这里锁加在对balance进行操作的地方，而不是对整个方法枷锁
    try:
        balance = balance + n
        balance = balance - n
    finally:
        lock.release()

def run_thread(n):
    for i in range(100000):
        # lock.acquire()   #对要执行的代码添加锁
        # try:
            changbalance(n)
        # finally:
        #     # lock.release()  #释放锁

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()

t1.join()
t2.join()
print(balance)


'''
    threading.local()的使用，在每个线程上绑定变量值
'''

local_school = threading.local() #获取threading.local实例
def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread,args=("tom",))
t2 = threading.Thread(target=process_thread,args=("jerry",))

t1.start()
t2.start()

t1.join()
t1.join()



