a=eval(input('enter 1st number\n'))
b=eval(input('enter 2nd number\n'))
c=eval(input('enter 3rd number\n'))
if a>b and a>c:
    print(a,'is big no')
    if b>c:
        print(b,'is 2nd big no')
    else:
        print(c,' 2nd is big no')
elif b>c:
    print(b, 'is big no')
    if a>c:
        print(a,'is 2nd big no')
    else:
        print(c,'is 2nd big no')
else:
    print(c,'is big no')
    if a>b:
        print(a,'is 2nd big no')
    else:
        print(b,' 2nd is big no')