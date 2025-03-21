import pandas as pd
from openpyxl import Workbook

df = pd.read_excel('/Users/weixiaoyu/Downloads/工作簿1.xlsx')

# 输出每一列的内容
for column in df.columns:
    if column == '商品名字':
        data = df[column].tolist()  # 将列的数据转换为列表
        new_lst = []
        for word in data:
            if "," in word:
                word = word.replace(",", " ")
                
            if r"/" in word:
                word = word.replace(r"/"," ")
               
            if "!" in word:
                word = word.replace("!"," ")
                
            if "\"" in word:
                word = word.replace("\""," ")
                
            if "." in word:
                word = word.replace("."," ")
            if "(" in word:
                word = word.replace("("," ")
            if ")" in word:
                word = word.replace(")"," ")
            new_lst.append(word)
        for word in new_lst:
            print("word01:",word)
        test_data = {}
        for word01 in new_lst:
            data01 = word01.split(" ")
            print("data01:",data01)
            print("\n")
            for word02 in data01:
                if word02 == '':
                    continue
                else:
                    if word02 in test_data:
                        test_data[word02] += 1
                    else:
                        test_data[word02] = 1
        print(test_data)

wb = Workbook()  # 创建Workbook对象
ws = wb.active  # 获取当前活动的工作表

row_num = 1  # 起始行号
for key, value in test_data.items():
    ws.cell(row=row_num, column=1, value=key)  # 写入键到第一列
    ws.cell(row=row_num, column=2, value=value)  # 写入值到第二列
    row_num += 1

filename = '/Users/weixiaoyu/Downloads/工作簿3.xlsx'
wb.save(filename)  # 保存工作簿

            

