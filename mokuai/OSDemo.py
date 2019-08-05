import os
#获取操作系统类型

print(os.name)  #nt表示windoes系统，posix表示linux操作系统

#os.uname 获取操作系统的详细信息，仅支持linux系统下使用
# print(os.uname())

#查看系统的环境变量
print(os.environ)
print(os.environ.get("path"))  #获取具体变量的值


#查看当前目录的绝对路径"."表示表示当前目录  ".."表示上一级目录
print(os.path.abspath("."))

#目录拼接
ss="d:\\code"
print(os.path.join(ss,"PyProject01"))


#创建目录
os.mkdir("aaa")

#删除一个目录
os.rmdir("aaa")


#拆分路径
print(os.path.split("d:\\code\PyProject01\\test.txt"))

#获取文件扩展名
print(os.path.splitext("d:\\code\\PyProject01\\test.txt"))

#重命名文件
# print(os.rename("test1.jpg","test_bak.jpg"))

#删除文件
# print(os.remove("test_bak.jpg"))


#显示当前目录下的所有目录
def printDir():
    for x in os.listdir("."): #显示目录下的所有内容
        if os.path.isfile(x) and os.path.splitext(x)[1] == ".py":  #判断x是否是一个文件
            print(x)
printDir()


#删除多层目录
# print("*" * 20)
# os.removedirs("aaaa1\\bbb")



#运行系统命令
ss="java -version"
os.system(ss)

#获取当前正在工作的目录
print(os.getcwd())

#获取文件名
print(os.path.basename("d:\\code\\PyProject01\\test.txt"))
