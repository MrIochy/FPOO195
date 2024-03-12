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
#from clase import GenerarMatricula

class GeneradorMatriculaInterfaz:
    def __init__(self, cuadro):
        self.cuadro = cuadro
        self.cuadro.title("Generador de Matriculas")
        self.cuadro.geometry("600x400")
        self.generador = GenerarMatricula()
        self.interfaz()

    def interfaz(self):
        self.labelNombre = Label(self.cuadro, text="Nombre:")
        self.labelNombre.grid(row=0, column=0)

        self.labelApellidoPat = Label(self.cuadro, text="Apellido Paterno:")
        self.labelApellidoPat.grid(row=1, column=0)
        
        self.labelApellidoMat = Label(self.cuadro, text="Apellido Materno:")
        self.labelApellidoMat.grid(row=2, column=0)

        self.labelAñoNacimiento = Label(self.cuadro, text="Año en nacimiento:")
        self.labelAñoNacimiento.grid(row=3, column=0)

        self.labelCarrera = Label(self.cuadro, text="Carrera:")
        self.labelCarrera.grid(row=4, column=0)
        
        #----------------------------------------------------------------------------------------- 
        
        self.espacioNombre = Entry(self.cuadro)
        self.espacioNombre.grid(row=0, column=0)

        self.espacioApellidoPat = Entry(self.cuadro)
        self.espacioApellidoPat.grid(row=0, column=1)
        
        self.espacioApellidoMat = Entry(self.cuadro)
        self.espacioApellidoMat.grid(row=0, column=2)

        self.espacioAñoNacimiento = Entry(self.cuadro)
        self.espacioAñoNacimiento.grid(row=0, column=3)

        self.espacioCarrera = Entry(self.cuadro)
        self.espacioCarrera.grid(row=0, column=4)
        
        #-----------------------------------------------------------------------------------------
        
        self.botonGenerar = Button(self.cuadro, text="Generar Matricula", command=self.generar_matricula)
        self.botonGenerar.grid(row=3, column=1)

        self.espacioMatricula = Entry(self.cuadro)
        self.espacioMatricula.grid(row=4, column=1)

#----------------------------------------------------------------------------------------------------------------

    def generar_matricula(self):
        longitud = int(self.espacioLongitud.get())

        contraseña = self.generador.generar_contraseña(longitud, incluir_mayusculas, incluir_especiales)
        self.espacioContraseña.delete(0, 'end')
        self.espacioContraseña.insert(0, contraseña)

    def comprobar_fortaleza(self):
        contraseña = self.espacioContraseña.get()
        fortaleza = self.generador.comprobar_fortaleza(contraseña)
        messagebox.showinfo("Fortaleza de la contraseña", fortaleza)

if __name__ == "__main__":
    cuadro = Tk()
    GeneradorMatriculaInterfaz(cuadro)
    cuadro.mainloop()