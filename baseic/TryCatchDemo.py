def mod(x,y):
    try:
        result = x/y
    except ZeroDivisionError :
        print("除数不能为0")
    else :
        print("结果为:result=" + str(result))
    finally:
        print("我是finally的内容！！！！")

mod(10,5)



