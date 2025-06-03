import time
from multiprocessing.dummy import Pool


def test_pool(item):
    print(item)
    time.sleep(1)


if __name__ == '__main__':
    start_t = time.time()
    mult_pool = Pool(20)  # 创建线程池(数量)
    some_list = [i for i in range(100)]  # 需要处理的多列表任务
    for item in some_list:
        mult_pool.apply_async(test_pool, args=(item,))  # 异步调用多线程，test_pool是需要多线程调用的函数,args是函数的传参(以元组形式【注意逗号结尾】)
    mult_pool.close()  # 关闭进程池
    mult_pool.join()  # 阻塞进程，这样才可以一个个地去完成
    print(f"耗时：{time.time() - start_t:.3f}秒")
