import calendar
import datetime
import time
ticks= time.time()
print(ticks)

#获取当前时间
localtime = time.localtime(time.time())
print(localtime)
print(time.localtime())


#格式化时间  Tue Apr 23 15:08:53 2019
formattime= time.asctime(time.localtime(time.time()))
print(formattime)

#格式化成2016-03-20 11:45:39形式
formatdate=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(formatdate)

# 格式化成Sat Mar 28 22:24:24 2016形式
formatdate1=time.strftime("%a %b %H:%M:%S %Y",time.localtime())
print(formatdate1)


#将字符串转为日期
a="2019-01-21 17:03:20"
strdate=time.strptime(a,"%Y-%m-%d %H:%M:%S")

print(strdate)
print(time.mktime(strdate))  #将日期转换为时间戳

#获取2019年1月的日历
cal = calendar.month(2019,1)
print(cal)


#获取cpu的时钟时间,第一次调用返回的是程序运行的实际时间
#第二次之后的调用，返回的是自第一次调用后,到这次调用的时间间隔
print(time.clock())
time.sleep(2)
print(time.clock())


print(calendar.isleap(2019))  #判断2019年是否闰年

print(calendar.month(2019,1,2,1)) #返回一个多行字符串格式的year年month月日历，两行标题，一周一行

print(calendar.monthcalendar(2019,1)) #返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0

print(calendar.monthrange(2019,1))   #第一个是该月的星期几的日期码，第二个是该月的日期码


#计算今天后的n天
n_days = 4
now = datetime.datetime.now()
n_date = datetime.timedelta(days=n_days)
n_day = now + n_date
print(n_day.strftime("%Y-%m-%d"))







