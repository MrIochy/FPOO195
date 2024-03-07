from tkinter import Tk, Frame, Button, Label, Entry, messagebox
from persona import Persona

class LoginInterfaz:
    def __init__(self, cuadro, persona):
        self.cuadro = cuadro
        self.cuadro.title("Iniciar Sesion")
        self.persona = persona
        self.interfaz()

    def interfaz(self):
        self.labelUsuario = Label(self.cuadro, text="Nombre:")
        self.labelUsuario.grid(row=0, column=0)
        
        self.labelcontraseña = Label(self.cuadro, text="Contraseña:")
        self.labelcontraseña.grid(row=1, column=0)
        
        self.espacioUsuario = Entry(self.cuadro)
        self.espacioUsuario.grid(row=0, column=1)
        
        self.espaciocontraseña = Entry(self.cuadro, show="*")
        self.espaciocontraseña.grid(row=1, column=1)
        
        self.botonvalidar = Button(self.cuadro, text="Iniciar sesión", command=self.validar)
        self.botonvalidar.grid(row=2, column=2)

    def validar(self):
        id = self.espacioUsuario.get()
        contraseña = self.espaciocontraseña.get()
        
        if not id or not contraseña:
            messagebox.showerror("Error", "Campos vacios")
            return
        
        usuario_encontrado = self.persona.buscarUsuarioPorNombre(id)
        if usuario_encontrado and usuario_encontrado['Contraseña'] == contraseña:
            messagebox.showinfo("Bienvenido", "Inicio de sesión exitoso.")
        else:
            messagebox.showerror("Error", "Nombre o contraseña incorrectos.")

def iniciar_sesion(persona):
    interfaz = Tk()
    LoginInterfaz(interfaz, persona)
    interfaz.mainloop()