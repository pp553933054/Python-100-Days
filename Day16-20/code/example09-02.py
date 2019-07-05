from functools import wraps

'''不加修饰wrap'''


def my_decorator(func):
    def wrapper(*args, **kwargs):
        '''decorator'''
        print('Calling decorated function...')
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def example():
    """Docstring"""
    print('Called example function')


print(example.__name__, example.__doc__)

'''加wraps装饰'''


def y_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        '''decorator'''
        print('Calling decorated function...')
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def example():
    """Docstring"""
    print('Called example function')


print(example.__name__, example.__doc__)
