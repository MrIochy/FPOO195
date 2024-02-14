"""
Crea un programa usando funciones y lo que necesites para que el usuario inserte
N números en una Tupla, después de la captura debe desplegar el siguiente menú
funcional
1. Sumatoria de los elementos de la lista
2. Numero mayor de la lista
3. Numero menor de la lista
4. Promedio
5. Moda: es el valor que más se repite de un conjunto de datos
6. Rango: es la diferencia entre el valor máximo y el valor mínimo de un
conjunto de datos
"""
#listas
print("Inserte los números separados por espacios para crear una lista:")
numeros = [int(x) for x in input().split()]

print("Seleccione una opción:")
print("1. Sumatoria de los elementos de la lista")
print("2. Numero mayor de la lista")
print("3. Numero menor de la lista")
print("4. Promedio")
print("5. Moda")
print("6. Rango")

opcion = int(input("Ingrese el número de la opción deseada: "))

if opcion == 1:
    print("La sumatoria de los elementos de la lista es:", sum(numeros))
    
elif opcion == 2:
    print("El número mayor de la lista es:", max(numeros))
    
elif opcion == 3:
    print("El número menor de la lista es:", min(numeros))
    
elif opcion == 4:
    print("El promedio de la lista es:", sum(numeros) / len(numeros))
    
elif opcion == 5:
    frecuencias = {}
    for num in numeros:
        if num in frecuencias:
            frecuencias[num] += 1
        else:
            frecuencias[num] = 1
    moda_valor = max(frecuencias, key=frecuencias.get)
    print("La moda de la lista es:", moda_valor)
    
elif opcion == 6:
    print("El rango de la lista es:", max(numeros) - min(numeros))
    
else:
    print("Opción no válida")

#tuplas
"""
print("Inserte los números separados por espacios para crear una tupla:")
numeros = tuple(int(x) for x in input().split())

print("Seleccione una opción:")
print("1. Sumatoria de los elementos de la lista")
print("2. Numero mayor de la lista")
print("3. Numero menor de la lista")
print("4. Promedio")
print("5. Moda")
print("6. Rango")

opcion = int(input("Ingrese el número de la opción deseada: "))

if opcion == 1:
    print("La sumatoria de los elementos de la lista es:", sum(numeros))
    
elif opcion == 2:
    print("El número mayor de la lista es:", max(numeros))
    
elif opcion == 3:
    print("El número menor de la lista es:", min(numeros))
    
elif opcion == 4:
    print("El promedio de la lista es:", sum(numeros) / len(numeros))
    
elif opcion == 5:
    frecuencias = {}
    for num in numeros:
        if num in frecuencias:
            frecuencias[num] += 1
        else:
            frecuencias[num] = 1
    moda_valor = max(frecuencias, key=frecuencias.get)
    print("La moda de la lista es:", moda_valor)
    
elif opcion == 6:
    print("El rango de la lista es:", max(numeros) - min(numeros))
    
else:
    print("Opción no válida")
    """