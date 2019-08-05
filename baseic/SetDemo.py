s = set([1,2,3])
print(s)

ss = {1,5,6}
print(ss)

s1={} #这样写默认是字典类型
s2=set({})
print(type(s1))
print(type(s2))

#set和字典类似，无序和无重复元素的集合
s3 = set([5,6,8,8,9])
print(s3)  #{8, 9, 5, 6}

s3.add("10")  #向集合中添加元素
print(s3)


s3.remove("10")  #删除元素
print(s3)












