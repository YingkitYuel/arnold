from _socket import *
import time

udp_surver = socket(AF_INET, SOCK_DGRAM)

ip_port = ('127.0.0.1',9904)
buf_size = 1024

udp_surver.bind(ip_port)

while True:
    data,addr = udp_surver.recvfrom(buf_size)
    print('The message Surver is :', data.decode('utf-8'))
    print('Link:', addr)
    if not data:
        fmt = '%Y-%m-%d %T'
    else:
        fmt = data.decode('utf-8')
    back_time = time.strftime(fmt)
    udp_surver.sendto(back_time.encode('utf-8'), addr)