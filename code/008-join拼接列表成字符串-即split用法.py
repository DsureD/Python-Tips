a = 'Hello World Yes'
b = a.split(' ')   # split(括号内不填则默认用空格)方法是将a用字符串‘ ’切片成列表b：['Hello', 'World', 'Yes']
c = '*'.join(b)    # ‘’.join(列表)方法是本例中，将列表b多个内容用字符串‘*’拼接成一个字符串：Hello*World*Yes
print(b,c)
