# __new__魔法函数：是一个 静态方法，它是类实例化（创建对象）的第一步，负责创建实例并分配内存。和init不同的是，new是在对象创建之前调用的，而init是在对象创建之后调用的。__new__方法必须返回一个对象实例，而__init__方法不需要返回任何值。通常情况下，我们不需要重写__new__方法，除非我们需要控制对象的创建过程，比如实现单例模式。
# 应用场景：__new__方法通常用于实现单例模式、元类等高级用法。__init__方法通常用于初始化对象的属性和状态。
# 单例模式：单例模式是一种设计模式，确保一个类只有一个实例，并提供一个全局访问点。单例模式通常用于需要频繁创建和销毁对象的场景（内存优化），比如数据库连接、线程池等。实现单例模式的方法有很多种，最常见的方法是使用__new__方法。
class singleton(object):
    _instance = None # 类变量，存储单例对象的引用

    def __new__(cls, *args, **kwargs): # cls是类本身，args和kwargs是传入的参数
        if not cls._instance: # 如果类变量_instance为空，则创建一个新的实例
            cls._instance = super(singleton, cls).__new__(cls) # 调用父类的__new__方法创建实例
        return cls._instance # 返回类变量_instance的值
    
    def __init__(self, name): # 初始化对象的属性
        self.name = name
        print(f"对象{self.name}被创建了")

# 测试单例模式
a = singleton("小明") # 创建一个对象,会自动调用__new__方法和__init__方法
b = singleton("小红") # 创建一个对象,会自动调用__new__方法和__init__方法
print(a.name) # 打印对象的属性
print(b.name) # 打印对象的属性
print(a is b) # 判断两个对象是否是同一个对象
print(id(a), id(b)) # 打印对象的内存地址
# 以上代码实现了单例模式，确保一个类只有一个实例，并提供一个全局访问点。通过重写__new__方法来控制对象的创建过程，确保只有一个实例被创建。__init__方法用于初始化对象的属性和状态。