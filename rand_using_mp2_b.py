import multiprocessing as mp
from time import sleep

from rand_multiprocessing_b import foo


if __name__ == '__main__':
    ctx = mp.get_context('spawn')
    qa = ctx.Queue()
    qb = mp.Queue()
    p = ctx.Process(target=foo, args=(qa, qb, "bla!", "bla-2!"))
    p2 = ctx.Process(target=foo, args=(qa, qb, "AAA!!!", "AAA222!!!"))
    p.start()
    # sleep(1)
    p2.start()
    print("before join")
    print(qa.get())
    print(qa.get())
    print(qb.get())
    print(qb.get())
    p.join()
    p2.join()