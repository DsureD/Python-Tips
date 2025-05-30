import random as rd
import time

'''案例一 ======================================='''
# -----------被调用方----------------
def newRN(fn):  # 生成10个[0,1)之间小数
    ns = []
    for i in range(10):
        n = round(rd.random(), 2)
        ns.append(n)
    # 不用直接return,因为调用方通知不接返回结果
    # 改成回调函数方式
    fn(ns)  # 调用是调用方函数,这一操作称之为回调


# 定义回调函数--- 调用方  ----
def abc(*args):
    # 进入到本函数内,意味蓍被调用方函数己执行完
    print("生成数据成功")
    print(args)


newRN(abc)

'''案例二 ======================================='''
def test(fn,n):
    start_time = time.time()
    for i in range(n):
        rd.random()
        time.sleep(0.1)
        end_time = time.time()
        seconds = round(end_time - start_time)
        fn(seconds,n)
def test_callback(tm_s,n):
    print(f'生{n}成个数，用时{tm_s}秒')

test(test_callback,5)
