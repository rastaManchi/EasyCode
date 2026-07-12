from functools import wraps


def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Проверить статус админа')
        result = func(*args, **kwargs)
        return result
    return wrapper


@admin_required
def admin_panel(username):
    print('Дать доступ к админ панели')
    

@admin_required
def approve_post():
    print('Разрешить пост')
    
    
admin_panel("Булат")
approve_post()