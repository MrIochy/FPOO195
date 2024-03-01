class Personaje:
    
    # Constructor para crear los objetos
    def __init__(self, esp, nom, alt):
        self.__especie = esp
        self.__nombre = nom
        self.__altura = alt
    
    # Método para que el personaje piense
    def pensar(self):
        return f"{self.__nombre} está pensando."
    
    # Métodos para obtener y establecer los atributos
    def get_especie(self):
        return self.__especie
    
    def set_especie(self, esp):
        self.__especie = esp
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nom):
        self.__nombre = nom
    
    def get_altura(self):
        return self.__altura
    
    def set_altura(self, alt):
        self.__altura = alt
    
    # Métodos del personaje
    def correr(self, estado):
        if estado:
            print(f"El personaje {self.__nombre} está corriendo")
        else:
            print(f"El personaje {self.__nombre} está muerto")
            
    def lanzarGranada(self):
        print(f"{self.__nombre} lanzó una granada")
