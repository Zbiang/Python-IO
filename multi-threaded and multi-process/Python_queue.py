import threading
"""
线程间的通信

"""
import time
import threading

detail_url_list = []

def get_detail_html(detail_url_list):
    # 爬取文章详情页
    # 由于爬取文章列表页更快，所以爬取文章详情页要用并发的形式，用pop，不能用for了
    while True:
        if len(detail_url_list):
            # 可能引发线程安全问题
            url = detail_url_list.pop()
            # for url in detail_url_list:
            print('get detail html started')
            time.sleep(2)
            print("get detail html end")

def get_detail_url(detail_url_list):
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
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_list,))
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_url, args=(detail_url_list,))
        html_thread.start()
    start_time = time.time()
    # thread1.start()
    # thread2.start()
    # # 设置线程阻塞
    # thread1.join()
    # thread2.join()

    print("last time: {}".format(time.time() - start_time))
