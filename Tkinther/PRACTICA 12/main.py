from persona import Persona
from logintkinter import iniciar_sesion

def main(persona):
    while True:  
        print("")  
        print("-- Menú -----")  
        print("1. Insertar Usuarios: ")  
        print("2. Mostrar todos los Usuarios: ")  
        print("3. Buscar Usuario:")  
        print("4. Eliminar Usuario: ")  
        print("5. Editar Usuario: ")  
        print("6. Salir")  
        print("7. Inicio de sesión")  
        print("")  
        opcion = input("Elige una opción: ")  

        if opcion == "1":  
            
            print("Bienvenido a la funcion: Insertar Usuarios")  
            id = input("Escribe el Id: ")
            nom = input("Escribe el Nombre: ")
            contraseña = input("Escribe la Contraseña: ")
            persona.Insertar(id, nom, contraseña)  
            print(" -- Persona Agregada correctamente --")  

        elif opcion == "2":  
            
            print("Bienvenido a la funcion: Mostrar todos los Usuarios")  
            print("Estos son los Usuarios almacenados:")
            print(persona.consultarTodos())

        elif opcion == "3":  
            print("Bienvenido a la funcion: Buscar Usuario")  
            id = input("Introduce Id de la persona :: ")  
            usuario = persona.buscarUsuario(id)  
            if usuario:  
                print(usuario)  
            else:  
                print("Usuario no encontrado")  

        elif opcion == "4":  
            print("Bienvenido a la funcion: Eliminar Usuario")  
            id = input("Introduce Id de la persona a eliminar : ")  
            if persona.eliminar(id):  
                print(":: Usuario Eliminado ::")  
            else:  
                print("Usuario no encontrado")  

        elif opcion == "5":  
            print("Bienvenido a la funcion: Editar Usuario")  
            id = input("Introduce Id de la persona a editar : ")  
            nom = input("Nombre: ")  
            contraseña = input("Contraseña: ")  
            if persona.editar(id, nom, contraseña):  
                print(":: Usuario Editado ::")  
            else:  
                print("Usuario no encontrado")  

        elif opcion == "6":  
            print("¡Hasta luego!")  
            break  

        elif opcion == "7":  
            iniciar_sesion(persona)  

        else:  
            print("Opción no válida. Inténtalo de nuevo.")  

if __name__ == "__main__":  
    persona = Persona()  
    main(persona)  
