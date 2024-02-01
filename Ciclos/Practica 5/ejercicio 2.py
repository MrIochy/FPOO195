"""
Escribir un programa que pida al usuario un número entero positivo y muestre
por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""
numero= int(input("Digite un numero positivo\n"))

if numero <= 0:
    print("Tenia que digitar un numero positivo")
else:
    while numero > 0:
        print(numero, end=", ")
        numero -= 1
    else:
        print(numero)
        print("Esos son todos los numeros impares del 1 al", numero)