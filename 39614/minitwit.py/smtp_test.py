def check_session(func):
    def wrapper(*args, **kwargs):
        print('Привет')
        return func(*args, **kwargs)
    return wrapper

@check_session
def test():
    print('Как дела')
    
    
@check_session
def test2(a, v, b):
    print('123')
    

test2(10, 2, 3)
test2(a=10, v=2, b=3)
test()