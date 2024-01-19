num=int(input('enter a number:'))
i=1
n=0
while i<=num:
    if num%i==0:
        n+=1
    i+=1
if n==2:
    print('prime')
else:
    print('Not Prime')
    
