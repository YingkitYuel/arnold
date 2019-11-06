from wsgiref.simple_server import make_server
import time


def foo1(req):
    f = open('index1.html', 'rb')
    data = f.read()
    return data

def login(req):
    print(req['user'])
    print(req['pwd'])
    return b'welcome!'

def signup(req):
    pass

def show_time(reg):
    times = time.ctime()

    #return ('<h1>time:%s</h1>' %str(times)).encode('utf8')
    f = open('show_time.html', 'r')
    data = f.read()
    data.replace('{{time}}', times)
    return data.encode('utf8')

def router():
    url_pattern = {
        ('/login', login),
        ('/signup', signup),
        ('/yue', foo1),
        ('/show_time', show_time),
    }
    return url_pattern




def application(environ, start_response):

    print('path', environ['PATH_INFO'])

    start_response('200 OK', [('Content-Type', 'text/html')])

    path = environ['PATH_INFO']
    # if path == '/yue':
    #     return [foo1()]
    #     #return [b'<h1>Hello, yue!</h1>']
    # else:
    #     return [b'404']
    #
    # return [b'<h1>Hello, web!</h1>']

    url_patterns = router()
    print(url_patterns)


    func = None
    for item in url_patterns:
        if item[0] == path:
            func = item[1]
            break
    if func == None:
        return [b'404']

    return [func(environ)]


httpd = make_server('', 8090, application)

print('Serving HTTP on port 8090...')
# 开始监听HTTP请求:
httpd.serve_forever()