"""
Crea un programa que pregunte al usuario por el número de horas trabajadas y el
coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
"""
pregunta1= float(input("¿Cuantas horas trabajaste? \n"))
pregunta2= float(input("¿Cuanto te pagan por hora? \n"))
resultado= pregunta1 * pregunta2
print("Tu pago corresponde a ", resultado, " pesos")