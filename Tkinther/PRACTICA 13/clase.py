"""
Crea una interfaz gráfica que genere password automáticos, solicitara al  usuario la longitud (8 caracteres por default), si quiere incluir Mayúsculas o 
Caracteres especiales, dentro de las opciones que tendrá agregar una para comprobar fortaleza del password esta interfaz debe incluir los siguientes 
requerimientos 
1. Crea un diagrama de clases para la solución antes de comenzar a programar
2. Debe estar programado usando tus Clases y objetos propios junto con los de Tkinter, Encapsular lo necesario
3. La contraseña generada debe estar mostrada en un MessageBox y también disponible en un Entry para copiar y pegar
4. Cuidar el diseño de la interfaz
"""
import random
import string
from tkinter import messagebox

class GeneradorContraseña:
    def generar_contraseña(self, longitud=8, incluir_mayusculas=False, incluir_especiales=False):
        caracteres = string.ascii_lowercase
        if incluir_mayusculas:
            caracteres += string.ascii_uppercase
        if incluir_especiales:
            caracteres += string.punctuation
        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
        messagebox.showinfo("Contraseña generada", f"La contraseña generada es:\n{contraseña}")
        return contraseña

    def comprobar_fortaleza(self, contraseña):
        if len(contraseña) < 1:
            return "No hay ninguna contraseña."
        if len(contraseña) <= 4:
            return "La contraseña es debil."
        if len(contraseña) <= 8:
            return "La contraseña es moderada."
        else:
            return "La contraseña es FUERTE."