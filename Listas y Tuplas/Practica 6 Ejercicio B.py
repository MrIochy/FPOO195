"""
Crea un programa que llene una lista de 30 valores aleatorios en un rango del 10
al 20, con la lista llena el usuario podrá
a. Contar número repetidos
b. Eliminar numero repetidos
c. Remplazar los repetidos con 0
"""
import random

print("Digite una letra para elegir la función:")
print("a. Contar número repetidos")
print("b. Eliminar numero repetidos")
print("c. Remplazar los repetidos con 0")

l = input("Ingrese la letra correspondiente a la función deseada: ")
letra = l.lower()

lista = [random.randint(10, 20) for _ in range(30)]
print("Los números generados fueron:", lista)

if letra == "a":
    numeros_repetidos = {}
    for num in set(lista):
        numeros_repetidos[num] = lista.count(num)
    print("Esta es la cantidad de veces que se repiten los números:", numeros_repetidos)


elif letra == "b":
    numeros_vistos = set()
    nueva_lista = []
    for num in lista:
        if num not in numeros_vistos:
            nueva_lista.append(num)
            numeros_vistos.add(num)
    print("Esta es la lista sin los números repetidos:", nueva_lista)

elif letra == "c":
    numeros_vistos = set()
    nueva_lista = []
    for num in lista:
        if num in numeros_vistos:
            nueva_lista.append(0)
        else:
            nueva_lista.append(num)
            numeros_vistos.add(num)
    print("Esta es la lista de los números repetidos reemplazados por un 0:", nueva_lista)

else:
    print("Opción no válida")