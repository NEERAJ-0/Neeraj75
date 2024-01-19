s=input('enter a String:')
i=0
out=[]
start=0
while i<len(s):
    if s[i]==' ':
        out+=[s[start:i]]
        start=i+1
    i+=1
if start<len(s):
    out+=[s[start:]]
print(out)

''' st=input('enter a string:')
    out=[]
    i=0
    temp=''
    while i<len(st):
        if st[i]!=' ':
            temp+=st[i]
        else:
            out+=[temp]
            temp=''
        i+=1
    else:
        if temp:
            out+=[temp]
    print(out)
'''