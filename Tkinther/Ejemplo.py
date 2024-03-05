from tkinter import Tk, Frame, Button, messagebox

# metodo para mensaje
def mostrarMensajes():
    print(messagebox.showinfo('showinfo', 'Information'))
    print(messagebox.showerror('showerror', 'Error'))
    print(messagebox.showwarning('showwarning', 'Warning'))
    print(messagebox.askokcancel(message='¿Desea continuar?', title='Soy el titulo'))

# 
def addbtn():
    botonVerde.config(text="+")
    botonRosa = Button(seccion3, text="Nuevo", bg="#fd94ff")
    botonRosa.configure(height=3,width=4)
    botonRosa.pack()

# 1. Creamos la ventana
Ventana = Tk() # Uso de POO creando un Objeto Ventana
Ventana.title("Ejemplo con 3 Frames")
Ventana.geometry("600x400")

# 2. Colocamos Frames de la ventana
seccion1=Frame(Ventana, bg="black")
seccion1.pack(expand=True, fill='both')

seccion2=Frame(Ventana, bg="red")
seccion2.pack(expand=True, fill='both')

# seccion3=Frame(Ventana, bg="#42b1c9")
seccion3=Frame(Ventana, bg="yellow")
seccion3.pack(expand=True, fill='both')

# 3. Posicionar Botones

# place
"""botonAzul = Button(seccion1, text="Azul", fg="#4f42c9")
botonAzul.place(x=160,y=160,width=340,height=40)"""
botonAzul = Button(seccion1, text="Azul", fg="#4f42c9")
botonAzul.place(x=60,y=60,width=100,height=30)

# grid

botonNegro = Button(seccion2, text="Negro", fg="#77ff00", bg="#131321")
botonNegro.configure(height=2,width=10)
botonNegro.grid(row=0, column=1)

botonAmarillo = Button(seccion2, text="amarillo", bg="#fbff00", command=mostrarMensajes)
botonAmarillo.configure(height=2,width=10)
botonAmarillo.grid(row=1, column=2)

# pack

botonVerde = Button(seccion3, text="Verde", bg="#04ccc4", command=addbtn)
botonVerde.configure(height=2,width=10)
botonVerde.pack()

# Ejecuta la ventana
Ventana.mainloop()