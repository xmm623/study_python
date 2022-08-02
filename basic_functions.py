import requests
import json

# url = "https://api.mojohi.com/mojoread/books/ikgix/catalogs"


# print(response_json["objects"][0]["id"])


def get_book_catelogs_information(book_id):
    """
    获取书籍章节ID和对应长度
    return：章节ID，章节length
    """
    url = f"https://api.mojohi.com/mojoread/books/{book_id}/catalogs"
    headers = {"user-agent":"bayAgent/1.1 Android/12 com.mojohi.reading/1.1.502-qa shanbay-channel/0 vivo/V2118A frontend/4.8 api/2.2 device/Mobile",
           "Content-Type":"application/json; charset=UTF-8",
           "cookie":"auth_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6OTEsImV4cCI6MTY2MDIxMjQ2NCwiZXhwX3YyIjoxNjYwMjEyNDY0LCJkZXZpY2UiOiIiLCJ1c2VybmFtZSI6Ikdvb2dsZV85MWUxMzQxMTU0NWNiYzIzIiwiaXNfc3RhZmYiOjAsInNlc3Npb25faWQiOiIxNjc0ZDBkMjExODExMWVkYTYwZjBhYTA1NjVmMTE4NyJ9.fOasAjgT6LELZIVJ9143NJv6LBR2owBRZ6hycGwUr6Q; csrftoken=d93f57ef6dfa4282f1185de758ec26c7"
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
           "cookie":"auth_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjAsImV4cCI6MTY2MDE5NTg4NSwiZXhwX3YyIjoxNjYwMTk1ODg1LCJkZXZpY2UiOiIiLCJ1c2VybmFtZSI6Ikdvb2dsZV85OWViNzM3ZTViMmIzNWNjIiwiaXNfc3RhZmYiOjAsInNlc3Npb25faWQiOiI3Yzc0ODFlYzExNWExMWVkYTYwZjBhYTA1NjVmMTE4NyJ9.x62nmWwwqQzGgTlBavyrTPqHwl4_6FPforTiQiakUvU; csrftoken=0b843bd169ca20ff1cb8881afe152ceb"
}
    data = {
          "stamina_balance":stamina,
          "user_id":user
          }
    response = requests.put(url,data=data,headers=headers,)
    if response.status_code == 200:
        print("恢复耐力值成功")
    else:
        print("恢复失败，请重试！")