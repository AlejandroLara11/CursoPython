#CREAR UNA FUNCION QUE AL PASAR UN NUMERO, GENERE NUMEROS PRIMOS HASTA LLEGAR HASTA ESE NUMERO
def es_primo(num):
    for valor_actual in range(2,num-1):
        #Verificamos que el numero no pueda dividirse por
        #ningun numero entre 2 y ese mismo numero -1
        if (num % valor_actual) == 0: return False
        #Si es divisible por alguno, cortamos y retornamos false
    return True
    #Si no es divisible, retornamos TRUE


def primos_hasta(num):
    primos = list([]) #Lista para guardar los primos
    for i in range(3, num+1): #Omitimos el cero, uno y dos, ya que son muy obvios
                              #Y agragamos un +1 para tomar en cuenta el mismo numero digitado
        #Verificamos que el numero sea primo
        resultado = es_primo(i)
        if resultado == True:
            #Si el valor es primo, lo agregamos a la lista
            primos.append(i)
    return primos
    

lista_primos = primos_hasta(int(input("Digite un numero: ")))
print(lista_primos) 

numeros = [2,3,4,1,1,2,4,6,7,6,8,7,12,13,60,24,13]
pares = list(filter(lambda x : x%2 == 0, numeros))
print(pares)

