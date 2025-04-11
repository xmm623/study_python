# for循环：用于遍历可迭代对象（如列表、元组、字符串等）中的每个元素。
# 基本语法：
# for 变量 in 可迭代对象:
#     # 循环体代码
# else: 当循环正常结束时（即没有被break语句提前中断）执行的代码块（可选）。
# 例子：
# 遍历列表中的每个元素
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
# 遍历字符串中的每个字符
for char in "hello":
    print(char)
# 遍历元组中的每个元素
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)
# 遍历字典中的每个键
person = {"name": "Alice", "age": 30, "city": "New York"}
for key in person:
    print(key)
# 遍历字典中的每个值
for value in person.values():
    print(value)
# 遍历字典中的每个键值对
for key, value in person.items():
    print(key, value)
# 遍历集合中的每个元素
colors = {"red", "green", "blue"}
for color in colors:
    print(color)
# 遍历range函数生成的数字序列
for i in range(5):
    print(i)


# 嵌套循环：在一个循环内部嵌套另一个循环。
# 基本语法：
# for 变量1 in 可迭代对象1:
#     for 变量2 in 可迭代对象2:
#         # 循环体代码
# 例子：
# 打印乘法表
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}", end="\t")
    print()
# 遍历二维列表
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# 遍历字典的嵌套结构
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25},
}
for key, value in nested_dict.items():
    print(key)
    for sub_key, sub_value in value.items():
        print(f"  {sub_key}: {sub_value}")  
# 遍历集合的嵌套结构
nested_set = {frozenset({1, 2}), frozenset({3, 4})}
for item in nested_set:
    print(item)
    for sub_item in item:
        print(f"  {sub_item}")
