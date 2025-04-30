# 生成器函数:生成器函数与普通函数的区别在于它使用了 yield 关键字，而不是 return。当 yield 被调用时，函数会暂停并返回一个值，函数的状态会被“记住”，下次调用生成器时会从上次返回的位置继续执行。
# 生成器：生成器是一个迭代器，但它与常规的迭代器不同。生成器不需要一次性计算并返回所有的值，而是按需计算每个值并返回，这种方式叫做惰性求值（lazy evaluation）。
# 预备知识：
#next()函数:用于获取迭代器（如生成器、列表、元组等）中的下一个元素。如果迭代器已经遍历完所有元素，再调用next（）函数会跑出stop Iteration异常
# yield关键字：用于定义生成器函数，yield语句会将函数的状态保存下来，并返回一个值。下次调用next()函数时，会从上次yield语句处继续执行
# 生成器表达式：类似于列表推导式，但使用圆括号而不是方括号。生成器表达式会返回一个迭代器，而不是一个列表
# 列表推导式：
[x for x in range(10)]
print(list(x for x in range(10)))  # 输出: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 生成器表达式：
shencheng = (x for x in range(10))
print(next(shencheng))
print(next(shencheng))

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1
# 以上代码的解释：count_up_to 函数是一个生成器函数，它使用 yield 关键字返回一个值。每次调用 next(count_up_to(5)) 时，函数会暂停并返回当前的 count 值，直到达到 max 值为止。
counter = count_up_to(5)
print(type(counter))  # 输出: <class 'generator'>
print(next(counter))  # 输出: 1
print(next(counter))  # 输出: 2
print(next(counter))  # 输出: 3
print(next(counter))  # 输出: 4
print(next(counter))  # 输出: 5 
print(next(counter))  # 抛出 StopIteration 异常，因为已经遍历完所有元素
# print(next(counter))  # 抛出 StopIteration 异常，因为已经遍历完所有元素
# 以上代码的解释：当我们调用 next(counter) 时，生成器函数会从上次 yield 语句处继续执行，直到遇到下一个 yield 语句或函数结束。每次调用 next() 函数时，都会返回下一个值。
# 生成器的优点：
# 1. 节省内存：生成器不会一次性计算并返回所有的值，而是按需计算每个值并返回，这种方式叫做惰性求值（lazy evaluation）。这使得生成器在处理大量数据时更加高效。
# 2. 简化代码：生成器函数的语法比普通函数更简洁，使用 yield 关键字可以轻松实现迭代器的功能。
# 3. 可读性：生成器函数的代码更易于理解，因为它们使用了简单的循环和条件语句，而不是复杂的迭代器类。
# 生成器缺点：
# 1. 只能遍历一次：生成器只能被迭代一次，不能重复使用。如果需要多次使用生成器的值，需要将其转换为列表或其他可重复迭代的对象。
# 2. 状态不可见：生成器的状态是隐式的，无法直接访问。这使得调试和测试变得更加困难。
# 3. 性能：在某些情况下，生成器的性能可能不如列表或其他数据结构，因为它们需要在每次迭代时计算值。

# 生成器与迭代器的区别：
# 生成器是迭代器的一种特殊类型。