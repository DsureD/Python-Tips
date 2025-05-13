def add(a, b):
    print(a + b)


dict1 = {'a': 5, 'b': 8}
tuple1 = (7, 9)

add(**dict1)  # 相当于add(a=5,b=8),把字典的键值对作为参数传递过去  注意：2个**
add(*tuple1)  # 相当于add(7,9)，把元组作为参数传递过去 注意：1个*
