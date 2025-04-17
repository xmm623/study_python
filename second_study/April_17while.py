# while循环：只要条件满足，就会一直执行代码块
# 基本语法：
# while 条件：
#    # 条件为True时执行的代码
# 例子：想象你有一包薯片，只要袋子里还有薯片，你就继续吃：
chips = 100
while chips != 0:
    print("咔嚓！吃一片香香的薯片")
    chips -= 1
    print(f"还剩{chips}片！")
print("薯片吃完啦！饱饱哒～")
# while循环的三个关键要素：
# 1.初始化条件：设置循环开始前的初始状态
# 2.循环条件：决定是否继续循环的表达式
# 3.更新语句：改变循环条件的代码

# 循环控制语句：break 立刻停止循环；continue，跳过本次循环
# 常见使用场景：不确定次数的循环：
password = ""
while password != "123456":
    password = input("请输入密码：")
    if password != "123456":
        print("密码错误，请重试！")
print("登录成功！")