"""用户"""

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






