"""
@author: zhuchb
@date: 2018年12月10日17:02:37
"""
"""
定义一个函数，在函数内部再定义一个函数，并且这个函数用到了外边函数的变量
"""
def test(number):
    def test_in(number_in):
        print("in test_in 函数, number_in is %s"%number_in)
        return number + number_in
    return test_in

ret = test(20)


print(ret)
print(type(ret))
print(ret(100))
print(ret(200))

"""
内部函数对外部函数作用域里变量的引用（非全局变量）,则称内部函数为闭包
"""

# nonlocal访问外部函数的局部变量

start = 10

def counter(start = 0):
    def incr():
        nonlocal start
        # global start
        start += 1
        return start
    return incr
c1 = counter(5)
print(c1())
print(c1())
print(c1())


