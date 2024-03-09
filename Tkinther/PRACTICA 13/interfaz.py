from tkinter import Tk, Label, Entry, Button, IntVar, Checkbutton  
from clase import GeneradorContraseña  

class GeneradorContraseñaInterfaz:
    def __init__(self, cuadro):
        self.cuadro = cuadro  
        self.cuadro.title("Generador de Contraseñas")
        self.cuadro.geometry("600x400")
        self.generador = GeneradorContraseña()  
        self.interfaz()  

    def interfaz(self):
        
        self.labelLongitud = Label(self.cuadro, text="Longitud:")  
        self.labelLongitud.grid(row=0, column=0)  

        self.espacioLongitud = Entry(self.cuadro)  
        self.espacioLongitud.grid(row=0, column=1)  
        self.espacioLongitud.insert(0, "8")  

        self.checkboxMayusculasEstado = IntVar()  
        self.checkboxMayusculas = Checkbutton(self.cuadro, text="Incluir mayúsculas:", variable=self.checkboxMayusculasEstado)  
        self.checkboxMayusculas.grid(row=1, column=0)  

        self.checkboxEspecialesEstado = IntVar()  
        self.checkboxEspeciales = Checkbutton(self.cuadro, text="Incluir caracteres especiales:", variable=self.checkboxEspecialesEstado)  
        self.checkboxEspeciales.grid(row=2, column=0)  

        self.botonGenerar = Button(self.cuadro, text="Generar Contraseña", command=self.generar_contraseña)  
        self.botonGenerar.grid(row=3, column=1)  

        self.espacioContraseña = Entry(self.cuadro)  
        self.espacioContraseña.grid(row=4, column=1)  

    def generar_contraseña(self):
        
        longitud = int(self.espacioLongitud.get())  
        incluir_mayusculas = bool(self.checkboxMayusculasEstado.get())  
        incluir_especiales = bool(self.checkboxEspecialesEstado.get())  
        
        contraseña = self.generador.generar_contraseña(longitud, incluir_mayusculas, incluir_especiales)  
        self.espacioContraseña.delete(0, 'end')  
        self.espacioContraseña.insert(0, contraseña)  

if __name__ == "__main__":
    cuadro = Tk()  
    GeneradorContraseñaInterfaz(cuadro)  
    cuadro.mainloop()  