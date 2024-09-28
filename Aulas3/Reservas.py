continuar = "s"
contador = 0

nomes = [] # Cria uma lista vazia
destinos = [] # Cria uma lista vazia
continuar = "s"
while continuar == "s":
    nome = input("Insira o nome do passageiro: ")
    nomes.append(nome) # Adiciona o nome na lista de nomes
    destino = input("Insira o destino: ")
    destinos.append(destino) # Adiciona o destino na lista de destinos
    continuar = input("Deseja continuar? s/n")


# len() é uma função que retorna o tamanho de uma lista
for i in range(len(nomes)):
    print(f"{i + 1} Reserva - {nomes[i]}, Destino - {destinos[i]}")

