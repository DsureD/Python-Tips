import time
from threading import Thread


def output1():
    while True:
        print('11111',end='',flush=True)
        time.sleep(0.1)

def output2():
    while True:
        print('22222',end='',flush=True)
        time.sleep(0.1)
def main():
    t1 = Thread(target=output1)   # 注意函数名后没有()，这里不是调用，只是告诉线程的目标是函数output1
    t1.start()
    t2 = Thread(target=output2)  # 如果函数需要传参数，这样：Thread(target=output2,args=('ping',))，注意arges=后要元组类型数据。
    t2.start()

if __name__ == '__main__':
    main()
