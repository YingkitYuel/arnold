
# import queue
# import multiprocessing
# import time
#
# def foo(q):
#     time.sleep(1)
#     q.put(123)
#     q.put('yuel')
#     print('son', id(q))
#
# if __name__ == '__main__':
#
#     # q = queue.Queue   #是线程队列
#     q = multiprocessing.Queue()  #进程队列
#
#     print('parent', id(q))
#
#     p = multiprocessing.Process(target=foo,args=(q,))
#     #考虑传过去的q，和foo里面的q是不是一个q
#     #考虑copy，
#
#     p.start()
#
#
#     print(q.get())
#     print(q.get())

# from multiprocessing import Process, Pipe
#
# def f(conn):
#     conn.send([12, {"name":"yuan"}, 'hello'])
#     response=conn.recv()
#     print("response",response)
#     conn.close()
#     print("q_ID2:",id(child_conn))
#
# if __name__ == '__main__':
#
#     parent_conn, child_conn = Pipe()  #双向管道
#
#
#     print("q_ID1:",id(child_conn))
#     p = Process(target=f, args=(child_conn,))
#     p.start()
#
#
#     print(parent_conn.recv())   # prints "[42, None, 'hello']"
#     parent_conn.send("儿子你好!")
#     p.join()



from multiprocessing import Process, Manager

def f(d, l,n):
    d[n] = '1'
    d['2'] = 2
    #d[0.25] = None
    l.append(n)
    #print(l)

    print("son process:",id(d),id(l))

if __name__ == '__main__':

    with Manager() as manager:

        d = manager.dict()

        l = manager.list(range(5))

        print("main process:",id(d),id(l))

        p_list = []

        for i in range(10):
            p = Process(target=f, args=(d,l,i))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()

        print(d)
        print(l)