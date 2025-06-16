# session：
#【持久化cookie】：自动处理服务器返回的cookie并在后续的请求中发送

import requests
from jsonpath import jsonpath as jp
session = requests.Session()
session.headers.update({
    "Authorazation": "Bearer auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUwOTkxMTgwLCJleHAiOjE3NTc0OTYzNDgsImV4cF92MiI6MTc1NzQ5NjM0OCwiZGV2aWNlIjoiIiwidXNlcm5hbWUiOiJhdXRvdGVzdDMiLCJpc19zdGFmZiI6MCwic2Vzc2lvbl9pZCI6IjNhMTEwYTcwNDc2ZjExZjA4YWM2YjY5MTQ5Y2EwMjg0In0.BS8VNqgsK7dQHedMUhcvWsg3jSzRA_YeJOV28lcFy2E"
}) # 创建session并设置全局头

url_sbay_weekly_articles = "https://apiv3.shanbay.com/news/weekly_articles"

response_weekly_articles = session.get(url_sbay_weekly_articles)
weekly_articles_data = response_weekly_articles.json()
for index,article in enumerate(weekly_articles_data["objects"]):
    print(f"第{index+1}篇热门短文：{article['title_cn']}，阅读人数：{article['num_read']}, 完成阅读人数：{article['num_finished']}, 文章长度：{article['length']}")

url_sbay_articles = "http://apiv3.shanbay.com/news/daily_articles"

response_articles = session.get(url_sbay_articles)
print(response_articles.ok) # OK方法用于判断请求是否成功，如果状态码是200-299返回true，否则返回false
try:
    response_articles.raise_for_status() # 状态码不是2开头抛出HTTPError
except requests.exceptions.HTTPError as e:
    print(f"请求失败，错误信息：{e}")
sbay_articles = response_articles.json()
# print(sbay_articles)
print(jp(sbay_articles, "$.[0].date"))
assert jp(sbay_articles, "$.[0].date") == ["2025-06-16"] 
# print(sbay_articles)
for index,article in enumerate(sbay_articles["objects"]):
    print(f"今日短文第{index+1}篇,中文名是:{article['title_cn']}")
