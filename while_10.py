str='Hello my name is Neeraj'
i=0
n=' '
while i<len(str):
    if str[i]==' ':
       n+='_'
    else:
        n+=str[i]
    i+=1
print(n)
