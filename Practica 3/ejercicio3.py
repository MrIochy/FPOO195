"""
Escribir un programa que solicite un entero X, introducido por el usuario y después
muestre en pantalla la suma de todos los enteros desde 1 hasta X .
"""
numerox= int(input("Introduce un numero entero\n"))
resultado= 0
for i in range(1, numerox+1):
    resultado += i
    print(resultado)