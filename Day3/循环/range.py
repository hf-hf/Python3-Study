# -*- coding: utf-8 -*-
# 如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，
# 可以生成一个整数序列，再通过list()函数可以转换为 list。比如range(5)生成的序列是从0开始小于5的整数：
if __name__ == '__main__':
    sum = 0
    for x in range(101):
        sum = sum + x
    print(sum)  # 5050