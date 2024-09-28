numeros = []
contador = 1

while contador != 0:
   numero = float (input(f"Digite o {contador}- numero: "))
   numeros.append(numero)
   contador += 1

  
if numero == 0:
    resposta = input("Deseja ordenar em ordem Crescente ou Decrescente? C/D ")
    if resposta == "C":
        
        for i in range(len(numeros)):
           print(numeros[i])
           break

 