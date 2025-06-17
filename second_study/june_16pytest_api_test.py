import requests


session = requests.Session()
session.headers.update({
    "Authorazation": "Bearer auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjIwMDIzNjIwLCJleHAiOjE3NTc4MzcxNDIsImV4cF92MiI6MTc1NzgzNzE0MiwiZGV2aWNlIjoiIiwidXNlcm5hbWUiOiJyZWFkdGVzdDIwIiwiaXNfc3RhZmYiOjAsInNlc3Npb25faWQiOiJiMzIyNzJiNjRhODgxMWYwOTk0ZjEyNWRhZWQxZjk5NCJ9.LZ6PIJFnPfbkDU4YxqqVmfZtUo50JYwlghHnZg_ZlCQ"
})

url_sbay_weekly_articles = "https://apiv3.shanbay.com/news/weekly_articles"
response_weekly = session.get(url_sbay_weekly_articles)
class TestDemo:
    def test_api_publish_status(self):
        
        for article in response_weekly.json()["objects"]:
            assert article["publish_status"] == 1

    def test_api_free_for_membership(self):  
        for article in response_weekly.json()["objects"]:
            if article["length"] > 500: # 一般来说，字数在500字以上的都是精讲短文
                assert article["free_for_membership"] is True
            else:
                assert article["free_for_membership"] is False

if __name__ == "__main__":
    import pytest
    pytest.main()

"""

```python
if __name__ == "__main__":
    pytest.main()
```

这是一个 Python 中常用的惯用写法，让我解释一下：

1. `if __name__ == "__main__":` 是一个条件判断，用来检查当前文件是否作为主程序运行
   - 当这个文件被直接运行时（比如 `python june_16pytest_api_test.py`），`__name__` 的值会是 `"__main__"`
   - 当这个文件被其他文件导入时，`__name__` 的值会是模块名

2. `pytest.main()` 是启动 pytest 测试框架的命令
   - 这行代码会执行当前文件中所有的测试用例
   - 在你的代码中，它会运行 `TestDemo` 类中的两个测试方法：
     - `test_api_publish_status()`
     - `test_api_free_for_membership()`

简单来说，这段代码的作用是：当你直接运行这个文件时，它会自动执行所有的测试用例。这是一个很方便的方式来运行测试，不需要在命令行中手动输入 `pytest` 命令。
"""