"""
1. Escribir una función que calcule el total de una factura tras aplicarle 
el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de
IVA a aplicar, y devolver el total de la factura. Si se invoca la función
sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
"""
cantidad=float(input("Digite la cantidad a aplicar IVA: "))
IVA=input("Digite el porcentaje de IVA: ")
if IVA.strip():
    IVA=float(IVA)
else:
    IVA=21

def factura(cantidad, IVA=21):
    total = cantidad + cantidad*IVA/100
    return total

total = factura(cantidad, IVA)
print("El total de la factura es: ", total)