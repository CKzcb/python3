#!/usr/bin/python3
"""
@Author   :   zhuchb
@time     :   2018/12/13
@File     :   遍历目录
@note     :   
"""
import os

def main():
    p = os.path.abspath(".")


def get_file(path):
    if os.path.isdir(path):
        print(path)
        get_file()
        os.path.