import random


def printme(str):
    print(str)
    return

printme("aaaa1")
printme(str="bbbb")


def message(name,age):
    print(name + str(age))
    return

message("zs",20)
# message(20,"li") #不加关键字时，参数顺序会影响
message(age=20,name="wangwu")  #添加关键字后，参数顺序可以改变

#返回值调用
def suiji(liebiao):
    liebiao=list(liebiao)
    random.shuffle(liebiao)
    return liebiao

lie1=[1,5,6,8,9]
print(suiji(lie1))


#函数默认值
def defaultFun(name,age=20):
    print(name + str(age))
    return

defaultFun(name="JJ") #不传递默认参数时，会取默认的值


#不定长参数
def MoreArgs(arg1,*args): #加了*号的变量名会存放所有未命名的参数
    print(arg1)
    for x in args:
        print("这是可变参数：" + str(x))
    return

MoreArgs(10)  #不定长的参数可能没有
MoreArgs(10,55,66,77) #多个不定长的参数
tup1=(11,22,33,44,55)
MoreArgs(*tup1)

def MoreArgs1(arg1,**kw): #**可以传递加关键字的多个参数
    print('arg1:', arg1, 'other',kw)

MoreArgs1("参数1",adress="BJing",job="IT")





#匿名函数，只能编写简单的逻辑表达式，不能写代码块
sum = lambda  arg1,arg2 : arg1 + arg2
print(sum(10,20))

#多个参数，其实传递的是一个元祖过来，所以可以获取元祖中的元素
count = lambda arg1,*argx : argx[0]
print(count(10,55,66))



#全局变量和局部变量
total=0
def sumFun():
    total = 50 #局部变量
    return total
print(total)
print(sumFun())

def sumFun1():
    global  total #调用全局变量
    total = 100
    return total

print(total)
print(sumFun1())
print(total)


#嵌套函数
def outer():
    print("这是外部函数")
    def inner():  #内部函数只能在外部函数中调用，无法直接调用内部函数
        print("这是嵌套函数")
    inner()

outer()

testnum=11
def outer1():
    print("这是外部函数")
    global testnum
    testnum1=22
    print(testnum)
    print(testnum1)
    def inner1():  #内部函数只能在外部函数中调用，无法直接调用内部函数
        print("这是嵌套函数")
        print(testnum1) #内部函数中直接调用外部函数的变量
        print(testnum)
    inner1()

outer1()


def outer2():
    print("这是外部函数")
    testnum2=111
    print(testnum2)
    def inner2():  #内部函数只能在外部函数中调用，无法直接调用内部函数
        print("这是嵌套函数")
        nonlocal testnum2  #nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量
        print(testnum2)
    inner2()

outer2()















