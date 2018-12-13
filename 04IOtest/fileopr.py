#!/usr/bin/python3
"""
@Author   :   zhuchb
@time     :   2018/12/13
@File     :   fileopr
@note     :   
"""

f = open("a.txt", 'r')


print(f.read())

f.close()

f = open("b.txt", encoding='utf8')

print(f.read())

f.close()