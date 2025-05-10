def func(a, b, c):
    print(a, b, c)


list1 = [1, 2, 3]
func(*list1)  # 把列表中的所有元素，当作参数进行传递   注意是一个*
tuple1 = (4, 5, 6)
func(*tuple1)

dict1 = {'a': 7, 'b': 8, 'c': 9}
func(**dict1)  # 将字典作为参数进行传递，相当于a=7,b=8,c=9关键字参数进行传递    注意是两个**
