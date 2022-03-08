# pizzas=['dameile','bishengke','e']
# for pizza in pizzas:
#     print(f"I like {pizza.title()}!")
# print("Thanks!")

# squars=[]
# for value in range (1,11):
#     square=value**2
#     squars.append(square)
# print(squars)

# for i in range(1,21):
#     print(f"{i}")

# squars=[]
# for squar in range(1,1000001):
#     squars.append(squar)
# print(squars)
# print(max(squars))
# print(min(squars))
# print(sum(squars))

# odd_numbers=[]
# for odd_number in range(1,21):
#     if odd_number % 2 !=0:
#         odd_numbers.append(odd_number)
# print(odd_numbers)

# numbers=[]
# for number in range(3,31):
#     if number % 3 ==0:
#         numbers.append(number)
#         print(number)

# cubes=[]
# for cube in range(1,11):
#     value=cube**3
#     cubes.append(value)
# print(cubes)

# cubes=[cube**3 for cube in range(1,11)]
# print(cubes)

# my_foods=['pizza','falafel','carrot cake']
# friend_foods=my_foods[:]
# my_foods.append("cannoli")
# print("My favorite foods are:")
# print(my_foods)
# friend_foods.append("ice cream")
# print("My friend's favorite foods are:")
# print(friend_foods)

# cars=['audi','bmw','subaru','toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# car='subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'aidi'? I predict False.")
# print(car == 'audi')

# age=12
# if age <4:
#     print("Your admission cost is $0.")
# elif age <18:
#     print("Your admission cost is $25.")
# else:
#     print("Your admission cost is $40.")

# alien_color = 'yellow'
# if alien_color == 'yellow':
#     print("Pass")

# alien_color = 'yellow'
# if alien_color == 'green':
#     print("You get 5!")
# elif alien_color == 'yellow':
#     print("You get 10!")
# else:
#     print("You get 15!")

# age=15
# if age < 2:
#     person_type='婴儿'
# elif age < 4:
#     person_type='幼儿'
# elif age < 13:
#     person_type='儿童'
# elif age < 20:
#     person_type='青少年'
# elif age <65:
#     person_type='老年人'
# print(f"The people is {person_type}.")

# favorite_fruits = ['apple','banana','candy','xigua']
# fruit = 'apple'
# if fruit in favorite_fruits:
#     favorite_fruit = fruit
# if fruit in favorite_fruits:
#     favorite_fruit = fruit
# print(f"You really like {favorite_fruit}.")

# requested_toppings=['mushrooms','green peppers','extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping == "green peppers":
#         print("Sorry,we are out of green peppers")
#     else:
#         print(f"Adding {requested_topping}.")
# print("\nFinished making your pizza!")

# requested_toppings=[]
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}.")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

# available_toppings = ['mushrooms','olives','green peppers','pepperoni',
# 'poneapple','extra cheese']
# requested_toppings = ['mushrooms','french fries','extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"Adding {requested_topping}.")
#     else:
#         print(f"Sorry ,we don't have {requested_topping}.")
# print("\nFinished making your pizza!")

# users = ['admin','peter','amy','ema','pat']
# if users:
#     for user in users:
#         if user == 'admin':
#             print("Hello admin,would you like to see a status report?")
#         else:
#             print(f"Hello {user},thank you for logging in again.")
# else:
#     print("We need to find some users!")

# current_users=['amy','angla','bim','carole','ema']
# new_users = ['admin','Amy','peter','ema','candy']
# current_users_upper=[]
# for current_user in current_users:
#     current_users_upper.append(current_user.upper())
# for new_user in new_users:
#     if new_user.upper() in current_users:
#         print(f"You need to input other user_name,{new_user} was be used!")
#     else:
#         print(f"{new_user} not be used!")


# numbers=list(range(1,10))
# for number in numbers:
#     if number == 1:
#         biaozhi='st'
#     elif number == 2:
#         biaozhi='nd'
#     elif number == 3:
#         biaozhi = 'rd'
#     else:
#         biaozhi='th'
#     print(f"{number}{biaozhi}")

# alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
# print(f"Original x-position:{alien_0['x_position']}")
# # 向右移动外星人
# # 根据当前速度确定将外星人向右移动多远
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     # 这个外星人的移动速度肯定很快
#     x_increment = 3

# # 新位置为旧位置加上移动距离
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position:{alien_0['x_position']}")

# del alien_0['speed']
# print(alien_0)

# favorite_languages = {
#     'jen':'python',
#     'sarah':'c',
#     'edward':'ruby',
#     'phil':'python',
# }
# friends = ['phil','sarah']
# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}.")
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()},I see you love {language}!")
# for name,favorite_language in favorite_languages.items():
# for name in favorite_languages:
#     print(name)


    # print(f"\n{name.title()}'s favorite language is {favorite_language.title()}.")

# alien_0 = {'color':'green','speed':'slow',}
# point_value = alien_0.get('points','No point value assigned.')
# print(point_value)

# xiaoyu_wei = {'first_name':'xiaoyu','last_name':'wei','age':24,'city':'nanj'}
# print(xiaoyu_wei['first_name'])

# words_table = {'切片':'在Python中切片指的是截取指定范围的数据,对于字符串,元组,和列表都是可以进行切片',
#     '对象':' 在python里,对象就是变量,对象其实是一个指针,指向一个数据结构,数据结构里有属性,有方法。',
#     '方法':'方法用来描述对象所具有的行为。',
#     '方法_1': 'Python中的类方法,指的是在类中定义的函数,函数在类的内部称为方法',
#     '属性':'变量在类的内部,称为属性。',
#     '集合':'集合set是一个无序的不重复元素序列。',
#     '道义':'python中一切皆对象',
#     '函数装饰器':'修改其他函数的功能的函数',
#     'class属性':'class一般是用于统一样式设置',
#     'classname':'通过class name返回的是一个数组',
#     }



# for dingyi,value in words_table.items():
#     print(f"{dingyi}:{value}")
    



# user_0 = {
#     'user_name':'efermi',
#     'first':'enrico',
#     'last':'fermi',
# }
# for key,value in user_0.items():
#     print(f"\nKey:{key}")
#     print(f"Value:{value}")

# rivers = {'隆迪':'尼罗河',
# '卢旺达':'尼罗河',
# '坦桑尼亚':'尼罗河',
# }
# for country,river in rivers.items():
#     print(f"The {river} runs through {country}.")

# favorite_languages = {'Bile':'C','amy':'ruby','Chang':'PHp' ,'liu':'java'}
# should = ['Bile','Chang','Pat','huoqianliuming']
# for person in should:
#     if person in favorite_languages.keys():
#         print(f"Thank you {person}!")
#     else:
#         print(f"{person},We provide you join us team.")
