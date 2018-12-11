#!/usr/bin/python3
"""
@Author   :   zhuchb
@time     :   2018/12/11
@File     :   gctest
@note     :   
"""
import gc
import sys
class GCTest:
    def __init__(self, name):
        self._name = name
        print("object create %s"%(self._name))


def main():
    c1 = GCTest("zhuchb")
    c2 = GCTest("CK")
    c1.t = c2
    c2.t = c1
    print("--------------1----------------")
    del c1
    del c2
    print("--------------2----------------")
    print(gc.garbage)
    print("--------------3----------------")
    print(gc.collect())
    print("--------------4----------------")
    print(gc.garbage)
    print("--------------5----------------")



if __name__ == "__main__":
    gc.set_debug(gc.DEBUG_LEAK)
    main()
    import time
    time.sleep(100)