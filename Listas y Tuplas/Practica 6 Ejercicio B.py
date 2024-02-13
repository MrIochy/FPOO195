"""
Crea un programa que llene una lista de 30 valores aleatorios en un rango del 10
al 20, con la lista llena el usuario podrá
a. Contar número repetidos
b. Eliminar numero repetidos
c. Remplazar los repetidos con 0
"""
import random 

lista = [random.randint(10,20) for _ in range (30)]
print("Los numeros generados fueron", lista)

numerosrepetidos = {num: lista.count(num) for num in set (lista)}
print("Esta es la cantidad de veces que se repiten los numeros", numerosrepetidos)

eliminarnumrep = list(set(lista))
print("Esta es la lista sin los numeros repetidos", eliminarnumrep)

numerosrepigualacero= [0 if lista.count(num) > 1 else num for num in lista]
print("Esta es la lista de los numeros repetidos reemplazados por un 0", numerosrepigualacero)