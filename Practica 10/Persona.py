class AccionesCRUD:
    def __init__(self):
        self.__id=0
        self.__nombre=""
        self._email=""
        self.__contraseña=""
        
    def crearUsuario(self):
        self.__id=input("Ingrese elID del usuario: ")
        self.__nombre=input("Ingrese el nombre del usuario: ")
        self.__email=input("Ingrese el email del usuario: ")
        self.__contraseña=input("Ingrese la contraseña del usuario: ")
        
    def consultarUsuario(self):
        print("ID:", self.__id)
        print("Nombre:", self.__nombre)
        print("Email:", self.__email)
        print("Contraseña:", self.__contraseña)

    def modificarUsuario(self):
        nuevo_nombre=input("Ingrese el nuevo nombre del usuario: ")
        nuevo_email=input("Ingrese el nuevo nombre del usuario: ")
        nueva_contraseña=input("Ingrese la nueva contraseña del usuario: ")
        self._nombre=nuevo_nombre
        self._email=nuevo_email
        self._contraseña=nueva_contraseña
    
    def eliminarUsuario(self):
        self.__id=0
        self.__nombre=""
        self.__email=""
        self.__contraseña=""