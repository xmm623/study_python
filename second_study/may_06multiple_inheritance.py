# 多继承：一个子类继承多个父类
class A:
    def show(self):
        print("A show")
class B:
    def show(self):
        print("B show")
class C(A, B): # C类继承A和B类
    def show(self):
        print("C show")
        super().show() # 调用父类的方法
        B.show(self) # 显式调用B类的方法
c = C()
c.show() # 输出: C show
# # 方法解析顺序（MRO）：Python使用C3线性化算法来确定方法的调用顺序
# # MRO是一个列表，表示类的继承顺序
# # MRO的计算顺序是从左到右，从上到下
# # 1. 首先查找当前类的方法
# # 2. 然后查找父类的方法
# # 3. 如果父类有多个，按照继承顺序查找
