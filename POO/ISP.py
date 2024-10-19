#INTERFACE SEGREGATION PRINCIPLE  ISP
"""NO FORCEMOS AL CLIENTE A QUE DEPENDA DE INTERFACES QUE NO USAMOS"""

from abc import ABC, abstractmethod

class Trabajador(ABC):
    
    @abstractmethod
    def trabajar(self):
        pass

class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class Durmiente:
    @abstractmethod
    def dormir(self):
        pass

    
class Humano(Trabajador, Durmiente, Comedor):
    
    def comer(self):
        print("El humano esta comiendo")
    def trabajar(self):
        print("El humano esta trabajando")
    
    def dormir(self):
        print("El humano esta durmiendo")
      
        
class Robot(Trabajador):
    
    def trabajar(self):
        print("El robot esta trabajando")
        
robot = Robot()
humano = Humano()

robot.trabajar()
humano.trabajar()
humano.dormir()
humano.comer()