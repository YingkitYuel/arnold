# import time
# import threading
#
#
# li = ['liupan', 1, 2, 'leilei']
#
#
# def pri():
#     while li:
#         a = li[-1]
#         print(a)
#         time.sleep(1)
#         li.remove(a)
#         # try:
#         #     li.remove(a)
#         # except Exception as e:
#         #     print('----' ,a, e)
#
# t1 = threading.Thread(target=pri, args=())
# t1.start()
# t2 = threading.Thread(target=pri, args=())
# t2.start()

# import queue  #线程队列
#
#
#
#
# q = queue.Queue(3)   #先进先出
#
# q.put(12)
# q.put('hello')
# q.put({'name': 'qin'})
# #q.put(4, False)
#
# while 1:
#     data = q.get(block=False)
#     print(data)
#     print('-------')
#

#先进后出

# import queue
#
# q = queue.LifoQueue()
#
# q.put(12)
# q.put('hello')
# q.put({'name': 'qin'})
# #q.put(4, False)
#
# while 1:
#     data = q.get()
#     print(data)
#     print('-------')


#优先级
import queue

q = queue.PriorityQueue()

q.put([3, 12])
q.put([2, 'hellow'])
q.put([4, {'name': 'liu'}])

while 1:
    data = q.get()
    print(data)
    print('--------')