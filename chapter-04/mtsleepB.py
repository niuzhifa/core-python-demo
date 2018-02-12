# encoding=utf-8

import _thread
from time import ctime, sleep

loops = [4, 2]


def loop(nloop, nsec, lock):
    print('start loop ', nloop, 'at :', ctime())
    sleep(nsec)
    print('loop', nloop, ' done at :', ctime())
    lock.release()


def main():
    print('start all at :', ctime())

    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked():
            pass


if __name__ == '__main__':
    main()
