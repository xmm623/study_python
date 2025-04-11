# match case语句
# 类似于其他语言的switch case语句
# 语法
# match <expression>:
#     case <pattern1>: 
#         <statement1>  当表达式匹配到<pattern1>时执行的语句
#     case <pattern2>:
#         <statement2>  当表达式匹配到<pattern2>时执行的语句
#     ...
#     case _: 当表达式不匹配任何模式时执行的语句,类似于其他语言里的default分支

# 例子
def match_case_example(value):
    match value:
        case 1:
            print("Value is 1")
        case 2:
            print("Value is 2")
        case 3 | 4: # 使用 | 来匹配多个值
            print("Value is 3 or 4")
        case _:
            print("Value is something else")
# 测试
match_case_example(1)  # 输出: Value is 1
match_case_example(2)  # 输出: Value is 2
match_case_example(4)  # 输出: Value is 4

