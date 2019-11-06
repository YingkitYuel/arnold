# from multiprocessing import Process, Lock
# import time
#
# def f(l,i):
#     l.acquire()
#     time.sleep(1)
#     print('Hello World %s' %i)
#     l.release()
#
#
# if __name__ == '__main__':
#     lock = Lock()
#
#     for num in range(10):
#         Process(target=f, args=(lock, num)).start()


#进程池

from  multiprocessing import Process,Pool
import time,os

def Foo(i):
    time.sleep(1)
    print(i)
    return i+100

def Bar(arg):

    print(os.getpid())
    print(os.getppid())
    #print('logger:',arg)

if __name__ == '__main__':


    pool = Pool(4)

    #Bar(1)
    print("----------------")

    for i in range(100):
        #pool.apply(func=Foo, args=(i,))
        #pool.apply_async(func=Foo, args=(i,))
        pool.apply_async(func=Foo, args=(i,), callback=Bar)
        #回调函数：就是某个动作或者函数执行成功后再去执行的函数

    pool.close()   #在进程池中close必须在join前面，调用顺序是固定的
    pool.join()
    print('end')