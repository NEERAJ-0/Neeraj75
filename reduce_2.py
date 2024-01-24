from functools import reduce
b=[1,2,3,4,5]
c=['hi','hello','welcome']
    
print(reduce(lambda x,y:x+' '+y,c))

print(reduce(lambda x,y:x+y,map(lambda a:a**2,b)))