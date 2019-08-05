dict1={"name":"lisi","sex":25}
print(dict1["name"])

#更新字典的值
dict1["name"] = "wangwu"
print(dict1["name"])
print(dict1)


dict2={"brand":"奥迪","price":20000,"produce":"china"}
del dict2["produce"]  #删除指定的key
print(dict2)
dict2.clear() #清空字典对象
print(dict2)
del dict2  #删除dict2对象

dict3 = dict1.copy()  #复制一个字典
print(dict3)

dict4={"name":"lisi","sex":25}
aa=[1,5,6]
dict5 = dict.fromkeys(aa,7) #创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
print(dict5)

#判断key是否存在
print(dict4.__contains__("name"))

print(dict4.items())

print(dict4.keys())

dict4.setdefault("age")
print(dict4)


dict5={}
dict5.update(dict4)  #吧dict4的内容更新到dict5中
print(dict5)


print(dict5.pop("age"))  #删除指定的key.并返回对应value

print(dict5.popitem()) #随机删除一个键值对，并以元祖的形式返回




dict6={"name":"lisi","name":"zs"}
print(dict6)

dict7 = dict(name="wangwu",age=22)
print(dict7)

