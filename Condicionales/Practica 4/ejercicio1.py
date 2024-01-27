"""
Escribir un programa que almacene la cadena de caracteres una contraseña en
una variable, después que solicite al usuario una contraseña e imprima en
pantalla si la contraseña introducida por el usuario coincide con la guardada en
la variable sin tener en cuenta mayúscula y minúscula.
"""
contraseña= str(input("Por favor digita una contraseña: \n"))
verificarcontraseña= str(input("Por favor vuelva a digitar su contraseña: \n"))
if contraseña == verificarcontraseña:
    print("Las contraseñas coinciden")
else:
    print("Las contraseñas NO coinciden")