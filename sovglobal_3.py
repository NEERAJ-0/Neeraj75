a=10 #global variable
def fun():
    global a #modifying global variable
    a=40
    print(a)
print(a)
fun()
print(a)