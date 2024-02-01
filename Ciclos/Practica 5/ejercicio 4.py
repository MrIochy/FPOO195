"""
Escribir un programa que pida al usuario un número entero y muestre por
pantalla un triángulo rectángulo como el de más abajo, de altura el número
introducido.
"""
numero = int(input("Introduce un numero entero: "))

for filas in range (1, numero + 1):
    for sumas in range (filas, 0, -1):
        print( sumas, end=" ")
    print()