# 闭包函数：内部函数引用外部函数的变量，外部函数将内部函数作为返回值返回
def outer_function():
    x = 10  # 外部函数的局部变量

    def inner_function():
        print(f"Value of x is {x}")  # 内部函数引用外部函数的变量,这里没有用到nolocals函数的原因是因为没有修改外部函数的变量，只是使用它
    return inner_function  # 返回内部函数的引用
outer_function()()  # 调用外部函数，返回内部函数并立即调用
