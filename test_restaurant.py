"""餐馆"""

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