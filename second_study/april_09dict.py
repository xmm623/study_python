# 字典的定义：可变的，无序的键值对集合，用花括号表示
# 特点：# 1. 键必须是不可变类型（字符串、数字、元组等）
#       2. 键必须是唯一的

# 定义一个字典
person =  {"name":"Alice","age":30,"city":"New York"}
# 创建一个空字典
empty_dict = {}
# 使用dict()函数创建字典
person2 = dict(name = "Bob", age = 25, city = "Los Angeles")
# 创建一个嵌套字典
person3 = {
    "name": "Charles",
    "age": 28,
    "address": {
        "city": "Chicago",
        "state": "Illinois"
    }
}

# 访问字典中的值
print(person["name"])
# 访问嵌套字典中的值
print(person3["address"]["city"])
# 访问不存在的键会引发KeyError
# print(person["country"])  # 会引发错误
# 使用get()方法访问字典中的值
print(person.get("age"))
print(person.get("country", "Not Found"))  # 如果键不存在，返回默认值

# 通过键来添加或修改字典中的值
person["age"] = 31 #键存在则是修改
person["country"] = "USA" #键不存在则是添加
print(person)

# 删除字典中的键值对
# 使用del语句
del person["country"]
print(person)
# 使用pop()方法删除键值对，并返回被删除的值
removed_value = person.pop("city")
print(removed_value, person)

# 遍历字典
# 遍历键
for key_print in person:
    print(key_print)
# 遍历值
for value_print in person.values():
    print(value_print)
# 遍历键值对
for key,value in person.items():
    print(key,value)

# 字典的其他操作
# 获取字典的键
keys_list = person.keys()
print(keys_list)
# 获取字典的值
values_list = person.values()
print(values_list)
# 获取字典的键值对
items_list = person.items()
print(items_list)
# 字典的长度
dict_length = len(person)
print(dict_length)
# 清空字典
person.clear()
print(person)




