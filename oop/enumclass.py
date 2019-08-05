from enum import Enum, unique

from enum import Enum

# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# #这样我们就获得了Month类型的枚举类
#
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)


@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
#@unique装饰器可以帮助我们检查保证没有重复值。

#访问这些枚举类型可以有若干种方法：

day1 = Weekday.Mon
print(day1)