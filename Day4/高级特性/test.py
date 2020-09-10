if __name__ == '__main__':
    L = []
    for i in range(1, 100, 2):
        L.append(i)
    print(L)

    l = list(range(1, 100, 2))
    print(l)
    print(l[:int(len(l) / 2)])
    print(l[-int(len(l) / 2):-1])
    print(l[:-1])
