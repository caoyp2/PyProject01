'''
    序列化和反序列化
    pickle.dumps()  //将对象转成二进制数据
    pickle.dump()     //可直接将对象写入文件中

    pickle.loads()  //把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象
    pickle.load()   //将序列化的文件，反序列化出对象
'''
import pickle

dict01 = dict(name='lisi',age=20)

#序列化
file = open('dump.txt','wb')
pickle.dump(dict01,file)  #pickle.dump将对象直接写入文件中
file.close()

#反序列化
file01 = open("dump.txt","rb")
dict02 = pickle.load(file01)
print(dict02)





