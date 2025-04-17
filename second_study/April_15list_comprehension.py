# 列表推导式
# 基础语法
# [表达式 for 变量 in 可迭代对象 if 条件] 
# ·功能：
#   ·通过一行代码生成一个新的列表，可以包含一个或多个for循环和可选的if条件
# ·组成部分：
#   ·表达式：对可迭代对象中的每个元素进行处理，然后将处理结果添加到新列表中
# 使用场景：需要多次访问且修改结果，数据量不大（数据量过大会占用大量内存），需要列表特有的方法(如sort)
squares = [i*10 for i in range(5)]
print(squares)
fruits = ["芒果","西瓜","樱桃","猕猴桃","羊角蜜","榴莲"]
squares2 = ["我爱吃"+x for x in fruits]
print(squares2,fruits)
squares3 = [i for i in range(100) if i%2==0]
print(squares3)

# 序列生成器
# 基础语法
# (表达式 for 变量 in 可迭代对象 if 条件)
# 功能类似于列表推导式，但是生成的是一个生成器对象，而不是完整的列表，也就是说它不会一次性生成所有的元素，只是预先制造一个生成器，有需要再取，这样可以节省内存
# 使用场景：处理大数据集，只需🏪一次，构建数据处理管道
squares4 = (x for x in range(10000000))
for i in range(10):
    print(next(squares4))
squares5 = sum(y for y in range(10))
print(squares5)     
squares5 = max(y for y in range(10))
print(squares5)         
squares5 = min(y for y in range(10))
print(squares5)      
squares5 = max(z for z in range(1000) if z%2 != 0)
print(squares5)