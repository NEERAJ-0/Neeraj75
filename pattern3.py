r=int(input('enter no of rows:'))
out=''
for i in range(r):
    for j in range(r):
        if i==j or i==r-j-1:
            out+=' '
        else:
            out+='*'
    out+='\n'
name=input('enter file name:')
with open(f'{name}.txt','w') as file:
    file.write(out)