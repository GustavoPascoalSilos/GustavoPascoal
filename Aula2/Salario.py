#Peça ao usuário para inserir seu salário e o tempo de serviço.
nome = input ("Seja bem vindo, qual seu nome?")
print("Vamos calcular seu bônus de tempo de serviço?")
salario = float(input("Insira seu salário: "))
tempoServico = int(input("Insira seu tempo de serviço em anos: "))

if tempoServico >= 5 :
    bonus = salario * 0.05 + salario
    print(f"{nome}, seu salário com o valor do bonus é de {bonus:.2f}")
else:
    print("Você não possui bonus :( ")