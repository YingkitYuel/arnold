import threading
import time
num = 100


def sub():
    global num
    lock.acquire()
    temp = num
    time.sleep(0.001)
    num = temp - 1
    lock.release()

l = []
lock = threading.Lock()
for i in range(100):
    t = threading.Thread(target=sub)
    t.start()
    l.append(t)

for t in l:
    t.join()

print(num)
