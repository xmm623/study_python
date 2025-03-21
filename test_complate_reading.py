import basic_functions
import requests


catelog_ids,catelog_lengths = basic_functions.get_book_catelogs_information("btnmfq")   # 跑另一本书时需要修改书籍id
data = {
    "used_time":240
}
# proxy = {
#     "http":"http://192.168.29.157:8888",
#     "https":"http://192.168.29.157:8888"
# }
headers = {"user-agent":"bayAgent/1.1 Android/12 com.mojohi.reading/1.1.602-qa shanbay-channel/0 vivo/V2118A frontend/4.8 api/2.2 device/Mobile",
           "Content-Type":"application/json; charset=UTF-8",
<<<<<<< HEAD
           "cookie":"auth_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6OTcsImV4cCI6MTY2MTM5OTkyOCwiZXhwX3YyIjoxNjYxMzk5OTI4LCJkZXZpY2UiOiIiLCJ1c2VybmFtZSI6Ikdvb2dsZV85Yzk3OTVjNThlNjQ1NTZmIiwiaXNfc3RhZmYiOjAsInNlc3Npb25faWQiOiIzMjMzMjc2NDFhMWYxMWVkOGJkNzRlODEyNTA3YTI2OCJ9.7Uuq-30JUxirjVcZmi5BMrfAqisWEakgZuhAIiF-M3I; csrftoken=d215502ab5896726cbf964cb8c75b685"
}
mojo_balance = 2658   # 跑另一本书时需要修改mojo结余的值
stamina_balance = 2000   # 初始化耐力值
i = 11
flag = 0
is_vip = True
chapters_read = ['bcqibg', 'omjdu', 'bstpcx', 'bbtixc', 'aplog','bqqcca', 'pckli', 'ftcgn', 'vmkjl', 'bcjvdp', 'lggzs']   # 读过的章节
try:
    for catelog_id in catelog_ids:
        if catelog_id in chapters_read:
            continue
        url = f"https://api.mojohi.com/mojoread/user/articles/{catelog_id}"
        response = requests.post(url,json=data,headers=headers)
        length = catelog_lengths[i]
        mojo_reward_count = basic_functions.calc_mojo_reward_count(length,stamina_balance,is_vip)
        mojo_balance = mojo_balance + mojo_reward_count
        stamian_consume_count = basic_functions.calc_stamina_consume_count(length,stamina_balance)
        stamina_balance = basic_functions.calc_stamina_balance(length,stamina_balance)
        assert response.status_code == 200,response.status_code
        print("状态码正常")
        print(response.json())
        print(f"我计算的应发放的mojo数量为{mojo_reward_count} ，章节字数为{length}")
        assert response.json()["mojo_reward_count"] == mojo_reward_count, response.json()["mojo_reward_count"]
        print("mojo发放数量正确")
        print(f"我计算的mojo累计数量为{mojo_balance}")
        assert response.json()["mojo_balance"] == mojo_balance,response.json()["mojo_balance"]
        print("mojo累计数量正确")
        print(f"我计算的耐力值结余为{stamina_balance}")
        assert response.json()["stamina_balance"] == stamina_balance,response.json()["stamina_balance"]
        print("耐力值剩余值正确")
        print(f"我计算的消耗耐力值数量为{stamian_consume_count}")
        assert response.json()["stamina_consume_count"] == stamian_consume_count,response.json()["stamina_consume_count"]
        print("被扣除的耐力值正确")
        i += 1
        chapters_read.append(catelog_id)
        if stamina_balance == 0:   # 耐力值为0就恢复
            basic_functions.recovery_stamina(2000,"dtxgn")
            stamina_balance = 2000
except requests.exceptions.RequestException as e:
    while flag < 3:   # 最多进行3次重试
        print(f"报错信息：{e}")
        flag += 1
        print("重新请求完成阅读接口需要先恢复耐力值，恢复中...")
        #   重试之前先恢复耐力值，重置耐力值
