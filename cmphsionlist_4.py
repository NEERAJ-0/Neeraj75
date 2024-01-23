def fact(n):
    out=1
    for i in range(1,n+1):
        out*=i
    return out
print([fact(i) for i in range(1,10) if i%2==0])
#or
import math
print([math.factorial(i) for i in range(1,10) if i%2==0])
