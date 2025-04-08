# None
#类型：属于NoneType类型，此类型只有一个值，那就是None
a = None
print(a)
# None的用途
# 1. 用于初始化变量
b = None
print(b)
# 2. 用于函数的默认参数，如果函数中没有return语句，则默认返回None
def example_function():
    pass
result = example_function()
print(result)
#  用于检查变量是否被赋值
e = None
if e is None:
    print("e is None")
else:
    print("e is not None")
