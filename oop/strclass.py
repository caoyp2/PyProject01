'''
    __str__()类似于定于java中类的tostring()方法
    通常__str__()和__repr__()代码都是一样的,__str__()返回给用户看 ，__repr__()返回给程序开发者看

'''
class demo01:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'demo01 Object:(name=%s)' % self.name
    __repr__ = __str__   #简便写法，意思就是__repr__函数的方法和__str__代码相同

de1 = demo01("lisi")
print(de1)