import optparse
import socketserver
from conf import settings

from core import server

class ArgvHandler():

    def __init__(self):
        self.op = optparse.OptionParser()

        #self.op.add_option("-s", "--server", dest = "server")
        #self.op.add_option("-P", "--port", dest="port")

        options, args = self.op.parse_args()

        #print(options)
        #print(options.server)
        #print(options.port)
        #print(args)

        self.verify_args(options, args)

    def verify_args(self, options, args):
        cmd = args[0]

        #为了用cmd接收不同的参数值，所以用反射的知识
        if hasattr(self, cmd):
            func = getattr(self, cmd)
            func()

    def start(self):
        print('server is working...')
        s = socketserver.ThreadingTCPServer((settings.IP, settings.port), server.ServerHandler)
        s.serve_forever()

    def help(self):
        pass