'''
    使用__slots__来限制类的属性
    __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
'''

class Book:
    __slots__ = ("name","price")
    def __init__(self,name,price):
        self.name = name
        self.price = price


book = Book("lisi",20)
print(book.name)

#给book添加一个其他属性，会报错，因为slots是我限制
book.time = "1999"
