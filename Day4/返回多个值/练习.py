# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    tmp3 = (b ** 2)
    tmp2 = tmp3 - (4 * a * c)
    tmp = math.sqrt(tmp2)
    first = (-b + tmp) / (2 * a)
    second = (-b - tmp) / (2 * a)
    return first, second

if __name__ == '__main__':
    print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
    print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

    if quadratic(2, 3, 1) != (-0.5, -1.0):
        print('测试失败')
    elif quadratic(1, 3, -4) != (1.0, -4.0):
        print('测试失败')
    else:
        print('测试成功')