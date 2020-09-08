# -*- coding: utf-8 -*-
if __name__ == '__main__':
    age = 3
    if age >= 18:
        print('your age is', age)
        print('adult')
    else:
        print('your age is', age)
        print('teenager')

    age = 3
    if age >= 18:
        print('adult')
    elif age >= 6:
        print('teenager')
    else:
        print('kid')
    # elif是else if的缩写，完全可以有多个elif，所以if语句的完整形式就是：
    # ⭐ if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，
    # 就忽略掉剩下的elif和else，所以，下面的程序打印的是teenager：
    age = 20
    if age >= 6:
        print('teenager')
    elif age >= 18:
        print('adult')
    else:
        print('kid')