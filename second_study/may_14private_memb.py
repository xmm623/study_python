# 私有函数、私有变量：不希望被类外部访问的成员，虽然python并没有严格的访问控制，但通过特定的命名约定，可以实现一定程度上的“私有话”。
# 命名约定：单下划线开头：实际上是一个约定，意味着该变量或方法被认为是“内部使用的”，但它仍然可以从外部访问，这是一种弱提示，告诉其他开发者这个成员可能是内部实现细节，不应该直接依赖。
# 双下划线开头：这会触发名称改写，是的变量或方法在类外部难以直接访问。这是为了防止子类意外覆盖基类中的同名成员。
class MyClass:
    def __init__(self):
        self._internal_var = 42 # 弱私有变量

    def _internal_method(self): # 弱私有方法
        return self._internal_var
# 使用示例
obj = MyClass()
print(obj._internal_var)
print(obj._internal_method()) # 可以访问这些变量和方法，但是不建议这样使用

class HisClass:
    def __init__(self):
        self.__private_var = 43 # 强私有变量
    def __private_method(self):
        return self.__private_var
    
obj_his = HisClass()
# print(obj_his.__private_var) #会报错：AttributeError
print(obj_his._HisClass__private_var) # 可以访问，但不建议
# 在类中定义了以双下划线开头的成员时，python会对这些名称进行改写成_ClassName__variable，以避免在继承体系中发生名称冲突。
