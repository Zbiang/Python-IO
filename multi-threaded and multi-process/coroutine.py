# def get_url(url):
#     # do something 1
#     html = get_html(url) # 耗IO的操作，等待网络请求，此处暂停，切换到其他函数
#     # parse html
#     urls = parse_url(html)

"""
传统的函数调用过程：A->B->C，栈
我们需要一个可以暂停的函数，并且可以在适当的情况下恢复该函数
出现了协成->有多个入口的函数，可以暂停的函数（可以向暂停的地方传入值），生成器yield
"""

def gen_func():
    # 可以产出值，可以接收值（调用方传递进来的值）
    html = yield "https://baidu.com"
    print(html)
    yield 2
    yield 3
    return "bobby"
"""
1.生成器不只是可以产出值，还可以接收值

1.启动生成器的方式有两种，next(),send()
"""
if __name__ == "__main__":
    gen = gen_func()
    url = next(gen)
    # 第一次调用gen的方法且为send时，只能传递None
    # 在调用send发送非none值之前，我们必须启动一次生成器方式有两种：1.gen.send(None) 2.next(gen) 
    html = "vhbn"
    print(gen.send(html))
    print(url)
    # send可以传递值进入生成器内部，同时还可以重启生成器执行下一个yield的位置
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))