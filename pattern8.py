r=int(input('enter no of rows:'))
temp=r//2
for i in range(r):
    for j in range(r):
        if i in [0,j,r-j-1,temp] or j in [temp]:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

