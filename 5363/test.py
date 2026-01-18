# a = 50000000
# b = 50000000
# id_a = id(a)
# id_b = id(b)
# print(id_a, id_b)

# a+=1
# id_a = id(a)
# id_b = id(b)
# print(id_a, id_b)


# a = True
# id_a = id(a)
# print(id_a)

# a = False
# id_a = id(a)
# print(id_a)

# a = True
# id_a = id(a)
# print(id_a)


# class Test:
#     def __init__(self):
#         self.name = 'default'


# obj1 = [1]
# print(id(obj1))
# obj1 = [1, 2]
# print(id(obj1))


# t = (1, 2, 3)
# t[0] = "123"


# a = 'Привет'
# a[0] = 'К'

def uppercase_decorator(func):
    def wrapper(text):
        new_test = text.upper()
        func(new_test)
    return wrapper

def repeat(num_times):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print('До функции')
            for i in range(num_times):
                func(*args, **kwargs)
            print('После функции')
        return wrapper
    return my_decorator

@uppercase_decorator
@repeat(3)
def test(text):
    print(text)


@repeat(10)
def test2(n1, n2, n3=0, n4=0):
    print(n1 + n2)
    
test('Привет')
test2(5, 10, n4=7, n3=1)