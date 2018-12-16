#!/usr/bin/python3
"""
@Author   :   zhuchb
@time     :   2018/12/13
@File     :   operation
@note     :   
"""

import os


# 查看当前目录的绝对路径
print(os.path.abspath('.'))

print(os.path.join(os.path.abspath('.'), "test"))

p1 = os.path.abspath(".")
p2 = os.path.join(p1, "test")
#
# os.mkdir(p2)

print(os.path.isdir(p2))


