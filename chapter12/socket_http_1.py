import socket
from selectors import DefaultSelector,EVENT_READ,EVENT_WRITE
from urllib.parse import urlparse

stop = False
selector = DefaultSelector()
urls = []

class Fetcher:
    # def __init__(self,urls):
    #     # self.selector = DefaultSelector()
    #     self.urls = urls
    #     self.stop = False

    def connected(self,key):
        # self.selector.unregister(key.fd)
        selector.unregister(key.fd)
        self.client.send(
            "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        # self.selector.register(self.client.fileno(),EVENT_READ,self.readable)
        selector.register(self.client.fileno(),EVENT_READ,self.readable)


    def readable(self,key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            # self.selector.unregister(key.fd)
            data = self.data.decode("utf8","ignore")
            htmls = data.split("\r\n\r\n")
            html = htmls[1]
            print(html)
            self.client.close()
            # self.urls.remove(self.spider_url)
            urls.remove(self.spider_url)
            print(urls)
            global stop
            if not urls:
            # if not self.urls:
                # self.stop = True
                stop = True

    def get_url(self,url):
        self.spider_url = url
        url = urlparse(url)
        self.host=url.netloc
        self.path=url.path
        self.data = b""
        if self.path=="":
            self.path = "/"

        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.setblocking(False)

        try:
            self.client.connect((self.host,80))
        except BlockingIOError as e:
            pass

        # self.selector.register(self.client.fileno(),EVENT_WRITE,self.connected)
        selector.register(self.client.fileno(),EVENT_WRITE,self.connected)

    # def run(self):
    #     for url in urls:
        # for url in self.urls:
        #     self.get_url(url)
        # self.loop()

def loop():
    while not stop:
        # ready = fetcher.selector.select()
        ready = selector.select()
        for key,mask in ready:
            call_back = key.data
            call_back(key)

if __name__ == "__main__":
    urls =["http://www.baidu.com","http://www.qq.com"]
    # for i in range(20):
    #     urls.append("http://shop.projectsedu.com/goods/{}/".format(i))
    # fetcher = Fetcher()
    # fetcher = Fetcher(urls)
    # fetcher.run()
    for i in urls:
        fetcher = Fetcher()
        fetcher.get_url(i)
    loop()