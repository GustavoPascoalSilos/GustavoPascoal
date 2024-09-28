import os
print("Olá, vamos fazer a conversão de graus Celsius para Fahrenheit.")
nome = input("Qual seu nome? ")

temperatura = float(input("Qual temperatura em graus Celsius?"))
#Calculando a conversão
Fahrenheit = 1.8 * temperatura + 32

print(f"{nome}, a sua conversão de {temperatura} graus Celsius para Fahrenheit é de {Fahrenheit:.2f} ")

#os.system('cls')

print("Olá, vamos fazer o cálculo da area de um circulo utilizando o tamanho do raio.")
nome = input("Qual seu nome? ")

raio = float(input("Qual o tamanho do raio do circulo?"))
#Calculando area do circulo
areacirculo = 3.14 * raio**2

print(f"{nome}, a area do circulo de acordo com o seu raio é de {areacirculo:.2f} ")