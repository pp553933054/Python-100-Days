from functools import wraps


def decorate(func):
    print('running decorate', func)

    @wraps(func)
    def decorate_inner():
        print('running decorate_inner function', decorate_inner)
        return func()

    return decorate_inner


@decorate
def func_1():
    print('running func_1', func_1)


if __name__ == '__main__':
    func_1()
