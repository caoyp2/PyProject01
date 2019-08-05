class Person:

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def printMessage(self):
        print(self.__name,self.__age)

    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age = age

    #标识该方法为静态方法，静态方法不用实例化对象就可以访问
    @staticmethod
    def printWord():
        print("这是一个静态方法")

    #定义一个类方法
    @classmethod
    def printClassMethond(cls):
        print("这是一个类方法")

    #定义一个属性
    @property
    def porpertyMethod(self):
        print("这是一个属性")

p1 = Person("JJ",20)
print(p1.get_name())
print(p1.get_age())
p1.set_name("JJ01")
print(p1.get_name())

Person.printWord() #直接访问静态方法
p1.printWord()  #实例访问静态方法

Person.printClassMethond()  #访问类方法
p1.printClassMethond() #实例访问类方法

Person.porpertyMethod  #访问属性


