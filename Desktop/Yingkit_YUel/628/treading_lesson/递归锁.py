import threading
import time

class MyThread(threading.Thread):

    def actionA(self):
        r_lock.acquire()
        print(self.name, 'gotA', time.ctime())

        time.sleep(2)

        r_lock.acquire()
        print(self.name, 'gotB', time.ctime())
        time.sleep(2)

        r_lock.release()
        r_lock.release()

    def actionB(self):
        r_lock.acquire()
        print(self.name, 'gotB', time.ctime())

        time.sleep(2)

        r_lock.acquire()
        print(self.name, 'gotA', time.ctime())
        time.sleep(2)

        r_lock.release()
        r_lock.release()

    def run(self) -> None:
        self.actionA()
        self.actionB()


if __name__ == '__main__':

    # A = threading.Lock()
    # B = threading.Lock()

    r_lock = threading.RLock()

    L = []

    for i in range(5):
        t = MyThread()
        t.start()
        L.append(t)

    for i in L:
        i.join()

    print('ending.....')