from socket import *
import json
import struct

ip_port = ('127.0.0.1', 8898)
buf_size = 1024

client_link = socket(AF_INET, SOCK_STREAM)
client_link.connect(ip_port)

while True:
    cmd = input('请输入一个命令：').strip()
    if not cmd:continue
    client_link.send(cmd.encode('utf-8'))

    #接收报文头长度
    len_dict = client_link.recv(4)

    #把Byte解开
    head_len_dict = struct.unpack('i', len_dict)
    print(head_len_dict)
    head_len_dict = head_len_dict[0]

    #收报文
    dict_data = client_link.recv(head_len_dict).decode('utf-8')

    #将报文的json解开
    dict = json.loads(dict_data)

    #取得数据长度
    data_len = dict['lenth']

    #收数据
    recv_size = 0
    total_data = b''
    while recv_size < data_len:
        data = client_link.recv(1024)
        total_data += data
        recv_size += len(data)

    print(data.decode('utf-8'))

client_link.close()