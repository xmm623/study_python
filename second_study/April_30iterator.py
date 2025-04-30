# 迭代器：迭代器（Iterator）是 Python 中用于遍历元素的对象，它允许你逐个访问一个集合（如列表、元组、字典等）中的元素，而不需要直接暴露集合的内部结构。

# 迭代器对象实现了 __iter__() 和 __next__() 方法。__iter__() 方法返回迭代器对象本身，通常这意味着支持迭代的对象（如列表、字符串、字典等）调用 __iter__() 会返回一个迭代器。__next__() 方法返回序列中的下一个元素，当序列结束时，抛出 StopIteration 异常，表示迭代已经完成。

# 如何使用迭代器：
# 在python中，任何实现了__iter__() 和 __next__() 方法的对象都可以被称为迭代器。我们可以使用 for 循环来遍历迭代器，也可以使用 next() 函数手动获取下一个元素，也可以使用iter() 函数获取迭代器对象。
# 例如：
numbers = [1,2,3,4,5,6]
iterator = iter(numbers)  # 获取迭代器对象
print(next(iterator))  # 输出: 1
print(next(iterator))  # 输出: 2
print(next(iterator))  # 输出: 3
# 代码解释：iter(numbers)返回一个迭代器对象iterator，它是列表numbers的迭代器
# dir（iterator）可以查看迭代器对象的所有属性和方法
a = {1,2,3,4,5,"ff"}
print(dir(a))
# 通常，我们不需要手动调用 next() 来遍历迭代器，因为 Python 的 for 循环自动处理了这个过程。for 循环会隐式地调用 __iter__() 来获取迭代器对象，并且在内部使用 __next__() 逐个访问元素，直到没有更多元素时自动处理 StopIteration 异常。
for item in numbers:
    print(item)  # 输出: 1 2 3 4 5 6
# 以上代码的解释：for 循环会自动调用 numbers 的 __iter__() 方法获取迭代器对象，并在每次循环中调用 __next__() 方法获取下一个元素，直到没有更多元素时自动处理 StopIteration 异常。
# 迭代器的应用：
# 使用迭代器处理大数据集：迭代器可以逐个访问元素，而不需要将整个数据集加载到内存中，这对于处理大数据集非常有用。