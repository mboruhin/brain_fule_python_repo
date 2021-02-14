import multiprocessing as mp
from time import sleep

from rand_multiprocessing import foo


if __name__ == '__main__':
    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    p = ctx.Process(target=foo, args=(q, "bla!"))
    p2 = ctx.Process(target=foo, args=(q, "AAA!!!"))
    p.start()
    # sleep(1)
    p2.start()
    print("before join")
    print(q.get())
    print(q.get())
    p.join()
    p2.join()