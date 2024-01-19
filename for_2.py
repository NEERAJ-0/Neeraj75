s="user@123#admin"
out=''
for char in s:
    if not '0'<=char<='9':
        out+=char
print(out, end='')
