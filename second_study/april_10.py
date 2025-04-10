# python的运算
# 1.算数运算
a = 10
b = 5
# 加法
add_result = a+b
print("加法结果：", add_result)
# 减法
sub_result = a-b
print("减法结果：", sub_result)
# 乘法
mul_result = a*b
print("乘法结果：", mul_result)
# 除法
div_result = a/b 
print("除法结果：", div_result)
# 整除（向下取整）
floor_div_result = a//b
print("整除结果：", floor_div_result)
# 取余
mod_result = a%b
print("取余结果：", mod_result)
# 幂运算
pow_result = a**b   
print("幂运算结果：", pow_result)
# 算数运算符的优先级
#括号内的表达式最先计算。
#幂运算 (**)。
#乘法 (*)、除法 (/)、整除 (//) 和取模 (%) 具有相同的优先级。
#加法 (+) 和减法 (-)。


# 2.比较运算
# 等于
equal_result = (a == b)
print("等于结果：", equal_result)
# 不等于        
not_equal_result = (a != b)
print("不等于结果：", not_equal_result)
# 大于
greater_result = (a > b)        
print("大于结果：", greater_result)
# 小于
less_result = (a < b)
print("小于结果：", less_result)
# 大于等于
greater_equal_result = (a >= b)
print("大于等于结果：", greater_equal_result)
# 小于等于  
less_equal_result = (a <= b)
print("小于等于结果：", less_equal_result)

# 3.逻辑运算
# 与运算
and_result = (a > 5 and b < 10)
print("与运算结果：", and_result)
# 或运算
or_result = (a > 15 or b < 10)
print("或运算结果：", or_result)
# 非运算
not_result = not(a > 5)
print("非运算结果：", not_result)
# 注意：非空字符串、非零数字和非空集合在逻辑运算中被视为 True，空字符串、0 和空集合被视为 False。

# 4.身份运算
c = 23
d = 23
e = 24
f = e
# is 运算符：用于判断两个变量是否引用自同一个对象（内存地址相同）
is_result = (c is d)
print("is 运算结果：", is_result)
# is not 运算符：用于判断两个变量是否引用自不同的对象（内存地址不同）
is_not_result = (e is not f)
print("is not 运算结果：", is_not_result)
# is和==的区别：
# is 判断的是对象的身份（内存地址），而 == 判断的是对象的值是否相等。
print(id(c), id(d), id(e), id(f))

# 5.成员运算
# in 运算符：用于判断一个元素是否在序列（如字符串、列表、元组）或集合中
list1 = [1, 2, 3, 4]
in_result = (1 in list1)
print("in 运算结果：", in_result)
# not in 运算符：用于判断一个元素是否不在序列或集合中
not_in_result = (5 not in list1)        
print("not in 运算结果：", not_in_result)

