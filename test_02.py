# aliens=[]

# # 创建30个绿色外星人
# for alien_number in range(30):
# 	new_alien = {'color':'green','points':5,'speed':'slow'}
# 	aliens.append(new_alien)


# for alien in aliens[:3]:
#     if alien ['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
# # 显示前5个外星人
# for alien in aliens[:5]:
#     print(alien)
# print("...")

# # 显示创建了多少个外星人
# print(f"Total number of aliens:{len(aliens)}")

# 存储所点披萨信息
# pizza = {
#     'crust':'thick',
#     'toppings':['mushrooms','extra cheese'],
# }

# # 概述所点披萨
# print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
# for topping in pizza['toppings']:
#     print(topping)

# favorite_languages = {
#     'jen':['python','ruby'],
#     'sarah':['C'],
#     'edward':['ruby','go'],
#     'phil':['python','haskell'],
# }

# for name,languages in favorite_languages.items():
#     if len(languages) > 1:
#         print(f"\n{name.title()}'s favorite languages are: ")
#         for language in languages:
#             print(f"\t{language.title()}")
#     else:
#         print(f"{name.title()}'s favorite language is:\n\t{language}")

# users = {
#     'aeinstein':{
#         'first':'albert',
#         'last':'einstein',
#         'location':'princeton'
#     },

#     'mcurie':{
#         'first':'marie',
#         'last':'curie',
#         'location':'paris',

#     },
# }
# for username,user_info in users.items():
#     print(f"\nUsername:{username}")
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']

#     print(f"\tFull name:{full_name.title()}")
#     print(f"\tLocation:{location.title()}")

# haizhu = {'first_name':'haizhu','last_name':'chen','age':24,'city':'datong'}
# hongyan = {'first_name':'hongyan','last_name':'zhu','age':23,'city':'yongfeng'}
# youjuan = {'first_name':'youjuan','last_name':'song','age':23,'city':'guantang'}
# people = [haizhu,hongyan,youjuan]
# for person in people:
#     print(person)

# dog_1 = {'pet_type':'dog','master_name':'peter'}
# cat_1 = {'pet_type':'cat','master_name':'penny'}
# pets = [dog_1,cat_1]
# for pet in pets:
#     print(pet)

# favorite_places = {
#     'pennt':['shanghai','guangzhou','hefei'],
#     'petty':['nanjing','beijing'],
#     'crstina':['tianjing','xian'],
# }
# for name,places in favorite_places.items():
#     places = ','.join(places)
#     print(f"name:{name}\nMy favorite places is {places}.")
   

# favorite_numbers = {
#     'penny':['1','3','6','9'],
#     'amy':['2','4','6','8','9','0'],
#     'chang':['1','3','4']
# }
# for name,numbers in favorite_numbers.items():
#     numbers = ','.join(numbers)
#     print(f"{name} favorite numbers are {numbers}")



# cities = {
#     'beijing':{
#     'Country':'China',
#     'Population':21893095,
#     'Event':'奥运会/首都/冬奥会/天安门',
#     },
#     'xian':{
#     "Country":'China',
#     'Population':1295.29,
#     'Event':'十三朝古都/回族',
#     },
#     'jifu':{
#     "Country":'Ukraine',
#     'Population':4131.98,
#     'Event':'Be invaded',
#     }
# }
# for city,shuxing in cities.items():
#     print(f"city:{city}\tCountry:{shuxing['Country']}\tPopulation:{shuxing['Population']}\tEvent:{shuxing['Event']}")

# message = input("Tell me something,and I will repeat it back to you:")
# print(message)

# prompt = "If you tell us who you are,we can personalize the message you see."
# prompt += "\nwhat is your first name?"

# name = input(prompt)
# print(f"\nHello,{name}!")

# prompt = input("What kind of car would you like to rent? ")
# print(prompt)

# prompt = input("How many people have dinner? ")
# number = int(prompt)
# if number > 8:
#     print("Sorry!We don't have an empty table for the time being.")
# else:
#     print("OK！Come with me!")

# prompt = input("Please input a number: ")
# number = int(prompt)
# if number % 10 == 0:
#     print(f"The number {number} is an integral multiple of 10. ")
# else:
#     print("Sorry!")

# current_number = 1 
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# prompt = "\nTell me something,and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message) 

# prompt = "\nTell me something,and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program. "

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.)"
# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print(f"I 'd love to go to {city.title()}!")

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 ==0:
#         continue

#     print(current_number)

# prompt = "\nPlease enter the small material you want to add. "
# prompt += "\n(Enter 'quit' when you are finished. )"

# small_materials = []
# small_material = ''

# while small_material != 'quit':
#     small_material = input(prompt)
#     small_materials.append(small_material)
    
#     print(f"You will add: {','.join(small_materials)}")
#     continue
# print(small_materials)
# 以上代码有bug

# prompt = "\nWhat is your age? "
# prompt += "\n(Enter 'quit' when you are finished.)"

# while True:
#     age = input(prompt)
#     if age != 'quit':
#         age = int(age)
#         if age < 3:
#             print("You can watch movies for free!")
#         elif age <= 12:
#             print("Your ticket price is $10!")
#         elif age >12:
#             print("Your ticket price is $15!")
#     elif age == 'quit':
#         break


# # 首先，创建一个待验证用户列表
# # 和一个用于存储已验证用户的空列表。
# unconfirmed_users = ['alice','brian','candace']
# confirmed_users = []

# # 验证每个用户，直到没有未验证的用户为止。
# # 将每个经过验证的用户都移到已验证用户列表中。
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print(f"Verifying user:{current_user.title()}")
#     confirmed_users.append(current_user)
# # 显示所有已验证的用户
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

# responses = {}

# # 设置一个标志，指出调查是否继续
# polling_active = True

# while polling_active:
#     # 提示输入被调查者的名字和回答
#     name = input("\nWhat is your name? ")
#     response  = input("which mountain would you like to climb someday? ")

#     # 将回答存储在字典中
#     responses[name] = response # 在字典responses中新建一个键值对

#     # 看看是否还有人要参与调查
#     repeat = input("Would you like to let another person respond?(Yes/no)")
#     if repeat == 'no':
#         polling_active = False

# # 调查结果，显示结果
# print("\n--- Poll Results ---")
# for name,response in responses.items():
#     print(f"{name} would like to climb {response}.")

# sandwich_orders = ['salad','rich','meat']
# finished_sandwiches = []
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"I made your {current_sandwich}.")
#     finished_sandwiches.append(current_sandwich)
# print(finished_sandwiches)

# sandwich_orders = ['meat','salad','pastrami','rich','fruit','pastrami','drink',
# 'pastrami']
# finished_sandwiches = []
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print("Sorry ,wo have no pastrami!")
# while sandwich_orders:
#     current_sandwich  = sandwich_orders.pop()
#     print(f"I made your {current_sandwich}.")
#     finished_sandwiches.append(current_sandwich)
# print(finished_sandwiches)

# active = True
# responses = {}
# while active:
#     name = input("\nWhat your name? ")
#     response = input("\nWhat is you want to go? ")
#     responses[name] = response
#     repeat = input("Would you like to let another person respond?(yes/no)")
#     if repeat == 'no':
#         active = False

# print("\n--- Poll Results ---")

# for name,response in responses.items():
#     print(f"{name} would like to climb {response}.")