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
    
    def __str__(self): # __str__方法是一个魔法函数，当我们使用print（）或者str（）函数打印对象时，python会自动调用这个方法，它的作用是定义对象被打印时的现实内容，使其输出更具可读性。
        return f"这是类A的__str__方法"
    
    
    # def __setattr__(self, name, value): # __setattr__方法是一个魔法函数，当我们给对象的属性赋值时，Python会自动调用这个方法,在这里，name是属性名，value是属性值
    #     if name == "name" and value in ("小明","小红", "小华") or name == "age" and value in(18,20): # 如果属性名是小明或小红，允许赋值
    #          print(f"正在给属性{name}赋值为{value}") # 打印正在赋值的属性名和属性值
    #          super().__setattr__(name, value) # 调用父类的__setattr__方法，确保属性被正确赋值,因为改写了setattr方法，所以在给属性赋值时会自动调用这个方法
    #     else:
    #         raise ValueError(f"属性{name}不允许赋值为{value}") # 否则，抛出异常

    def __delattr__(self, name):
        print(f"正在删除属性{name}")
        super().__delattr__(name)
    
    def __doc__(self): # __doc__方法是一个魔法函数，返回类的文档字符串  
        return "这是类A的文档字符串"
    
    def __name__(self): # __name__方法是一个魔法函数，返回类的名称
        return "A"
    
    def __repr__(self): # __repr__方法是一个魔法函数，返回对象的字符串表示
        return f"属性name的值是{self.name}, age的值是{self.age}"
    

    
    def __eq__(self, other): # __eq__方法是一个魔法函数，当我们使用==运算符比较两个对象时，Python会自动调用这个方法,默认情况下，__eq__方法比较的是对象的内存地址，而不是对象的属性值。self代表当前对象，other代表要比较的对象。
        if isinstance(other, A):
            return self.name == other.name and self.age == other.age    
        return False

    def __ne__(self, other): # __ne__方法是一个魔法函数，当我们使用!=运算符比较两个对象时，Python会自动调用这个方法
        # if isinstance(other, A):
        #     return self.name != other.name or self.age != other.age  # 如果是做这种逻辑判断，那么__ne__方法就没有必要了，因为__eq__方法已经做了这个判断
        # return False  
        return abs(self.value - other.value) >= 0.01 # 当不等判断和相等判断逻辑不一样时，可以使用__ne__方法来实现不等判断的逻辑
    
    def __call__(self, *args, **kwargs): # __call__方法是一个魔法函数，当我们使用()运算符调用对象时，Python会自动调用这个方法
        print(f"对象{self.name}被调用了")
        return self.name, self.age
    
    def __iter__(self): # __iter__方法是一个魔法函数，当我们使用for循环遍历对象时，Python会自动调用这个方法
        return self # 返回对象本身
    
    def __next__(self): # __next__方法是一个魔法函数，当我们使用next()函数获取对象的下一个值时，Python会自动调用这个方法
        if self.age > 30:
            raise StopIteration      # 如果年龄大于30，抛出StopIteration异常，表示迭代结束
        else:
            num = self.age
            self.age += 2
            return num
        
    def __ge__(self, other): # __ge__方法是一个魔法函数，当我们使用>=运算符比较两个对象时，Python会自动调用这个方法,如果不重写__ge__方法，python会默认使用__lt__和__eq__方法来实现大于等于的比较
        return self.age >= other.age
    
    def __lt__(self, other): # __lt__方法是一个魔法函数，当我们使用<运算符比较两个对象时，Python会自动调用这个方法,如果不重写__lt__方法，python会默认使用对象的内存地址来实现小于的比较
        return self.age < other.age
    
    def __add__(self, other):  #如果不重写add函数，尝试将两个自定义类型的对象相加会导致typeerror
        return self.age + other.age, self.name + '&' + other.name
    
    def __len__(self):
        return len(self.name)

class Task:
    PRIORITIES = {"low": 1, "medium": 2, "high": 3}

    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __gt__(self, other):
        return self.PRIORITIES[self.priority] > self.PRIORITIES[other.priority]

# 使用示例
task1 = Task("清理缓存", "low")
task2 = Task("修复漏洞", "high")
print(f"修复漏洞的优先级是否大于清理缓存？{task2 > task1}")  # 输出: True

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __sub__(self, other):
        if isinstance(other, Date):
            # 简化示例：计算天数差
            days_self = self.year * 365 + self.month * 30 + self.day
            days_other = other.year * 365 + other.month * 30 + other.day
            return days_self - days_other
        return NotImplemented

  
    
# 使用示例
d1 = Date(2023, 10, 1)
d2 = Date(2023, 9, 1)
print(f"两个时间点之间的天数是{d1 - d2}")  # 输出: 30（简化计算）


a = A("小明", 18) # 创建一个对象,会自动调用__init__方法

# del a # 删除对象,会自动调用__del__方法

aa = A("小红", 20) # 创建一个对象,会自动调用__init__方法

print(aa) # 打印对象,会自动调用__str__方法，如果__str__方法不存在，则会调用__repr__方法

print(repr(aa),"这是用的repr方法,随时获取类的状态") # 打印对象,会自动调用__repr__方法

# del aa.age # 删除对象的属性,会自动调用__delattr__方法

print(a == aa) # 比较两个对象,会自动调用__eq__方法
print(2 == 2)   # 对于内置类型（例如 int, str, list, dict 等等），当使用 == 操作符进行比较时，Python 使用的是针对这些类型优化过的比较逻辑。只有当你自己定义的类实例之间进行比较时，Python 才会调用这些实例所在类中定义的 __eq__ 方法。

print(a.__dict__) # 打印对象的属性字典,会自动调用__dict__方法

print(aa)
# str魔法函数和repr魔法函数的区别
# str函数在类中未定义时是回退repr函数，目标受众是终端用户，核心要求是可读性。且在定义类是不是必须实现的。按需实现。
# 另外，__repr__方法的目标受众是开发者，核心要求是准确性和无歧义性，调用场景是交互式环境，repr（obj）或日志记录，默认行为时输出类名和内存地址，最好是所有类都重写。
# repr函数的“真相原则”
# class Vector:
#     def __repr__(self):
#         return f"Vector(x={self.x}, y={self.y})"  # 可eval重建
    
# v = Vector(3, 4)
# print(repr(v))  # Vector(x=3, y=4)
#str函数的“友好原则”
# class Vector:
#     def __str__(self):
#         return f"→({self.x},{self.y})"  # 简洁可视化
    
# print(str(v))  # →(3,4)
# 不要用 __repr__ 实现用户界面，也不要用 __str__ 替代调试信息。
result = aa() # 调用对象,会自动调用__call__方法
print(result) # 打印调用结果

counter = A("小华", 18) # 创建一个对象,会自动调用__init__方法
for i in counter: # 遍历对象,会自动调用__iter__方法和__next__方法
    print(i) # 打印遍历结果

print(aa >= a) # 比较两个对象,会自动调用__ge__方法  

print(aa <= a)

print(a < aa)

print(a + aa)

print(f"aa的名字是{len(aa)}位数")