tup1=(10,20,30)
tup2=(5,8,8,9,8,9)
tup3=tup1+tup2
print(tup3)

del tup1   #删除整个元祖对象，删除后不能再调用
print(tup3[::-1])  #分片翻转元祖

print(tup2.count(8))  #统计元祖中8出现的次数

print(tup2.index(8))  #返回第一个8出现的索引位置
print(tup2.index(8,3)) #可以指定区间找出8第一次出现的位置

for x in tup3:
    print(x)

#多层元祖
tup4=(1,5,(2,8),9)
for x in tup4:
    print(x)

print(5 in tup2)  # 判断5是否存在元祖中
print(5 not in tup2)  # 判断5是否不存在元祖中
print(8 in tup4[2])  #判断8是否在元祖中的宁一个元祖中


#元祖中没有添加和删除元素的方法
#所以只能通过元祖拼接的形式实现该功能
tup5=("aa","bb")
tup5=tup5 + ("cc",)  #通过拼接添加元祖内容
print(tup5)

tup5= tup5[0] + ("BB") #修改第二个元素的内容
print(tup5)



