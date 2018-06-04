from threading import Lock, RLock
total = 0
lock = Lock()
def add():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total += 1
        lock.release()

def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()
import threading
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

"""
1.load a
2.load 1
3.+
4.赋值给a

线程以字节码行数为单位，赋值给a这个很容易被覆盖

web电商开发中容易遇到这个问题，减库存的时候，多个用户多个线程操作一个变量

如何解决这个问题：
线程同步机制
加上Lock后，一旦代码段被锁住，该代码段执行完后才会解锁去执行其他代码段
acquire和release可以利用上下文管理器来解决更加优雅
加上锁后性能会变差
锁会引起死锁：例如acquire后没有释放又进行acquire（子函数形式），但是可以引入可重入的锁
RLock:在同一个线程里面，可以连续调用多次acquire，但是acquire的次数要和release的次数相等 
死锁情况：
    A(a,b)
    acquire(a)
    acquire(b)
    
    B(a,b)
    acquire(b)
    acquire(a)
    资源竞争问题
"""

# def add1(a):
#     a += 1
#
# def desc1(a):
#     a -= 1
#
# import dis
# print(dis.dis(add1))
# print(dis.dis(desc1))
#
thread1.join()
thread2.join()
print(total)