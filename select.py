import time
"""
1.epoll并不代表一定比select好
    在并发高的情况下，连接活跃度不是很高，epoll比select
    并发性不高，同时连接很活跃，select比epoll好
"""

"""
通过非阻塞io实现http请求

该方法是同步方法
"""
import socket
from urllib.parse import urlparse


def get_url(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)
    try:
        client.connect((host, 80))
    except BlockingIOError as e:
        pass

    while True:
        try:
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n")
            break
        except OSError as e:
            pass

    data = b""
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue
        if d:
            data += d
        else:
            break

    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()

if __name__ == "__main__":
    get_url("http://www.baidu.com")
