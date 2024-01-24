def fib(n):
    i=0
    a,b=0,1
    while i<n:
        yield a
        a,b=b,a+b
        i+=1
out=fib(10)
print(list(out))