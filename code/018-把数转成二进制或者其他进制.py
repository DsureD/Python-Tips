num = 15

# 下面的0是索引，对应着format中的索引（如果只有一个，前面0可以不写）
print('{0:b}'.format(num))  # b 二进制数
print('{0:c}'.format(num))  # c unicode
print('{0:d}'.format(num))  # d 整数类型
print('{0:o}'.format(num))  # o 八进制数
print('{0:x}'.format(num))  # x 十六进制小写
print('{0:X}'.format(num))  # X 十六进制大写

print(f'{num:b}')  # b 二进制数  上面的也都可以这样写
