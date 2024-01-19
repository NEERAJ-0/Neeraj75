s='Hello my name is neeraj'
i=0
n=' '
temp=True
while i<len(s):
    if s[i]==' ':
        temp=True
    elif temp and 'a'<=s[i]<='z':
        n+=chr(ord(s[i])-32)
        temp=False
    else:
        n+=s[i]
        temp=False
    i+=1
print(n)
