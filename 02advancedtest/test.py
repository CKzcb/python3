#!/usr/bin/python3
"""
@Author   :   zhuchb
@time     :   2018/12/17
@File     :   test
@note     :   
"""

def testg():
    a = 4
    b = 5
    c = 6
    for i in range(5):
        yield a
        print("a " + str(i))
        yield b
        print("b " + str(i))
        yield c
        print("c " + str(i))


if __name__ == '__main__':
    g = testg()
    for i in g:
        print(i)
