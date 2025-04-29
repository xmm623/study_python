# 定义函数
# 基础语法
# def 函数名（参数1，参数2，。。。）：
#     """函数说明（可选）"""
#    函数体
#    return 返回值 （可选）如果没有return语句，默认返回None
# 说明：函数名就是函数的名称，遵循变量命名规则（小写字母，下划线等）；参数是函数接收的输入值，可以有多个，也可以没有；函数体是具体实现功能的代码，return是返回的结果
# 调用函数
# 函数名(参数「可选」)
def greet(name):
    """这个函数用来向人打招呼"""
    print(f"你好，{name}")
greet("小猫咪")
def say_hello():
    print("你好")
say_hello()
def add(a, b):
    return a + b
print(add(2,3))

# 函数的传参方式
# 位置参数：上面的add函数就是，调用函数时，按照参数定义的顺序依次传递
print(add(b=12,a=10)) # 关键字参数，通过参数名指定值，顺序可以随意（写代码时最好用这种）
# 默认参数：定义函数时同时为参数定义默认值，调用函数时如果不传递该参数的话，就会用默认值。
def describe_pet(name,animal="狗"):
    print(f"我有一只{animal},它叫{name}")
describe_pet("臭屁咪咪")
# 可变参数：在函数定义时，参数前加*，表示接收任意数量的位置参数，并将其存储为元组；在函数定义时，参数前加**，表示接收任意数量的关键字参数，并将其存储为字典
def print_all(*args): # *args接收任意数量的位置参数，并将其存储为元组
    print(args)
print_all(1,2,3,4)
def make_pizza(*toppings):
    print("做一个有以下配料的披萨")
    for topping in toppings:
        print(f"-{topping}")
make_pizza("火腿","培根","菠萝","花蛤")
def print_info(**kwargs): # **kwargs接收任意数量的关键字参数，并将其存储为字典
    print(kwargs)
    for key,value in kwargs.items():
        print(f"key:{key}:,value:{value}")
print_info(name="小猫",age=1)
def build_profile(**info):
    profile = {}
    for key, value in info.items():
        profile[key] = value
    return profile
user = build_profile(name="小明", age=12, city="北京")
print(user)  # {'name': '小明', 'age': 12, 'city': '北京'}

# 变量的作用域
# 1.局部变量：在函数内部定义的变量，只能在函数内部使用
def jubu():
    x=1 # x是局部变量（在函数内定义的变量）
    print(x)
jubu()
# print(x) # NameError: name 'x' is not defined 报错，因为x是局部变量，只能在函数内部使用

# 2.全局变量：在函数外部定义的变量，可以在函数内部和外部使用
x=20
def quanju():
    print(x)
quanju()
# 3.如果要在函数内修改全局变量，需要使用global声明
z = 30
def modify():
    global z
    z = 40
modify()
print(z)
# 函数查找变量的顺序：LEGB -> LOCAL局部 -> GLOBAL全局（模块/一个py文件） -> BUILT-IN（内置对象：内置命名空间的生命周期贯穿整个 Python 解释器的运行过程，在程序的任何地方都能直接使用这些内置的名称。
# globals()函数：globals()返回一个字典，表示当前全局符号表的内容。全局符号表是一个包含所有全局变量和函数的字典。
# 这个字典的键是变量名，值是变量的值。可以用来查看当前模块中定义的所有全局变量和函数。
# 用途：可以用来调试代码，查看当前模块中定义的所有全局变量和函数，也可以用来动态地访问和修改全局变量。
# 注意：在函数内部使用globals()函数时，返回的是全局变量的字典，而不是局部变量的字典。
# globals()函数返回的字典是只读的，不能直接修改。如果要修改全局变量，可以使用global关键字声明全局变量，然后直接修改。
# 例如：
def modify_global_var():
    global x
    x = 100
modify_global_var()
print(x) # 100
global_dict = globals() # 获取全局变量
print(global_dict)
# nolocal关键字：用于在一个嵌套的函数中修改外层（但非全局）的变量。当你想在内部函数中修改外部函数（不是全局作用域）的变量时，就需要使用 nonlocal 声明。
# 用途：在嵌套函数中修改外层函数的变量
def outer_function():
    x = 10
    def inner_function():
        nonlocal x # 声明x是外层函数的变量
        x += 5
        print("内层函数修改后的x:", x)
    inner_function()
    print("外层函数中的x:", x)
outer_function()