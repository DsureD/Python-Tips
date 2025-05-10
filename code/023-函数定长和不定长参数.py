def func1(a,b='默认参数'):
    print(a,b)


func1(1,'自定义参数为主') # 定长参数，一一对应

def func2(*args): # 不定长参数，以元组形式接收传递
    print(args)


func2(1,2,3,4) # 只能使用位置传参，不定长参数，调用时可以不传或传多个参数，返回元组


def func3(**kwargs): # 以字典形式接收参数
    print(kwargs)

func3(a=1,b=2,c=3) # 只能使用关键字传参，不定长参数，调用时可以不传或传多个参数，返回字典

def func4(*args,**kwargs):  # 两种不定长参数混合使用
    print(args,kwargs)

func4(1,2,2,2,3,4,ok=2,bot="1oo1")  # args位置传参；kwargs关键字传参
