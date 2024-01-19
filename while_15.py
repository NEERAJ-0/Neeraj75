a='good night'
out=[]
i=0
while i<len(a):
    if a[i] in 'aeiouAEIOU':
        out+=[i]
    i+=1
print(out)