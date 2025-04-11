# if else条件判断语句
# if 条件：
    # 条件值为真时执行的语句
person = "Alice"
if person == "Alice":
    print("你好，Alice")

# if 条件：
#     条件值为真时执行的语句
# else：
#     条件值为假时执行的语句
age = 18
if age >= 18:
    print("你已经成年了")
else:
    print("你还未成年")

# if elif else条件判断语句
# if 条件1：
#     条件1值为真时执行的语句
# elif 条件2：
#     条件2值为真时执行的语句
# else：
#     条件值为假时执行的语句
score = 85
if score >= 90:
    print("成绩优秀")
elif score >= 80:
    print("成绩良好")
elif score >= 70:
    print("成绩中等")
elif score >= 60:
    print("成绩及格")
else:
    print("成绩不及格")
# 嵌套if语句
age = 20        
if age >= 18:
    print("你已经成年了")
    if age >= 65:
        print("你是老年人")
    else:
        print("你不是老年人")

# 使用布尔表达式
is_student = True
if is_student:
    print("你是学生")
else:
    print("你不是学生")
# 使用逻辑运算符
age = 25
if age >= 18 and age < 65:
    print("你是成年人")
else:
    print("你不是成年人")

# 三元表达式
# 条件为真时返回的值 if 条件 else 条件为假时返回的值
age = 16
status = "成年" if age >= 18 else "未成年"
print("你的状态是:", status)

# 注意：顺序很重要：条件判断是从上到下依次进行的

# 互斥性：一旦某个条件满足，后面的条件不会再判断

# else可选：可以只有if和elif，没有else

# 性能考虑与最佳实践
# 条件顺序优化：将最可能为True的条件放在前面
# 避免深层嵌套：尽量减少嵌套层级，保持代码清晰，超过3层应考虑重构