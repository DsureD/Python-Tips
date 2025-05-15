
with open("print2txt.txt", "w") as f:
    print('11111', file=f, end='\n', sep=' ')  # end默认打一行换一行，sep为分隔符，默认为空格
    print('22222', file=f)
