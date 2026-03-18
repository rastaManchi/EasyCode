def summ(*args):
    print(args)
    
def summ2(**kwargs):
    print(kwargs)
    
# summ(1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
summ2(a=1, b=2, c=3, d=4)