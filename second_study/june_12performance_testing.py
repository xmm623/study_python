import requests
import time

def performance_test(url, method='GET', data=None, headers=None, times=10):
    success = 0
    fail = 0
    response_times = []

    print(f"开始对接口 {url} 进行 {times} 次性能测试...\n")

    for i in range(times):
        try:
            start = time.time()
            if method.upper() == 'POST':
                response = requests.post(url, json=data, headers=headers)
            else:
                response = requests.get(url, params=data, headers=headers)
            elapsed = time.time() - start

            response_times.append(elapsed)

            if response.status_code == 200:
                success += 1
                print(f"[{i+1}] 成功 ✅ - 响应时间: {elapsed:.4f} 秒")
            else:
                fail += 1
                print(f"[{i+1}] 失败 ❌ - 状态码: {response.status_code} - 响应时间: {elapsed:.4f} 秒")

        except Exception as e:
            fail += 1
            print(f"[{i+1}] 异常 ❗ - {str(e)}")

    if response_times:
        print("\n📊 测试结果统计：")
        print(f"✅ 成功次数: {success}")
        print(f"❌ 失败次数: {fail}")
        print(f"⏱️ 平均响应时间: {sum(response_times)/len(response_times):.4f} 秒")
        print(f"🚀 最快响应时间: {min(response_times):.4f} 秒")
        print(f"🐢 最慢响应时间: {max(response_times):.4f} 秒")
    else:
        print("无有效响应时间数据，可能全部请求失败。")

# ✅ 使用示例（GET请求）
performance_test(
    url="https://apiv3.shanbay.com/reading/books/aedui/catalogs",  # 你可以换成真实测试接口
    method="GET",
    data={"list_all": 1},
    headers={
        "Authorization": "Bearer auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjIwMDIzNjE5LCJleHAiOjE3NTc0MTE1OTYsImV4cF92MiI6MTc1NzQxMTU5NiwiZGV2aWNlIjoiIiwidXNlcm5hbWUiOiJyZWFkdGVzdDE5IiwiaXNfc3RhZmYiOjAsInNlc3Npb25faWQiOiJlNWYzYjM3YzQ2YTkxMWYwYTQwMjY2YWFiNDBlYjJiMiJ9.pZ9S64HB1n7u8Q9apYWGvoM7OBNP-zGZPCwSHg4EALc"
    },
    times=5
)

# ✅ 使用示例（POST请求）
# performance_test(
#     url="https://httpbin.org/post",
#     method="POST",
#     data={"username": "test", "password": "1234"},
#     times=5
# )
