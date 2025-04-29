# 字典 嵌套列表 再嵌套字典 的情况
dict1 = {'subjects': [{'episodes_info': '', 'rate': '9.7', 'title': '肖申克的救赎', 'playable': True, 'id': '1292052'}]}

for value in dict1:  # 只针对有一个value嵌套的时候
    a = dict1[value]  # [{'episodes_info': '', 'rate': '9.7', 'title': '肖申克的救赎', 'playable': True, 'id': '1292052'}]
print(a)
print(dict1['subjects'])  # [{'episodes_info': '', 'rate': '9.7', 'title': '肖申克的救赎', 'playable': True, 'id': '1292052'}]

for i in a:
    print(f"{i['rate']}分，{i['title']}")  # 9.7分，肖申克的救赎

dict2 = {'A': 123, 'B': 345, 'C': 345}
for k in dict2:
    print(k, dict2[k])  # A 123 、 B 345  、 C 345
    print(k)  # A     、 B      、 C
    print(dict2[k])  # 123   、 345    、 345

spam = {'A': 123, 'B': 345, 'C': 345}
for k, v in spam.items():
    print(k, v)

a = {'name': {'age': 18}}
print(a['name']['age'])  # 18
print(a['name'])  # {'age':18}
