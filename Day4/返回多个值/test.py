# coding=utf-8
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

if __name__ == '__main__':
    x, y = move(100, 100, 60, math.pi / 6)
    print(x, y)
    # 但其实这只是一种假象，Python函数返回的仍然是单一值：
    r = move(100, 100, 60, math.pi / 6)
    print(r)
    # (151.96152422706632, 70.0)
    # 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，
    # 按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。