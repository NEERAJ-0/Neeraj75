r=int(input('enter no of rows:'))

for i in range(r):
    for j in range(r):
        if i==j:# or i==r-j-1: #for 2nd diagonal
            print(' ',end='')
        else:
            print('*',end='')
    print()

