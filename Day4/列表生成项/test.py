import os # 导入os模块，模块的概念后面讲到

if __name__ == '__main__':
    print([x * x for x in range(1, 11)])
    print([x * x for x in range(1, 11) if x % 2 == 0])
    print([m + n for m in 'ABC' for n in 'XYZ'])
    [d for d in os.listdir('.')]  # os.listdir可以列出文件和目录
    d = {'x': 'A', 'y': 'B', 'z': 'C'}
    [k + '=' + v for k, v in d.items()]
    ['y=B', 'x=A', 'z=C']