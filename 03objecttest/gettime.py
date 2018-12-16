#!/usr/bin/python3
"""
@Author   :   zhuchb
@time     :   2018/12/13
@File     :   gettime
@note     :   
"""

import requests

from logging import Logger

response = requests.get("http://www.beijing-time.org")

response.encoding = "gb2312"

target = response.text
# print(target)

print(target.find("hrs"))
print(target.find("min"))

