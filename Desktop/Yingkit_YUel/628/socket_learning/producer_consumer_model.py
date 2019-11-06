import time

def comsumer(name):
    print('I\'m %s, I\'m start to eat baozi~' %name)
    while True:
        baozi = yield
        time.sleep(1)
        print('I\'m %s, I ate %s' %(name, baozi))


def producer():
    c1 = comsumer('sblhj')
    c1.__next__()
    for i in range(10):
        time.sleep(1)
        c1.send('baozi %d' %i)

if __name__ == '__main__':
    producer()

