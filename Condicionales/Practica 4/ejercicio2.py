"""
Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es par o impar.
"""
numero= int(input("Ingresa un numero entero \n"))
if numero % 2 == 0:
    print(numero, " es par")
else:
    print(numero, "no es par")