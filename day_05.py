# a="123"
# print(type(a))
# a=int(a)
# print(type(a))

# a="12.3"
# print(type(a))
# a=float(a)
# print(type(a))

# a=123
# print(type(a))
# a=str(a)
# print(type(a))

# def print_sentence():
#     print('Hello WOrld')
# print_sentence()
# 没有任何参数的函数

# def xiu_gou(dog_type,dog_name): #定义函数
#     print('I have a {}'.format(dog_type))
#     print('It is name is {}'.format(dog_name))
# xiu_gou('big_dog','siugouer') #调用函数
# # 位置实参

# def pet_dog(dog_type,dog_name):
#     print("I have a {}".format(dog_type))
#     print("It is name is {}".format(dog_name))
# pet_dog(dog_type='small dog',dog_name="huanhuan")
#关键字实参

# def pet_dog(dog_name,dog_type='dog'):
#     print("I have a {}".format(dog_type))
#     print("It is name is {}".format(dog_name))
# pet_dog(dog_name="enheng")
#在定义函数时，需要将没有默认值的形参放在有默认值的形参前面，放后面会报错。
# 使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。这让Python依然能够正确地解读位置实参。