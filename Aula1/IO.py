nome = input("Digite o seu nome: ")
idade = input("Digite sua idade: ")
altura = input("Digite sua altura: ")

print("Olá,", nome, "você tem", idade, "anos de idade"," e sua altura é", altura)

#O sinal de mais + não adiciona espaç entre as palavras
print("Olá," + nome + "!")

#O sinal de vírgula , adiciona espaço entre as palavras
print("Olá,",nome + "!")

#O sinal de porcentagem % é uma forma antiga de formatar strings
print("Olá, %s!" % nome)

#O método format() é uma forma mais morderna de formatar strings
print("Olá, {}!".format(nome))

#O f-string é a forma mais morderna de formatar strings
print(f"Olá,{nome}!")





