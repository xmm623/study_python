import requests
from filetools import read_files,write_files

u="https://www.testgoup.com/sona/release/account/getLogin"
req_h={"content-type": "application/json"}
req_d={"type": 1, "phone": "17856165933", "password": "wxy19971211"}



rep2=requests.post(url=u,headers=req_h,json=req_d)
print(rep2.text)
assert rep2.status_code==200
print(rep2.json()["data"][0]["status"]) 
# assert rep2.json()["data"]["status"]==1
print(rep2.json())
token=rep2.json()["data"][0]["token"]
print(token)
write_files("/Users/weixiaoyu/Downloads/test.txt",token)
f=read_files("/Users/weixiaoyu/Downloads/test.txt")
print("取出的token为：",f)

# {"code":1,
# "msg":"登录成功",
# "data":[{"token":"ge8JlOzPAtZis0Q95ywXenNqF8CSaaAIqpyfcN/zo9HVMhdB4qdhfMSzq0q0uGSv",
# "status":1}]}