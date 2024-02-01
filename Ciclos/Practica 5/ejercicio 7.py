"""
Imprime un árbol de navidad formado con Asteriscos haciendo uso del while,
Solicitando al usuario la cantidad de * de la base
"""
numero = int(input("Introduce un numero entero: "))
i=0
for i in range (1, numero + 1):
    espacios = " " * (numero - i)
    asteriscos = "*" * (2*i-1)
    print( espacios + asteriscos)