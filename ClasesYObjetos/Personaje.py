class Personaje:
    
    # atributos de personajes
    especie = "Humano"
    nombre = "John"
    altura = 2.18
    
    # Metodos del personaje
    def correr(self,estado):
        if(estado):
            print("El personaje" + self.nombre + "esta corriendo")
        else:
            print("El personaje" + self.nombre + "esta muerto")
            
    def lanzarGranada(self):
        print(self.nombre + "lanzo una granada")
        
    def recargarArma(self, municion):
        cargador = 25 
        cargador + municion
        print("Arma recargada al" + str(cargador) + "%" )

# Creamos el objeto de la clase pensonaje
spartan = Personaje()

print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)