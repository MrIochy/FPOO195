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
    def generar_matricula(self, nombre, apep, apem, fecnac, carrera):
        año_actual = str(2024)[-2:]  
        año_nacimiento = str(fecnac)[-2:]  
        nombre_abreviado = nombre[0].upper()
        apep_abreviado = apep[:2].upper()
        apem_abreviado = apem[:2].upper()
        numeros_aleatorios = ''.join(random.choices('0123456789', k=2))
        carrera_abreviada = carrera[:3].upper()
        matricula = (nombre_abreviado + apep_abreviado + apem_abreviado + año_nacimiento + año_actual + carrera_abreviada + numeros_aleatorios)
        messagebox.showinfo("Matrícula generada", f"La matrícula generada es:\n{matricula}")
        return matricula