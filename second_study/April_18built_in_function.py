# 一些常用的内置函数
# 数学运算函数
# 1.abs(x) ：返回数字的绝对值
print(abs(-1))
# 2.round(x,n):对数字进行四舍五入操作，保留x位小数
print(round(3.141596789034, 2))
# 3.pow(x,y):计算X的Y次幂
print(pow(5,10))
# 4.sum(可迭代对象)：计算可迭代对象中所有元素的和
print(sum([2,4,-10,78,100,999,168]))
# 5.max()和min():返回可迭代对象中的最大值或最小值
print(max((2,4,-10,98,100)))
print(min((3,4,5,-100,98,999)))

# 类型转换函数
# int()：将一个对象转换为整数
a = "10"
print(int(a),type(int(a)))
b = 1.2
print(int(b),type(int(b)))
# float()：将一个对象转换为浮点数
c = "3.14"
print(float(c),type(float(c)))
d = 2
print(float(d),type(float(d)))
# str()：将一个对象转换为字符串
e = 2
print(str(e),type(str(e)))
# bool():将一个对象转换为布尔值
print(bool(2))
print(bool(0))
print(bool(""))
# list()\tuple()\set()：将其他数据类型转换为列表、元组或集合
print(list("hello"))
print(tuple([2,3,4]))
print(set([2,3,"dd"]))

# 输入输出函数
# print():将指定对象打印到控制台，可接收多个参数，多个参数之间用逗号分隔
# input():从标准输入设备读取用户输入的内容，并以字符串的形式返回

# 数据判断
# type()：返回对象的类型
# isinstance():判断对象是否是指定类型
print(isinstance("222",int))
# id():获取对象的内存地址

# 迭代器与生成器
# range():生成一个范围内的数字序列,范围规则是左闭右开
for i in range(2,10):
    print(i)
# enumerate(可迭代对象):遍历可迭代对象时，同时返回索引和值
for index,value in enumerate([2,3,"22","sd",999]):
    print(index,value)
# zip(*可迭代对象)：将多个可迭代对象中对应的元素打包成一个个元组，然后返回由这些元组组成的迭代器，这个迭代器会生成元组
g = ["alice","bob","sam"]
h = ["men","woman","man"]
zipped = zip(g,h)
print(tuple(zipped)) # 想要迭代器生成一个个元组，需要用tuple或者list方法先将它们转换为元组/列表
# 实际应用场景
# 1.同时遍历多个列表
for name,sex in zip(g,h):
    print(f"name{name},是{sex}人")
# 2.快速创建字典
zipped2 = dict(zip(g,h))
print(zipped2)
