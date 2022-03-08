import os
# str="keAiDeXiaoMaoMi"
# print(str*4)

# print('haha\nahahshs')
# input('按下回车后输入')
# j=1
# while j:
#     def Fibonacci(n):
#         a1=0
#         a2=1
        
#         for i in range(n-2):
#             count=a1+a2
#             a1=a2
#             a2=count
#             if i==0:
#                print("斐波那契数列：",0,1,end=",") 
#             print(count,end=",")
#         return count

#     m=input('请输入斐波那次数列的项数：')
#     print("需要求的项数为：",m)
#     d=Fibonacci(int(m))
#     print("\n斐波那次数为：",d)
#     c=input("是否继续求数？(是y/Y,否n/N)")
#     if c=='y' or c=='Y':
#         continue
#     else:
#         print("祝您生活愉快，感谢使用！")
#         break


# a='abcdefg'
# x=-7
# print(a[x])
# b=("123",23,4.6,128,"ggg","哈哈",(12,3))
# y=6
# print(b[y])
# c=[1,"23","333",'hahah',"哈哈哈",3.14,["qiantao",1],("hei","ren",1)]
# z=7
# print(c[z])
# d={"key":123,23:34,"op":"123"}
# w=2
# print(d[23])


# p=open("/Users/weixiaoyu/Downloads/test.txt",'r',encoding='UTF-8')
# f=p.read(8)
# print(f)
# p.close()

with open("/Users/weixiaoyu/Downloads/test.txt",'w+') as w:
    str="我醉了醉了醉了，我美了美了美了美了xiaosh"
    w.write(str)
print(w.read())

