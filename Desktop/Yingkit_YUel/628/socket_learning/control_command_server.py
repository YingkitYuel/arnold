from socket import *
import subprocess

ip_port = ('127.0.0.1', 8888)
buf_size = 1024
back_log = 5

link_server = socket(AF_INET,SOCK_STREAM)
link_server.bind(ip_port)
link_server.listen(back_log)

while True:
    conn, addr = link_server.accept()
    print('已成功连接：',addr)
    while True:
        cmd = conn.recv(buf_size)
        print('客户端收到的命令为：',cmd)
        try:

            res = subprocess.Popen(cmd.decode('utf-8'),shell=True,
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

            err = res.stderr.read()
            if err:
                cmd_res = err
            else:
                cmd_res = res.stdout.read()

            conn.send(cmd_res)

        except Exception as e:
            print(e)
            break
    conn.close()
