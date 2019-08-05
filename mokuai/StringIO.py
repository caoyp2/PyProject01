#字符流，写入内存中
from io import StringIO


def writeStringIo(ss):
    f = StringIO()
    f.write(ss)  #将字符串写入内存中
    print(f.getvalue())  #获取内存中写入的字符串

# writeStringIo("hello world")


#从内存中读取
def readStringIO():
    f = StringIO("hello\nworld")
    while True:
        ss=f.readline()
        if ss=='':
            break
        print(ss)

readStringIO()