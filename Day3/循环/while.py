if __name__ == '__main__':
    sum = 0
    n = 99
    while n > 0:
        sum = sum + n
        n = n - 2
    print(sum)
    # 在循环中，break语句可以提前退出循环。例如，本来要循环打印1～100的数字：
    n = 1
    while n <= 100:
        if n > 10:  # 当n = 11时，条件满足，执行break语句
            break  # break语句会结束当前循环
        print(n)
        n = n + 1
    print('END')