if __name__ == '__main__':
    a = ['c', 'b', 'a']
    a.sort()
    print a
    # a = ['a', 'b', 'c']
    a = 'abc'
    print(a.replace('a', 'A'))  # 'Abc'
    print(a)  # 'abc'
    a = 'abc'
    b = a.replace('a', 'A')
    print(b)  # 'Abc'
    print(a)  # 'abc'