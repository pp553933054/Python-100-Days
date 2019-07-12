# encoding:UTF-8

'''yield方法的执行顺序'''


def g():
    print('1')
    x = yield 'hello'
    print('2', 'x=', x)
    y = 5 + (yield x)
    print('3', 'y=', y)


def main():
    f = g()
    f.__next__()
    f.send(5)
    f.send(2)


if __name__ == '__main__':
    main()
