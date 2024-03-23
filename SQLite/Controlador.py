from tkinter import messagebox
import sqlite3
import bcrypt

class Controlador:
    
    def conexion(self):
        try: 
            conex=sqlite3.connect("C:/Users/Luis_/Documents/UPQ/5to Parcial/2. FUNDAMENTOS DE PROGRAMACIÓN ORIENTADA A OBJETOS/FPOO195/SQLite/db195.db")
            print("Conectado")
            return conex
        except sqlite3.OperationalError:
            print("No se pudo Conectar")
            
    def encriptarpass(self, cont):
        passPlana=cont
        passPlana=passPlana.encode()
        sal=bcrypt.gensalt()
        passHash=bcrypt.hashpw(passPlana,sal)
        
        return passHash
        
    def insertUsuario(self, nom, corr, cont):
        
        conexion = self.conexion()
        
        if(nom=="" or corr=="" or cont==""):
            messagebox.showwarning("Advertencia", "Inputs vacios")
            conexion.close()
            
        else:
            cursor = conexion.cursor()
            conH = self.encriptarpass(cont)
            datos=(nom,corr,conH)
            sqlInsert="insert into tbUsuarios(nombre,correo,contra) values(?,?,?)"
            
            cursor.execute(sqlInsert,datos)
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Exito","Datos ingresados correctamente")