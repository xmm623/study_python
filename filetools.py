def read_files(filepath):
    """
        方法：
            读取文件内容
        参数： 
            filepath：文件地址
        返回值：
            读取到的文件内容
    """
    with open(filepath,'r') as f:
        p=f.read()
        return p

def write_files(filepath,content):
    """
    方法：
        写入内容
    参数：
        filepath：文件地址
        content：要写入的内容
    """
    with open(filepath,'w') as f:
        f.write(content)
    
# test1="/Users/weixiaoyu/Downloads/test.txt"
# # f=read_files(test1)  #测试方法是否有用
# # print(f)

# write_files(test1,"zhuijia")
# f=read_files(test1)  #测试方法是否有用
# print(f)
