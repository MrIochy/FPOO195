"""
Se requiere un programa para la administración de cuenta en caja popular, con el
programa podremos consultar saldo, ingresar efectivo, retirar efectivo y depositar a otra
cuenta, cada cuenta tiene registrados los siguientes datos: No. Cuenta, titular, edad y
saldo
"""

class CuentaBanco:
    def __init__(self, numero, titular, edad, saldo):
        self.numero = numero
        self.titular = titular
        self.edad = edad
        self.saldo = saldo