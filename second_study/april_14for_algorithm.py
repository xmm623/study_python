# 使用for循环计算1000以内的偶数和
sum = 0
for i in range(0, 1000 , 2):
    sum += i
print("1000以内的偶数和为:", sum)

# 使用for循环打印99乘法表
for i in range(1, 10):
    for j in range(1,  i+1):
        print(f"{j} * {i} = {i*j}", end="\t")
    print() 
#print()的实际效果：输出一个换行符（\n)，相当于执行了一次换行操作。

# 冒泡排序
list = [98,64,27,98,-6,9,10,9,8]
for i in range(len(list)):
    for j in range(len(list)-i-1): #每轮比较的下标最大值是长度-i之后再减1，因为下方的if方法中用到了j+1，j+1就是每轮比较的下标最大值
        if list[j] > list[j+1]:
            list[j],list[j+1] = list[j+1],list[j]
print(list)

# 判断一个数是否为水仙花数
num = int(input("请输入一个数字，我来帮你检测它是否为水仙花数："))
x = num // 100
y = (num - x * 100) // 10
z= num % 10
if x ** 3 + y **3 +z **3 == num:
    print(f"{num}是水仙花数")
else:
    print(f"{num}不是水仙花数")

#判断一个数是否为偶数
num2 = int(input("请输入数字，我来帮你检测它是否为偶数："))
if num2 % 2 == 0:
    print(f"数字{num2}是偶数")
else:
    print(f"数字{num2}不是偶数")

# 求1-100之内所有偶数的个数
sum_ou = 0
for i in range(1,101):
    if i % 2 == 0:
        sum_ou +=1
print(f"偶数个数是{sum_ou}")

# 求100-999之间的水仙花数
sxh_list = []
for i in range(100,1000):
    x = i // 100
    y = (i - x * 100) // 10
    z = i % 10
    if x ** 3 + y ** 3 +z ** 3 == i:
        sxh_list.append(i)
print(f"100-999之间的水仙花数有{sxh_list}")

# 求1000以内的质数
zs_list = [2,]
for i in range(3,1000): #质数：大于1的自然数，除了1和它本身之外，不能被其他自然数整除
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        zs_list.append(i)
print(f"此范围内的质数有{zs_list}")

# 有一组学生成绩，要求输出及格的学生和不及格的学生
student_scores = {"张三": 34, "里斯": 89 ,"王武": 65, "赵八": 59}
failing_students = []
passing_students = []
for key,value in student_scores.items():
    if value < 60:
        failing_students.append(key)
    else:
        passing_students.append(key)
print(f"及格的学生：{passing_students}")
print(f"不及格的学生：{failing_students}")
        
# 有一组黑名单，如果用户输入的内容中包含黑名单的内容，那么输出时将黑名单词替换为*号
blacklist = ["傻逼", "习近平", "沙雕", "不文明用语"]
usr_input = input("请输入句子：")
for word in blacklist:
    if word in usr_input:
        usr_input = usr_input.replace(word, "**")  # replace方法不会在原本的变量作修改，replace会产生一个新的字符串
print(f"优化过后的句子：{usr_input}")
