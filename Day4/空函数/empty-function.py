def nop():
    pass
# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，
# 比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
# pass还可以用在其他语句里，比如：
if __name__ == '__main__':
    age = 1
    if age >= 18:
        pass
    # 缺少了pass，代码运行就会有语法错误。