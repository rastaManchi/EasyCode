a=int(input(': '))
b=int(input(': '))
c=int(input(': '))

Σ=0
for i in range(a,b+1,c):
    Σ+=((len(range(a,b+1,c))/2)/10)*(a+b)
print(Σ)