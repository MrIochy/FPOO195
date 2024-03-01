class Armas:
    
    # Metodos del personaje
    def recargarArma(self, municion):
        cargador = 25 
        cargador = cargador + municion
        print("Arma recargada al " + str(cargador) + "%" )
    
    def seleccionarArma(self,nombre):
        seleccion = int(input("Selecciona el arma:\n1 es un Rifle de Asalto \n2 es un Espada de Energia \n3 es un Rifle M392 \nSeleccion: "))
        
        if(seleccion==1):
            print("Rifle de asalto asignado a " + nombre)
            print("Municiones 7.62 * 52mm, sin mira")
        
        elif(seleccion==2):
            print("Espada de energia asignada a " + nombre)
            print("Arma creada por los Shagheili")
            
        elif(seleccion==3):
            print("Rifle M392 asignada a " + nombre)
            print("Municiones 7.62 * 52mm, con mira")
            
        else:
            print("Seleccion no valida")