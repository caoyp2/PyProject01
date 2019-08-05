import operator
ss=["a","b",11,22,"cc"]
ss.append("dd")
print(ss)

#删除列表中的元素
del ss[1]
print(ss)


a=[1,2,3]
print(a * 2)  #结果为：[1,2,3,1,2,3]

b=[1,2,3,4]
print(a+b)  #列表拼接

#获取列表的长度
print("列表的长度为：" + str(len(a)))

#比较两个列表的元素
print(operator.lt(a,b))  #判断小于
print(operator.eq(a,b))  #判断等于

aa=["a","1","5","8","9"]
#获取中元素个数
print(len(b))

print(max(aa))

aa.append("bb")
print(aa)

bb=["c","d"]
aa.extend(bb)
print(aa)

print(aa.count("a"))

print(aa.index("bb"))

aa.insert(2,"cc")
print(aa)

print(aa.pop())

print(aa.pop(1))

aa.remove("5")
print(aa)

aa.reverse()
print(aa)
print("分片翻转：" + str(aa[::-1]))  #分片翻转

aa.sort()
print(aa)

cc=[7,5,8,2]
cc.sort()
print(cc)

del cc  #删除cc对象，删除后不能再调用


#列表生成式
list = [x*x for x in range(1,11)]
print(list)


list=[m + n for m in "ABC" for n in "XYZ"]
print(list)





