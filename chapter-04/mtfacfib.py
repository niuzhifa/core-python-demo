# encoding = utf-8

import threading
from myThread import MyThread
from time import ctime, sleep


def fib(x):
    sleep(0.05)
    if x < 2:
        return 1
    return (fib(x - 2) + fib(x - 1))


def fac(x):
    sleep(0.1)
    if x < 2:
        return 1
    return (x * fac(x - 1))


def sum(x):
    sleep(0.1)
    if x < 2:
        return 1
    return (x + sum(x - 1))


funcs = [fib, fac, sum]
n = 12


def main():
    nfuncs = range(len(funcs))
    print('start single thread...')
    for i in nfuncs:
        print('start ', funcs[i].__name__, 'at :', ctime())
        print(funcs[i](n))
        print(funcs[i].__name__, 'finished at :', ctime())

    print('\nmultiple thread...')
    threads = []
    for i in nfuncs:
        thread = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(thread)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print(threads[i].getResult())

    print('all done...')

if __name__ == '__main__':
    main()
