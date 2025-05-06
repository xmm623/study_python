# 类的概念：类是一个用于创建对象的蓝图。定义了对象的属性和方法。
# 对象是类的实例化。对象是类的具体实现，具有类定义的属性和方法。你可以把类想象成图纸，对象就是根据图纸建造的房子。
# 类的定义：使用class关键字定义类，类名通常以大写字母开头。
# 类的属性：是所有类的实例共享的属性，它定义在类的内部，但是在方法外部。
# 类的方法：是定义在类内部的函数，通常用于操作类的属性。第一个参数通常是self，表示实例本身。
# 声明类：
class Dog:
    # 类属性:通过self.属性名来定义和访问
    species = "Canis familiaris" # 所有实例共享的属性"
    # 初始化方法（构造函数），在创建对象时自动执行，用于初始化对象的属性
    def __init__(self, name, age): # 实例属性必须在__init__方法中定义，__init___是一个特殊的方法，在创建类的实例时会自动调用。
        self.name = name #实例属性
        self.age = age
    # 方法：类中定义的函数，称为方法，self：代表实例本身，必须作为方法的第一个参数
    def description(self):
        return f"{self.name} is {self.age} years old."

# 创建对象（实例）：
my_dog = Dog("Buddy", 3) # 创建一个Dog类的实例，传入参数"Buddy"和3 
# 调用实例方法
print(my_dog.description()) # 输出: Buddy is 3 years old.
# 访问类属性
print(my_dog.species) # 输出: Canis familiaris
# 访问实例属性
print(my_dog.name) # 输出: Buddy
    


