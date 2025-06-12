# requests包：用于发送各种 HTTP 请求（GET、POST、PUT、DELETE 等）。作为软件测试工程师，你可以用它来测试 API 接口、模拟用户请求、验证响应数据等
import requests
url = "https://www.baidu.com"
response = requests.get(url)
print(response.text)  # 打印响应内容
print(response.status_code)  # 打印响应状态码
print(response.headers)  # 打印响应头信息
print(response.cookies)  # 打印响应的 cookies
print(response.elapsed)  # 打印请求耗时
print(response.url)  # 打印最终请求的 URL
print(response.encoding)  # 打印响应的编码方式
print(response.content)  # 打印响应的二进制内容
# print(response.json())  # 如果响应是 JSON 格式，可以直接解析为 Python 对象
# 注意：如果响应不是 JSON 格式，调用 response.json() 会抛出异常
print(response.ok)  # 检查响应是否成功（状态码在 200-400 之间）
print(response.raise_for_status())  # 如果响应状态码不是 200，会抛出 HTTPError 异常
print(response.history)  # 打印请求的历史记录（如果有重定向）


