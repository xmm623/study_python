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
        self.name = name #实例属性:每个实例独有
        self.age = age
    # 类方法：使用@classmethod装饰器定义，cls：代表类本身,
    @classmethod
    def from_birth_year(cls, name, birth_year): # 此类方法的用途是通过类方法创建实例，此方法称为工厂方法
        return cls(name, 2023 - birth_year)
    @classmethod
    def set_species(cls, species): # 此类方法的用途是修改类属性
        cls.species = species
        print(cls)
    @staticmethod
    def bark(times): # 静态方法：不需要访问类或实例属性的方法，通常用于工具函数,静态方法不需要self或cls参数
        for i in range(times):
            print("Woof!")
    # 实例方法：类中定义的函数，称为方法，self：代表实例本身，必须作为方法的第一个参数
    def description(self):
        print(self) # self指向实例对象
        return f"{self.name} is {self.age} years old."

# 创建对象（实例）：
my_dog = Dog("Buddy", 3) # 创建一个Dog类的实例，传入参数"Buddy"和3 
his_dog = Dog("Max", 5) # 创建另一个Dog类的实例，传入参数"Max"和5
her_dog = Dog.from_birth_year("Lucy", 2017) # 使用类方法创建实例，传入参数"Lucy"和2017
print(my_dog.description()) # 输出: Buddy is 3 years old.
print(her_dog.description()) # 输出: Lucy is 6 years old.
print(my_dog.species) # 输出: Canis familiaris
# 访问实例属性
print(my_dog.name) # 输出: Buddy
# 修改类属性（通过类修改）：修改之后所有实例访问该类的属性都会受到影响
Dog.species = "Canis lupus familiaris" # 修改类属性
print(my_dog.species) # 输出: Canis lupus familiaris
Dog.set_species("Canis lupus familiaris hhh") # 修改类属性
print(my_dog.species) # 输出: Canis lupus familiaris hhh
# 修改类属性（通过实例修改）：修改后只有该实例访问该类的属性会受到影响，其他实例访问该类的属性不会受到影响
my_dog.species = "Canis lupus" 
print(my_dog.species) # 输出: Canis lupus
print(his_dog.species) # 输出: Canis lupus familiaris
# 修改实例属性
my_dog.age = 4 # 修改实例属性
print(my_dog.description()) # 输出: Buddy is 4 years old.
my_dog.bark(3) # 调用静态方法，输出: Woof! Woof! Woof!
# 三种方法的使用场景：
# 1. 实例方法：用于操作实例属性，通常用于对象的行为
# 2. 类方法：用于操作类属性，通常用于工厂方法或修改类属性
# 3. 静态方法：用于不需要访问类或实例属性的方法，通常用于工具函数

    


