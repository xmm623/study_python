# 列表的定义：列表是 可变的（mutable）、有序的 元素集合，用 方括号 [] 表示。
# 列表的创建
# 创建一个空列表
empty_list = []

# 创建一个有多个元素的列表
fruits = ["apple","banana","cherry","oringe","grape","pear","peach"]

# 创建一个包含不同数据类型的列表
mixed_list = [1,"hello",3.14,True]

# 创建一个嵌套列表
nested_list = [1,[2,3],4,[5,]]

# 使用list（）函数创建列表
string_list = list("hello")
print(string_list)

# 列表的访问：通过索引下标访问列表中的元素，索引从0开始。
print(fruits[1]) # 输出: banana
print(mixed_list[-2])

# 列表的切片，依旧是左闭右开区间
print(fruits[1:4])
print(mixed_list[2:])
print(nested_list[-2:])
print(nested_list[::])

# 列表中的元素可以被修改
fruits[4] = "kiwi"
print(fruits)

# 列表的连接：可以用 + 操作符连接两个列表。
list1 = fruits + mixed_list
print(list1)

# 列表的重复：可以用 * 操作符重复列表。
list2 = mixed_list * 2
print(list2)

# 列表的成员资格测试：使用 in 和 not in 操作符检查元素是否在列表中。
print("banana" in fruits)   # 输出: True
print(3.14 not in mixed_list)

# 列表的长度：使用len()函数获取列表的长度
print(len(mixed_list))

# 列表的常用方法
# append()方法：在列表的末尾添加一个元素
mixed_list.append("new_item")
print(mixed_list)

# extend()方法：将一个可迭代对象的元素添加到列表的末尾
mixed_list.extend([23,"45",(7,8),3.45])
print(mixed_list)

# insert()方法：在指定索引位置插入一个元素
# 格式：list.insert(index,element)，其中，index是索引的下标，element是要插入的元素
mixed_list.insert(0,"first_element")
print(mixed_list)

# remove()方法：删除列表中第一个匹配的元素
mixed_list.remove("first_element")
print(mixed_list)

# pop()方法：删除指定索引位置的元素，并返回该元素，默认删除最后一个元素
removed_item = mixed_list.pop()
print(removed_item)
print(mixed_list)
removed_item2 = mixed_list.pop(0)
print(removed_item2)
print(mixed_list)

# clear()方法：清空列表中的所有元素
mixed_list.clear()
print("mixed_list = ",mixed_list)

# 列表的排序：使用sort()方法对列表进行排序
# 注意：sort()方法会修改原列表
# 默认情况下，sort()方法是升序排序
digits = [5,8,1,3,0.8,7.5,1.9,2.5,-8.4,-7,-1,-1.5]
strings = ["hahah","123","2","89",[2,3,4,5,"hah","34","4.5"],(1,2,3,"34")]
digits.sort()
print(digits)
# reverse参数控制升序或降序，True表示降序，False表示升序 
digits.sort(reverse = True)
print(digits)
# key参数指定排序的关键字函数
digits.sort(key=int)    #int()函数将元素转换为整数进行排序
print(digits)

digits.sort(key=abs)    #abs()函数将元素转换为绝对值进行排序
print(digits)

strings.sort(key=len)    #len()函数将元素转换为长度进行排序
print(strings) #注意，int类型的元素不可以用len()函数进行排序

# 反转列表：使用reverse()方法反转列表中的元素
digits.reverse()
print(digits)

# 列表的复制：使用切片或copy()方法复制列表
list3 = digits.copy() #个人认为直接赋值也可以达到复制的效果
print("list3 = ", list3)

# 访问嵌套列表中的元素
nested_list = [1,[2,3],4,[5,6]]
print(nested_list[1][1])

# 列表的解包：可以将列表中的元素赋值给多个变量。
a, b, c = fruits[1:4]
print(a, b, c)  # 输出: banana cherry oringe

# 列表与字符串的转换
# 使用join()方法将列表转换为字符串
joined_text = "+".join(fruits)
print(joined_text)  # 输出: apple+banana+cherry+oringe+grape+pear+peach

# 使用split()方法将字符串转换为列表
text = "apple+banana,cherry+oringe"
split_list = text.split("+")
print(split_list)  # 输出: ['apple', 'banana,cherry', 'oringe']

