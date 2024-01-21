def fib(a,b=0,c=1,out=()): #out=[]
    if c>=a:
        return out
    elif b==0:
        out+=(b,c)      #[b,c]
    else:
        out+=(c,)       #[c]
    return fib(a,c,b+c,out)
print(fib(100))
print(fib(50))

#if tuple out=() OUTPUT: 
# (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
#(0, 1, 1, 2, 3, 5, 8, 13, 21, 34)          

#if list out=[] OUTPUT:
#[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34]