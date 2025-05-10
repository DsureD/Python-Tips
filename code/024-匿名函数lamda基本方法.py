def func1(x,y):
    return x * y

print(func1(15,3))

# 语法结构   lambda 参数: 返回值
func2 = lambda x,y: x * y   # 功能等同于func1函数
print(func2(15,3))

salaries = {'a':3000,'b':8000,'c':2000,'d':100}

res = max(salaries)  # 默认按照key取值，也就a,b,c,d
print(res)

def func3(k):
    return salaries[k]
res2 = max(salaries,key=func3)   # 按salaries的value取最大值，这里还新建了个外置函数
print(res2)

res3 = max(salaries,key=lambda k:salaries[k])   # 等同于res2
print(res3)
