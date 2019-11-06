# import  threading
# import time
#
#
#
# def music():
#     print('begin to listen to %s' %time.ctime())
#     time.sleep(3)
#     print('stop to listen %s' %time.ctime())
#
# def game():
#     print('begin to play game to %s' %time.ctime())
#     time.sleep(5)
#     print('stop to play game %s' %time.ctime())
#
# if __name__ == '__main__':
#     # t1 = threading.Thread(target=music)
#     # t1.start()
#     #
#     # t2 = threading.Thread(target=game)
#     # t2.start()
#
#     t1 = threading.Thread(target=music)
#
#     t2 = threading.Thread(target=game)
#
#     t1.start()
#     t1.join()
#     t2.start()
#
#     #t1.join()  #join的意思是t1不执行完不会执行主线程
#     t2.join()  #。。。。。。t2。。。。。。。。。主线程
#
#     print('ending')

#####-----------调用方法1------------######

# import threading
# from time import ctime,sleep
#
# def ListenMusic(name):
#     print('Begin listening to %s. %s' %(name, ctime()))
#     sleep(3)
#     print('end listening %s' %ctime())
#
# def RecordBlog(title):
#     print('Begin recording the %s! %s' %(title, ctime()))
#     sleep(5)
#     print('end recording %s' %ctime())
#
# threads = []
#
# t1 = threading.Thread(target=ListenMusic, args=('水手',))
# t2 = threading.Thread(target=RecordBlog, args=('Python线程',))
#
# threads.append(t1)
# threads.append(t2)
#
# if __name__ == '__main__':
#
#     for t in threads:
#         #t.setDaemon(True) #注意：一定在start之前设置
#         t.start()
#         #t.join() #串行
#     #t1.join()
#     t1.setDaemon(True)
#     print('all over %s' %ctime())
#

#-------------调用方法2--------------#

import threading
import time
class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):  #定义每个线程要运行的函数

        print('running on number:%s' %self.num)
        time.sleep(3)

if __name__ == '__main__':
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()

    print('ending.....')