"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""
inicio = 1
numero= int(input("Digite un numero positivo\n"))

if numero <= 0:
    print("Tenia que digitar un numero positivo")

while inicio <= numero -1:
    print(inicio, end=", ")
    inicio += 2
else:
    print("\nEsos son todos los numeros impares del 1 al", numero)