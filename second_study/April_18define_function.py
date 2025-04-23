# 定义函数
# 基础语法
# def 函数名（参数1，参数2，。。。）：
#     """函数说明（可选）"""
#    函数体
#    return 返回值 （可选）
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
print(add(b=12,a=10)) # 关键字参数，通过参数名指定值，顺序可以随意
# 默认参数：定义函数时同时为参数定义默认值，调用函数时如果不传递该参数的话，就会用默认值。
def describe_pet(name,animal="狗"):
    print(f"我有一只{animal},它叫{name}")
describe_pet("臭屁咪咪")
# 可变参数：
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
