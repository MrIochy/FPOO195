class Personaje:
    
    """
    # atributos de personajes
    especie = "Humano"
    nombre = "John"
    altura = 2.18
    """
    
    # Atributo de personaje
    # Declaramos el constructor para crear los objetos
    def __init__(self,esp,nom,alt):
        self.especie= esp
        self.nombre= nom
        self.altura= alt
    
    # Metodos del personaje
    def correr(self,estado):
        if(estado):
            print("El personaje " + self.nombre + " esta corriendo")
        else:
            print("El personaje " + self.nombre + " esta muerto")
            
    def lanzarGranada(self):
        print(self.nombre + " lanzo una granada")
    """    
    def recargarArma(self, municion):
        cargador = 25 
        cargador + municion
        print("Arma recargada al " + str(cargador) + "%" )
        """
"""
# Creamos el objeto de la clase pensonaje
spartan = Personaje()

print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)

# Usamos los metodos del Spartan
spartan.correr(False)
spartan.lanzarGranada()
spartan.recargarArma(25)
"""