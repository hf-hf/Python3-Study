if __name__ == '__main__':
    # 正常输出偶数
    [x for x in range(1, 11) if x % 2 == 0]
    # 但是，我们不能在最后的if加上else
    #[x for x in range(1, 11) if x % 2 == 0 else 0]
    # 这是因为跟在for后面的if是一个筛选条件，不能带else，否则如何筛选？
    # 另一些童鞋发现把if写在for前面必须加else，否则报错：
    #[x if x % 2 == 0 for x in range(1, 11)]
    # 这是因为for前面的部分是一个表达式，它必须根据x计算出一个结果。
    # 因此，考察表达式：x if x % 2 == 0，它无法根据x计算出结果，因为缺少else，必须加上else：
    [x if x % 2 == 0 else -x for x in range(1, 11)]
