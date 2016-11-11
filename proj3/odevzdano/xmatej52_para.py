#!/usr/bin/env python3

#from threading import Thread
from multiprocessing import Process

def count(n):
    while n > 0:
        n -= 1

proc1 = Process(target=count,args=(10**8,))
proc1.start()

proc2 = Process(target=count,args=(10**8,))
proc2.start()

proc1.join(); proc2.join()

