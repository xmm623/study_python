# 装饰器：在不修改原函数代码的前提下，对函数的功能进行扩展。装饰器本质上是一个函数，它接受一个函数作为参数，返回一个新的函数。这个新的函数通常会在原函数的基础上添加一些功能。比如日志记录，性能测试，权限验证等。
# 装饰器的使用
def decorator(func): # 装饰器函数
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    # return wrapper
@decorator #装饰器语法糖，等价于 my_function = decorator(my_function)
def my_function():  # 这是被装饰的函数
    print("This is the original function.")

my_function()  # 调用被装饰的函数