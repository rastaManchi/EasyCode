# import random


# def summa(a, b):
#     result = a + b
#     random.randint(1, 10)
#     return result
#     print(result)

# a = summa(10, 5)
# print(a)

# Глобальная -- вне функции
# Локальная -- внутри функции
# Глобальные переменные можно ЧИТАТЬ внутри функции
# Локальный перемнные доступны ТОЛЬКО внутри функции

global_c = 10


def multipy(local_c):
    # global c
    local_c *= 10
    print(f"Локальная: {local_c}")
    return local_c
    
    
global_c = multipy(global_c)
print(f"Глобальная: {global_c}")