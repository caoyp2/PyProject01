
def readFiel(path):
    file = open(path,"r",encoding="utf-8")
    print(file.read())
    file.close() #关闭流

def readFiel02(path):
    # 使用with ....as的形式可以捕获异常，不用手动添加try except
    with open(path,"r",encoding="utf-8") as f:
        print(f.read())


def readFiel03(path):
    # 使用with ....as的形式可以捕获异常，不用手动添加try except
    with open(path,"r",encoding="utf-8") as f:
            print(f.readline())  #读取一行

def readFiel04(path):
    # 使用with ....as的形式可以捕获异常，不用手动添加try except
    with open(path,"r",encoding="utf-8") as f:
            for x in  f.readlines():  #读取所有行，返回一个列表
                print(x.strip())



# readFiel("file.txt")
# readFiel02("file.txt")
# readFiel03("file.txt")
# readFiel04("file.txt")

def writeFile(path):
    with open(path,"a+",encoding="utf-8") as f: #a+表示追加写入
        ss = '''
aaaa1
bbb
        
ccc
        '''
        f.write(ss)  #写入文件

# writeFile("write01.txt")


def writeFile01(path):
    with open(path,"a+",encoding="utf-8") as f:
        ss = ["aaaa1","bbb","ccc"]
        f.writelines(ss) #一次性写入

# writeFile01("write02.txt")


#拷贝图片
def copy(source,target):
    with open(source,"rb") as f:
        temp = f.read()
    with open(target,"wb") as wf:
        wf.write(temp)
        wf.flush()

# copy("test.jpg","test1.jpg")


def copy01(source,target):
    with open(target, "ab+") as wf:
        with open(source,"rb+") as f:
            temp = b'\x00'
            while temp != b'':
                temp = f.read(100)
                wf.write(temp)

copy01("test1.jpg","test2.jpg")






