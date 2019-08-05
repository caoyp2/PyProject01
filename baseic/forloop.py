aa=["aa","bb","cc",12,55]
for i in aa:
    print(i)

for i in range(0,10,2):
   print(i)


for i in range(20):
    print(i)
else:
    print("循环完毕")



count=0
while count < 5:
    print(count)
    count+=1
else:
    print("count大于5")


for i in range(10):
    if i == 5:
        pass
        print("this is pass模块")
    print(i)



#内置的enumerate函数可以把一个list变成索引-元素对
list1=[1,2,5,8,9]
for x in enumerate(list1):
    print(x[0],x[1])



#杨慧三角
def yhsj(max):
    triangles=[]
    temp=[]
    n=1
    while(n < max):
        for x in range(n):
            if(x == 0):
                triangles.append(1)
            elif(x > 0 and x == n - 1):
                triangles.append(1)
            else:
                triangles.append(temp[x - 1] + temp[x])

        temp = triangles;
        print(triangles)
        n=n + 1;
        triangles=[]


yhsj(6)







