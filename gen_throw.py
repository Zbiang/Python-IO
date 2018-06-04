import time
"""
 生成器的其他方法：throw，close
"""

def gen_func():
    try:
        yield "https://www.baidu.com"
    except Exception as e:
        pass
    yield 2
    yield 3
    return "bobby"

if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.throw(Exception, "DOWNLOAD ERROR")
    print(next(gen))
    gen.throw(Exception, "DOWNLOAD ERROR")
    # 是gen中的异常