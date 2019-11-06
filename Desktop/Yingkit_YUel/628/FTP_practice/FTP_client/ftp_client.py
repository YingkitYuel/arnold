import socket
import optparse
import configparser
import json
import os
import sys

STATUS_CODE = {
    250:'Invalid cmd format, e.g:',
    251:'Invalid cmd',
    252:'Invalid auth data',
}

class ClientHandler():
    def __init__(self):
        self.opt = optparse.OptionParser()

        self.opt.add_option('-s', '--server', dest='server')
        self.opt.add_option('-P', '--port', dest='port')
        self.opt.add_option('-u', '--username', dest='username')
        self.opt.add_option('-p', '--password', dest='password')

        self.options, self.args = self.opt.parse_args()

        self.verify_args(self.options, self.args)

        self.make_connection()

        self.mainPath = os.path.dirname(os.path.abspath(__file__))

        self.last = 0

    def verify_args(self, options, args):
        server = options.server
        port = options.port
        username = options.username
        password = options.password
        if int(port) > 0 and int(port) < 65535:
            return True
        else:
            exit('the port is in 0-65535')


    def make_connection(self):
        self.sock = socket.socket()
        self.sock.connect((self.options.server, int(self.options.port)))


    def interactive(self):
        print('Begin to interactive.....')
        if not self.authenticate():
            while 1:
                cmd_info = input('[%s]' %self.current).strip()  #put 12.png image

                cmd_list = cmd_info.split()
                if hasattr(self, cmd_list[0]):
                    func = getattr(self, cmd_list[0])
                    func(cmd_list)

    def put(self, *cmd_list):
        action, local_path, target_path = cmd_list
        local_path = os.path.join(self.mainPath, local_path)

        file_name = os.path.basename(local_path)
        file_size = os.stat(local_path).st_size #文件大小

        data = {
            'action': 'put',
            'file_name':file_name,
            'file_size':file_size,
            'target_path': target_path
        }

        self.sock.send(json.dumps(data).encode('utf-8'))

        is_exist = self.sock.recv(1024).decode('utf-8')

        has_sent = 0
        if is_exist == '253':
            #文件不完整
            choise = input('the file is exist, but not enough, is continue?[Y/N]')
            if choise.upper() == 'Y':
                self.sock.sendall('Y'.encode('utf-8'))
                continue_position = self.sock.recv(1024).decode('utf-8')
                has_sent += int(continue_position)
            else:
                self.sock.sendall('N'.encode('utf-8'))
        elif is_exist == '254':
            #文件完全存在
            return
        else:
            pass

        f = open(local_path, 'rb')
        f.seek(has_sent)
        while has_sent < file_size:
            data = f.read(1024)
            self.sock.sendall(data)
            has_sent += len(data)
            self.show_progress(has_sent, file_size)

        f.close()
        print('input success!')


    def show_progress(self, has,total):
        rate = float(has)/float(total)
        rate_number = int(rate*100)
        if self.last != rate_number:
            sys.stdout.write('%s%% %s\r' %(rate_number, '#'*rate_number))
        self.last = rate_number


    def authenticate(self):
        if self.options.username is None or self.options.password is None:
            username = input('please input username:')
            password = input('please input password:')
            return self.get_auth_result(username, password)
        return self.get_auth_result(self.options.username, self.options.password)

    def response(self):
        data = self.sock.recv(1024).decode('utf-8')
        data = json.loads(data)
        return data

    def get_auth_result(self, user, pwd):
        data = {
            'action':'auth',
            'username':user,
            'password':pwd
        }

        self.sock.send(json.dumps(data).encode('utf-8'))
        data = self.response()
        print('response:', data['status_code'])
        if data['status_code'] == 250:
            self.user = user
            self.current = self.user
            print(STATUS_CODE[250])
        else:
            print(STATUS_CODE[data['status_code']])

    def ls(self, *cmd_list):
        data = {
            'action':'ls'
        }
        self.sock.sendall(json.dumps(data).encode('utf-8'))

        data = self.sock.recv(1024).decode('utf-8')
        print(data)

    def cd(self, cmd_list):
        #cd images
        data = {
            'action':'cd',
            'dirname': cmd_list[1]
        }
        self.sock.sendall(json.dumps(data).encode('utf-8'))
        data = self.sock.recv(1024).decode('utf-8')
        print(os.path.basename(data))
        self.current = os.path.basename(data)

    def make_dir(self, **data):
        data = {
            'action': 'cd',
            'dirname': cmd_list[1]
        }
        self.sock.sendall(json.dumps(data).encode('utf-8'))
        data = self.sock.recv(1024).decode('utf-8')
        print(os.path.basename(data))
        self.current = os.path.basename(data)




ch = ClientHandler()

ch.interactive()