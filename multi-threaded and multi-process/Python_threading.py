"""
对io操作来说，多线程和多进程性能差别不大
多线程编程
1.通过Thread类实例化，爬虫就io型的，下面的例子就是爬虫例子
操作系统能过调度和操作的最小单元是线程
但是最开始的时候能调度的是进程，进程消耗资源较大
线程依赖进程，一个进程下有多个线程

当主线程退出的时候，子线程kill掉
setDaemon就是当主线程关闭后，该守护线程也会关闭掉
线程一般是并发的过程，通过设置时间就可以看到
join设置线程阻塞

当代码量较大的时候，可以继承Thread，使用第二种方法
"""
import time
import threading
def get_detail_html(url):
    # 爬取文章详情页
    print('get detail html started')
    time.sleep(2)
    print("get detail html end")

def get_detail_url(url):
    # 爬取文章列表页
    print('get detail url started')
    time.sleep(2)
    print("get detail url end")

if __name__ == "__main__":
    thread1 = threading.Thread(target=get_detail_html, args=('',))
    thread2 = threading.Thread(target=get_detail_url, args=('',))
    thread1.setDaemon(True)
    thread2.setDaemon(True)
    start_time = time.time()
    thread1.start()
    thread2.start()
    # 设置线程阻塞
    thread1.join()
    thread2.join()

    print("last time: {}".format(time.time() - start_time))

"""
方法二：通过继承Thread来实现多线程
    一般重载run方法，不重载start方法
    run方法里一般重写逻辑
    通过使用编写类的实例就可以完成多线程编程
"""

class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print('get detail html started')
        time.sleep(2)
        print("get detail html end")

class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print('get detail url started')
        time.sleep(4)
        print("get detail url end")

if __name__ == "__main__":
    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetDetailUrl("get_detail_url")
    start_time = time.time()
    thread1.start()
    thread2.start()
    # 设置线程阻塞
    thread1.join()
    thread2.join()

    print("last time: {}".format(time.time() - start_time))

"""
定义线程类可以加入复杂的逻辑，大部分情况下更加适用
简单的情况下第一种方法更加适用,动态的建立thread，用线程池
"""
