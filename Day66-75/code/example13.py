# encoding:UTF-8

'''yield方法的执行顺序'''


def yield_test(n):
    for i in range(n):
        yield call(i)
        print("i=", i)

        # 做一些其他的事情
    print("just do it")
    print("end")


def call(i):
    return i * 2


def main():
    for i in yield_test(5):
        print(i, ",")


if __name__ == '__main__':
    main()
