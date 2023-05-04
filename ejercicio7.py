# ---------------------Ejercicio 6---------------------


def factorial(n):

    if not isinstance(n, int) or n < 0:

        raise ValueError("El número debe ser un entero positivo")
    
    if n == 0:

        return 1
    
    else:
        
        return n * factorial(n-1)

try:

    n = int(input("Ingresa un número entero positivo: "))
    print(f"El factorial de {n} es {factorial(n)}")

except ValueError as e:

    print(e)
