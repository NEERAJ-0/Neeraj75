a=[1,2,'abc',2.5,9,[1,2,3],'2']
out=[]
res=[]
for i in a:
    if type(i)==int:
        out+=[i]
    else:
        res+=[i]
res+=out
print(res)
