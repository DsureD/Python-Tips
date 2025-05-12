import time

a = ''
for i in range(50):
    a += "▊"
    print(f'\r[{a:<50}]{i*2+2}%',end='')  # \r（配合end=''）每次都从行首打印
    time.sleep(0.1)
