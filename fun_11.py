def vowels(s):
    v='aeiouAEIOU'
    out=''
    for i in v:
        if  i not in s:
            out+=i                 
    return out
print(vowels('neerAj'))

'''(or)

def filter(string):
    vowels='aeiouAEIOU'
    out=''
    for i in string:
        if i in vowels:
            out+=i
    return out
def extract(st):
    res=''
    for j in 'aeiouAEIOU':
        if j not in st:
            res+=j
    return res
print(extract(filter('hello)))

'''