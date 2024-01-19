a=eval(input('enter a collection'))
if len(a)%2==0:
    print(a[0:len(a)+1:len(a)-1])
else:
    print(a[len(a)//2])
# or if len(a)%2==0
#print(a[0],a[-1])
#else
#print(a[len(a)//2])