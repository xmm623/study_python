# sys包：提供了访问由python解释器使用或维护的变量，以及与解释器强烈交互的函数
import sys
print(sys.argv) # 获取命令行参数，列表中第一个元素永远是脚本本身的名称（路径）。所以打印的结果就是这个py文件的路径
# 何为命令行参数：python在终端的执行语句，比如python test1.py hello就是一个命令行，参数就是hello.
# 此时我在终端执行python3 may_16sys_package.py hello命令，打印的值就是['may_16sys_package.py', 'hello']
print(sys.version) # 打印python版本号

print(sys.path) # 获取python的模块搜索路径

print(sys.executable) # 获取python解释器的路径

print("准备退出程序咯！")
sys.exit(0) # 退出程序
print("这行不会打印哦，因为在上一个语句中已经退出啦～")