# 装饰器：在不修改原函数代码的前提下，对函数的功能进行扩展。装饰器本质上是一个函数，它接受一个函数作为参数，返回一个新的函数。这个新的函数通常会在原函数的基础上添加一些功能。比如日志记录，性能测试，权限验证等。
# 装饰器的使用
def decorator(func): # 装饰器函数
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper
@decorator #装饰器语法糖，等价于 my_function = decorator(my_function)，语法糖的形式简化了装饰器的应用，不然怎么会叫”糖”呢
# 不使用装饰器语法糖的写法
# my_function = decorator(my_function) # 将 my_function 传入 decorator 函数，返回一个新的函数
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
# 先等于赋值，再执行函数

# 不使用装饰器语法糖的写法
def my_function_with_args(x, y):
    print("不使用装饰器语法糖的写法")
    print(f"Sum: {x + y}")
my_function_with_args = decorator_with_args("Hello")(my_function_with_args)  # 将 my_function_with_args 传入 decorator_with_args 函数，返回一个新的函数
my_function_with_args(5, 10)  # 调用带参数的装饰器函数，实际上是在调用 wrapper 函数
# 以上代码的解释：decorator_with_args 函数返回一个装饰器函数 decorator，decorator 函数接受一个函数 func 作为参数，并返回一个新的函数 wrapper。wrapper 函数在调用原函数 func 之前打印装饰器的参数 arg。最后，使用 @decorator_with_args("Hello") 装饰 my_function_with_args 函数。
# 设涉及到的知识点：
# # 1. 函数名带一个括号：调用这个函数，返回这个函数的执行结果
# 2. 函数名带两个括号：先调用一个函数，这个函数返回一个函数对象，接着再调用这个函数对象。