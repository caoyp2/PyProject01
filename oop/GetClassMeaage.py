from oop.Animal import Animal
from oop.Dog import Dog

str1="ABC"
print(type(str1))   #type判断数据类型

dog = Dog()
#判断的是一个对象是否是该类型本身，或者位于该类型的父继承链
print(isinstance(dog,Animal))

#获得一个对象的所有属性和print(dir(str1))方法，可以使用dir()函数，它返回一个包含字符串的list





