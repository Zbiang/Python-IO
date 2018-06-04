import os
import time
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
# fork只能用于linux/unix中
"""
子进程会将主进程的数据原样copy到进程中包括代码，但是数据是隔离的
子进程只会运行fork后面的代码

multiprocessing的实现也是基于PPE实现的
但是更建议用PPE实现，因为接口类型多线程和多进程是一样的，更加经典
"""
# pid = os.fork()
# print("Geovhbn")
# if pid == 0:
#     print("子进程 {} ， 父进程是： {} ".format(os.getpid(), os.getppid()))
# else:
#     print("我是父进程： {} ".format(pid))
#
# time.sleep(2)
# sleep的原因

# 多进程编程
import time
def get_html(n):
    time.sleep(n)
    print("sub_progress success")
    return n

"""
pid是进程的id
"""
# 使用进程池

if __name__ == "__main__":
    # progress = multiprocessing.Process(target=get_html, args=(2,))
    # print(progress.pid)
    # progress.start()
    # print(progress.pid)
    # progress.join()
    # print("main progress end")

    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    result = pool.apply_async(get_html, args=(3,))
    # 等待所有的任务完成
    pool.close()
    pool.join()
    print(result.get())


    # imap 完成的顺序和添加的顺序是一样的
    for result in pool.imap(get_html, [1,5,3]):
        print("{} sleep success".format(result))
    # 谁先完成先打印谁
    for result in pool.imap_unordered(get_html, [1,5,3]):
        print("{} sleep success".format(result))

