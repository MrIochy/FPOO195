from Personaje import * 
from Armas import * 

# Solicitar datos del Spartan
print("===== Datos de Heroe =====")
nombreS= input("Escribe el nombre de tu Spartan: ")
especieS= input("Escribe el especie de tu Spartan: ")
alturaS= float(input("Escribe la altura de tu Spartan: "))
print("")

# Solicitar datos del Nemesis
print("===== Datos de Nemesis =====")
nombreN= input("Escribe el nombre del Nemesis: ")
especieN= input("Escribe el especie del Nemesis: ")
alturaN= float(input("Escribe la altura del Nemesis: "))
print("")

# Creamos el objeto de la clase pensonaje
spartan = Personaje(especieS,nombreS,alturaS)
nemesis = Personaje(especieN,nombreN,alturaN)
Arma = Armas()

"""
# Creamos el objeto de la clase pensonaje
spartan = Personaje()
Arma = Armas()
"""

# Usamos los atributos Spartan
print("===== El objeto Spartan contiene =====")
print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)
print("")

# Usamos los atributos Nemesis
print("===== El objeto Nemesis contiene =====")
print(nemesis.nombre)
print(nemesis.especie)
print(nemesis.altura)
print("")

# Usamos los metodos del Spartan
print("===== Metodos del objeto Spartan =====")
spartan.correr(False)
spartan.lanzarGranada()
print("")

# Usamos los metodos del Nemesis
print("===== Metodos del objeto Nemesis =====")
nemesis.correr(True)
nemesis.lanzarGranada()
print("")

# Usamos los metodos del Arma
Arma.recargarArma(25)
Arma.seleccionarArma(spartan.nombre)