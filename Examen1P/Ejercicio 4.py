"""
Programa que solicite una palabra y que la descomponga en letras, ejemplo: IVAN
Resultado: Letra 1: I Letra 2: V Letra 3: A Letra 4: N
"""

print("Bienvenido al programa que descompone una palabra en letras")
palabra=str(input("Por favor escriba la palabra que quiere descomponer\n"))
palabramay=palabra.upper()
for i, letra in enumerate(palabramay, 1):
    print("Letra", i, ":", letra)