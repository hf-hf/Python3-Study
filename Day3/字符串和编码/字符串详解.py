#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

# 在最新的Python 3版本中，字符串是以 Unicode 编码的，也就是说，Python 的字符串支持多语言，例如：
if __name__ == '__main__':
    # print('包含中文的str')
    # 输出：包含中文的str
    # 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
    ord('A')  # 65
    ord('中')  # 20013
    chr(66)  # 'B'
    chr(25991)  # '文'
    # 由于Python的字符串类型是str，在内存中以 Unicode 表示，一个字符对应若干个字节。
    # 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
    # Python对bytes类型的数据用带b前缀的单引号或双引号表示：
    x = b'ABC'
    # 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
    # 以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
    L = '中文'
    print('ABC'.encode('ascii'))
    print(L.encode('utf-8'))
    # 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。
    # 含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
    # 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
    print(b'ABC'.decode('ascii'))
    print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
    # 要计算str包含多少个字符，可以用len()函数：
    print(len('ABC'))  # 3
    print(len('中文'))  # 2
    # len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
    print(len(b'ABC'))  # 3
    print(len(b'\xe4\xb8\xad\xe6\x96\x87'))  # 6
    print(len('中文'.encode('utf-8')))  # 6
    # 可见，1 个中文字符经过 UTF-8 编码后通常会占用 3 个字节，而 1 个英文字符只占用 1 个字节。