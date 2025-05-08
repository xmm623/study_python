# 魔法函数：Python 解释器会在特定的操作发生时自动调用这些魔法函数.
class A(object): # 等于class A(object):
    def __init__(self, name, age): # __init__方法是一个魔法函数，初始化对象的属性,创建类的实例时，python会自动调用这个方法
        self.name = name
        self.age = age
        print(f"对象{self.name}被创建了")

    # def __del__(self): # __del__方法是一个魔法函数，删除对象时，python会自动调用这个方法
    #     print(f"对象{self.name}被删除了") # 不过，__del__方法不一定会被调用，因为Python的垃圾回收机制不一定会立即删除对象

    def __doc__(self): # __doc__方法是一个魔法函数，返回类的文档字符串  
        return "这是类A的文档字符串"
    
    def __str__(self): # __str__方法是一个魔法函数，当我们打印一个对象时，Python会自动调用这个方法
        return f"这是类A的__str__方法"
    
    
    def __setattr__(self, name, value): # __setattr__方法是一个魔法函数，当我们给对象的属性赋值时，Python会自动调用这个方法,在这里，name是属性名，value是属性值
        if name == "name" and value in ("小明","小红") or name == "age" and value in(18,20): # 如果属性名是小明或小红，允许赋值
             print(f"正在给属性{name}赋值为{value}") # 打印正在赋值的属性名和属性值
             super().__setattr__(name, value) # 调用父类的__setattr__方法，确保属性被正确赋值,因为改写了setattr方法，所以在给属性赋值时会自动调用这个方法
        else:
            raise ValueError(f"属性{name}不允许赋值为{value}") # 否则，抛出异常

    def __delattr__(self, name):
        print(f"正在删除属性{name}")
        super().__delattr__(name)
    
    def __doc__(self): # __doc__方法是一个魔法函数，返回类的文档字符串  
        return "这是类A的文档字符串"
    
    def __name__(self): # __name__方法是一个魔法函数，返回类的名称
        return "A"
    
    def __repr__(self): # __repr__方法是一个魔法函数，返回对象的字符串表示
        return f"属性name的值是{self.name}, age的值是{self.age}"
    
    
    def __dict__(self): # __dict__方法是一个魔法函数，返回对象的属性字典
        return self.__dict__
    
    def __eq__(self, other): # __eq__方法是一个魔法函数，当我们使用==运算符比较两个对象时，Python会自动调用这个方法,默认情况下，__eq__方法比较的是对象的内存地址，而不是对象的属性值
        if isinstance(other, A):
            return self.name == other.name and self.age == other.age    
        return False


a = A("小明", 18) # 创建一个对象,会自动调用__init__方法

# del a # 删除对象,会自动调用__del__方法

aa = A("小红", 20) # 创建一个对象,会自动调用__init__方法

print(aa) # 打印对象,会自动调用__str__方法，如果__str__方法不存在，则会调用__repr__方法

print(repr(aa),"这是用的repr方法，随时获取类的状态") # 打印对象,会自动调用__repr__方法

# del aa.age # 删除对象的属性,会自动调用__delattr__方法

print(a == aa) # 比较两个对象,会自动调用__eq__方法
print(2 == 2)   # 比较两个对象,会自动调用__eq__方法
