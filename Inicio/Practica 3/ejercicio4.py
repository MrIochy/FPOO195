"""
Codifica un programa que pregunte el nombre del usuario y después de que el
usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde
<NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras
que tienen el nombre.
"""
nombre= str(input("Escribe tu nombre completo \n"))
nombremayusculas = nombre.upper()
print(nombremayusculas, " tiene ", len(nombre) , " letras ")
