name=input('enter a name:')
if len(name)<=4:
    raise Exception
else:
    print('Name is validated')