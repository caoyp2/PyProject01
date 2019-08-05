print("hello world！！！!");

a=10;
b=float(a);
print(type(b));

s1="a1" \
   "a2" \
   "a3"

s2='bbb'
s3='''
aaaa1
bbb
ccc
'''
print(s1.capitalize())
print("你好啊")

if True:
    print("True")
else:
    print("False")


a=input("请输入一个数字：")
a=int(a)

if a > 10:
    print("大于10")
elif a < 10:
    print("小于10")
else:
    print("等于10")


list1=[5,10,20,30]
aa=10
if aa in list1:
    print("存在")
else:
    print("不存在")

aa=10
bb=10
if aa is bb:
    print("有相同标识")
else:
    print("没有相同标识")


