class lengthError(Exception):
    pass
name=input('enter a name:')
if len(name)<=4:
    raise lengthError(f'Name should be more than 4 character but {len(name)} were given')
else:
    print('Name is validated')