# ---------------------Ejercicio 1---------------------

def primo(num):

    if num < 2:

        return False

    for i in range(2, num):

        if num % i == 0:

            return False

    return True

#Quitar el siguiente comentario para probar punto 1:

#print(primo(num=int(input("ingrese el número:"))))



# ---------------------Ejercicio 2---------------------

def listaPrimos():
    
    listnum = input("Ingresa una lista de números separados por espacios: ")
  
    listnum = [int(num) for num in listnum.split()]

    primos = []

    for numero in listnum:
        
        if primo(numero):
            
            primos.append(numero)

    return primos

#Quitar el siguiente comentario para probar punto 2:

#print("Los numeros primos en la lista son: ",listaPrimos())