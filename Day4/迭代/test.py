from collections import Iterable

if __name__ == '__main__':
    d = {'a': 1, 'b': 2, 'c': 3}
    for k, v in d.items():
        print(k)
        print(v)
    # 那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
    print(isinstance('abc', Iterable))  # str是否可迭代
    print(isinstance([1, 2, 3], Iterable))  # list是否可迭代
    print(isinstance(123, Iterable))  # 整数是否可迭代
    # 最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？
    # Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
    for i, value in enumerate(['A', 'B', 'C']):
        print(i, value)
