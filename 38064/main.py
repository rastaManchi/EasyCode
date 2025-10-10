c = 5

def test(local_c):
    local_c *= 10
    return local_c

c = test(c)
print(f'Глобальная: {c}')

