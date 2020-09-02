# dict 全称 dictionary，在其他语言中也称为 map，使用 键-值（key-value）存储，具有极快的查找速度。
if __name__ == '__main__':
    d = {'Michale': 92, 'Bod': 91, 'Jack': 100}
    for k in d:
        print(k)
        print(d[k])

    print(d)  # {'Michale': 92, 'Bod': 91, 'Jack': 100}
    print(d['Michale'])  # 92

    print(d[0])  # KeyError: 0
    # 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
    # 由于一个 key 只能对应一个value，所以，多次对一个 key 放入 value，后面的值会把前面的值冲掉
    # 判断key是否在dict中
    print('Thomas' in d)  # False
    print(d.get('Thomas'))  # None
    print(d.get('Thomas', -1))  # -1
    # delete
    d.pop('Bod')
    # 和 list 比较，dict有以下几个特点：
    # 查找和插入的速度极快，不会随着 key 的增加而变慢；
    #
    # 需要占用大量的内存，内存浪费多。
    #
    # 而 list 相反：
    #
    # 查找和插入的时间随着元素的增加而增加；
    #
    # 占用空间小，浪费内存很少。
    #
    # 所以，dict 是用空间来换取时间的一种方法。
    #
    # dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。