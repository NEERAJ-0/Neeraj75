b=[2,8,6,4,3,23,2,1,8,9]

def even(n):
    if n%2==0:
        return n**3
    else:
        return  False

print(list(filter(even,map(even, b))))
print(list(map(lambda k:k**3,filter(lambda i:i%2==0,b))))
print(list(filter(lambda i:i%2==0,map(lambda k:k**3,b))))
