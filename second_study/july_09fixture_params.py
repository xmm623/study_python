# 在pytest中，夹具函数的params参数允许你为夹具提供多个参数值，使测试能够针对不同参数值重复执行。这是实现数据驱动测试的核心机制之一，尤其适合测试需要覆盖多种输入场景或外部环境的情况。

# 示例1：你要测试一个接口/get_user_info,需要测试不同用户角色（admin、user、guest）登陆后返回的数据结构，权限，字段都不同。
# 方法一（每个角色写一条测试函数）：
# def test_admin():
#     token = login("admin", "admin123")
#     res = call_api(token)
#     assert res["role"] == "admin"

# def test_user():
#     token = login("user", "user123")
#     res = call_api(token)
#     assert res["role"] == "user"

# def test_guest():
#     token = login("guest", "guest123")
#     res = call_api(token)
#     assert res["role"] == "guest"
# 以上方法重复性太强，不好维护。

# 方法二（使用fixture+params参数）
import pytest

# def login(username, password):
#     print(f"登录用户：{username}")
#     return f"token_for_{username}"

# @pytest.fixture(params=["admin", "admin123", "user", "user123","guest", "guest123"], ids=["管理员","普通用户","游客"])
# def login_token(request):
#     username,password = request.param
#     return login(username,password)

# def test_get_user_info(login_token):
#     token = login_token
#     print(f"用token调用接口:{token}")
#     assert token.startswith("token_for_")

# 举个例子
@pytest.fixture(params=["mimi01","mimi02","mimi03"])
def chuandi(request):
    return request.param # 传递给测试函数要用这个语句

def test_chuandi(chuandi): # 使用fixture的方法时，需要在测试函数中调用该fixture函数
    print(f"传输数据：{chuandi}")

# fixture函数的params参数适用于参数化逻辑需要复杂的初始化或清理时，多个测试函数需要共享同一组参数化逻辑时，或者需要结合不同的作用域时。
# 测试函数pytest.mark.parametrize装饰器适用于参数化逻辑简单，不需要复杂的初始化时。。。