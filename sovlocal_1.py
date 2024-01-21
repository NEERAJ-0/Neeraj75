a=10 #global variable
def fun():
    c=20 #local variable
    def inner():
        nonlocal c #modifying local variable
        c=40
        print(c)    
    print(c)
    inner()
    print(c)
fun()
