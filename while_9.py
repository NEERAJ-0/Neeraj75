n=int(input('enter a number:'))
i=0
a,b=0,1
while i<n:
    print(a,end=' ')
    a,b=b,a+b
    i+=1