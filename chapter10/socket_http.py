import socket
from urllib.parse import urlparse

def get_url(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host,80))

    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path,host).encode("utf8"))

    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break

    html = data.decode("utf8")
    html = html.split("\r\n\r\n")
    html = html[1]
    print(html)
    client.close()

if __name__=="__main__":
    get_url("http://www.baidu.com")
