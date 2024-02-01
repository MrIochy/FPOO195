#2. Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
import math 
def area_circulo(radio):
    return ((3.1416)*(radio**2))

radio= float(input("ingrese valor del radio:"))
area_result=area_circulo(radio)

print(f"area del circulo: {area_result}")

def volumen(altura):
    return (area_result*altura)

altura_cilindro= float(input("ingrese valor de la altura:"))
volumen_cilindro=volumen(altura_cilindro)

print(f"volumen del cilindro: {volumen_cilindro}")