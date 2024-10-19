#PRINCIPIO DE INVERSION DE DEPENDENCIAS

# class Diccionario:
#     def verificar_palabra(self, palabra):
#         #Logica para verificar palabra
#         pass
    
# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()
        
#     def corregir_texto(self,texto):
#         #usamos el diccionario para corregir el texto
#         pass
    
from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self,palabra):
        pass
    
    
#----------DOS TIPOS DE VERIFICADORES SEGUN LA NECESIDAD---------------------------
   
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #Logica para verificar palabras si está en el diccionario
        pass

class ServicioOnline(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #Logica para verificar palabras desde el servicio web
        pass
#-------------------------------------------------------------------------     
    
    
class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador  = verificador #(DICCIONARIO O SERVICIO WEB)
    
    def corregir_texto(self,texto):
        #Usamos el verificador de diccionario o un servicio online
        pass