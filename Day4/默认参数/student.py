# coding=utf-8
# 举个例子，我们写个一年级小学生注册的函数，需要传入name和gender两个参数：
def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)

def enroll_default(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

if __name__ == '__main__':
    enroll('Sarah', 'F')
    # 如果要继续传入年龄、城市等信息怎么办？这样会使得调用函数的复杂度大大增加。
    # 我们可以把年龄和城市设为默认参数：
    # 这样，大多数学生注册时不需要提供年龄和城市，只提供必须的两个参数：
    enroll_default('Sarah', 'F')
    # 只有与默认参数不符的学生才需要提供额外的信息：
    enroll_default('Bob', 'M', 7)
    enroll_default('Adam', 'M', city='Tianjin')
    # 可见，默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，
    # 又可以传递更多的参数来实现。无论是简单调用还是复杂调用，函数只需要定义一个。
    # 有多个默认参数时，调用的时候，既可以按顺序提供默认参数，
    # 比如调用enroll('Bob', 'M', 7)，意思是，除了name，gender这两个参数外，
    # 最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。
    # 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，
    # 需要把参数名写上。比如调用enroll('Adam', 'M', city='Tianjin')，
    # 意思是，city参数用传进去的值，其他默认参数继续使用默认值。
