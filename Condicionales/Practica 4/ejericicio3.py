"""
Escribir un programa para una empresa que tiene salas de juegos para todas las
edades y quiere calcular de forma automática el precio que debe cobrar a sus
clientes por entrar. El programa debe preguntar al usuario la edad del cliente y
mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar
gratis, si tiene entre 4 y 18 años debe pagar $110 y si es mayor de 18 años, $190
"""
edad=0
edad= int(input("Ingresa tu edad \n"))
if edad<4 :
    print("Felicidades tu entrada es gratis")
elif 4 <= edad <= 18:
    print("Tu boleto cuesta $110.00")
else:
    print("Tu boleto cuesta $190.00")