# open是一个内置函数，用于打开文件并返回一个文件对象
# open(file,mode='',encoding='')
# file是文件名（可以是绝对路径或相对路径）
# mode是打开文件的模式，可选参数，默认是'r'只读。常见的模式包括：'r','w'写入,'a'追加
# encoding：文件编码（如"utf-8","gbk"等

filename = "second_study/file.txt"


with open(filename,mode='w',encoding="utf-8") as file:
    wcontent = "醉了"
    file.write(wcontent)

with open(filename,mode='a',encoding='utf-8') as file:
    acontent = "啊啊啊"
    file.write(acontent)

with open(filename,mode='r',encoding="utf-8") as file: # 为什么使用with...as...语句？with as时python的上下文管理器写法，with语句可以自动管理资源，比如文件的打开和关闭，当with代码块结束时，文建会自动关闭，无需file.close（）
    content = file.read() # read()是文件对象的方法，用来一次性读取文件的全部内容，并返回一个字符串
    print(content)

import yaml
# yaml文件读取
yfilename = 'second_study/july_24yaml.yaml'
with open(yfilename,mode='r',encoding='utf-8') as yfile:
    config = yaml.safe_load(yfile) # 安全的将yaml格式文本解析为python对象（如字典、列表等。）
print(config)

# yaml文件写入
data = {'name':'xiaomaomi','age':2,'is_animal':'cat','skill':['eat','sleep']}
with open(yfilename,mode='a',encoding='utf-8') as yfile:
    yaml.dump(data,yfile,allow_unicode=True) # allow_unicode表示允许写入中文等非英文字符，不会出现乱码。dump方法用来吧python数据转换成yaml格式，并写入到文件中。

    

