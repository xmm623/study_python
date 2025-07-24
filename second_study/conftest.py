import pytest

def pytest_collection(session):
    print("===正在收集测试用例===")

def pytest_sessionstart(session):
    print("\n=== 测试开始啦！准备中===")

def pytest_terminal_summary(terminalreporter):
    print("\n=== 自定义测试总结 ===")
    print(f"总共执行：{terminalreporter._numcollected} 个用例")
    print(f"通过：{len(terminalreporter.stats.get('passed', []))}")
    print(f"失败：{len(terminalreporter.stats.get('failed', []))}")

# pytest的钩子函数hook是pytest高级用法的一部分，主要用于自定义框架行为，比如控制测试运行流程、生成报告、在测试前后做特殊处理等。定义在根目录的conftest.py文件中，函数名必须以pytest开头