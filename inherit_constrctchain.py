class parent:
    a=10
    b=20
    
    def __init__(self,c,d):
        self.c = c 
        self.d = d
class child(parent):
    a=30

    
    def __init__(self,c,d,e,f):
        super().__init__(c,d)
        self.e=e
        self.f=f
        
obj=child(4,5,8,9)

