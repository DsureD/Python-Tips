import os
path = './filepath'  # 文件路径（当前文件夹下‘filepath’文件夹）
if not os.path.exists(path):
    os.mkdir(path)
