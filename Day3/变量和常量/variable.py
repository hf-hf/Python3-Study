if __name__ == '__main__':
    a = 123  # a是整数
    print(a)
    a = 'ABC'  # a变为字符串
    print(a)
    a = 'ABC'
    b = a
    a = 'XYZ'
    print(b)  # 输出 ABC