#3. Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.
numerobinario=int(input("Digite un numero para transformar a binario: "))
numerodecimal=int(input("Digite un numero para transformar a decimal: "))

def binariodecimal(numero):
    numero = list(str(numero))
    numero.reverse()
    decimal = 0
    for i in range (len(numero)):
        decimal += int(numero[i]) *2 **i
    return decimal

def decimalbinario(numero):
    binario =[]
    while numero > 0:
        binario.append(str(numero%2))
        numero//=2
    binario.reverse()
    return "".join(binario)

print(f"{numerobinario} en decimal: {decimalbinario(numerobinario)}")
print(f"{numerodecimal} en binario: {binariodecimal(numerodecimal)}")