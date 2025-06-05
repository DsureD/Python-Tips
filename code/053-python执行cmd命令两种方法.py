import os
import subprocess


os.system('dir')  # 执行cmd命令方法一


# 如果文件名中有空格需用""包起来,cmd的缺点
command = 'echo "Hello World"'
subprocess.call(command, shell=True)  # 执行cmd命令方法二
