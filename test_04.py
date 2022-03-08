# class Dog:
#     """一次模拟小狗的简单尝试"""
#     def __init__(self,name,age):
#         """初始化属性name和age"""
#         self.name = name
#         self.age = age

#     def sit(self):
#         """模拟小狗收到命令时蹲下"""
#         print(f"{self.name} is now sitting.")

#     def roll_over(self):
#         """模拟小狗收到命令时打滚"""
#         print(f"{self.name} rolled over!")

# my_dog = Dog("Willie",6)
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()

# class Restaurant:
#     """餐馆"""
#     def __init__(self,restaurant_name,cuisine_type):
#         """初始化属性restaurant_name和cuisine_type"""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         """打印餐馆名和餐饮类型"""
#         print(self.restaurant_name)
#         print(self.cuisine_type)

#     def open_restaurant(self):
#         """打印正在营业"""
#         print("正在营业")

# my_res = Restaurant("xiebaohuang",'hanberger')
# my_res.open_restaurant()
# my_res.describe_restaurant()
# print(my_res.cuisine_type)

class User:
    """用户"""
    def __init__(self,first_name,last_name,age):
        """初始化属性first_name,last_name"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        """打印用户信息摘要"""
        print(f"user_name: {self.first_name} {self.last_name}")
        print(f"\nUser age: {self.age}")

    def greet_user(self):
        """个性化问候"""
        print(f"\nHello,{self.first_name} {self.last_name}")

# new_user = User('haha','hehe',23)
# new_user.describe_user()

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        """将里程表读数设置为指定的值
        禁止里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

# my_new_car  = Car('audi','a4',2019)
# print(my_new_car.get_descriptive_name())
# # my_new_car.odometer_reading = 23  # 通过实例直接修改属性值

# my_new_car.update_odometer(23_500)
# my_new_car.read_odometer()

# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()

class Restaurant:
    """餐馆"""
    def __init__(self,restaurant_name,cuisine_type):
        """初始化属性restaurant_name和cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """打印餐馆名和餐饮类型"""
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        """打印正在营业"""
        print("正在营业")

    def set_number_served(self,number):
        """设置就餐人数"""
        self.number_served = number

    def increment_number_served(self,increment_number):
        """就餐人数递增"""
        self.number_served += increment_number


# restaurant = Restaurant("hanbaohuang",'hanbao')
# restaurant.set_number_served(10)
# restaurant.increment_number_served(20)
# print(restaurant.number_served)

# class User:
#     """用户"""
#     def __init__(self,first_name,last_name,age):
#         """初始化属性first_name,last_name"""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.login_attempts = 0

#     def describe_user(self):
#         """打印用户信息摘要"""
#         print(f"user_name: {self.first_name} {self.last_name}")
#         print(f"\nUser age: {self.age}")

#     def greet_user(self):
#         """个性化问候"""
#         print(f"\nHello,{self.first_name} {self.last_name}")

#     def increment_login_attempts(self):
#         """增加登陆次数"""
#         self.login_attempts = self.login_attempts + 1

#     def reset_login_attempts(self):
#         """"重置登录次数"""
#         self.login_attempts = 0

# new_user = User('haha','hehe',23)
# for i in range(5):
#     new_user.increment_login_attempts()
#     print(new_user.login_attempts)

# new_user.reset_login_attempts()
# print(new_user.login_attempts)

class Battery:
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self,battery_size=75):
        """初始化电瓶属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f"This car has a {self.battery_size} -KWH battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """检查电瓶容量，不足100则设为100"""
        if self.battery_size < 100:
            self.battery_size = 100

class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self,make,model,year):
        """初始化父类属性"""
        super().__init__(make,model,year)
        # 可以理解为，先定义一个类都有的__init()方法，然后方法需要属性，属性哪来呢，需要当前定
        # 义的子类去继承父类，super()。init就是把父类中一系列属性都拉过来
        self.battery = Battery()

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f"This car has a {self.battery_size} -KWH battery.")


my_tesla = ElectricCar('tesla','model s',2019)
print((my_tesla.get_descriptive_name()))
my_tesla.battery.describe_battery()  # 这里的battery是一个对象（实例），
# my_tesla.battery.describe_battery()表示的是，my_tesla实例对象的battery属性，在这里
# battery属性是一个实例化对象，是从Battery类中创造的实例，该实例中有describe_battery方法。
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# class IceCreamStand(Restaurant):
#     """冰淇淋小店"""
#     def __init__(self,restaurant_name,cuisine_type):
#         """初始化父类属性"""
#         super().__init__(restaurant_name,cuisine_type)
#         self.flavors = ['xiangcao','chocolate','milk']

#     def show_icecream(self):
#         """显示冰淇淋"""
    
#         for flavor in self.flavors:
#             print(f"{flavor} Icecream")

# binqil = IceCreamStand('binqilin','american')

# binqil.show_icecream()

class Privileges():
    """权限"""
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']

    def show_privileges(self):
        """打印管理员的权限"""
        print("This Privileges are:")
        for privilege in self.privileges:
            print(f"\n{privilege}")


class Admin(User):
    """管理员"""
    def __init__(self,first_name,last_name,age):
        """初始化父类属性"""
        super().__init__(first_name,last_name,age)
        self.privileges = Privileges()

    

# Admin_ausin = Admin('yase','chen',28)
# Admin_ausin.privileges.show_privileges()