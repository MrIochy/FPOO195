from clase import CuentaBanco
from tkinter import Tk, Label, Entry, Button, messagebox

class Interfaz:
    def __init__(self, cuadro):
        self.cuadro = cuadro
        self.cuadro.title("Caja Popular")
        self.cuadro.geometry("800x300")
        self.cuentas = [] 
        self.interfaz()

    def interfaz(self):
        self.ventana = self.cuadro
#_________________________________
        self.label_crear_cuenta = Label(self.ventana, text="Crear cuenta", font='bold')
        self.label_crear_cuenta.grid(row=0, column=0)
        self.label_numero_cuenta = Label(self.ventana, text="Numero de cuenta")
        self.label_numero_cuenta.grid(row=1, column=0)
        self.entry_numero_cuenta = Entry(self.ventana)
        self.entry_numero_cuenta.grid(row=1, column=1)
        self.label_titular = Label(self.ventana, text="Titular")
        self.label_titular.grid(row=2, column=0)
        self.entry_titular = Entry(self.ventana)
        self.entry_titular.grid(row=2, column=1)
        self.label_edad = Label(self.ventana, text="Edad")
        self.label_edad.grid(row=3, column=0)
        self.entry_edad = Entry(self.ventana)
        self.entry_edad.grid(row=3, column=1)
        self.label_saldo = Label(self.ventana, text="Saldo")
        self.label_saldo.grid(row=4, column=0)
        self.entry_saldo = Entry(self.ventana)
        self.entry_saldo.grid(row=4, column=1)
        self.boton_crear_cuenta = Button(self.ventana, text="Crear cuenta", command=self.crear_cuenta)
        self.boton_crear_cuenta.grid(row=5, column=1)
#_________________________________
        self.label_consultar_saldo = Label(self.ventana, text="Consultar saldo", font='bold')
        self.label_consultar_saldo.grid(row=0, column=3)
        self.label_numero_cuenta_consulta = Label(self.ventana, text="Numero de cuenta a consultar")
        self.label_numero_cuenta_consulta.grid(row=1, column=3)
        self.entry_numero_cuenta_consulta = Entry(self.ventana)
        self.entry_numero_cuenta_consulta.grid(row=1, column=4)
        self.boton_consultar_saldo = Button(self.ventana, text="Consultar saldo", command=self.consultar_saldo)
        self.boton_consultar_saldo.grid(row=2, column=4)
#_________________________________

        self.label_ingresar_efectivo = Label(self.ventana, text="Ingresar efectivo", font='bold')
        self.label_ingresar_efectivo.grid(row=0, column=6)
        self.label_numero_cuenta_ingreso = Label(self.ventana, text="Numero de cuenta")
        self.label_numero_cuenta_ingreso.grid(row=1, column=6)
        self.entry_numero_cuenta_ingreso = Entry(self.ventana)
        self.entry_numero_cuenta_ingreso.grid(row=1, column=7)
        self.label_saldo_depositar = Label(self.ventana, text="Saldo a depositar")
        self.label_saldo_depositar.grid(row=2, column=6)
        self.entry_saldo_depositar = Entry(self.ventana)
        self.entry_saldo_depositar.grid(row=2, column=7)
        self.boton_ingresar_efectivo = Button(self.ventana, text="Ingresar efectivo", command=self.ingresar_efectivo)
        self.boton_ingresar_efectivo.grid(row=3, column=7)
#_________________________________
        self.label_retirar_efectivo = Label(self.ventana, text="Retirar efectivo", font='bold')
        self.label_retirar_efectivo.grid(row=5, column=6)
        self.label_numero_cuenta_retiro = Label(self.ventana, text="Numero de cuenta")
        self.label_numero_cuenta_retiro.grid(row=6, column=6)
        self.entry_numero_cuenta_retiro = Entry(self.ventana)
        self.entry_numero_cuenta_retiro.grid(row=6, column=7)
        self.label_saldo_retirar = Label(self.ventana, text="Saldo a retirar")
        self.label_saldo_retirar.grid(row=7, column=6)
        self.entry_saldo_retirar = Entry(self.ventana)
        self.entry_saldo_retirar.grid(row=7, column=7)
        self.boton_retirar_efectivo = Button(self.ventana, text="Retirar efectivo", command=self.retirar_efectivo)
        self.boton_retirar_efectivo.grid(row=8, column=7)
