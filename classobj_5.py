class num:
    def __init__(self,a):
        self.a=a
    def __str__(self):
        return str(self.a)
    def prime(self,i=2):
        if self.a%2==0:
            return False
        elif self.a==i:
            return True
        return prime(self,i+1)
    
    def increment(self,step=1):
        self.a=self.a+step
        return self.a
    def decrement(self,step=1):
        self.a=self.a-step
        return self.a

    
        
            