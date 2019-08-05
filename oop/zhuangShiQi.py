import time


def decorator(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func()
        end_time = time.time()
        return end_time - start_time
    return wrapper

@decorator
def func():
    time.sleep(0.8)

print(func())   #相当于执行decorator(func())


