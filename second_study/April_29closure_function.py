# 闭包函数：内部函数引用外部函数的变量，外部函数将内部函数作为返回值返回
def outer_function():
    x = 10  # 外部函数的局部变量
    def inner_function():
        print(f"Value of x is {x}")  # 内部函数引用外部函数的变量,这里没有用到nolocals函数的原因是因为没有修改外部函数的变量，只是使用它
    return inner_function  # 返回内部函数的引用
inner_func = outer_function()  # 调用外部函数，返回内部函数的引用
inner_func()  # 调用内部函数
# 以上代码的解释：outer是一个外部函数，它内部定义了inner函数。outer函数返回inner函数对象，当我们调用outer函数时，会得到inner函数对象，并将其赋值给inner_func变量。此时，inner_func变量指向的是inner函数对象，之后执行inner_func()时就相当于调用inner函数。
# 学习过程中产生的疑问
# 1. 闭包函数的作用是什么？闭包函数可以访问外部函数的变量，即使外部函数已经返回。它可以用于数据封装和隐藏。
# 2.闭包函数中，return 函数名和直接调用函数有什么区别？return 函数名是返回函数对象本身，而不是调用这个函数。直接调用函数会执行这个函数并返回结果。
# 引用chatgpt的回答：
# 当你写一个函数名时，实际上你是在引用该函数对象，而不是执行它。简单来说，函数名不加括号时，它代表的是一个函数对象的引用，可以将它传递到其他地方，或者保存到变量中。
# 当你在函数名后面加上括号时，表示你在调用这个函数，也就是执行它。
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function  # 返回 inner_function 函数对象

closure = outer_function(10)
print(closure(5))  # 输出: 15
# 以上代码的解释：outer_function 函数返回 inner_function 函数对象，而不是执行它。closure 变量保存了 inner_function 函数对象，并且 x 的值被捕获在闭包中。当我们调用 closure(5) 时，实际上是在调用 inner_function(5)，并将 x 的值（10）和 y 的值（5）相加。


