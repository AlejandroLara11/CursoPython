#Creando una funcion que muestre la serie fibonacci entre 0 y el numero dado
def fibonacci(num):
    a,b = 0,1
    lista_fibonacci = list([0])
    for i in range(num):
        if b > num: 
            return lista_fibonacci
        else:
            lista_fibonacci.append(b)
            a, b = b, a+b

resultado = fibonacci(25)
print(resultado)