"""
异常处理:在python中,异常是指程序在执行过程中发生的错误。
 当这些错误发生时,python解释器会停止程序的正常执行,并抛出一个异常对象,
 如果不进行处理,程序将会崩溃,异常处理机制允许我们捕获并处理这些错误,从而使程序更加健壮和用户友好.

"""
try:
    # 可能引发异常的代码块
    a = 10
    b = 0 
    result = a / b
    print(result)
except ZeroDivisionError:   # 如果try代码块中的代码引发了异常，python会查找匹配该异常类型的except代码块，并执行其中的代码。except子句可以有多个
    print("除数不能是0！")

try:
    value = int("Not an integer")
except ValueError as e:  # as e：将捕获到的异常对象赋值给一个变量，通常命名为e或err，这样就可以访问异常的详细信息
    print(f"Value Error:{e}")
except TypeError as e:
    print(f"Type Error:{e}")

try:
    # 可能引发异常的代码块
    a = 10
    b = 0 
    result = a / b
    print(result)
except ZeroDivisionError:   # 如果try代码块中的代码引发了异常，python会查找匹配该异常类型的except代码块，并执行其中的代码。except子句可以有多个
    print("除数不能是0！")
else:   #  可选子句，如果try中的代码块没有引发任何异常，那么else子句中的代码将被执行
    print(f"计算结果是：{result}")

try:
    # 可能引发异常的代码块
    a = 10
    b = 0 
    result = a / b
    print(result)
except ZeroDivisionError:   # 如果try代码块中的代码引发了异常，python会查找匹配该异常类型的except代码块，并执行其中的代码。except子句可以有多个
    print("除数不能是0！")
else:   
    print(f"计算结果是：{result}")
finally:  # 可选子句，无论try中的代码块是否发生异常，此子句中的代码总是会被执行。通常用于执行清理操作，例如关闭文件或者释放资源
    print("程序运行结束")
    
