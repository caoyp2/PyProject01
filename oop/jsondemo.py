import json
'''
    json.dumps()  //将字典转换为json字符串
    json.dump()  //可以将内容序列化写入文件中
'''
dict01 = dict(name="lisi",age=20)
print(json.dumps(dict01))

dict011 = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
print(json.dumps(dict011,indent=2,separators=(',',':')))


json01= '{"name": "lisi", "age": 20}'
dict02 = json.loads(json01)
print(dict02)


class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age


def dict2Student(d):
    return Student(d['name'],d['age'])

stu = Student("张三",20)
#将对象转为json字符串
print(json.dumps(stu,ensure_ascii=False,default=lambda obj: obj.__dict__)) #ensure_ascii=False将转换的编码变为utf-8的编码，不用ascii

#将json字符串转为对象
stu1 = json.loads(json01,object_hook=dict2Student)
print(stu1)
