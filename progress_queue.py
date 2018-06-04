from multiprocessing import Process, Queue
# from queue import Queue
import time
# 多进程编程不能用一般的Queue,多线程可以，多线程的Queue
# def producer(queue):
#     queue.put("a")
#     time.sleep(2)
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)
#
# if __name__ == "__main__":
#     queue = Queue(10)
#     my_producer = Process(target=producer, args=(queue,))
#     my_consumer = Process(target=consumer, args=(queue, ))
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()

"""
共享全局变量，不能适用于多进程，但是可以适用于多线程
多进程数据是隔离的
"""
def producer(a):
    a += 1
    time.sleep(2)

def consumer(a):
    time.sleep(2)
    print(a)

if __name__ == "__main__":
    a = 1
    my_producer = Process(target=producer, args=(a,))
    my_consumer = Process(target=consumer, args=(a, ))
    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()

"""
multiprocessing中的queue不能用于pool进程池
"""

"""  
并发，并行，同步，异步（消息机制），阻塞，非阻塞（函数调用机制）
C10K问题，io多路复用
Unix下五种I/O模型：
    阻塞式I/O（浪费CPU资源）
    非阻塞式I/O（爬虫程序setblocking）阻塞不会消耗cpu（非阻塞式io反复去问数据是否准备好）
    
    I/O复用（相比非阻塞式io，select可以监听多个socket）
    信号驱动式I/O（使用较少）
    异步I/O（POSIX的aio_系列函数）
select，pill，epoll本质上都是同步IO
异步IO的实现本质上就是负责把数据从内核空间拷贝到用户空间
select
    缺点：单个进程能够监视的文件描述符的数量存在最大限制
poll
    pollfd的指针
    没有最大数量限制
epoll
    在windows下不支持
    没有描述符的限制，红黑树
"""