from Persona import AccionesCRUD

def MenuOpciones():
    print("_________________________________")
    print("Menu")
    print("_________________________________")
    print("1. Para crear usuario")
    print("2. Para consultar usuario")
    print("3. Para modificar usuario")
    print("4. Para eliminar usuario")
    print("Cualquier otro valor para salir")
    print("_________________________________")
    
def main():
    registro=AccionesCRUD()
    while True:
        MenuOpciones()
        opcion = input("\nSeleccione una opcion: ")
        if opcion == '1':
            registro.crearUsuario()
        elif opcion == '2':
            registro.consultarUsuarios()
        elif opcion == '3':
            registro.modificarUsuario()
        elif opcion == '4':
            registro.eliminarUltimoUsuario()
        else:
            print("Cerrando sesion...")
            break
if __name__ == "__main__":
    main()