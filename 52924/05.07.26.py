
def fib(n, prev=None, prevprev=None):
    if not prev:
        prev = 1
        prevprev = 0
        n -= 2
    current = prev + prevprev
    if n == 0:
        return current
    prevprev = prev 
    return fib(n-1, current, prevprev)


print(fib(8))