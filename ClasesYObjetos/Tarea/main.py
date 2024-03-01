from Personaje import Personaje
from Armas import Armas

# Solicitar datos del Spartan
print("===== Datos de Héroe =====")
nombreS = input("Escribe el nombre de tu Spartan: ")
especieS = input("Escribe el especie de tu Spartan: ")
alturaS = float(input("Escribe la altura de tu Spartan: "))
print("")

# Solicitar datos del Nemesis
print("===== Datos de Nemesis =====")
nombreN = input("Escribe el nombre del Nemesis: ")
especieN = input("Escribe el especie del Nemesis: ")
alturaN = float(input("Escribe la altura del Nemesis: "))
print("")

# Creamos los objetos de la clase personaje
spartan = Personaje(especieS, nombreS, alturaS)
nemesis = Personaje(especieN, nombreN, alturaN)
arma = Armas()

# Usamos los atributos Spartan
print("===== El objeto Spartan contiene =====")
print(spartan.get_nombre())
print(spartan.get_especie())
print(spartan.get_altura())
print("")

# Usamos los atributos Nemesis
print("===== El objeto Nemesis contiene =====")
print(nemesis.get_nombre())
print(nemesis.get_especie())
print(nemesis.get_altura())
print("")

# Usamos los métodos del Spartan
print("===== Métodos del objeto Spartan =====")
spartan.correr(False)
spartan.lanzarGranada()
print(spartan.pensar())
print("")

# Usamos los métodos del Nemesis
print("===== Métodos del objeto Nemesis =====")
nemesis.correr(True)
nemesis.lanzarGranada()
print(nemesis.pensar())
print("")

# Usamos los métodos del Arma
arma.recargarArma(25)
arma.seleccionarArma(spartan.get_nombre())
