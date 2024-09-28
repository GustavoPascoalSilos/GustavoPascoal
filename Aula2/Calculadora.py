print("Olá, bem vindo ao Calculator!")
print("Preciso que digite 2 números, e escolha a operação matemática")
print("As operações são +, -, /, * ")

#Solicitar 2 numeros
numeroUm = float(input("Qual primeiro número? "))
numeroDois = float(input("Qual segundo número? "))
operador = input("Qual operação voce deseja? + ou - ou / ou * ")

resultado = 0

#Calculo das operacões
if operador == "+":
    resultado = numeroUm + numeroDois
elif operador == "-":
    resultado = numeroUm - numeroDois
elif operador == "/":
    if numeroDois == 0:
        print("Não é possivel dividir por zero ")
    else: resultado = numeroUm / numeroDois
if operador == "*":
    resultado = numeroUm * numeroDois

print(f"O resultado da sua operação é {resultado:.2f}")