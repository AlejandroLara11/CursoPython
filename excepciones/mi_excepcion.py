#Creando mi propia excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"el error que cometiste es: {err}")
        
#Manejando mi excepcion
try:
    raise MiExcepcion("Jajajaja, persona poco culta")

except:
    print("Como vas a cometer ese error...")