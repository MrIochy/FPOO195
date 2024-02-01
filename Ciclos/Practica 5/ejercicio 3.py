"""
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""
numero= int(input("Digite un numero positivo\n"))

if numero == 0:
    print("De nada sirve la tabla del 0")
else:
    for i in range (1,11):
        print(numero, " * ", i, " = ", i*numero)