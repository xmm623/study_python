#requests的get请求demo
import requests
import json
u="https://www.testgoup.com/sona/open/advertisement/release/listBanner/1001"
res=requests.get(url=u)
print("action")
print(res.text)
# print(res.status_code)
# print(res.json())
# assert res.json()["status"]==200 #判断接口结果码
# assert res.status_code==405 #判断接口状态码
print("执行成功！")