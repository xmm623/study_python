import pytest


@pytest.fixture(scope="class")
def test_times():
    """
    ceshi
    :return:
    """
    print("调用方法前执行")

class Test_001():
    """
    haha
    """
    def test_01(self,test_times):
        print("测试用例1")

    def test_02(self,test_times):
        print("测试用例2")

class Test_002():
    """
    heheh
    """
    def test_03(self,test_times):
        print("测试用例3")

    def test_04(self,test_times):
        print("测试用例4")