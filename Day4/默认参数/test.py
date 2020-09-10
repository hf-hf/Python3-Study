# coding=utf-8
def power(x):
    return x * x

def power_2(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def power_2defaultn(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def power_3(x, n, m):
    s = 1
    if n == None:
        n = m
    while n > 0:
        n = n - 1
        s = s * x
        m = n
    return s

if __name__ == '__main__':
    print(power(5))
    print(power(15))
    print(power_2(5, 2))
    print(power_2(5, 3))
    print(power_2defaultn(5))
    print(power_2defaultn(5, 2))
    # 可以不按参数顺序，指定参数名传递入参
    print(power_3(5, m=2, n=1))
    # 从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
    # 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
    # 二是如何设置默认参数。
    # 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
    # 使用默认参数有什么好处？最大的好处是能降低调用函数的难度。