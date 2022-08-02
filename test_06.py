# with open('files/pi_digits.txt') as file_object:
#     lines = file_object.readlines()
    
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()

# print(pi_string)
# print(len(pi_string))
    
# def test_01(test1,test2=2):
#     """测试把形参默认值写在前面"""
#     print(test1,test2)

# test_01(test1=3,4)

def make_album(singer,album_name):
    """制作专辑"""
    album = {"singer":singer.title(),"album_name":album_name.title()}
    return album

album_haha = make_album("zhangjie","yueliang")
print(album_haha)