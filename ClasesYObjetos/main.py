from Personaje import * 
from Armas import * 

# Creamos el objeto de la clase pensonaje
spartan = Personaje()
Arma = Armas()

print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)

# Usamos los metodos del Spartan
spartan.correr(False)
spartan.lanzarGranada()
Arma.recargarArma(25)
Arma.seleccionarArma(spartan.nombre)