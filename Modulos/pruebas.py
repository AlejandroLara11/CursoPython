import sys
sys.path.append("C:\\Users\\dany1\\OneDrive\\Escritorio\\CursosPython\\Pruebas_modulos")

import contra_calc as cc

contraseña = cc.pass_generator(2)
print(contraseña)

suma = cc.calculadora("suma", 4, 2)
res = cc.calculadora("resta", 4, 2)
m = cc.calculadora("multiplicacion", 4, 2)
div = cc.calculadora("division", 4, 2)

print(suma)
print(res)
print(m)
print(div)
