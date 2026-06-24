from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Проверка прав')
        func(*args, **kwargs)
    return wrapper


@my_decorator
def admin_panel(a):
    print('Показать панель админа!')
    

@my_decorator
def admin_edit_post(a, b, c):
    print('Пост исправлен!')
    
    
admin_panel(a=1)
admin_edit_post(2, 4, 5)
    
