def vowels(st):
    out=''
    for i in st:
        if i in 'aeiouAEIOU':
            out+=i
    j=-1
    res=''
    for k in st:
        if k in 'aeiouAEIOU':
            res+=out[j]
            j+=-1
        else:
            res+=k
    return res       
print(vowels('Hello'))        