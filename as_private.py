class cname:
    __a=10
    b=20
    def __init__(self,c,d):
        self.__c=c
        self.d=d
    def __display(self):
        print(self.__c,self.d)
        
    @classmethod
    def classdisplay(cls):
        print(cls.__a,cla.b)
obj=cname(5,6)
#__a,self.__c,__display() are private but can also accessed