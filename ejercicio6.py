
# ---------------------Ejercicio 6---------------------

def temp(valor, origen, destino):

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



temperaturas = [("C", "F"), ("C", "K"), ("F", "C"), ("F", "K"), ("K", "C"), ("K", "F")]

for medida_origen, medida_destino in temperaturas:

    valor = float(input(f"Ingrese la temperatura en grados {medida_origen}: "))
    resultado = temp(valor, medida_origen, medida_destino)
    
    print(f"{valor} grados {medida_origen} son {resultado:.2f} grados {medida_destino}")

