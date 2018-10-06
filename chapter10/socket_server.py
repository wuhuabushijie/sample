import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0',8000))
server.listen()


def handle_sock(sock,addr):
    while True:
        data = sock.recv(1024)
        message_received = data.decode("utf8")
        print("Client: " + message_received)
        message_sent = input("Me: ")
        sock.send(message_sent.encode("utf8"))

while True:
    sock, addr = server.accept()
    sub_thread = threading.Thread(target=handle_sock,args=(sock,addr))
    sub_thread.start()