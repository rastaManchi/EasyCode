c = 0


def summa():
    global c
    c += 1
    print(f'локальная: {c}')


summa()
print(f'Глобальная: {c}')
