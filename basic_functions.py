import requests
import json

# from requests.adapters import HTTPAdapter

# # 超时重连机制
# s = requests.session()
# s.mount('https://',HTTPAdapter(max_retries=5))
# url = "https://api.mojohi.com/mojoread/books/ikgix/catalogs"


def get_book_catelogs_information(book_id):
    """
    获取书籍章节ID和对应长度
    return：章节ID，章节length
    """
    url = f"https://api.mojohi.com/mojoread/books/{book_id}/catalogs"
    headers = {"user-agent":"bayAgent/1.1 Android/12 com.mojohi.reading/1.1.502-qa shanbay-channel/0 vivo/V2118A frontend/4.8 api/2.2 device/Mobile",
           "Content-Type":"application/json; charset=UTF-8",
           "cookie":"auth_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6OTcsImV4cCI6MTY2MDMwMDcyNywiZXhwX3YyIjoxNjYwMzAwNzI3LCJkZXZpY2UiOiIiLCJ1c2VybmFtZSI6Ikdvb2dsZV85Yzk3OTVjNThlNjQ1NTZmIiwiaXNfc3RhZmYiOjAsInNlc3Npb25faWQiOiI5Nzc0Y2Y1MjEyNGUxMWVkOGJkNzRlODEyNTA3YTI2OCJ9.9RULGAB5cF43UUfRrCZTokxSv4TbtQ_p9srU0RMJOtg; csrftoken=e3a79536b8ef42a85bf5bef3a7a2d3cb"
}
    response = requests.get(url, headers=headers)
    response_json = response.json()
    catelog_num = len(response_json["objects"])  # 章节数
    catelog_ids = []
    catelog_lengths = []
    for i in range(catelog_num):
        catelog_id = response_json["objects"][i]["id"]
        catelog_ids.append(catelog_id)
        catelog_length = response_json["objects"][i]["length"]
        catelog_lengths.append(catelog_length)
    print(catelog_ids, catelog_lengths)
    return catelog_ids,catelog_lengths


def recovery_stamina(stamina,user):
    """
    恢复用户耐力值
    """
    url = "https://api.mojohi.com/mojoread/admin/user_stamina"
    headers = {"user-agent":"bayAgent/1.1 Android/12 com.mojohi.reading/1.1.502-qa shanbay-channel/0 vivo/V2118A frontend/4.8 api/2.2 device/Mobile",
           "Content-Type":"application/json; charset=UTF-8",
           "cookie":"auth_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjAsImV4cCI6MTY2MTA3NTk3OSwiZXhwX3YyIjoxNjYxMDc1OTc5LCJkZXZpY2UiOiIiLCJ1c2VybmFtZSI6Ikdvb2dsZV85OWViNzM3ZTViMmIzNWNjIiwiaXNfc3RhZmYiOjAsInNlc3Npb25faWQiOiI5ZGExNTgxZTE5NWIxMWVkOTI3NDRlODEyNTA3YTI2OCJ9.jp1XUGCCrw4K6O7UPKDemqWh7oy32XlMs1u7WM3wcQ0; csrftoken=8e8aa8d6b678a2ea10b83ec8c86983e5"
}
    data = {
          "stamina_balance":stamina,
          "user_id":user
          }
    
    try:
        response = requests.put(url,json=data,headers=headers)
        i = 0
        if response.status_code == 200:
            print("恢复耐力值成功")
            i = 3
    except requests.exceptions.RequestException as e:
        while i < 3:
            print(f"报错信息:{e}")
            i += 1
            print("请求失败，正在进行第！" + str(i) + "次请求")
            response = requests.put(url,json=data,headers=headers)
            if response.status_code == 200:
                print(f"第{i}次重试成功，耐力值成功恢复！")
                i = 3



<<<<<<< HEAD
    

=======
>>>>>>> b1bfdd8ad5898bcc8853559febf439fbf92cf01f
def calc_mojo(lengthx,is_vip):
    """
    计算应该发放的mojo数量
    int_num:mojo数量
    flag_num:判断是否四舍五入的标志
    """
    if lengthx < 50:   # 小于50的情况，就算四舍五入应该发放的mojo也为0
        int_num = 0
    elif lengthx >= 50 and lengthx < 100:
        int_num = 1
    elif lengthx >= 2000:   # length大于等于2000的情况
        int_num = 20
    else:   # length三位数和四位数的情况
        decimal = lengthx/100
        a = str(decimal).split('.') #将除以100之后的数按小数点左右拆分开来
        int_num = int(a[0])
        if len(a[1]) == 2: #如果有2位小数
            flag_num = int(a[1])//10
        elif len(a[1]) == 1: #如果有1位小数
            flag_num = int(a[1])
        if flag_num >= 5:
            int_num += 1
    if is_vip:
        return int_num * 2
    else:
        return int_num

    
def calc_mojo_reward_count(length,stamina_balance,is_vip):
    """
    判断应该走的mojo计算逻辑
    """
    if length < stamina_balance: # 如果耐力值大于章节词数
        pass
    else: # 如果耐力值小于章节词数
        length = stamina_balance   # 此时mojo计算就要以剩余的耐力值作为章节长度了，因为最多可以消耗的就是剩余耐力值了，当章节词数大于剩余耐力值时
    return calc_mojo(length,is_vip)


def calc_stamina_balance(length,stamina_balance):
    """
    计算耐力值结余
    """
    if length <= stamina_balance:
        stamina_balance = stamina_balance - length
    else:
        stamina_balance = 0
    return stamina_balance

def calc_stamina_consume_count(length,stamina_balance):
    """
    计算消耗的耐力数量
    """
    if length <= stamina_balance:
        stamina_cousume_count = length
    else:
        stamina_cousume_count = stamina_balance
    return stamina_cousume_count