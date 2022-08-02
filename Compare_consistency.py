import json
# def compare_consistency():
#     with open('category.txt') as category_object:
#         category_file  = category_object.readline()
#     with open('section_category.txt') as section_category_object:
#         section_category_file = section_category_object.readline()
#     for section_category_file in sec:

global category_file,section_category_file,category_json,section_category_json
with open('category.txt') as category_object:
    category_file  = category_object.read()
with open('section_category.txt') as section_category_object:
    section_category_file = section_category_object.read()

category_json = json.loads(category_file)
section_category_json = json.loads(section_category_file)
for i in category_json:
    name=i['object']
    print(name)