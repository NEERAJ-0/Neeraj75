class cname:
    _a=10
    b=20
    def __init__(self,c,d):
        self._c=c
        self.d=d
    def display(self):
        print(self.c,self.d)
class sub(cname):
    pass
obj=cname(5,6)
#_a,self_c are protected but can also accessed