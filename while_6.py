str=input('enter a string:')
char=input('enter a character:')
i=0
n=0
while i<len(str):
    if str[i] in char:
        n+=1
    i+=1
print(n)