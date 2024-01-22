class mtca:
    principal='Mr.prabhakar'
    college='MTI of Computer Application'
    location='Palamaner'
    def __init__(self,sn,mo,em,s):
        self.sname=sn
        self.mobile=mo
        self.email=em
        self.sem=s
    def update_mob(self,new):
        self.mobile=new
        print('mobile updated')
    def update_mail(self,new):
        self.email=new
        print('email updated')
    def update_sem(self,new):
        self.sem=new
        print('sem updated')
    @classmethod
    def change_principal(cls,new):
        cls.principal=new

neeraj=mtca('neeraj',786785659,'neeraj05@gmail.com','1st')
prashant=mtca('prashant',9342325529,'prasant@gmail.com','1st')   
