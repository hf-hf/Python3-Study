# 不可变有序列表 - 元组 tuple ( )#
if __name__ == '__main__':
    # tuple 和 list 非常类似，但是 tuple 一旦初始化就不能修改，比如同样是列出同学的名字：
    classmates = ('Michael', 'Bob', 'Tracy')
    # 现在，classmates 这个 tuple 不能变了，它也没有 append()，insert() 这样的方法。
    # 其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，
    # 但不能赋值成另外的元素。
    # 不可变的 tuple 有什么意义？因为 tuple 不可变，所以代码更安全。
    # 如果可能，能用 tuple 代替 list 就尽量用 tuple。
    # empty tuple
    t = ()
    print(t)  # ()
    # 定义的不是 tuple，是1这个数！这是因为括号()既可以表示 tuple，
    # 又可以表示数学公式中的小括号，这就产生了歧义，
    # 因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
    t = (1)
    print(t)  # 1
    # 所以，只有 1 个元素的 tuple 定义时必须加一个逗号,，来消除歧义：
    t = (1,)
    print(t)  # (1,)
    # “可变的”tuple ：
    t = ('a', 'b', ['A', 'B'])
    t[2][0] = 'X'
    t[2][1] = 'Y'
    print(t)  # ('a', 'b', ['X', 'Y'])
    # 当我们把list的元素'A'和'B'修改为'X'和'Y'后
    # 表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，
    # 而是list的元素。tuple一开始指向的list并没有改成别的list，
    # 所以，⭐ tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，
    # 就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
    # 理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。