# 类反射：动态获取对象信息的方法。何为动态：指在程序运行时，而非编写代码时进行的操作，动态检查的核心特点是：不需要提前知道对象的具体结构，而是根据程序运行时的实际情况来检查和操作对象。
# 预备知识：
# 动态和静态的关键区别：
"""
维度         静态方式                     动态方式
知晓时机    编写代码时已知所有结构        运行时才能确定对象结构
典型代码    obj.fixed_method()        getattr(obj,method_name)()
灵活性      低（修改需要修改源代码）      高（可通过配置改变行为）
错误发现    编码时即可发现               运行时可能会暴露问题
典型应用    常规业务逻辑                框架/插件系统/协议适配
"""
"""
为什么需要动态检查？
1.处理未知对象：当需要操作第三方库或者用户提供的对象时，无法提前知道具体的接口。
2.提高代码的复用性：同一段代码可以处理多种不同类型的对象。
"""
# 核心反射函数
"""
函数/方法	                         作用	                              示例
type(obj)	                     获取对象类型	                 type(42) → <class 'int'>
isinstance(obj, cls)	         检查对象类型	                 isinstance([], list) → True
issubclass(sub, parent)	         检查类继承关系	                  issubclass(bool, int) → True
hasattr(obj, 'attr')	         检查属性是否存在	              hasattr(str, 'split') → True
getattr(obj, 'attr'[, default])	 获取属性值	                     getattr([], 'append') → 方法对象
setattr(obj, 'attr', value)	     设置属性值	                      setattr(obj, 'x', 10)
dir(obj)	                     获取对象所有属性和方法	            dir(str) 查看字符串方法列表
"""
class Animal:
    animal_name = "wangwang"
    def __init__(self, name):
        self.name = name

    

dog = Animal("wang")
print(dir(Animal))  # 获取类的所有属性和方法
print(getattr(Animal,"animal_name")) # 获取animal_name的属性值
print(hasattr(Animal,"animal_name")) # 检查Animal类是否存在animal_name属性
setattr(Animal, "age",1) # 设置Animal类的新属性age
print(getattr(Animal,"age"))
print(type(Animal))
print(isinstance(Animal,type))  #判断Animal类是否是一个类对象（而不是一个普通实例）。（在python中，所有的类本质上都是type类的实例）
print(isinstance(dog,Animal)) # 检查dog对象是不是Animal类的实例
setattr(dog,"simple","spot") # 设置狗的皮肤
print(getattr(dog,"simple"))
all = globals()
print(all)
def jubu():
        jububianliang = 22
        return locals()
print(jubu())
