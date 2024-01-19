n='rohit sharma'
out=''
for i in range(len(n)):
    if n[i] in n[i+1:]:
        if n[i] not in out:
            out+=n[i]
print(out)









'''(or)
n='rohit sharma'
out=''
res=''
for char in n:
    if char not in out:
        out+=char
    else:
        res+=char
print(res)'''