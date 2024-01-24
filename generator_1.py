def fun(a,b):
    yield a+b
    yield a*b
out=fun(2,3)
for i in out:
    print (i)
print(list(out))