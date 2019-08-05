'''
    __iter__
    如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法

    __getitem__
    使实例可以像list一样通过下标获取元素

'''

class demo02:
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        if self.a != 0:
            self.a = self.a + 2
            if(self.a > 100):
                raise StopIteration()
        return self.a

    def __getitem__(self, item):
        list1 = range(0,101,2)
        return list1[item]


for x in demo02():
    print(x)

print(demo02()[3])

