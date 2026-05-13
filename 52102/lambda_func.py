def test(a):
    print(a*2)
    
    
y = lambda x=2: test(x)
y()