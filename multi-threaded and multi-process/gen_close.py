import time
"""
 生成器的其他方法：throw，close
"""

def gen_func():
    try:
        yield "https://www.baidu.com"
    except GeneratorExit:
        pass
    yield 2
    yield 3
    return "bobby"

if __name__ == "__main__":
    gen = gen_func()
    next(gen)
    gen.close()
    # 是向上抛出异常,main
    next(gen)

    # GeneratorExit是继承自BaseException,Exception