def gen(n):

   while n>=1:
    a=n%2
    n=n//2
    yield a

out=gen(10)
print(list(out)[::-1])