"""
Crea una interfaz gráfica que genere password automáticos, solicitara al  usuario la longitud (8 caracteres por default), si quiere incluir Mayúsculas o 
Caracteres especiales, dentro de las opciones que tendrá agregar una para comprobar fortaleza del password esta interfaz debe incluir los siguientes 
requerimientos 
1. Crea un diagrama de clases para la solución antes de comenzar a programar
2. Debe estar programado usando tus Clases y objetos propios junto con los de Tkinter, Encapsular lo necesario
3. La contraseña generada debe estar mostrada en un MessageBox y también disponible en un Entry para copiar y pegar
4. Cuidar el diseño de la interfaz
"""
from tkinter import Tk, Label, Entry, Button, IntVar, Checkbutton, messagebox
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

        self.botonComprobarFortaleza = Button(self.cuadro, text="Comprobar Fortaleza", command=self.comprobar_fortaleza)
        self.botonComprobarFortaleza.grid(row=5, column=1)

    def generar_contraseña(self):
        longitud = int(self.espacioLongitud.get())
        incluir_mayusculas = bool(self.checkboxMayusculasEstado.get())
        incluir_especiales = bool(self.checkboxEspecialesEstado.get())

        contraseña = self.generador.generar_contraseña(longitud, incluir_mayusculas, incluir_especiales)
        self.espacioContraseña.delete(0, 'end')
        self.espacioContraseña.insert(0, contraseña)

    def comprobar_fortaleza(self):
        contraseña = self.espacioContraseña.get()
        fortaleza = self.generador.comprobar_fortaleza(contraseña)
        messagebox.showinfo("Fortaleza de la contraseña", fortaleza)

if __name__ == "__main__":
    cuadro = Tk()
    GeneradorContraseñaInterfaz(cuadro)
    cuadro.mainloop()