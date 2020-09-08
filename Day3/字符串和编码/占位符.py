# -*- coding: utf-8 -*-
# %运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，
# %d表示用整数替换，%f 浮点数 %x 十六进制整数，有几个%?占位符，后面就跟几个变量或者值，
# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
# 顺序要对应好。如果只有一个%?，括号可以省略。
if __name__ == '__main__':
    print('Hello, %s' % 'world')
    # 输出：Hello, world
    print('Hello, %s, you have %d money' % ('Jack', 100))
    # 输出：Hello, Jack, you have 100 money
    print('Age: %s Gender: %s' % (25, True))
    # 输出：Age: 25 Gender: True
    # 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
    print('growth rate: % d % % ' % 7)
    # 输出：'growth rate: 7 %'
    # 另一种格式化字符串的方法是使用字符串的format()方法，
    # 它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：
    print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
    # 输出：Hello, 小明, 成绩提升了 17.1%