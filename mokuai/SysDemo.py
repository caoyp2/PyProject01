import sys

#返回当前pythonpath的列表
print(sys.path)

#退出当前python进程
# sys.exit()

#判断当前系统
print(sys.platform)

#将信息重定向到指定文件
log = open("log.txt","a")
sys.stdout = log
print("111111")

