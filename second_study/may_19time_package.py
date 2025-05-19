# time包：提供了各种与时间相关的函数和方法
# 获取时间戳（时间戳：表示从特定的时间点，通常是1970年1月1日00:00:00 UTC到现在的秒数）
import time 
current_timestamp = time.time()
print(f"当前时间戳：{current_timestamp}")

# 让当前线程暂停执行的秒数
print("程序开始...")
time.sleep(1) # 暂停5秒
print("程序在休眠5秒后继续执行。")

# 将时间戳转换为本地时间，返回一个struct_time对象,struct_time对象是一个包含9个元素的元组，分别表示年、月、日、时、分、秒、星期几、今年第几天和夏令时标志,通过索引或属性访问
local_time = time.localtime(current_timestamp)
print(f"本地时间：{local_time}")
print(time.localtime()[1]) # 通过索引访问，获取月份
print(time.localtime().tm_year) # 通过属性访问，获取年份