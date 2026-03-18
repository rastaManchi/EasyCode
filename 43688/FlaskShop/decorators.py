from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Перед функцией')
        res = func(*args, **kwargs)
        print('После функции')
        return res
    return wrapper


@my_decorator
def hello():
    print('Привет')
    
@my_decorator
def bye(text):
    print('Привет')
    
    
hello()
bye('123')