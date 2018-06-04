# 生成器是可以暂停的函数
import inspect
def gen_func():
    value = yield 1
    # 返回值给调用方，调用方通过sned方式返回值给gen
    return "vhbn"
"""
用同步的方式编写异步的代码，
晕晕晕(((φ(◎ロ◎;)φ)))
"""

if __name__ == "__main__":
    gen = gen_func()
    print(inspect.getgeneratorstate(gen))
    next(gen)
    print(inspect.getgeneratorstate(gen))
    try:
        next(gen)
    except StopIteration as e:
        pass
    print(inspect.getgeneratorstate(gen))