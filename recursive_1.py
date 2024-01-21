def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))


'''(or)
def fact(n,out=1):
    if n==1:
        return out
    out*=n
    return fact(n-1,out)
print(fact(5)) '''