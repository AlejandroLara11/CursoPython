#LSP
"""
PRINCIPIO DE SUSTITUCION DE LISNKOV
SI LA CLASE B ES UNA SUBCLASE DE A, ENTONCES A DEBE PODER UTILIZARSE
EN DONDE B
"""
# class Ave:
#     def volar(self):
#         return "Estoy volando"
        
# class Pinguino(Ave):
#     def volar(self):
#         return "No puedo volar"
        
# def hacer_volar(ave = Ave):
#     return ave.volar()

# print(hacer_volar(Pinguino()))

class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        print("Estoy volando")
        
class AveNoVoladora(Ave):
    pass

