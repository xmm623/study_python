# 单继承：一个子类只继承一个父类。
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")
    def run(self):
        print(f"{self.name} is running.")
class Dog(Animal): # Dog类继承Animal类，子类名后的括号中指定父类名
    pass
# 子类会自动获得父类的属性和方法，包括初始化方法
# Dog类没有定义自己的__init__方法，所以会自动调用父类的__init__方法
dog = Dog("Buddy")
dog.speak() # 输出: Buddy makes a sound.

class Cat(Animal):
    def speak(self): # 重写父类的方法
        print(f"{self.name} meows.")
    def climb(self):
        print(f"{self.name} is climbing.")
        super().run() # 调用父类的方法，使用super()函数
cat = Cat("Kitty")
cat.speak() # 输出: Kitty meows.

class Bird(Animal):
    def __init__(self, name, species): #如果子类有自己的__init__方法，必须调用父类的__init__方法
        super().__init__(name)
        self.species = species
hummingbird = Bird("Hummingbird", "Trochilidae")
print(hummingbird.name) # 输出: Hummingbird 
print(hummingbird.species) # 输出: Trochilidae
hummingbird.eat() # 输出: Hummingbird is eating.
# 继承的好处：
# 1. 代码重用：子类可以直接使用父类的方法和属性，避免重复编写相同的代码。
# 2. 代码组织：通过继承，可以将相关的类组织在一起，形成一个层次结构，便于管理和维护。
# 3. 多态：子类可以重写父类的方法，实现不同的行为，增强了代码的灵活性和可扩展性。
