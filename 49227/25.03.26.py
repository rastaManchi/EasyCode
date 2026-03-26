fibs = [0, 1]


def fib_num(n):
    print(fibs)
    if n == 1:
        return 0
    elif n == 2:
        return fibs[-1]
    prevnum = fibs[-1]
    prev2num = fibs[-2]
    newnum = prev2num + prevnum
    fibs.append(newnum)
    n -= 1
    return fib_num(n)


print(fib_num(20))