from threading import Condition
import threading
"""
条件变量，用于复杂的线程间的同步

利用lock解决不了
"""
# class XiaoAi(threading.Thread):
#     def __init__(self, lock):
#         super().__init__(name="小爱")
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print("{} : 在 ".format(self.name))
#         self.lock.release()
#
#         self.lock.acquire()
#         print("{} : 在 ".format(self.name))
#         self.lock.release()
#
# class TianMao(threading.Thread):
#     def __init__(self, lock):
#         super().__init__(name="天猫精灵")
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print("{} : 小爱同学 ".format(self.name))
#         self.lock.release()
#
#         self.lock.acquire()
#         print("{} : 小爱同学 ".format(self.name))
#         self.lock.release()

"""
通过condition完成协同对话
condition自带上下文管理器，enter自动调用acquire，exit自动调用release
wait允许等待某个条件变量的通知
notify通知线程里调用wait的方法启用

wait先启动，启动顺序很重要
调用with语句后才可以调用wait和notify方法
详细见源码，condition有两把锁，一把底层锁会在线程调用了wait方法的时候释放，上面的锁会在每次调用wait的时候分配一把并放入到condition的等待队列中
，等待notify方法的唤醒
condition内部也用到了deque
"""

class XiaoAi(threading.Thread):
    def __init__(self, condition):
        super().__init__(name="小爱")
        self.condition = condition

    def run(self):
        with self.condition:
            self.condition.wait()
            print("{} : 在 ".format(self.name))
            self.condition.notify()
            self.condition.wait()
            print("{} : ok ".format(self.name))
            self.condition.notify()


class TianMao(threading.Thread):
    def __init__(self, condition):
        super().__init__(name="天猫精灵")
        self.condition = condition

    def run(self):
        with self.condition:
            print("{} : 小爱同学 ".format(self.name))
            self.condition.notify()
            self.condition.wait()
            print("{} : 我们来对古诗吧 ".format(self.name))
            self.condition.notify()
            self.condition.wait()


if __name__ == "__main__":
    condition = threading.Condition()
    xiaoai = XiaoAi(condition)
    tianmao = TianMao(condition)

    xiaoai.start()
    tianmao.start()
