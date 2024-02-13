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
sumatoria=0
print("Digite una serie de numeros")
while True:
    NumerosGuardados = input()
    if not NumerosGuardados:
        break
    datos = tuple(map(int, NumerosGuardados.split( )))
    for num in datos:
        sumatoria += num
        
        
print("1. Sumatoria de los elementos de la lista", sumatoria)

#tuplas
