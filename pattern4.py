r=int(input('enter no of rows:'))
out=''
for i in range(r):
    for j in range(r):
        if i==r//2 or j==r//2:
            print(' ',end='')
        else:
            print(' +',end='')
    print()

