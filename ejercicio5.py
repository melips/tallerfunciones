# ---------------------Ejercicio 5---------------------

def temp():

    valor = float(input("Ingrese la temperatura a convertir: ")),
    origen = input("Ingrese la medida de origen (C, F, K): "),
    destino = input("Ingrese la medida de destino (C, F, K): ")

    if origen == "C":

        if destino == "F":

            return valor * 9/5 + 32
        
        elif destino == "K":

            return valor + 273.15
        
        elif destino == "C":

            return valor
        
        else:

            print("La medida de destino no es válida.")
        
    elif origen == "F":

        if destino == "C":

            return (valor - 32) * 5/9
        
        elif destino == "K":

            return (valor - 32) * 5/9 + 273.15
        
        elif destino == "F":

            return valor
        
        else:

            print("La medida de destino no es válida.")

    elif origen == "K":

        if destino == "C":

            return valor - 273.15
        
        elif destino == "F":

            return (valor - 273.15) * 9/5 + 32
        
        elif destino == "K":

            return valor
        
        else:

            print("La medida de destino no es válida.")
        
    else:

        print("La medida de origen no es válida.")


resultado = temp()
print("El resultado de la conversión es:", resultado)







