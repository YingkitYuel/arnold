import socket

Connector = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creat the connector

Connector.bind(('127.0.0.1', 8000))  #bind the local ip address and the port

Connector.listen(5) # wait for the connect socket

conn,addr = Connector.accept() #wait for thr link
while True:
    msg = conn.recv(1024) #recept the message
    print('服务器端收到的消息为：', msg.decode('utf-8'))
    conn.send(msg.upper())

conn.close()

Connector.close()