# def greet_user():
#     """显示简单的问候"""
#     print("Hello!")
# greet_user()

# def greet_user(username):
#     """显示带姓名的问候"""
#     print(f"Hello,{username.title()}")
# greet_user('Jimmy')

# def display_message():
#     """在本章学习了什么"""
#     print("I studyed balabala")
# display_message()

# def favorite_book(title):
#     """最喜欢的书"""
#     print(f"My favorite_book is {title.title()}")
# favorite_book('balabal')

# def describe_pet(animal_type,pet_name):
#     """显示宠物信息"""
#     print(f"\n I have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('dog','miki')

# def describe_pet(animal_type,pet_name):
#     """显示宠物的信息"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(animal_type='hamster',pet_name='harry')

# def describe_pet(pet_name,animal_type='dog'):
#     """显示宠物信息"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(pet_name='haha')

# def make_shirt(size,sentence):
#     """制作T恤"""
#     print(f"I want an {size.upper()}-Size T-shirt.")
#     print(f"It says '{sentence}'.")

# make_shirt(sentence='M',size="I love china")

# def make_shirt(size="XXL",sentence="I love Python"):
#     """有默认参数的制作T恤"""
#     print(f"I want a {size.upper()}-size T-shirt.")
#     print(f"It says '{sentence}'.")

# make_shirt(sentence='haha')

# def describe_city(city,country='China'):
#     """城市"""
#     print(f"{city} is in {country}.")

# describe_city('newyork')
# describe_city('kendeji','american')
# describe_city('morago',country='japan')

# def get_formatted_name(first_name,last_name):
#     """返回整洁的姓名"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name("jimi",'hendrix')
# print(musician)

# def get_formatted_name(first_name,last_name,middle_name=''):
#     """返回整洁的姓名"""
#     if middle_name:
#         full_name= f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('jimi','win')
# print(musician)

# def build_person(first_name,last_name):
#     """返回一个字典，其中包含有关一个人的信息"""
#     person = {'first':first_name,'last':last_name}
#     return person

# musician = build_person('jimi','hendrix')
# print(musician)

# def build_person(first_name,last_name,age=None):
#     """返回一个字典，其中包含有关一个人的信息"""
#     person = {'first':first_name,'last':last_name}
#     if age:
#         person['age'] = age
#     return person

# musician = build_person('jimi','hendrix',28)
# print(musician)

# def get_formatted_name(first_name,last_name):
#     """返回整洁的姓名"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# # 这是一个无限循环
# while True:
#     print("\nPlease tell me your name:")
#     print("\n(Enter 'quit' to end of program.)")
#     f_name = input("First name:")
#     if f_name == 'quit':
#         break

#     l_name = input("Last name:")
#     if l_name == 'quit':
#         break

#     formatted_name = get_formatted_name(f_name,l_name)
#     print(f"Hello,{formatted_name}!")

# def city_country(city,country):
#     """城市名"""
#     print(f'"{city},{country}"')

# city_country('santy','china')

# def make_album(singer,album_name,song_number=None):
#     """专辑"""
#     album = {'singer':singer,'name':album_name}
#     if song_number:
#         album['song_number']= song_number
#     return album

# album  = make_album("zhangjie",'month',29)
# print(album)
# album = make_album(singer='linjunjie',album_name='jiangan',song_number= 8)
# print(album)
# album = make_album('lihong',album_name= 'huatiancuo',)
# print(album)

# def make_album(singer,album_name,song_number=None):
#     """专辑"""
#     album= {'singer':singer,'album_name':album_name}
#     if song_number:
#         album['song_number'] = song_number

#     return album

# prompt = "\nPlease input message:"
# prompt += "Enter 'quit' to end of program: "

# while True:

#     singer = input("Singer: ")
#     if singer == 'quit':
#         break
#     album_name = input("Album_name: ")
#     if album_name == 'quit':
#         break
#     number  = input("Song number: ")
#     if number == 'quit':
#         break
#     elif number == '':
#         album = make_album(singer,album_name)
#     else:
#         number = int(number)
#         album = make_album(singer,album_name,number)
#         # 以上的elif和else处理age为空的和退出的情况
#     print(album)
        
# def greet_users(names):
#     """向列表中的每位用户发出简单的问候（接受一个列表，并赋值给names）"""
#     for name in names:
#         msg = f"Hello,{name.title()}!"
#         print(msg)

# usernames = ['hannah','peter','penny']
# greet_users(usernames)  #通过变量名来传递实参

# def print_models(unprinted_designs,completed_models):
#     """模拟打印每个设计，直到没有未打印的设计为止
#     打印每个设计后，都将其移到列表completed_models中。
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model:{current_design}")
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     """显示打印好的所有模型"""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['phone case','robot pendant','dodecahedron']
# completed_models = []

# print_models(unprinted_designs,completed_models)
# show_completed_models(completed_models)

# def show_message(megs):
#     """消息"""
#     for msg in megs:
#         print(msg)

# messages = ['hahah','zhuibushangwoba ','lalal']
# show_message(messages)

# def send_messages(megs):
#     """发送消息"""
#     while megs:
#         current_message = megs.pop()
#         print(f"Printing message:{current_message}")
#         sent_messages.append(current_message)

# messages = ['letting','go','我的眼泪你的战利品']
# sent_messages = []
# send_messages(messages[:])
# print(messages)
# print(sent_messages)

# def make_pizza(*toppings):
#     """打印顾客点的所有配料"""
#     print(f"\nMaking a pizza with the following toppings:")
#     for topping in toppings:

#         print(f"-{toppings}")

# make_pizza('haha')
# make_pizza('wozuile','piza')

# def make_pizza(size,*toppings):
#     """概述要制作的比萨"""
#     print(f"\nMaking a {size} -inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"-{topping}")

# make_pizza(16,'pepperoni')
# make_pizza(12,'mushrooms','geen peppers','extra cheese')

# def build_profile(first,last,**user_info):
#     """创建一个字典，其中包含我们知道的有关用户的一切。"""
#     user_info['first_name'] = first # 根据需求手动在字典中新建键值对
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('albert','einstein',location = 'princeton',
# filed = 'physics')
# print(user_profile)
# 这里为什么打印出来的集合location和filed在前面，而first和last在集合后面，可以理解为新建一个
# 集合的时候，就已经把内定好的键值对类型（location和filed）放到集合里了，然后再新建一个
# 键值对first和last
# 最新理解：**user_info创建一个名为user_info的空字典，然后将收到的名称值对放入到字典中，位置
# 实参的信息存入到变量中，然后根据需求手动在字典中新建键值对

# def make_sandwich(*toppings):
#     """三明治"""
#     print(f"You will add list shicai:{toppings}")

# toppingsh = make_sandwich('vegetable')

# def build_profile(first,last,**user_info):
#     """用户信息"""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     print(user_info)

# build_profile('haha','last',sex='girl',tall = 160)

# def make_car(manufacturer,model,**message):
#     """汽车"""
#     message['manufacturer'] = manufacturer
#     message['model'] = model
#     return message

# car = make_car('subaru','outback',color = 'blue',tow_package = True)

# print(car)


