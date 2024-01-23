class grandparent:
    a=10
    b=20
    
    def __init__(self,c,d):
        self.c = c 
        self.d = d

class parent(grandparent):
    
    def __init__(self,c,d,e,f):
        super().__init__(c,d)
        self.e=e
        self.f=f
class child(parent):

    def __init__(self,c,d,e,f,x=0,y=0):
        super().__init__(c,d,e,f)
        self.x=grandparent.b
        self.y=grandparent.a
                
obj=child(4,5,8,9,1)
