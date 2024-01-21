def fun(a,b,c=0,**kwargs):
    print(a,b,c,kwargs)
fun(*[1,2],**{'c':1,'d':2})