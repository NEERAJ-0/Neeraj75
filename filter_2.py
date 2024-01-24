b=[2,57,8,6,4,3,23,2,1,21,35,8,9]
def multi(n):
    if n%3==0:
        return True
    else:
        return False
print(list(filter(multi,b)))
print(list(filter(lambda b:b%3==0,b)))