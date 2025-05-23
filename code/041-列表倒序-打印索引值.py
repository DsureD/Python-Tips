a = [0, 1, 2, 3, 4, 5]

for index, item in enumerate(a[-1::-1]):
    print(index, item)
b = [i for i in a[-1::-1]]
print(a)  # [0, 1, 2, 3, 4, 5]
print(b)  # [5, 4, 3, 2, 1, 0]
