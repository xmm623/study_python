# 魔法函数：Python 解释器会在特定的操作发生时自动调用这些魔法函数.
class A(object): # 等于class A(object):
    def __init__(self, name, age): # __init__方法是一个魔法函数，初始化对象的属性,创建类的实例时，python会自动调用这个方法
        self.name = name
        self.age = age
        print(f"对象{self.name}被创建了")

    def __del__(self): # __del__方法是一个魔法函数，删除对象时，python会自动调用这个方法
        print(f"对象{self.name}被删除了") # 不过，__del__方法不一定会被调用，因为Python的垃圾回收机制不一定会立即删除对象

    def __doc__(self): # __doc__方法是一个魔法函数，返回类的文档字符串  
        return "这是类A的文档字符串"
    
    def __str__(self): # __str__方法是一个魔法函数，当我们打印一个对象时，Python会自动调用这个方法
        return f"这是类A的__str__方法"
    
    def __repr__(self): # __repr__方法是一个魔法函数，返回对象的字符串表示
        return f"A()"
    
    def __doc__(self): # __doc__方法是一个魔法函数，返回类的文档字符串  
        return "这是类A的文档字符串"
    
    def __name__(self): # __name__方法是一个魔法函数，返回类的名称
        return "A"
a = A("小明", 18) # 创建一个对象,会自动调用__init__方法
del a # 删除对象,会自动调用__del__方法
aa = A("小红", 20) # 创建一个对象,会自动调用__init__方法
print(aa) # 打印对象,会自动调用__str__方法
print(repr(aa)) # 打印对象,会自动调用__repr__方法