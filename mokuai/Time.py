#datetime的使用
import datetime
#将日期转为时间戳
import time

#日期转时间戳
dtime = datetime.datetime.now()
un_time = time.mktime(dtime.timetuple())
print(un_time)

d1_time = datetime.datetime.strptime("2019-04-27 13:23:00","%Y-%m-%d %H:%M:%S")
time_stamp = time.mktime(d1_time.timetuple())
print(time_stamp)

#时间戳转日期
ts=1556351013.0
times = datetime.datetime.fromtimestamp(ts)
print(times)

#计算两个日期之间的差值
d1 = datetime.datetime.strptime("2019-04-27 13:23:00","%Y-%m-%d %H:%M:%S")
d2 = datetime.datetime.strptime("2019-04-20 13:23:00","%Y-%m-%d %H:%M:%S")
date = d1 - d2
print(date)

#日期转字符串
time_now = datetime.datetime.now()
print(time_now)
time_str = datetime.datetime.strftime(time_now,"%Y-%m-%d")
print("当前时间：" + time_str)

#当前日期加一天后的日期
now = datetime.datetime.now()
days_date = datetime.timedelta(days = 2)

print(now + days_date)


#当前时间加小时的日期
now = datetime.datetime.now()
hour_date = datetime.timedelta(hours=2)
print(now + hour_date)



