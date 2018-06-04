"""
gil global interpreter lock
python中一个线程对应于c语言中的一个线程(cpython)
gil使得同一时刻只有一个线程在一个线程在一个cpu上执行字节码，无法将多个线程映射到多个cpu上执行
python的运行过程将py文件转换成字节码
dis反字节码库
pypi就是去gil化的
gil使得无法利用多核优势
"""
import dis
def add(a):
    a = a + 1
    return a

print(dis.dis(add))

"""
gil在某些情况下是会被释放的，不会被一直占用
gil的释放在py2和py3中有所区别
gil释放根据的是字节码的行数以及根据时间片来划分，gil在遇到io操作的时候主动释放，不是根据线程的完成后才释放
gil在遇到io操作的时候主动释放，这使得gil的多线程在io操作频繁的情况下是使适用的
"""

total = 0
def add():
    global total
    for i in range(1000000):
        total += 1

def desc():
    global total
    for i in range(1000000):
        total -= 1
import threading
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(total)