from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador import *

objControlador= Controlador()

def ejecutaInsert():
    objControlador.insertUsuario(var1.get(),var2.get(),var3.get())
    
def BusUsuario():
    usuarioBD = objControlador.BuscarUsuario(varBus.get())
    if usuarioBD == []:
        messagebox.showwarning("Inexistente", "Id no existe en la base de datos")
    else:
        consulta.delete(1.0, END)
        consulta.insert(END, usuarioBD)
def mostrarBaseDatos():
    usuarios = objControlador.obtenerUsuarios()
    for i in tabla.get_children():
        tabla.delete(i)
    for datos in usuarios:
        tabla.insert("", "end", values=(datos[0], datos[1], datos[2], datos[3]))

# 1. Crear la ventana
Ventana= Tk()
Ventana.title("CRUD de Usuarios")
Ventana.geometry("500x300")

# 2. Preparar el notebook para pestañas
panel = ttk.Notebook(Ventana)
panel.pack(fill='both', expand="yes")

# 3. Definir las pestañas del notebook
pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)

# 4. Agregamos las pestañas
panel.add(pestana1, text="Crear Usuario")
panel.add(pestana2, text="Buscar Usuario")
panel.add(pestana3, text="Consultar Usuarios")
panel.add(pestana4, text="Editar Usuario")
panel.add(pestana5, text="Borrar Usuario")

# 5. Pestaña 1: Formulario de Insert
Label(pestana1, text="Registro de Usuarios", fg="blue", font=("Lato", 18)).pack()

var1= tk.StringVar()
Label(pestana1, text="Nombre: ").pack()
Entry(pestana1, textvariable=var1).pack()

var2= tk.StringVar()
Label(pestana1, text="Correo: ").pack()
Entry(pestana1, textvariable=var2).pack()

var3= tk.StringVar()
Label(pestana1, text="Contraseña: ").pack()
Entry(pestana1, textvariable=var3).pack()

Button(pestana1, text="Guardar usuario", command=ejecutaInsert).pack()

# 6. Pestaña 2: Buscar Usuario

Label(pestana2, text="Buscar Usuario", fg="red", font=("Mono",18)).pack()

varBus=tk.StringVar()
Label(pestana2, text="Id: ").pack()
Entry(pestana2, textvariable=varBus).pack()

Button(pestana2, text="Buscar usuario", command=BusUsuario).pack()

Label(pestana2, text="Registrado:", fg="blue", font=("Mono",16)).pack()
consulta = tk.Text(pestana2, height=5, width=52)
consulta.pack()

# 7. Pestaña 3: Consultar Usuarios
Label(pestana3, text="Consultar Usuarios", fg="green", font=("Lato", 18)).pack()

tabla = ttk.Treeview(pestana3, columns=("ID", "Nombre", "Correo", "Contraseña"), show="headings")
tabla.column("ID", width=40, anchor=CENTER)
tabla.column("Nombre", width=80)
tabla.column("Correo", width=160)
tabla.column("Contraseña", width=140)

tabla.heading("ID", text="ID")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Correo", text="Correo")
tabla.heading("Contraseña", text="Contraseña")
tabla.pack()

Button(pestana3, text="Mostrar Base de Datos", command=mostrarBaseDatos, font=("Mono", 8)).pack()

Ventana.mainloop()