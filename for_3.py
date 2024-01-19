a='Hello world'
out=''
for char in a:
    if char not in out:
        out+=char
print(out)