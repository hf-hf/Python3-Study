# -*- coding: utf-8 -*-
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
#
# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，
# 因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。

if __name__ == '__main__':
    s = set([1, 2, 3])
    print(s)  # {1, 2, 3}
    s = set([1, 1, 2, 2, 3, 3])
    print(s)  # {1, 2, 3}
    s.add(4)
    print(s)  # {1, 2, 3, 4}
    s.add(4)
    print(s)  # {1, 2, 3, 4}
    s.remove(4)
    print(s)  # {1, 2, 3}
    s1 = set([1, 2, 3])
    s2 = set([2, 3, 4])
    print(s1 & s2)  # {2, 3}
    print((s1 | s2))  # {1, 2, 3, 4}