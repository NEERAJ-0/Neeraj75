db={'u':'neeraj','p':'5302'}
x=input('enter username\n')
y=input('enter password\n')
if x==db['u'] and y==db['p']:
    print('Hello, welcome',db['u'],'this is pyhton application')
else:
    print('invalid username/password')
