import os
#Solicitar os dados
nome = input("Bem vindo! Qual seu nome?")

print(f"{nome}, vamos calcular seu IMC, irei precisar de alguns dados: ")

altura = float(input("Qual sua altura? "))
peso = float(input("Qual seu peso? "))

os.system('cls')
#Realizar o calculo do IMC
resultado = peso/(altura*altura)

#Calculos das médias
if resultado < 18.4:
    print("Você está abaixo do peso")

if resultado > 18.5 and resultado < 24.9:
    print("Você está no peso ideal")

if resultado >= 25 and resultado <29.9:
    print("Você está acima do peso")

if resultado >= 30 and resultado < 34.9:
    print("Você está no grau obesidade 1")

if resultado > 35:
    print("Você está no grau de obesidade 2")


print(f"{nome}, o resultado do seu IMC é: {resultado:.2f}")

