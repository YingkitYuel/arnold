from socket import *

buf_size = 1024
ip_port = ('127.0.0.1', 8888)
client_server = socket(AF_INET, SOCK_STREAM)

client_server.connect(ip_port)

while True:
    cmd = input('Please input a command:').strip()
    if not cmd:continue
    if cmd == 'quit':break
    client_server.send(cmd.encode('utf-8'))
    msg = client_server.recv(buf_size)
    print('收到的消息为：',msg.decode('gbk'))
client_server.close()