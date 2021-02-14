import multiprocessing as mp
from time import sleep

from rand_multiprocessing import foo


if __name__ == '__main__':
    mp.set_start_method('spawn')
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q, "bla!"))
    p2 = mp.Process(target=foo, args=(q, "AAA!!!"))
    p.start()
    # sleep(1)
    p2.start()
    print("before join")
    print(q.get())
    print(q.get())
    p.join()
    p2.join()