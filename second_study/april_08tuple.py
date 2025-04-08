# 元组的定义：元组是不可变（immutable）的有序序列，用圆括号 () 表示。
# 创建元组的3种方式
# 1. 使用圆括号直接创建
tuple1 = (1, 2, 3)
# 2. 使用tuple()函数创建
tuple2 = tuple([4, 5, 6])
# 3. 创建只有一个元素的元组时，必须在元素后加逗号
tuple3 = (7,)
# 4. 创建空元组
tuple4 = ()
# 5.省略圆括号创建元组
tuple5 = 8, 9, 10

# 元组的访问：通过索引访问元组中的元素，索引从0开始。
print(tuple1[0])  # 输出: 1
print(tuple2[1])  # 输出: 5

# 元组的切片：可以使用切片操作访问元组的一部分。
print(tuple1[1:3])  # 输出: (2, 3),也是左闭右开区间
print(tuple2[-2:]) # 输出: (5, 6)
# 元组的不可变性：元组中的元素不能被修改。

# 尝试修改元组中的元素会引发错误
# tuple1[0] = 10  # TypeError: 'tuple' object does not support item assignment

# 元组的连接：可以使用 + 操作符连接两个元组。
tuple6 = tuple1 + tuple2
print(tuple6)  # 输出: (1, 2, 3, 4, 5, 6)

# 元组的重复：可以使用 * 操作符重复元组。
tuple7 = tuple2 * 3
print(tuple7) # 输出: (4, 5, 6, 4, 5, 6, 4, 5, 6)

# 元组的成员资格测试：使用 in 和 not in 操作符检查元素是否在元组中。
print(4 in tuple1)
print(4 in tuple2)  # 输出: True
print(10 not in tuple1)  # 输出: True

# 元组的长度：使用 len() 函数获取元组的长度。
print(len(tuple2))

# 元组的嵌套：元组可以包含其他元组。
tuple8 = (1, (2, 3), (4, 5))
print(tuple8[1]) # 输出: (2, 3)

# 元组的解包：可以将元组中的元素赋值给多个变量。
a,b,c = tuple2
print(a,b,c)    # 输出: 4 5 6

# 元组的方法
# 元组的方法很少，主要有count()和index()方法。
# count() 方法：返回指定元素在元组中出现的次数。
tuple9 = (1, 2, 3, 2, 1)
print(tuple9.count(9))  # 输出:2

# index() 方法：返回指定元素在元组中第一次出现的索引。  
print(tuple9.index(2))  # 输出: 1
# 注意：如果元素不存在，index() 方法会引发 ValueError。
try:
    print(tuple9.index(9))  # 会引发 ValueError
except ValueError as e:
    print(e)
# max() 和 min() 方法：可以获取元组中的最大值和最小值。
print(max(tuple9))
print(min(tuple9))