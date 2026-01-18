import time
import datetime


n = 6


def summ(index=3, n1=0, n2=1):
    n3 = n1 + n2
    if index == n:
        return n3
    return summ(index+1, n1=n2, n2=n3)


print(summ())

