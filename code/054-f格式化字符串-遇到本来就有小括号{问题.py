var_name = "8888"
# 有百分号的问题，不能使用 % format(var_name)  # 把小括号变成两个{{xxxx}}
# 原内容为：'st=8888&ext={"state":222}'
lst = f'st={var_name}&ext={{"state":222}}'

print(lst)

lst2 = 'st={}&ext={{"state":222}}'.format(var_name)  # 把小括号变成两个{{}}
print(lst2)
