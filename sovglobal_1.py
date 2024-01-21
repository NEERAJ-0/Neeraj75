a=10 #global variable
b=20 #global variable
def fun():
    a=40 #local variable
    c=30 #local variable
    print(a)
    print(c)
print(a)
fun()
print(a)