str1="Hello World"
print(str1[:6])
str2="e"
print(str2 in str1)

list1=["a","b","c","d","e"]
print(str2 in list1)

print("my name is %s and age is %d")

str3="aaeebcdeeff"
str4="e"
print(str3.count(str4)) #在整个字符串中统计str4出现的次数
print(str3.count(str4,3)) #在整个字符串中从第4个字符(包括第4个字符)开始统计str4出现的次数
print(str3.count(str4,3,8))#从第4个字符到第9个之间统计str4出现的次数


#将首字母大写
print(str3.capitalize())

#返回一个将源字符串居中，并用空格填充至长度width的新字符串
#长度小于字符串自身的长度时，返回原字符串
print(str3.center(5))
print(str3.center(15))

#判断字符串是否以a开头
print(str3.startswith("a"))

#判断字符串是否以a结尾
print(str3.endswith("a"))

str5="aabbccddeeff"
str6="a"
print(str5.find(str6))
print(str5.find(str6,1))
print(str5.find(str6,5,8))  #在一个区间中找第一次出现的索引，没有找到返回-1

str7="AAAA"
print(str5.islower())  #判断字符串是否全为小写
print(str7.isupper())  #判断字符串是否全为大写

list2=["1","2","3","4"]
print("+".join(list2)) #返回一个用+拼接的字符串

print("aaaa1".ljust(10))


str8="     qwer"
print(str8.lstrip())
str9="aaaqwer"
print(str9.lstrip("a")) #可以指定切掉左边的什么字符


str10="hello world"
print(str10.replace("hello","my"))

str11="hello hello world"
print(str11.replace("hello","my",1)) #指定替换次数


print("aaaa1".ljust(10))  #返回一个原字符串左对齐，填充至指定长度的字符串
print("aaaa1".zfill(10)) #返回一个原字符串右对齐，用0填充至指定长度的字符串

print("AAaa".swapcase())  #将字符串的大小写转换
str12="asdasdasdas"

del str12 #删除字符串对象







