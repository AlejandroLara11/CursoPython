numeros = [-9,-8,-7,-6,-5,-4,-3,-2,-1,0, 1,2,3,4,5,6,7,8,9]
#Creando una funcion que diga si es par o no
def es_par(num):
    if num%2 == 0:
        return True

numeros_pares = filter(es_par, numeros)
print(list(numeros_pares))




"""FUNCIONES LAMBDA"""

#Filter utiliza una función que devuelva "True o False" y crea una lista
#con los valores en los que la función devuelve TRUE

numeros_pares = filter(lambda num:num%2 == 0, numeros)
print(sorted((list(numeros_pares)), reverse = True))

numeros_mayores_cero = filter(lambda num:num>0, numeros)
print(list(numeros_mayores_cero))