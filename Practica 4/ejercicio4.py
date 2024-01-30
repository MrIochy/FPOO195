"""
Codifica un programa que solicite una cadena de caracteres e imprima como
resultado si la cadena es palíndromo o no
"""
palabra= str(input("Escribe tu frase o palabra para demosotrar si es un PALINDROMO \n"))
palindromo= palabra.upper()

if palindromo == palindromo[::-1]:
    print(palabra, " es un palindromo")
else:
    print(palabra, " NO es un palindromo")