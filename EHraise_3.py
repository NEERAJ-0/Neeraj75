class mobilenoError(Exception):
    pass
class lengthError(Exception):
    pass
try:
    name=input('enter a name:')
    if len(name)<=4:
        raise lengthError(f'Name should be more than 4 character but {len(name)} were given')
    else:
        print('Name is validated')
        
    no=input('enter a mobile:')
    if len(no)!=10:
        raise mobilenoError(f'Mobile number should be  10 digits but {len(no)} were given')
    else:
        print('Mobile is validated')
except (lengthError,mobilenoError) as e:
    print(e)