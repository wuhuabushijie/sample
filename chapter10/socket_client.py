import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',8000))

while True:
    message = input("Me: ")
    client.send(message.encode("utf8"))
    data = client.recv(1024)
    message_received = data.decode("utf8")
    print("server:"+message_received)
