import time
"""
python为了将语义变得更加明确，就引入了async和await关键词用于定义原生的协成
yield不能出现在async中
await只能出现在async中
"""

async def downloader(url):
    return "vhbn"

async def download_url(url):
    # do somethings
    html = await downloader(url)
    return html

if __name__ == "__main__":
    coro = download_url("http")
    coro.send(None)