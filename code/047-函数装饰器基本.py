import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"函数：{func.__name__} 运行耗时：{(end_time - start_time):.2f} 秒")
        return result
    return wrapper

@timing_decorator
def my_function():
    # do something
    print('aaa')
    for i in range(5):
        time.sleep(1)
        print(i)


my_function()
