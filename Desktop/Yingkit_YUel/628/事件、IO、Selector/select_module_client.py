import socket

sk = socket.socket()

sk.connect(('127.0.0.1', 8090))

while 1:
    data = input('please input:')
    sk.send(data.encode('utf8'))
    recv_data = sk.recv(1024)
    print(recv_data.decode('utf8'))
