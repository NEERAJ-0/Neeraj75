r=int(input('enter no of rows:'))

for i in range(r):
    for j in range(r):
        if i in [0,r-1,j,r-j-1] or j in [0,r-1]:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

