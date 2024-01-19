a='good morning'
i=0
while i<len(a):
    if a[i] not in a[i+1:]:
        print(a[i])
        break
    i+=1