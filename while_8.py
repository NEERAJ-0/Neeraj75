p=int(input('enter a number:'))
i=1
sum=0
while i<p:      #(or) for k in range(1,num):
    if p%i==0:
        sum+=i
    i+=1
if sum==p:
    print('perfect')
else:
    print('not perfect')



