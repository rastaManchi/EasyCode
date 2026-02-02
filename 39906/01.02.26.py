class OddError(Exception):
    pass



num = int(input('Введите четное число: '))
if num % 2 != 0:
    raise OddError("Было введено нечетное число")
