from socket import *
import subprocess
import json
import struct

ip_port = ('127.0.0.1', 8898)
buf_size = 1024
back_log = 5

server_link = socket(AF_INET,SOCK_STREAM)
server_link.bind(ip_port)
server_link.listen(back_log)

while True:
    conn,addr = server_link.accept()
    print('已经成功连接：', addr)
    while True:
        try:
            cmd = conn.recv(buf_size)
            res = subprocess.Popen(cmd.decode('utf-8'), stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            res_out = res.stdout.read()
            res_err = res.stderr.read()

            if res_err:
                res_data = res_err
            else:
                res_data = res_out

            #制作数据报的报头
            data_dict = {
                'lenth' : len(res_data),
                'filename' : 'a.txt',
                'md5' : 'asdadasdsadadsad'
            }
            head_dict = json.dumps(data_dict).encode('utf-8')

            #发送报头的长度
            head_len = struct.pack('i', len(head_dict))
            conn.send(head_len)

            #发送数据报
            conn.send(head_dict)

            #发送真实数据
            conn.send(res_data)
        except Exception as e:
            print(e)
            break
    conn.close()
server_link.close()

