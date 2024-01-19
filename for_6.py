a='good night'
out=[]
i=0
for i in range(len(a)):
    if a[i] in 'aeiouAEIOU':
        out+=[i]
print(out)