#OCP PRINCIPIO DE ABIERT-CERRADO
class Notificador:
    def __init__(self, usuario, msj):
        self.usuario = usuario
        self.msj = msj
        
    def notificar(self):
        raise NotImplementedError()
    
    
class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por mail a {self.usuario}.mail...")

class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por SMS a {self.usuario}.telefono...")

class NotificadorWhatsapp(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por SMS a {self.usuario}.whatsap...")
        
"""
SE LE PUEDE AGREGAR FUNCIONALIDAD PERO SIN MODIFICAR LAS CLASES PRINCIPALES
ESTO PERMITE ECALABILIDAD Y LIMPIEZA

"""

user = Notificador("Alex", "UNONOTICIAS*")


Alex = NotificadorEmail("Alex", "UNOTV")
Alex.notificar()