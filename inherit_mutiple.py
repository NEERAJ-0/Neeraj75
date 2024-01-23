class add:
    @staticmethod
    def add2(a,b):
        return a+b 
    @staticmethod
    def add3(a,b,c):
        return a+b+c

class sub:
    @staticmethod
    def sub2(a,b):
        return a-b

class mul:
    @staticmethod
    def mul2(a,b):
        return a*b 

class Cal(add,sub,mul):
    pass
obj=Cal()
print(obj.add2(3,4))
print(obj.add3(3,4,9))
print(obj.mul2(3,4))
print(obj.sub2(12,8))

