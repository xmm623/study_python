"""骰子类"""

from random import randint
class Die():
    """骰子"""
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        """打印摇到的点数"""
        
        print(f"摇到的点数为：{randint(1,self.sides)}")

yaoshaizi = Die(20)
for i in range(10):
    yaoshaizi.roll_die()