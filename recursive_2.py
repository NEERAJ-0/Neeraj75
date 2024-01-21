
def prime(n,i=2):
    if n>1:
        if n%2==0:
            return 'not prime'
        elif n==i:
            return'prime'
        return prime(n,i+1)
    else:
        return 'enter number greater than 1'
print(prime(7))

