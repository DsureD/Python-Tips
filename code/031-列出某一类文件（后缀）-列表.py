import glob

csv_list = glob.glob(r'*.py')  # 列出当前文件夹下，后缀为.py的文件列表

print(csv_list)  # ['01-一行写if-else判断语句.py', '02-提取字典的key 和 value.py',...]
