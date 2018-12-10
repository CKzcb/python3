"""
@author: zhuchb
@date: 2018年12月10日17:16:51
@note: 装饰器
"""
"""
装饰器功能：
1、引入日志
2、函数执行时间统计
3、执行函数前预备处理
4、执行函数后清理功能
5、权限校验等场景
6、缓存
"""

# 无参数装饰器
from time import ctime, sleep
def timefun1(func):
    def wapperfunc():
        print("%s called at %s"%(func.__name__, ctime()))
        func()
    return wapperfunc

@timefun1
def showtime():
    print("this is showtime")

# 有参数的装饰器
def timefun2(func):
    def wapperdfunc(a, b):
        print("%s called at %s"%(func.__name__, ctime()))
        print(a, b)
        func(a, b)
    return wapperdfunc

@timefun2
def foo(a, b):
    print(a + b)


"""
装饰器带有参数，在原有装饰器的基础上，设置外部变量
"""
def timefun_arg(pre="hello"):
    def timefun(func):
        def wrappedfunc():
            print("%s called at %s %s"%(func.__name__, ctime(), pre))
            return func()
        return wrappedfunc
    return timefun

@timefun_arg("zhuchb")
def foo2():
    print("I am foo2")

@timefun_arg("ck")
def foo3():
    a = 2
    print(globals())
    print(locals())
    print("I am foo3")

cc = 5

if __name__ == '__main__':
    aa = 3
    bb = 4
    foo2()
    foo3()