def fun(f):
    def inner(a,b):
        return f(a)
    return inner

#Decorator
@fun    #sample=fun(sample) 
def sample(a):
    return a**2
#print(sample(5))

@fun    #cube=fun(cube)
def cube(a):
    return a**3
print(cube(4))