s='overconfidence'
i=0
n=' '
while i<len(s):
    if 'a'<=s[i]<='z':
        n+=chr(ord(s[i])-32)
    else:
        n+=s[i]
    i+=1
print(n)

