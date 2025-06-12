import requests
url_sby_add_book = "https://apiv3.shanbay.com/news/words"

headers = {
    "Authorization": "Bearer auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjIwMDIzNjE5LCJleHAiOjE3NTc0MTE1OTYsImV4cF92MiI6MTc1NzQxMTU5NiwiZGV2aWNlIjoiIiwidXNlcm5hbWUiOiJyZWFkdGVzdDE5IiwiaXNfc3RhZmYiOjAsInNlc3Npb25faWQiOiJlNWYzYjM3YzQ2YTkxMWYwYTQwMjY2YWFiNDBlYjJiMiJ9.pZ9S64HB1n7u8Q9apYWGvoM7OBNP-zGZPCwSHg4EALc",
    "Referer": "https://apiv3.shanbay.com",
    "Origin": "https://apiv3.shanbay.com"
}
cookies = {
    "cookie_csrftoken": "cac8bd5e4d7c5213fa773517fe811218"
}
data = {
	"source_content": "You know that feeling when you're peacefully scrolling through your phone and suddenly spot someone you absolutely do not want to talk to heading straight toward you? ",
	"vocab_id": "ttlkg",
	"sentence_id": "A207565P1217735S1",
	"source_name": "调研显示：这些小事儿，最让人抓狂！",
	"summary": "feeling",
	"business_id": 2,
	"article_id": "jzypx",
	"paragraph_id": "A207565P1217735"
} # 请求体数据，post请求用json传递
response_add_book = requests.post(url_sby_add_book, json=data, headers=headers)
if response_add_book.status_code == 200:
    print("书籍添加成功:", response_add_book.json())
else:
    print("书籍添加失败:", response_add_book.status_code, response_add_book.text)

    # 这个接口肯定会请求失败，因为接口做了很多安全验证，仅作为学习观察用

