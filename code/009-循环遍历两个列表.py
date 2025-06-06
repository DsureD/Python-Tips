list1 = ['a','b','c','d','e','f','g']
list2 = [1,2,3,4,5,6,7]

for x,y in zip(list1,list2):  # zip()将多个列表封装，一一对应分别遍历，如果两个列表长度不一样，以最少的列表次数遍历
    print(x,y)   # x 对应list1，y对应list2

'''运行结果：如果两个列表长度不一样，以最少的列表次数遍历（结果为list1[0]，对应list2[0]，一一对应）
a 1
b 2
c 3
d 4
e 5
f 6
g 7
'''
