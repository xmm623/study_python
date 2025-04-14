# enumerate函数：在遍历可迭代对象（如列表、元组、字符串等）时同时获取元素的索引和值。
# 语法：enumerate(iterable, start=0)
# 参数：
# - iterable：要遍历的可迭代对象。
# - start：索引起始值，默认为0。
# 返回值：返回一个enumerate对象，包含索引和值的元组。
# 使用示例：
lst = ['a', 'b', 'c']
for index, value in enumerate(lst):
    print(f"Index: {index}, Value: {value}")
# 实际使用场景：
# 查找列表中某个元素的索引。
lst = ['apple', 'banana', 'cherry']
for index, value in enumerate(lst):
    if value == 'banana':
        print(f"Index of 'banana': {index}")

# range 函数：用于生成一个整数序列，常用于循环控制。
# 语法：range(start, stop[, step])
# 参数：
# - start：序列的起始值，默认为0。
# - stop：序列的结束值（不包含）。左闭右开
# - step：步长，默认为1。
# 返回值：返回一个可迭代的range对象。
# 使用示例：
for i in range(5):
    print(i)  # 输出0到4
for i in range(1, 10, 2):
    print(i)  # 输出1, 3, 5, 7, 9   




