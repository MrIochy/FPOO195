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
from clase import GenerarMatricula

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
        self.espacioNombre.grid(row=0, column=1)

        self.espacioApellidoPat = Entry(self.cuadro)
        self.espacioApellidoPat.grid(row=1, column=1)
        
        self.espacioApellidoMat = Entry(self.cuadro)
        self.espacioApellidoMat.grid(row=2, column=1)

        self.espacioAñoNacimiento = Entry(self.cuadro)
        self.espacioAñoNacimiento.grid(row=3, column=1)

        self.espacioCarrera = Entry(self.cuadro)
        self.espacioCarrera.grid(row=4, column=1)
        
        #-----------------------------------------------------------------------------------------
        
        self.botonGenerar = Button(self.cuadro, text="Generar Matricula", command=self.generar_matricula)
        self.botonGenerar.grid(row=5, column=0)

        self.espacioMatricula = Entry(self.cuadro)
        self.espacioMatricula.grid(row=5, column=1)

#----------------------------------------------------------------------------------------------------------------
    def generar_matricula(self):
        nombre  = str(self.espacioNombre.get())
        apep  = str(self.espacioApellidoPat.get())
        apem = str(self.espacioApellidoMat.get())
        fecnac  = str(self.espacioAñoNacimiento.get())
        carrera = str(self.espacioCarrera.get())

        matricula = self.generador.generar_matricula(nombre, apep, apem, fecnac, carrera)
        self.espacioMatricula.delete(0, 'end')
        self.espacioMatricula.insert(0, matricula)
        
if __name__ == "__main__":
    cuadro = Tk()
    GeneradorMatriculaInterfaz(cuadro)
    cuadro.mainloop()