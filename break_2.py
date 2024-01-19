a='neeraj kumar'
i=-1    #len(a)-1
while i>=-len(a):   #i>0
    if a[i] not in a[:i-1]:
        print(a[i])
        break
    i-=1