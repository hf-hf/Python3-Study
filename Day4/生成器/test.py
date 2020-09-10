# 通过列表生成式，我们可以直接创建一个列表。
# 但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，
# 那后面绝大多数元素占用的空间都白白浪费了。
#
# 所以，如果列表元素可以按照某种算法推算出来，
# 那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，
# 从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
#
# 要创建一个generator，有很多种方法。第一种方法很简单，
# 只要把一个列表生成式的[]改成()，就创建了一个generator：

# 函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

# 这就是定义generator的另一种方法。
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
# 这里，最难理解的就是generator和函数的执行流程不一样。
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

# 举个简单的例子，定义一个generator，依次返回数字1，3，5：
# 可以看到，odd不是普通函数，而是generator，在执行过程中，
# 遇到yield就中断，下次又继续执行。执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错。
#
# 回到fib的例子，我们在循环过程中不断调用yield，就会不断中断。
# 当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。
#
# 同样的，把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代：
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

if __name__ == '__main__':
    L = [x * x for x in range(10)]
    g = (x * x for x in range(10))
    print(next(g))
    for i in g:
        print(i)
    fib(6)
    f = fib2(6)
    # 调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值：
    o = odd()
    next(o)  # 1
    next(o)  # 3
    next(o)  # 5
    for n in fib2(6):
        print(n)
    # 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
    # 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
    while True:
        try:
            x = next(g)
            print('g:', x)
        except StopIteration as e:
            print('Generator return value:', e.value)
            break