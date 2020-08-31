if __name__ == '__main__':
    classmates = ['Jack', 'Bod', 'Track']
    print(classmates)  # 输出 ['Jack', 'Bod', 'Track']
    print(len(classmates))  # 3
    L = ['Apple', 123, True]
    s = ['python', 'java', ['asp', 'php'], 'scheme']
    print(len(s))  # 4
    p = ['asp', 'php']
    # s可以看成是一个二维数组
    s = ['python', 'java', p, 'scheme']
    print(s)
    print(classmates[0])  # Jack
    print(classmates[-1])  # Track
    print(classmates[-1])  # Track
    print(classmates[-2])  # Bod
    print(classmates[-3])  # Jack
    # list 是一个可变的有序表，所以，可以利用 append 往 list 中追加元素到末尾
    classmates.append('Admin')
    classmates.insert(1, 'Michael')
    classmates.pop()
    # 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
    classmates.pop(1)
    # replace
    classmates[1] = 'Sarah'