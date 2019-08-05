import math
import random

a = 10
b = -5

print(abs(b))  # 求绝对值
print(math.ceil(5.1))  # 向上取整
print(pow(2, 3))  # 2的3次方的值

# 产生10以内的一个随机数
print(random.choice(range(10)))
#产生一个10-20且步长为2的集合中的随机数
print(random.randrange(10,20,2))
#产生一个[0,1）的随机数
print(random.random())
#将序列随机排序
list1=[1,2,3,4,5,6]
random.shuffle(list1)
print(list1)
#生成一个指定范围内的实数
print(random.uniform(10,20))
