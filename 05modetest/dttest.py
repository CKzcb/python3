#!/usr/bin/python3
"""
@Author   :   zhuchb
@time     :   2018/12/14
@File     :   dttest
@note     :   
"""

# datetime模块

from datetime import datetime


dt = datetime.now()

print(dt)

print(dt.hour)

# dt.strftime()

# str转成datetime
str = "2018-12-14"

dt = datetime.strptime(str, "%Y-%m-%d")

print(dt, type(dt))

# datetime 转成str

str1 = dt.strftime("%Y/%m/%d")
print(str1)

# datetime加减
from datetime import timedelta




