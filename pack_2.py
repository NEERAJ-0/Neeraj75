def fun(a,*args,b):
    print(a,args,b)
fun(1,b=5)
fun(1,2,3,4,b=5)
fun(1,2,3,4)