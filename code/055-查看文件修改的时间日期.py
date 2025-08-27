import os
import time

file_path = "example.txt"

# 获取最后修改时间（时间戳）
mtime = os.path.getmtime(file_path)

# 格式化为可读时间
readable_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(mtime))

print("最后修改时间戳:", mtime)
print("最后修改时间:", readable_time)

# 更简单的一种方法 --------------------------------------
'''
from pathlib import Path
import time

file_path = Path("example.txt")

mtime = file_path.stat().st_mtime
print("最后修改时间:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(mtime)))
'''
