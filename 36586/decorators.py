from functools import wraps

def for_range(num: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Проверить авторизован ли')
            for i in range(num):
                func(*args, **kwargs)
        return wrapper
    return decorator

@for_range(1)
def home():
    print('Домой')
    
    
@for_range(10)
def settings(a: int, b: str, c: bool) -> bool:
    print(f'Настройки {a}, {b}, {c}')
    return True
    
    
settings(1, 3, 7)
settings(b=1, a=7, c=3)
settings(1, c=10, b=20)