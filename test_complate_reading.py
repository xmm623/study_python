import basic_functions
import requests

def calc_mojo_reward_count(length):
    """
    计算应该发放的mojo数量
    """
    if len(str(length)) == 2:
        int_num = 1
        return int_num
    else:
        decimal = length/100
        a = str(decimal).split('.')
        int_num = int(a[0])
        flag_num = str(decimal)[-2]
        if int(flag_num) >= 5:
            int_num += 1
            return int_num
        else:
            return int_num

catelog_ids,catelog_lengths = basic_functions.get_book_catelogs_information("ikgix")
data = {
    "used_time":330
}
headers = {"user-agent":"bayAgent/1.1 Android/12 com.mojohi.reading/1.1.502-qa shanbay-channel/0 vivo/V2118A frontend/4.8 api/2.2 device/Mobile",
           "Content-Type":"application/json; charset=UTF-8",
           "cookie":"auth_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6OTQsImV4cCI6MTY2MDI5NjkzNiwiZXhwX3YyIjoxNjYwMjk2OTM2LCJkZXZpY2UiOiIiLCJ1c2VybmFtZSI6Ikdvb2dsZV85ZmYzZTcwNWQwYjgyZWExIiwiaXNfc3RhZmYiOjAsInNlc3Npb25faWQiOiJjMzkzNDI1MjEyNDUxMWVkYjcwNjBhYTA1NjVmMTE4NyJ9.TBTUPdW8B0N6bcuv8pg0JZ5iaevXfyfIzJgL8GhzxRg; csrftoken=9eaf7894a439d09487ed17758f0d7e3c"
}
mojo_balance = 0
for catelog_id in catelog_ids:
    url = f"https://api.mojohi.com/mojoread/user/articles/{catelog_id}"
    response = requests.post(url,data=data,headers=headers)
    for length in catelog_lengths:
        mojo_reward_count = calc_mojo_reward_count(length)
        mojo_balance = mojo_balance + mojo_reward_count
        stamina_balance = 2000 - length
        print(response.json())
        break
    break
    #     assert response.status_code == '200'
    #     print("状态码正常")
    #     assert response.json()["mojo_reward_count"] == mojo_reward_count
    #     print("mojo发放数量正确")
    #     assert response.json()["mojo_balance"] == mojo_balance
    #     print("mojo累计数量正确")
    #     assert response.json()["stamina_balance"] == stamina_balance
    #     print("耐力值剩余值正确")
    #     assert response.json()["stamina_consume_count"] == length
    #     print("被扣除的耐力值正确")
    # basic_functions.recovery_stamina(2000,"ynhoq")




    