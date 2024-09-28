import os
numeros = []
contador = 0
#solicitar numeros
while contador <5:
   numero = float (input(f"Digite o {contador +1} numero: "))
   numeros.append(numero)
   contador += 1
#calculo da soma dos numeros
os.system('cls')
somadosnumeros = 0
for numero in numeros:
    somadosnumeros += numero

print(f"A soma dos numeros é: {somadosnumeros:.2f}")
