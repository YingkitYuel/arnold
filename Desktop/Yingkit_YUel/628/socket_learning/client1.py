import socket

Connector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Connector.connect(('127.0.0.1', 8080))

while True:
    msg = input('>>:').strip()
    Connector.send(msg.encode('utf-8'))
    data = Connector.recv(1024)
    print('客户端收到的消息为：', data.decode('utf-8'))
