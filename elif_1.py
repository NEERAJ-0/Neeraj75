x=input('enter character\n')
if 'a'<=x and 'z'>=x:
    print('lowercase')
elif 'A'<=x and 'Z'>=x:
    print('UPPERCASE')
elif x in '0123456789':
    print('Number')
else:
    print('Special Character')