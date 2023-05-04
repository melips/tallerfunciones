# ---------------------Ejercicio 3---------------------

from collections import Counter

def repetido(lista_num):
   
    contador = Counter(lista_num)
    masRep, frecuencia = contador.most_common(1)[0]

    return masRep, frecuencia

lista_num = input("Ingresa una lista de números separados por espacios: ").split()
masRep, frecuencia = repetido(lista_num)

#Quitar el siguiente comentario para probar punto 3:

#print("El número más repetido es {} y aparece {} veces :)".format(masRep, frecuencia))


# ---------------------Ejercicio 4---------------------


def numerosRep(lista_num, tipo="mayor"):
 
    contador = Counter(lista_num)
    masRep = contador.most_common()

    if tipo == "mayor":

        return masRep[0]
    
    elif tipo == "menor":

        return masRep[-1]
    
    else:

        print("Debes solicitar 'mayor' o 'menor'.")

numero_mayor, frecuencia_mayor = numerosRep(lista_num, tipo="mayor")
numero_menor, frecuencia_menor = numerosRep(lista_num, tipo="menor")

#Quitar los siguientes comentarios para probar punto 4:

#print("El número más repetido es {} y aparece {} veces".format(numero_mayor, frecuencia_mayor))
#print("El número menos repetido es {} y aparece {} veces".format(numero_menor, frecuencia_menor))
