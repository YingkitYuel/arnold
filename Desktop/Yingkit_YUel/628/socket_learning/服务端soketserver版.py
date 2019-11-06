import socketserver
import subprocess

class MySever(socketserver.BaseRequestHandler):
    def handle(self):
        print('conn is:',self.request)  #conn
        print('addr is:',self.client_address)  #addr

        while True:
            try:
                #收消息
                data = self.request.recv(1024)
                if not data:break
                print('收到客户端的消息是：', data, self.client_address)

                res = subprocess.Popen(data.decode('utf-8'), stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                res_out = res.stdout.read()
                res_err = res.stderr.read()
                if not res_err:
                    res_data = res_out
                else:
                    res_data = res_err




                #发消息
                self.request.send(res_data)

            except Exception as e:
                print(e)
                break

if __name__ == '__main__':
    s = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), MySever)
    s.serve_forever()