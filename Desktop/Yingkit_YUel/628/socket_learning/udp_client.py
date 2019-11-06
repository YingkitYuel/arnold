from _socket import *

udp_client = socket(AF_INET, SOCK_DGRAM)
ip_port = ('127.0.0.1', 9904)
buf_size = 1024

while True:
    msg = input('Please input a string:').strip()
    udp_client.sendto(msg.encode('utf-8'), ip_port)

    data,addr = udp_client.recvfrom(buf_size)
    print('The ntp Server time is:', data.decode('utf-asd'))
