"""
Programa que genera la serie de Collatz de un numero entero solicitado al usuario se construye de la siguiente forma:
Si el numero es par, se lo deivide entre dos; si es impar, se le multiplica por tres y se le suma uno; la serie termina al llegar a uno
"""
numero = 1
print("Bienvenido al programa Serie de Collatz")
numero=int(input("Por favor ingresa un numero entero\n"))
while numero > 1:
    if numero % 2 == 0:
        numero = numero//2
    else:
        numero = numero*3+1
    print(numero)
else:
    print("La serie de Collatz del numero finalizado exitosamente")