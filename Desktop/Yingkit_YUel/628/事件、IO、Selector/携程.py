#携程：  协作式，------非抢占式的程序
#    A------>B------>A------>C
#协程是一个用户态的切换
#类似于yield

# 协程，又称微线程，纤程。英文名Coroutine。
#
# 优点1: 协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
#
# 优点2: 不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。
#
# 因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。

#生成器小回忆

# def f():
#     print('OK')
#     s = yield 6
#     print(s)
#     print("OK2")
#     yield
#
# gen = f()  #此时不会打印OK，只会返回一个生成器对象
# RET = next(gen)  #此时会执行f函数,另一种写法 gen.__next__()
# print(RET) #此时RET会接受yield回时的6
# #next(gen) #此时会打印OK2
# #next(gen)  #此时已经没发继续执行，会提示StopIteration
# gen.send(5) #此时f会继续执行，s会收到send过去的5


# import time
# import queue
#
# def consumer(name):
#     print("--->ready to eat baozi...")
#     while True:
#         new_baozi = yield
#         print("[%s] is eating baozi %s" % (name,new_baozi))
#         #time.sleep(1)
#
# def producer():
#
#     r = con.__next__()
#     r = con2.__next__()
#     n = 0
#     while 1:
#         time.sleep(1)
#         print("\033[32;1m[producer]\033[0m is making baozi %s and %s" %(n,n+1) )
#         con.send(n)
#         con2.send(n+1)
#
#         n +=2
#
#
# if __name__ == '__main__':
#     con = consumer("c1")
#     con2 = consumer("c2")
#     p = producer()


# from greenlet import greenlet
#
#
# def test1():
#     print(12)
#     gr2.switch()
#     print(34)
#     gr2.switch()
#
#
# def test2():
#     print(56)
#     gr1.switch()
#     print(78)
#
#
# gr1 = greenlet(test1)
# gr2 = greenlet(test2)
# gr2.switch()


import gevent

import requests,time


start=time.time()

def f(url):
    print('GET: %s' % url)
    resp =requests.get(url)
    data = resp.text
    print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([

        gevent.spawn(f, 'https://www.python.org/'),
        gevent.spawn(f, 'https://www.yahoo.com/'),
        gevent.spawn(f, 'https://www.baidu.com/'),
        gevent.spawn(f, 'https://www.sina.com.cn/'),

])

# f('https://www.python.org/')
#
# f('https://www.yahoo.com/')
#
# f('https://baidu.com/')
#
# f('https://www.sina.com.cn/')

print("cost time:",time.time()-start)
