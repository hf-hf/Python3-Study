# 生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，
# 直到最后抛出StopIteration错误表示无法继续返回下一个值了。
#
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
from collections.abc import Iterator, Iterable

if __name__ == '__main__':
    # 可以使用isinstance()判断一个对象是否是Iterable对象
    isinstance([], Iterable)
    # 可以使用isinstance()判断一个对象是否是Iterator对象：
    isinstance((x for x in range(10)), Iterator)
    # 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
    # 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
    isinstance(iter([]), Iterator)
    isinstance(iter('abc'), Iterator)
    # 这是因为Python的Iterator对象表示的是一个数据流，
    # Iterator对象可以被next()函数调用并不断返回下一个数据，
    # 直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，
    # 但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，
    # 所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
    # Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。