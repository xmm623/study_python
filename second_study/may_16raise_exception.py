# 抛出异常：raise ExceptionType(”错误描述“)
def check_age(age):
    if age < 0:
        raise ValueError("年龄不可以是负数")
    elif age < 18:
        print("未成年")
    else:
        print("已成年")

try:
    check_age(-5)
except ValueError as e:
    print(f"捕获到错误：{e}")

# 常见的python内置异常类型
"""
Exception: 所有内置非系统退出异常的基类。
AttributeError: 尝试访问对象没有的属性或方法时引发。
ImportError: import 语句无法找到模块定义时引发。
ModuleNotFoundError: ImportError 的子类，当模块未找到时引发 (Python 3.6+)。
IndexError: 当序列（如列表、元组）的索引超出范围时引发。
KeyError: 当在字典中查找一个不存在的键时引发。
NameError: 尝试使用一个未定义的变量名时引发。
OSError: 当系统函数返回一个与系统相关的错误时引发，例如 I/O 失败。
FileNotFoundError: OSError 的子类，当尝试打开一个不存在的文件或目录时引发。
PermissionError: OSError 的子类，当尝试执行一个没有足够权限的操作时引发。
SyntaxError: 当 Python 解释器遇到语法错误时引发。这种异常通常在程序运行前就会被检测到。
IndentationError: SyntaxError 的子类，当代码缩进不正确时引发。
TypeError: 当操作或函数应用于不兼容类型的对象时引发。
ValueError: 当内置操作或函数接收到类型正确但值不合适的参数时引发。
ZeroDivisionError: 当除法或模运算的第二个参数为零时引发。
RuntimeError: 当检测到一个不属于任何其他类别的错误时引发。
"""
# 异常处理的最佳实践：
"""
1. 只捕获你能预期并知道如何处理的异常
2.保持try代码块尽可能的小
3.提供有意义的错误消息
4.使用finally进行清理，确保资源得到释放
"""
# 自定义异常:继承Exception类，可以创建自定义异常
class MyCustonError(Exception):
    """这是一个自定义的异常类型"""
    def __init__(self, message="发生了一个自定义错误"):
        self.message = message
        super().__init__(self.message)

try:
    # 假设某个条件触发了自定义错误
    raise MyCustonError("这是一个特定的错误信息！")
except MyCustonError as e:
    print(f"捕获到自定义错误：{e}")
