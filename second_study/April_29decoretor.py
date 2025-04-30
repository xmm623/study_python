# 装饰器：在不修改原函数代码的前提下，对函数的功能进行扩展。装饰器本质上是一个函数，它接受一个函数作为参数，返回一个新的函数。这个新的函数通常会在原函数的基础上添加一些功能。比如日志记录，性能测试，权限验证等。
# 装饰器的使用
def decorator(func): # 装饰器函数
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper
@decorator #装饰器语法糖，等价于 my_function = decorator(my_function)
def my_function():  # 这是被装饰的函数
    print("This is the original function.")

my_function()  # 调用被装饰的函数，执行步骤：# 1. 调用 decorator 函数，传入 my_function 作为参数
# 2. decorator 函数返回 wrapper 函数
# 3. wrapper 函数被调用，执行装饰器的逻辑
# 4. wrapper 函数调用原函数 my_function
# 5. wrapper 函数执行完毕，返回到调用点

# 带参数的装饰器
def decorator_with_args(arg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator argument: {arg}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
@decorator_with_args("Hello")
def my_function_with_args(x, y):
    print(f"Sum: {x + y}")
my_function_with_args(5, 10)  # 调用带参数的装饰器函数