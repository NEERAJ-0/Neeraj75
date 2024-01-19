a=int(input('enter 1st number\n'))
b=int(input('enter 2nd number\n'))
y=input('enter operator')
if y=='+':
    print('addition=',a+b)
elif y=='-':
    print('subtraction=',a-b)
elif y=='*':
    print('multiplication=',a*b)
elif y=='/':
    print('division=',a/b)
elif y=='//':
    print('floor division=',a//b)
elif y=='**':
    print('exponential=',a**b)
else:
    print('inalid operator')