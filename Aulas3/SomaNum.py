numeros = []
contador = 0

while contador <5:
   numero = float (input(f"Digite o {contador +1} numero: "))
   numeros.append(numero)
   contador += 1

somadosnumeros = 0
for numero in numeros:
    somadosnumeros += numero

print(f"A soma dos numeros é: {somadosnumeros:.2f}")
