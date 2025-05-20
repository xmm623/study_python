# json包：用于解析和生成json数据
# 将字典转换为json字符串
import json
data = {"key": "value"}
json_str = json.dumps(data)
print(type(json_str),json_str)  # <class 'str'> {"key": "value"}

# 将json字符串转换为字典
json_data = json.loads(json_str)
print(type(json_data), json_data)  # <class 'dict'> {'key': 'value'}