#_________________________________
        self.label_depositar_otra_cuenta = Label(self.ventana, text="Depositar a otra cuenta", font='bold')
        self.label_depositar_otra_cuenta.grid(row=5, column=3)
        self.label_numero_cuenta_origen = Label(self.ventana, text="Numero cuenta origen")
        self.label_numero_cuenta_origen.grid(row=6, column=3)
        self.entry_numero_cuenta_origen = Entry(self.ventana)
        self.entry_numero_cuenta_origen.grid(row=6, column=4)
        self.label_numero_cuenta_destino = Label(self.ventana, text="Numero cuenta destino")
        self.label_numero_cuenta_destino.grid(row=7, column=3)
        self.entry_numero_cuenta_destino = Entry(self.ventana)
        self.entry_numero_cuenta_destino.grid(row=7, column=4)
        self.label_saldo_transferir = Label(self.ventana, text="Saldo a transferir")
        self.label_saldo_transferir.grid(row=8, column=3)
        self.entry_saldo_transferir = Entry(self.ventana)
        self.entry_saldo_transferir.grid(row=8, column=4)
        self.boton_depositar_otra_cuenta = Button(self.ventana, text="Depositar a otra cuenta", command=self.depositar_otra_cuenta)
        self.boton_depositar_otra_cuenta.grid(row=9, column=4)

    def crear_cuenta(self):
        numero = self.entry_numero_cuenta.get()
        titular = self.entry_titular.get()
        edad = self.entry_edad.get()
        saldo = self.entry_saldo.get()
        if numero and titular and edad and saldo:
            cuenta = CuentaBanco(numero, titular, edad, float(saldo))
            self.cuentas.append(cuenta)
            messagebox.showinfo("Cuenta creada", "Se ha creado la cuenta correctamente.")
        else:
            messagebox.showerror("Error", "Por favor completa todos los campos.")

    def consultar_saldo(self):
        numero_cuenta = self.entry_numero_cuenta_consulta.get()
        if numero_cuenta:
            cuenta = self.buscar_cuenta(numero_cuenta)
            if cuenta:
                messagebox.showinfo("Consultar Saldo", f"El saldo de la cuenta {cuenta.numero} es: ${cuenta.saldo}")
            else:
                messagebox.showerror("Error", "Cuenta no encontrada.")
        else:
            messagebox.showerror("Error", "Por favor ingresa el número de cuenta.")

    def ingresar_efectivo(self):
        numero_cuenta = self.entry_numero_cuenta_ingreso.get()
        cantidad = self.entry_saldo_depositar.get()
        if numero_cuenta and cantidad:
            cuenta = self.buscar_cuenta(numero_cuenta)
            if cuenta:
                cuenta.saldo += float(cantidad)
                messagebox.showinfo("Operación Exitosa", f"Se han ingresado ${cantidad} a la cuenta {cuenta.numero}. Nuevo saldo: ${cuenta.saldo}")
            else:
                messagebox.showerror("Error", "Cuenta no encontrada.")
        else:
            messagebox.showerror("Error", "Por favor ingresa el número de cuenta y la cantidad.")

    def retirar_efectivo(self):
        numero_cuenta = self.entry_numero_cuenta_retiro.get()
        cantidad = self.entry_saldo_retirar.get()
        if numero_cuenta and cantidad:
            cuenta = self.buscar_cuenta(numero_cuenta)
            if cuenta:
                if float(cantidad) <= cuenta.saldo:
                    cuenta.saldo -= float(cantidad)
                    messagebox.showinfo("Operación Exitosa", f"Se han retirado ${cantidad} de la cuenta {cuenta.numero}. Nuevo saldo: ${cuenta.saldo}")
                else:
                    messagebox.showerror("Error", "No hay suficiente saldo en la cuenta.")
            else:
                messagebox.showerror("Error", "Cuenta no encontrada.")
        else:
            messagebox.showerror("Error", "Por favor ingresa el número de cuenta y la cantidad.")

    def depositar_otra_cuenta(self):
        numero_origen = self.entry_numero_cuenta_origen.get()
        numero_destino = self.entry_numero_cuenta_destino.get()
        cantidad = self.entry_saldo_transferir.get()
        cuenta_origen = self.buscar_cuenta(numero_origen)
        cuenta_destino = self.buscar_cuenta(numero_destino)
        if cuenta_origen and cuenta_destino and cantidad:
            if float(cantidad) <= cuenta_origen.saldo:
                cuenta_origen.saldo -= float(cantidad)
                cuenta_destino.saldo += float(cantidad)
                messagebox.showinfo("Operación Exitosa", f"Se han transferido ${cantidad} de la cuenta {cuenta_origen.numero} a la cuenta {cuenta_destino.numero}.")
            else:
                messagebox.showerror("Error", "No hay suficiente saldo en la cuenta origen.")
        else:
            messagebox.showerror("Error", "Por favor ingresa los números de cuenta y la cantidad.")

    def buscar_cuenta(self, numero_cuenta):
        for cuenta in self.cuentas:
            if cuenta.numero == numero_cuenta:
                return cuenta
        return None

if __name__ == "__main__":
    cuadro = Tk()
    Interfaz(cuadro)
    cuadro.mainloop()