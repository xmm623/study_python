# 数据类型转换
a = 1
b = 2.6
c = "3"
d = 0
e = ""
# 整数转浮点数
float_a = float(a)
print("type:", type(float_a), "value:", float_a)
# 浮点数转整数，直接截断小数点
int_b = int(b)
print("type:", type(int_b), "value:", int_b)
# 字符串转整数
int_c = int(c)
print("type:", type(int_c), "value:", int_c)
# 字符串转浮点数
float_c = float(c)
print("type:", type(float_c), "value:", float_c)
# 整数转字符串
str_a = str(a)
print("type:", type(str_a), "value:", str_a)
# 浮点数转字符串
str_b = str(b)
print("type:", type(str_b), "value:", str_b)
# 字符串转布尔值
bool_c = bool(c)
print("type:", type(bool_c), "value:", bool_c)
bool_e = bool(e)
print("type:", type(bool_e), "value:", bool_e)
# 整数转布尔值
bool_a = bool(a)
print("type:", type(bool_a), "value:", bool_a)
bool_d = bool(d)
print("type:", type(bool_d), "value:", bool_d)
# 浮点数转布尔值
bool_b = bool(b)
print("type:", type(bool_b), "value:", bool_b)

# 字符串string/元组tuple/列表list/集合set之间相互转换
# 字符串转元组
str_to_tuple = tuple("hello")
print("type:", type(str_to_tuple), "value:", str_to_tuple)
# 字符串转列表
str_to_list = list("hello")
print("type:", type(str_to_list), "value:", str_to_list)
# 字符串转集合
str_to_set = set("hello")
print("type:", type(str_to_set), "value:", str_to_set)
# 元组转字符串
tuple_to_str = "".join(('h','e','l','l','o'))
print("type:", type(tuple_to_str), "value:", tuple_to_str)
# 列表转字符串
list_to_str = "".join(['h','e','l','l','o'])
print("type:", type(list_to_str), "value:", list_to_str)
# 集合转字符串 没必要很少用到
set_to_str = "".join(sorted(set("hello")))
print("type:", type(set_to_str), "value:", set_to_str)
# 元组转列表
tuple_to_list = list(('h','e','l','l','o'))
print("type:", type(tuple_to_list), "value:", tuple_to_list)
# 列表转元组
list_to_tuple = tuple(['h','e','l','l','o'])
print("type:", type(list_to_tuple), "value:", list_to_tuple)
# 集合转列表
set_to_list = list(set("hello"))
print("type:", type(set_to_list), "value:", set_to_list)
# 元组转集合
tuple_to_set = set(('h','e','l','l','o'))
print("type:", type(tuple_to_set), "value:", tuple_to_set)
# 列表转集合
list_to_set = set(['h','e','l','l','o'])
print("type:", type(list_to_set), "value:", list_to_set)
# 集合转元组
set_to_tuple = tuple(set("hello"))
print("type:", type(set_to_tuple), "value:", set_to_tuple)

# 特殊类型转换
# None转布尔值
none_to_bool = bool(None)
print("type:", type(none_to_bool), "value:", none_to_bool)
# eval函数：解析并执行传入的字符串表达式，返回表达式的计算结果
string1 = "1"
string2 = "2.6"
string3 = "1 + 2"
string4 = "None"
string5 = "False"
string6 = "{'abc':123,'222':222}"
string7 = "(1,2,3,'abc')"
string8 = "['list','this',1,2,3,5.6]"
print(type(string1),type(string2),type(string3),type(string4),type(string5),type(string6),type(string7),type(string8),)
string1_eval = eval(string1)
print("eval:", type(string1_eval), "value:", string1_eval)
string2_eval = eval(string2)
print("eval:", type(string2_eval), "value:", string2_eval)
string3_eval = eval(string3)
print("eval:", type(string3_eval), "value:", string3_eval)
string4_eval = eval(string4)
print("eval:", type(string4_eval), "value:", string4_eval)
string5_eval = eval(string5)
print("eval:", type(string5_eval), "value:", string5_eval)
string6_eval = type(string6)
print("eval:", type(string6_eval), "value:", string6_eval)
string7_eval = eval(string7)
print("eval:", type(string7_eval), "value:", string7_eval)
string8_eval = eval(string8)
print("eval:", type(string8_eval), "value:", string8_eval)  
#注意：eval() 函数虽然功能强大，但如果不小心使用，可能会导致严重的安全漏洞。这是因为 eval() 可以执行任意代码，包括恶意代码。

# 隐式类型转换
# Python会自动进行类型转换
x = 1
y = 2.5
z = x + y
print("type:", type(z), "value:", z)
# 布尔值参与运算
bool_x = True
z = bool_x + 2
print("type:", type(z), "value:", z)
