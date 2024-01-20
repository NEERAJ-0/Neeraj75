def vowels(s):
    out=[]
    for i in range(len(s)):
        if s[i] in 'aeiouAEIOU':
            out+=[i]
    return out
print(vowels('neerAj'))