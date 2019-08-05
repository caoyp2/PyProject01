'''
实例属性和类属性
'''

class Student:

    name="Student"  #类属性


s = Student()
print(s.name)  #获取类属性

s.name="Test"  #给实例添加实例属性name
print(s.name)  #实例属性优先级大于类属性的优先级

del s.name  #删除name实例属性
print(s.name)