=======
           "cookie":"auth_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6OTcsImV4cCI6MTY2MTA3MjY0NCwiZXhwX3YyIjoxNjYxMDcyNjQ0LCJkZXZpY2UiOiIiLCJ1c2VybmFtZSI6Ikdvb2dsZV85Yzk3OTVjNThlNjQ1NTZmIiwiaXNfc3RhZmYiOjAsInNlc3Npb25faWQiOiI5Nzc0Y2Y1MjEyNGUxMWVkOGJkNzRlODEyNTA3YTI2OCJ9.ETeQ-WjY82hkuxLSqZYNu2Cs7ShQL9ytZLRCpynTXYU; csrftoken=f40d5abf0e431c718aff1fec686caa67"
}
mojo_balance = 876
stamina_balance = 2000   # 初始化耐力值
i = 24
is_vip = True
for catelog_id in catelog_ids:
    if catelog_id in('hnjxn', 'qgbvg', 'bskjqa', 'xxasi', 'ebnhz', 'uvpax', 'bvfmee', 'osons', 'bainku', 'phufp', 'feuvq', 'cavla', 'bkptss', 'mmeqe', 'jtzjg', 'speyu', 'buqzml', 'zcdpc', 'bszvz', 'bqzxbg','piyse','ffxxc','cbydu','bkwwol'):
        continue
    url = f"https://api.mojohi.com/mojoread/user/articles/{catelog_id}"
    response = requests.post(url,json=data,headers=headers,timeout = 20)
    length = catelog_lengths[i]
    mojo_reward_count = basic_functions.calc_mojo_reward_count(length,stamina_balance,is_vip)
    mojo_balance = mojo_balance + mojo_reward_count
    stamian_consume_count = basic_functions.calc_stamina_consume_count(length,stamina_balance)
    stamina_balance = basic_functions.calc_stamina_balance(length,stamina_balance)
    assert response.status_code == 200,response.status_code
    print("状态码正常")
    print(f"我计算的应发放的mojo数量为{mojo_reward_count} 章节字数为{length}")
    assert response.json()["mojo_reward_count"] == mojo_reward_count,response.json()["mojo_reward_count"]
    print("mojo发放数量正确")
    print(f"我计算的mojo累计数量为{mojo_balance}")
    assert response.json()["mojo_balance"] == mojo_balance,response.json()["mojo_balance"]
    print("mojo累计数量正确")
    print(f"我计算的耐力值结余为{stamina_balance}")
    assert response.json()["stamina_balance"] == stamina_balance,response.json()["stamina_balance"]
    print("耐力值剩余值正确")
    print(f"我计算的消耗耐力值数量为{stamian_consume_count}")
    assert response.json()["stamina_consume_count"] == stamian_consume_count,response.json()["stamina_consume_count"]
    print("被扣除的耐力值正确")
    i += 1
    if stamina_balance == 0:
>>>>>>> b1bfdd8ad5898bcc8853559febf439fbf92cf01f
        basic_functions.recovery_stamina(2000,"dtxgn")
        stamina_balance = 2000
        # mojo_balance = mojo_balance - mojo_reward_count   # 重试时需要把之前计算好的总mojo数量恢复到请求失败前的结果
        print(f"正在进行第{flag}次完成阅读重试")
        for catelog_id in catelog_ids:
            if catelog_id in chapters_read:
                continue
            url = f"https://api.mojohi.com/mojoread/user/articles/{catelog_id}"
            response = requests.post(url,json=data,headers=headers)
            length = catelog_lengths[i]
            mojo_reward_count = basic_functions.calc_mojo_reward_count(length,stamina_balance,is_vip)
            mojo_balance = mojo_balance + mojo_reward_count
            stamian_consume_count = basic_functions.calc_stamina_consume_count(length,stamina_balance)
            stamina_balance = basic_functions.calc_stamina_balance(length,stamina_balance)
            assert response.status_code == 200,response.status_code
            print("状态码正常")
            print(response.json())
            print(f"我计算的应发放的mojo数量为{mojo_reward_count} ，章节字数为{length}")
            assert response.json()["mojo_reward_count"] == mojo_reward_count, response.json()["mojo_reward_count"]
            print("mojo发放数量正确")
            print(f"我计算的mojo累计数量为{mojo_balance}")
            assert response.json()["mojo_balance"] == mojo_balance,response.json()["mojo_balance"]
            print("mojo累计数量正确")
            print(f"我计算的耐力值结余为{stamina_balance}")
            assert response.json()["stamina_balance"] == stamina_balance,response.json()["stamina_balance"]
            print("耐力值剩余值正确")
            print(f"我计算的消耗耐力值数量为{stamian_consume_count}")
            assert response.json()["stamina_consume_count"] == stamian_consume_count,response.json()["stamina_consume_count"]
            print("被扣除的耐力值正确")
            i += 1
            chapters_read.append(catelog_id)
            if stamina_balance == 0:   # 耐力值为0就恢复
                basic_functions.recovery_stamina(2000,"dtxgn")
                stamina_balance = 2000
    if flag == 3:
        print("已超过最大重试次数")
    else:
        print("f整本书{i}个章节全部读完～up~up")

        
print("棒～整本书📖都完成✅阅读啦～～")


# 每次运行需要检查用户ID，初始mojo数量，耐力值的初始化，起始章节，要阅读的书籍ID

    