def toggle():
    st='HellO gOOd'
    n=''
    for i in st:
        if 'a'<=i<='z':
           n+=chr(ord(i)-32)
        elif 'A'<=i<='Z':
            n+=chr(ord(i)+32)
        else:
            n+=i
    return n
x=toggle()
print(x)