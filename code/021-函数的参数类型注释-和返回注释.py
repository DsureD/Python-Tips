def add(x: int, y: int) -> int:  # 冒号后的int表示x是int类型（不是也不会报错），->注释说明该函数返回整数型数据(也可能不是，不会报错）
    '''
    在函数下方敲三个单（或双）引号，回车，有些IDE就会自动生成函数的功能说明文档注释，例如参数是什么，返回值是什么的说明
    :param x: int类型数据
    :param y: int类型数据
    :return: 返回 x和y相加的结果
    '''
    print(x, y)
    return x + y


add(12, 34)
