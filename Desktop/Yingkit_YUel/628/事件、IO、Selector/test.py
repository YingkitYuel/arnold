from multiprocessing import Process,Lock
import time


def num(lock, number):
    lock.acquire()
    time.sleep(2)
    print('Hello World %s' %number)
    lock.release()

if __name__ == '__main__':
    lock = Lock()

    for i in range(10):
        p = Process(target=num, args=(lock, i))
        p.start()