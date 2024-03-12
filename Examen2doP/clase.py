"""
Crea un programa con interfaz y su clase en archivos propios que solicite 
nombre
apellido paterno
apellido materno
año de nacimiento 
carrera
Con los datos solicitados la interfaz debe generar una matricula con las siguientes caracteristicas
2 digitos del año en curso
2 digitos del año de nacimiento 
primera letra del nombre
2 letras de cada apellido
2 digitos aleatorios
3 primeras letras de la carrera

PRIMER LETRA DEL NOMBRE + 2 LETRAS APELLIDO PATERNO + 2 LETRAS APELLIDO MATERNO + 2 DIGITOS DEL AÑO DE NACIMIENTO + ...
... + 2 DIGITOS DEL  AÑO CURSO + 3 PRIMERAS LETRAS DE LA CARRERA +  2 NUMEROS RANDOM

--Mostrar todo esto en un mesasagebox--
"""
import random
from tkinter import messagebox

class GenerarMatricula:
    def generar_matricula(self, añocurso, añonac, nombre, apep, apem, carrera):
        matricula = nombre + apep + apem + añonac + añocurso + carrera + random.
        
        messagebox.showinfo("Matricula generada", f"La matricula generada es:\n{matricula}")
        return matricula
        
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
    
    
import random
from tkinter import messagebox