# import test_pizza #使用import方法导入的是一整个模块，没有导入具体的函数，所以需要用模块名.函数名

# test_pizza.make_pizza(16,'pepperoni')
# test_pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')

# from test_pizza import make_pizza  #使用from导入具体的函数就不用句点表示发了，因为已经导入了具体的函数
# make_pizza(16,'aha')

# from test_pizza import make_pizza as mp  # 使用as 给函数指定别名
# mp(15,'haha')

# import test_pizza as p #给模块指定别名
# p.make_pizza(12,'haha')