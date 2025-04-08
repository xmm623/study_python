#布尔类型
#只有两个值，True和False
#布尔值的来源
#1.直接赋值
a = True
b = False

#2.比较运算符
c = 10 > 5
d = 10 < 5
e = 10 == 5
f = 10 != 5
g = 10 >= 5
h = 10 <= 5
print(a, b, c, d, e, f, g, h)
#3.逻辑运算符
i = True and False
j = True or False
k = not True
print(i, j, k)
#4.布尔值的转换
#任何非零数字和非空字符串都被认为是True
l = bool(1)  # True
m = bool(0)  # False
n = bool("Hello")  # True
o = bool("")  # False
p = bool([])  # False
q = bool([1, 2, 3])  # True
print(l, m, n, o, p, q)
#5.布尔值在条件语句中的应用
if a:
    print("a is True")
else:
    print("a is False")
if not b:
    print("b is False")
else:
    print("b is True")
if c:   # 注意这里c是布尔值
    # 如果c为True，则执行下面的代码
    print("c is True")
else:
    print("c is False")
#6.布尔值在循环中的应用
count = 0
while count < 5:  # 当count小于5时循环
    print("Count is:", count)
    count += 1  # 每次循环count加1
print("Loop ended. Final count is:", count)

#易错点
# 在条件语句中，布尔值的判断是非常直接的
# 例如，if a: 直接判断a是否为True
# 但是在一些情况下，可能会出现误解
# 例如，if 1: 也是True，因为1被认为是True
# 但是if 0: 是False，因为0被认为是False
# 所以在使用布尔值时要注意
# 1. 不要将非布尔值直接用于条件判断
# 2. 使用bool()函数可以明确地转换为布尔值
# 3. 在循环和条件语句中，布尔值的判断要清晰明了
# 4. 注意逻辑运算符的优先级
# 5. 在使用逻辑运算符时，要注意短路求值
# 6. 短路求值：在使用and和or时，如果第一个条件已经决定了结果，后面的条件就不会被计算
# 例如：
x = 0
y = 10
# 使用and时，如果x为0（False），y的值不会被计算
#首字母大写
#=号和==号的区别