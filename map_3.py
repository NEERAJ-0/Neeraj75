b=[1,2,[4,5,6],'xyz',(4,1,2,3)]

def fun(n):
    if type(n) in [str,list,tuple,set,dict]:
        return len(n)
    else:
        return n
    
print(list( map(fun,b)))