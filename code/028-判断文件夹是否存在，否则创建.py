import os

file_path = './test6/001/002'  # ../上当前运行的上级文件夹,最后的那"/"加不加都可，主要根据后面的要求
if not os.path.exists(file_path):
    os.makedirs(file_path)  # os.makedirs()可以创建多层(或单层)文件夹； os.mkdir()只能创建一层文件夹  【注意两者区别】
print('done')
