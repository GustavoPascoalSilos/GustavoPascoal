import os
continuar = "s"
contador = 0

nomes = [] # Cria uma lista vazia
salarios = [] # Cria uma lista vazia
continuar = "s"
while continuar == "s":
    nome = input("Insira o nome do funcionario: ")
    nomes.append(nome) # Adiciona o nome na lista de nomes
    salario = float (input("Insira o salário: "))
    salarios.append(salario) # Adiciona o salario na lista de salarios
    continuar = input("Inserir outro?? s/n")
os.system('cls')

somasalarios = 0
mediasalario = 0
maiorsalario = 0
menorsalario = 0
totalsalarios = 0

#Calculo media de salarios
for salario in salarios:
    somasalarios += salario


# len() é uma função que retorna o tamanho de uma lista
for i in range(len(nomes)):
    print(f"{i + 1} Funcionário - {nomes[i]}, Salário - {salarios[i]}")
 
 
print(f"A média dos salários da empresa é {somasalarios/len(nomes):.2f}")


