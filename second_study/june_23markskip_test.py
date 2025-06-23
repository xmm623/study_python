# pytest 的标记系统（mark）是一个强大的功能，允许你为测试用例添加元数据，从而实现对测试用例的分类、筛选和特殊处理。
import pytest

api_version = 1.0
# 无条件跳过测试
@pytest.mark.skip(reason="功能尚未完成")
def test_skip_example():
    print("已经被跳过，不会被打印")

# 满足条件时跳过测试
@pytest.mark.skipif(api_version >2.0, reason="接口版本号大于2.0就需要跳过此用例")
def test_skipif_example():
    print("不满足跳过条件，会被执行")

