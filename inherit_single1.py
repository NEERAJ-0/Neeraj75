class parent:
    a=10
    b=20
    
    def __init__(self,c,d):
        self.c = c 
        self.d = d
class child(parent):
    pass
obj=child(4,5)

