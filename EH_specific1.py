a=10
try:
    a+'10'
except TypeError:
    print('exception handled')
b=20
c=30
print(a+b+c)