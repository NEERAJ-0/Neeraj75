from abc import ABC, abstractmethod
class Modelcar(ABC):

    @abstractmethod
    def Break():
        pass
    
    @abstractmethod
    def speed_up():
        pass

    @abstractmethod
    def speed_down():
        pass
class Nexon(Modelcar):
    def __init__(self,brk=True,spd=0):
        self.stop=brk
        self.speed=spd

    def speed_up(self):
        self.speed+=5
        self.stop=False
        return self.speed

    def speed_down(self):
        if self.speed>0:
            self.speed-=5
            return self.speed
        else:
            self.stop=True
            return 'car stopped'
        
    def Break(self):
        self.speed=0
        self.stop=True
        return 'break applied'

class indica(Modelcar):
    def __init__(self,brk=True,spd=0):
        self.stop=brk
        self.speed=spd

    def speed_up(self):
        self.speed+=2
        self.stop=False
        return self.speed

    def speed_down(self):
        if self.speed>0:
            self.speed-=2
            return self.speed
        else:
            self.stop=True
            return 'car stopped'
        
    def Break(self):
        self.speed=0
        self.stop=True
        return 'break applied'

car1=Nexon()
car2=indica()
