import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

"""
selectors是基于select实现的，但是包装的更加好用，会根据平台自动选择使用poll还是epoll
使用select完成http请求

1.select本身不支持register模式
2.socket状态变化以后的回调是有程序员完成的
select+回调+事件循环
事件循环来驱动回调

该程序并发性高
使用单线程不存在切换消耗问题

可以利用该方法实现聊天群，爬虫


回调之痛:
回调函数执行不正常，异常处理问题
回调嵌套问题
回调嵌套异常问题
数据被多个回调处理（类方式可以解决）
（同步体验）
如何变量共享
总结如下：
1.可读性差
2.共享状态管理困难
3.异常处理困难

以上问题可以由协程解决，解决回调编写困难的问题
C10K问题：并发问题
C10M问题：保持高并发连接

1.回调模式编码复杂度高
2.同步编程的并发性不高
3.多线程需要线程间的同步，lock

1.采用同步的方式去编写异步的代码
2.使用单线程去切换任务
    1.线程由操作系统切换的，单线程切换意味着需要程序员自己去调度任务
    2.不在需要锁，并发性高，如果单线程内切换函数，性能远高于线程切换，并发性更高
"""
selector = DefaultSelector()
urls = ["http://www.baidu.com"]
stop = False

class Fetcher:
    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send("GET")
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        while True:
            d = self.client.recv(1024)
            if d:
                self.data += d
            else:
                selector.unregister(key.fd)
                data = self.data.decode("utf8")
                html_data = data.split("\r\n\r\n")[1]
                print(html_data)
                self.client.close()
                urls.remove(self.spider_url)
                if not urls:
                    global stop
                    stop = True

    def get_url(self, url):
        self.spider_url = url
        self.data = b""
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        if self.path == "":
            path = "/"

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)

        try:
            self.client.connect((self.host, 80))
        except BlockingIOError as e:
            pass

#         注册
        selector.register(self.client.fileno(), EVENT_WRITE, )

def loop():
    # 事件循环，不停的请求socket的状态并调用对应的回调函数
    # 回调+事件循环+select(poll\epoll)
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)


if __name__ == "__main__":
    fetcher = Fetcher()
    fetcher.get_url("http://www.baidu.com")
    loop()