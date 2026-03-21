def check_session(func):
    def wrapper():
        print('Привет')
        return func()
    return wrapper

@check_session
def test():
    print('Как дела')
    

test()