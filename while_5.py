str=input('enter a string:')
i=0
n=0
while i<len(str):
    if str[i] in 'aeiouAEIOU':
        n+=1
    i+=1
print(n)
'''(or)
str=input('enter a string:')
i=-1
n=0
while i>=-len(str) (or) i<0:
    if str[i] in 'aeiouAEIOU':
        n+=1
    i-=1
print(n)'''