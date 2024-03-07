class Persona:
    def __init__(self):
        self.__listaBD = []  

    def Insertar(self, id, nom, contraseña):
        self.__listaBD.append({"Id": id, "Nombre": nom, "Contraseña": contraseña})

    def consultarTodos(self):
        return self.__listaBD

    def buscarUsuario(self, id):
        for usuario in self.__listaBD:  
            if usuario['Id'] == id:  
                return usuario  
        return None  
    
    def buscarUsuarioPorNombre(self, nom):
        for usuario in self.__listaBD:  
            if usuario['Nombre'] == nom:  
                return usuario  
        return None  

    def eliminar(self, id):
        usuarios_a_eliminar = [usuario for usuario in self.__listaBD if usuario['Id'] == id]  
        for usuario in usuarios_a_eliminar:  
            self.__listaBD.remove(usuario)  
        return bool(usuarios_a_eliminar)  

    def editar(self, id, nom, contraseña):
        for usuario in self.__listaBD:  
            if usuario['Id'] == id:  
                usuario['Nombre'] = nom  
                usuario['Contraseña'] = contraseña  
                return True  
        return False