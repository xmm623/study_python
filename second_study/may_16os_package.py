# os包：提供了与操作系统进行交互的功能，例如操作文件目录、获取环境变量、管理进程等。
import os # 使用之前先导入
# 获取当前工作目录
print(f"当前工作目录:{os.getcwd()}")

# 创建目录
# os.mkdir("new_dir")
# 删除目录
# os.rmdir("new_dir")

# 统计CPU的核心数
print(f"此电脑的CPU核心数：{os.cpu_count()}")

#执行CMD命令
os.system("which python")