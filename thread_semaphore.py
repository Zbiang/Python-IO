import threading
"""
Semaphore 是用于控制进入数量的锁
文件，读，写，写一般只是用于一个线程写，读可以允许有多个，

做爬虫，控制并发数量
semaphore的acqiure和release方法有点不一样，减法原理，加法原理
semaphore内部的实现是用的condition
Queue也是内部实现是用的condition，看Queue源码
"""
import time

class HtmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("got html text success")
        self.sem.release()

class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()
            html_thread = HtmlSpider("https://baidu.com/{}".format(i), self.sem)
            html_thread.start()


if __name__ == "__main__":
    sem = threading.Semaphore(3)
    url_producer = UrlProducer(sem)
    url_producer.start()
