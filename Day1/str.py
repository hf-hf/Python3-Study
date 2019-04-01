#!/usr/bin/python3

if __name__ == '__main__':
    word = '字符串'
    sentence = "这是一个句子。"
    paragraph = """这是一个段落，
    可以由多行组成"""
    str = "1"

    print(str * 2)  # 输出字符串两次
    print(str + '你好')  # 连接字符串

    print('------------------------------')

    print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
    print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

    print(sentence[-2:-1])

    x = "a"
    y = "b"
    # 换行输出
    print(x)
    print(y)

    print('---------')
    # 不换行输出
    print(x, end=" ")
    print(y, end=" ")
    print()