from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Проверка аккаунта')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@my_decorator
def home(a, b):
    print('привет')

@my_decorator
def search(c, d, e):
    print('Поиск')
    
search(1, 2, 3)