# 上一次学习了夹具函数fixture的params参数的用法，知道了夹具函数不是直接用在测试函数上。这一次我们学习直接用在测试函数上的装饰器
# parametrize为测试函数提供多组参数，使测试函数针对每组参数重复执行。
import pytest

# 单个参数的参数化
@pytest.mark.parametrize("single",['a','b','c'])
def test_single(single): # 此处的参数名需要和装饰器中的参数名一致
    print(single)

# 多个参数的参数化
@pytest.mark.parametrize("first,second,expected",[(1,2,3),(2,3,5),(3,4,7)])
def test_double(first,second,expected):
    assert first + second == expected