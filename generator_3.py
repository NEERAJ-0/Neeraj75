def gen(n):
    out=1
    for i in range(1,n+1):
        yield out
        out*=2
out=gen(10)
print(list(out))