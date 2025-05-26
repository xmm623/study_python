# re包：提供对正则表达式的支持，使得你可以执行复杂的字符串搜索、替换等操作。
# 正则表达式基础
"""
字符匹配：
 . 英文点号：匹配除换行符外的任意单个字符
\d 匹配任何数字字符【0-9】
\D 匹配任何非数字字符
\w 匹配字母、数字、下划线
\s 匹配空白字符（空格、制表符、换行符等）
\S 匹配非空白字符
（） 将括号内的表达式视为一个整体，可以对这个整体使用量词。
【】定义一个字符集，匹配方括号中列出的任意一个字符。
（）括号内的表达式称为捕获组，正则表达式可以有多个捕获组。可以一次性匹配多个字符。
| 竖线：表示或的关系，匹配竖线两边的任意一个表达式。
^ 匹配字符串的开头
$ 匹配字符串的结尾
"""
"""
数量限定
* 星号：匹配前一个字符0次获多次（前一个字符指的是字符匹配，比如\d,\D这些）
+ 加号：匹配前一个字符1次获多次
？问号：匹配前一个字符0次或1次
{n} :匹配前一个字符恰好n次
{n,}:匹配前一个字符至少n次
{n,m}:匹配前一个字符至少n次，至多m次
"""
# 在python中定义正则表达式时，强烈建议使用原始字符串，即在字符串前加上r。这样做可以避免python本身的转义机制与正则表达式的转义机制发生冲突。
# match对象：match对象包含了匹配的文本，匹配的位置等。
# 如何使用match对象：
# 1. group（index）：如果index是0或不传，返回整个正则表达式匹配到的完整字符串。如果index>0，返回第index个捕获组匹配到的字符串，索引从1开始
# 2.groups（）：返回分组匹配到的内容，从group(1)开始，如果没有分组，则返回空元组。另外，此方法只返回正则表达式匹配到的字符串，不返回完整字符串。
import re
pattern1 = r"\d+"
text1 = "12348888abc456def_789ggg"
result1 = re.match(pattern1,text1)
# 以上代码匹配过程：
# 1.从字符串开头开始匹配，\d+表示匹配1个或多个数字字符，所以匹配到的字符串是“12348888”
print(f"执行re.match命令后，得到的结果是一个match对象：{result1}")  # 返回的是一个match对象
print(result1.group(0))  # 返回匹配的字符串

pipei2 = r"\d+\s\w+\D+ ABC123 \d"
pattern2 = re.compile(pipei2) # 编译正则表达式
text2 = "123 _223asd_&&&: ABC123 0"
result2 = pattern2.match(text2)
if result2: # 如果匹配成功
    print("匹配成功")
    print(f"匹配到的完整字符串:{result2.group(0)}")
    print(f"匹配到的第一个组:{result2.group()}")
    print(f"匹配的起始位置：{result2.start()}")
    print(f"匹配的结束位置：{result2.end()}")
    print(f"匹配的起始和结束位置：{result2.span()}") 
    print(f"匹配的原始字符串：{result2.string}")
else:
    print("匹配失败")
# 以上代码匹配过程：
# 1.从字符串开头开始匹配，\d+表示匹配1个或多个数字字符，所以匹配到的字符串是“123”
# 2.接下来是\s，表示匹配一个空格字符，所以匹配到的字符串是数字123后面的空格。
# 3.接下来是\w+，表示匹配1个或多个字母、数字、下划线，所以匹配到的字符串是“_223asd_”
# 4.接下来是\D+，表示匹配1个或多个非数字字符，所以匹配到的字符串是“&&&: ”。
# 5.接下来是ABC123，表示匹配字符串“ABC123”，所以匹配到的字符串是“ABC123”
# 6.接下来是\d，表示匹配1个数字字符，所以匹配到的字符串是“0”。


pipei3 = r"My name is (\w+) and I am (\d+) years old."
text3 = "My name is Jack and I am 25 years old."
pattern3 = re.compile(pipei3)
result3 = pattern3.search(text3)
if result3:
    print("匹配成功")
    print(f"匹配到的完整字符串:{result3.group(0)}")
    print(f"匹配到的第一个组:{result3.group(1)}")
    print(f"匹配到的第二个组:{result3.group(2)}")
    print(f"匹配到的所有组：{result3.groups()}")
    print(f"匹配的起始位置：{result3.start()}")
    print(f"匹配的结束位置：{result3.end()}")
    print(f"匹配的起始和结束位置：{result3.span()}") 
    print(f"匹配的原始字符串：{result3.string}")
else:
    print("匹配失败")
# 以上代码匹配过程：
# 1.从字符串开头开始匹配，\w+表示匹配1个或多个字母、数字、下划线，所以匹配到的字符串是“Jack”
# 2.接下来是\d+，表示匹配1个或多个数字字符，所以匹配到的字符串是“25”。
# 3.接下来是years old.，表示匹配字符串“years old.”，所以匹配到的字符串是“years old.”。



# 提前编译正则表达式：通过re.compile()函数会创建可复用的正则表达式对象，提高性能。
# 常用方法：和re模块中的方法一致,但是使用正则表达式对象调用。
# match(pattern,string)方法：从字符串开头开始匹配，失败返回None。
# search（pattern，string）方法：在字符串任意位置搜索第一个匹配，失败返回None。
# findall（pattern，string）方法：查找所有匹配的子串，返回字符串列表
# finditer（。。。）：查找所有匹配，返回迭代器，每个元素是match对象。
# match对象的常用属性和方法：
# start()：返回匹配的起始位置
# end()：返回匹配的结束位置
# span()：返回匹配的起始和结束位置
# string():获取原始匹配的字符串



# 分组命名：在标准的捕获组中，我们通过数字索引（如 group(1)、group(2)）来引用捕获到的内容。当正则表达式变得复杂，或者有大量的捕获组时，仅仅依靠数字索引会变得非常难以阅读和维护，因为你很难记住 group(3) 到底代表什么。
# 为了解决这个问题，正则表达式引入了命名捕获组。它允许你为捕获组指定一个有意义的名称，然后通过这个名称来引用捕获到的内容。
# 命名捕获组的语法是在常规捕获组的左括号 ( 后面加上 ?P<name>，其中 name 是你为该组定义的名称。
# (?P<name>...) ...: 这是你希望捕获的正则表达式模式。


text2 = "Name: Bob, Age: 25"
pattern_named = r"Name: (?P<person_name>\w+), Age: (?P<person_age>\d+)"

match_named = re.search(pattern_named, text2)

if match_named:
    # 直接通过名称访问，代码更清晰
    name = match_named.group("person_name")
    age = match_named.group("person_age")
    print(f"命名捕获 - 名字: {name}, 年龄: {age}")

    # 当然，你仍然可以通过索引访问 (索引顺序按从左到右的括号出现顺序)
    print(f"命名捕获 - 索引访问 名字: {match_named.group(1)}, 年龄: {match_named.group(2)}")

    # 命名捕获组也可以在 groups() 方法中出现
    print(f"所有捕获组 (包括命名): {match_named.groups()}")

    # 获取命名捕获组的字典
    print(f"命名捕获组字典: {match_named.groupdict()}")

"""
总结
分组 () 在正则表达式中扮演着多重关键角色：
捕获匹配到的子字符串，方便后续提取和使用。
将一系列字符视为一个整体，以便对其应用量词。
限定“或”操作符 | 的作用范围，实现复杂的选择逻辑。
"""
