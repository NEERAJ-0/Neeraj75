a=10 #global variable
def fun():
    print(a) #unboudlocalerror
    a=40
print(a)
fun()
print(a)