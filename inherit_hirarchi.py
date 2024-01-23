class mtca:
    chairman ='Mr.Sunil'
    location ='Palamaner'
    college  ='MTCA'

    def __init__(self,name,mobile):
        self.name=name
        self.mobile=mobile 
class mca(mtca):
    principal='Mr.Prabhakar'
    strenth  =240
    staff    =9
class btech(mtca):
    principal='Mr.Mohan'
    strenth  =350
    staff    =35

Neeraj=mca('Neeraj',77343542535)
Raju=btech('Raju',6535433543)