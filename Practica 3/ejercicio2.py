"""
Codifica un programa que pregunte el nombre completo del usuario en la consola y
después muestre por pantalla el nombre completo del usuario tres veces, una con
todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la
primera letra del nombre y de los apellidos en mayúscula. El usuario puede
introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""
nombre= str(input("Escribe tu nombre completo \n"))
apellido= str(input("Escribe tu apellido \n"))
nombreminusculas= nombre.lower() + " " + apellido.lower()
nombremayusculas = nombre.upper() + " " +  apellido.upper()
nombremaymin=apellido.title()
print("Tu nombre en minusculas es: ", nombreminusculas)
print("Tu nombre en mayusculas es: ", nombremayusculas)
print("Tu nombre es: ", nombremayusculas[:1], nombremaymin)