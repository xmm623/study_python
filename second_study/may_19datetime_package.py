# datetime包：日期处理
from datetime import datetime,date,time,timedelta
print(datetime.now())  # 打印当前时间
print(date.today()) # 打印当前日期（不包括时间）
d = date(2025, 5, 19) # 创建特定日期
t = time(18 ,42, 47) # 创建特定时间
print(d)
print(t)
dt = datetime(2025, 5, 20, 17,20, 20) # 创建特地日期时间
print(dt)

date_str = "2023-05-21"
d = datetime.strptime(date_str, "%Y-%m-%d") # 将字符串时间转换为datetime对象
print(type(d))
time_str = "14:30:45"
t = datetime.strptime(time_str, "%H:%M:%S") # 将字符串时间转换成datetime对象
print(type(t))
datetime_str = "2023-05-19 14:30:45"
dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")  # 将字符串日期时间转换为datetime对象
print(type(dt))

formatted = dt.strftime("%Y/%m/%d %A %p %I:%M") # 将datetime对象转换成字符串
print(formatted)
print(type(formatted))

dt2  = datetime(2025, 5, 20, 17, 34, 52)
tomorrow = dt2 + timedelta(days=1) # 加一天
print(tomorrow)
one_hour_ago = dt2 -timedelta(hours=1) # 减去一小时
print(one_hour_ago)
dt3 = datetime(2025, 5, 24, 17, 34, 45)
delta = dt3 - dt2 # 计算两个日期的差值
print(delta.days) # 打印相差的天数