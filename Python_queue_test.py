from queue import Queue
"""
通过queue的方式进行线程间同步

"""
import time
import threading

detail_url_list = []

def get_detail_html(queue):
    # 爬取文章详情页
    # 由于爬取文章列表页更快，所以爬取文章详情页要用并发的形式，用pop，不能用for了
    while True:
        # 可能引发线程安全问题

        # get方法是阻塞的方法
        # 用queue就是线程安全的，可见put，get方法具体实现
        # dqueue是双端队列是线程安全的，在字节码的级别上就达到了线程安全，Queue的get方法实际上用的就是deque的popleft方法
        # 队列的put_nowait方法是异步方法，向队列中放数据的时候没必要等到完成后才返回
        # 队列的join函数会阻塞主线程，要调用taskdone函数join函数才会退出
        # 线程通信首选Queue
        # 当数据类型过多的时候也可以选用共享变量的方法来完成线程通信
        url = queue.get()
        # for url in detail_url_list:
        print('get detail html started')
        time.sleep(2)
        print("get detail html end")

def get_detail_url(queue):
    # 爬取文章列表页
    while True:
        print('get detail url started')
        time.sleep(2)
        for i in range(20):
            detail_url_list.append("https://projectsedu.com/{id}".format(id=i))
        print("get detail url end")

"""
1.线程间的通信方式-共享变量，这种方法在多进程中是行不通的，也可以为共享变量单独创建一个py文件，import的时候不要直接import变量，import文件就行
共享变量不适用来做线程间的通信，存在线程安全问题

"""
if __name__ == "__main__":
    detail_url_queue = Queue(maxsize=1000)
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
        html_thread.start()
    start_time = time.time()
    # thread1.start()
    # thread2.start()
    # # 设置线程阻塞
    # thread1.join()
    # thread2.join()

    print("last time: {}".format(time.time() - start_time))