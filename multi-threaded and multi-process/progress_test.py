import time
"""
多线程编程 无法利用多核优势，耗cpu的操作需要用多进程编程，io使用多线程编程，线程间的切换代价远远小于进程
多进程编程 显卡的gpu运算速度大于cpu

1.对于耗费cpu的操作，多进程优于多线程
使用多进程的PPE的时候必须放在if __name__...中
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor
# def fib(n):
#     if n <= 2:
#         return 1
#     return fib(n-1) + fib(n-2)
#
#
# if __name__ == "__main__":
#     with ProcessPoolExecutor(3) as executor:
#         all_task = [executor.submit(fib, (num)) for num in range(25, 35)]
#         start_time = time.time()
#         for future in as_completed(all_task):
#             data = future.result()
#             print("exe result: {}".format(data))
#
#         print("last time is: {}".format(time.time()-start_time))

"""
2.对于IO操作来说，多线程优于多进程
"""
def random_sleep(n):
    time.sleep(n)
    return n

if __name__ == "__main__":
    with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, (num)) for num in [2]*30]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result: {}".format(data))

        print("last time is: {}".format(time.time()-start_time))

