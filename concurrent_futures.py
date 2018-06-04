from concurrent.futures import ThreadPoolExecutor, as_completed, wait
from concurrent.futures import Future
"""
Future未来对象，task的返回容器
因为submit后的对象没有完成，有可能在将来完成
阅读源码 
阻塞的方法都有timeout参数
event也是一个锁
"""



"""
线程池  为什么要用线程池：方便管理并发大小和功能
主线程中可以获取某一个线程的状态或者某一个任务的状态，以及返回值
当一个线程完成的时候我们主线程能立即知道状态和返回值
futures可以让多线程和多进程编码接口一致

通过submit函数提交执行的函数到线程池中，submit是立即返回
done方法用于判定某个任务是否完成
result方法是个阻塞的方法，获取task的执行结果
cancel方法在submit返回的对象上才能进行操作，在执行中（就是在线程池中的时候）或执行后是取消不了的

要获取已经成功的task的返回
    用到as_completed
    as_completed实际上是一个生成器，只会返回已经完成的yield
    task是异步的，一旦异步的task完成，as_completed就可以接收到
    map的顺序是一致的，而as_completed是谁先完成谁先打印
wait函数可以让主线程进行阻塞，可以指定特定的task进行阻塞，当该task完成后才继续向下进行
可以接收什么时候不进行阻塞的参数
"""

import time

def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times

executor = ThreadPoolExecutor(max_workers=1)

# 获取已经成功的task的返回
urls = [3,2,4]
all_task = [executor.submit(get_html, (url)) for url in urls]
wait(all_task, return_when='FIRST_COMPLETED')
print("main")
# for future in as_completed(all_task):
#     data = future.result()
#     print("get {} page success".format(data))

# 通过executor的map获取已经完成的task的值
# for data in executor.map(get_html, urls):
    # 自动完成了data的赋值
    # data = future.result()
    # map也是生成器
    # print("get {} page success".format(data))

# task1 = executor.submit(get_html, (3))
# task2 = executor.submit(get_html, (2))
# print(task1.done())
# print(task2.cancel())
# time.sleep(3)
# print(task1.done())
# print(task1.result())