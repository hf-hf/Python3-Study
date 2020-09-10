# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 比如定义一个函数，包含上述若干种参数：

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。

if __name__ == '__main__':
    f1(1, 2)
    f1(1, 2, c=3)
    f1(1, 2, 3, 'a', 'b')
    f1(1, 2, 3, 'a', 'b', x=99)
    f2(1, 2, d=99, ext=None)
    # 最神奇的是通过一个tuple和dict，你也可以调用上述函数：
    args = (1, 2, 3, 4)
    kw = {'d': 99, 'x': '#'}
    f1(*args, **kw)
    args = (1, 2, 3)
    kw = {'d': 88, 'x': '#'}
    f2(*args, **kw)
    # 所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
    # 虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。