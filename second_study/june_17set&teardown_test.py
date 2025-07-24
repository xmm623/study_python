# 优先并尽可能地使用 Fixtures。它们是 Pytest 的精髓所在，提供了无与伦比的灵活性、模块化和可复用性。只有在维护一些非常古老的、遵循 xUnit 风格的项目时，或者在编写极其简单的测试脚本时，才考虑使用 xUnit 风格的 setup/teardown 函数。
# 在 pytest 中，setup 和 teardown 机制用于在测试之前进行必要的准备工作（如初始化环境、准备数据），以及在测试之后清理资源（如关闭连接、删除临时文件）。这种机制确保每个测试用例都在一个干净的环境中运行，避免了测试之间的相互影响。
# pytest 提供了几种不同的方式来实现 setup 和 teardown 操作，主要包括：fixture函数，类级别的setup/teardown方法，模块级别的setup/teardown方法，但是，最好还是使用fixture，灵活性更高
# fixture的作用域：
"""
scope='function':(默认)每个测试函数都执行一次
scope='slass':每个测试类执行一次
scope='module'：每个模块（文件）执行一次
scope-'session‘:整个测试会话（运行pytest命令）只执行一次
"""
import pytest

class Calculator:
    def add(self,a,b):
        return a+b
    

@pytest.fixture(scope='module')
def module_setup_teardown():
    """
    一个模块级的fixture
    """
    print("\n---[Fixture-Module]开始执行模块测试---")
    yield
    print("\n---[Fixture-Module]模块测试执行完毕---")

@pytest.fixture(scope='function') 
def calculator_instance():
    """
    一个函数级的fixture，为每个测试创建一个Calculator实例
    """
    print("\n-[Fixture-Function]创建Calculator实例-")
    calc = Calculator()
    yield calc # yield将实例提供给测试函数，当测试函数需要 calculator_instance 这个 fixture 时，pytest 会先执行到 yield calc，把 calc 作为参数传递给测试函数。
    # 每当执行到 yield 语句时，函数会暂停并返回一个值给调用者。当然，返回的这个值可以没有，当再次从生成器请求值时，函数会从上次暂停的地方继续执行，而不是从头开始。
    # 它是实现 Setup/Teardown 的利器：当 yield 只用一次时，它之前的代码是 Setup，之后的代码是 Teardown，非常适合资源管理，这也是它在 pytest fixtures 和上下文管理器中的核心用法。
    print("\n-[Fixture-Function]清理Calculator实例-")

def test_addition(calculator_instance,module_setup_teardown): # 就算模块级的名字放在后面，也是模块级的装饰器先调用
    """
    测试函数讲fixture名称作为参数
    pytest会自动查找并执行这些fixture
    """
    assert calculator_instance.add(2,3) == 5

def test_subtraction(module_setup_teardown):
    pass

@pytest.mark.usefixtures("module_setup_teardown") # 这个装饰器的作用是让指定的 fixture （括号中的fixture就是指定的）在测试类或测试函数执行前自动运行，但不会把 fixture 的返回值（yield 的值）传递给测试方法。另外，这个测试标记是多余的，因为高作用域（如 module 或 session）的 fixture 只要在它的作用域内被任何一个测试请求（无论是通过参数还是 usefixtures），它就会对整个作用域生效。这是使用夹具函数的另一种方式。
class TestCalculatorWithFixtures:

    @pytest.fixture(scope='class')
    def class_scoped_calculator(self):
        """
        一个类级别的fixture
        """
        print("\n--[Fixure-Class]为测试类创建一个共享的Calculator实例--")
        return Calculator()
    
    def test_add_positive(self,class_scoped_calculator):
        assert class_scoped_calculator.add(5,5) == 10

    def test_add_negative(self,class_scoped_calculator):
        assert class_scoped_calculator.add(-3,-4) == -7

# autouse=True：测试方法自动执行 fixture 的前后置逻辑，但不会把 yield 的值传给测试函数。此实例中yield要传参，所以不适用autouse参数。可以理解为自动调用属性。
#只有把 fixture 名字写在测试函数参数里（显示调用），pytest 才会把 yield 的值（比如 calc）传递进来。
"""
按资源类型选择调用方式
Fixture 类型	推荐调用方式	适用场景
昂贵资源	模块级 + autouse	数据库连接、HTTP 会话
共享数据	类级 + 显式调用	测试数据集、配置信息
环境准备	方法级 + autouse	临时文件、重置状态
特殊依赖	方法级 + 显式调用	需要灵活控制的资源
"""
# 对于未设置 autouse=True 的 fixtures，需要在测试方法中显式声明才能使用，所以一般模块级的fixture与autouse连用。
"""
你可以为 fixture 定义不同的作用范围：

function：每个测试函数调用一次（默认）
class：每个测试类调用一次
module：每个模块调用一次
session：整个测试会话期间只调用一次
虽然官方为fixture定义了不同的作用范围，但是还是要显示/自动调用，鸡肋！
调用这些fixture的优先级从下往上
"""