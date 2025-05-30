def add(a, b):
    print(f'{a} + {b} = {a + b}')


def by(a, b):
    print(f'{a} * {b} = {a * b}')


def_list = [add, by]
for i in def_list:
    i(8, 9)
