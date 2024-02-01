""""
Escribir un programa en el que se pregunte al usuario por una frase y una letra,
y muestre por pantalla el número de veces que aparece la letra en la frase.
"""
frase = input("Introduce una frase: ")
letra = input("Introduce la letra que quieres buscar: ")

repeticiones = 0
recorrido = 0

while recorrido < len(frase):
    if frase[recorrido] == letra:
        repeticiones += 1
    recorrido +=1

print("La letra", letra, "aparece", repeticiones, "veces en la frase" )