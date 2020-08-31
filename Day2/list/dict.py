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
