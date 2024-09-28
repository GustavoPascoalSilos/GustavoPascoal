# multiplicador = int(input("Olá, qual tabuada você deseja imprimir?"))
# numero = 0
# while numero <= 10:
#     print(f"{multiplicador} x {numero} = {numero*multiplicador}")
#     numero += 1


resposta = "Sim"
while resposta == "Sim":
    multiplicador = int(input("Olá, qual tabuada você deseja imprimir?"))
    numero = 0

    while numero <= 10:
        print(f"{multiplicador} x {numero} = {numero*multiplicador}")
        numero += 1
        resposta = ""

    resposta = input("Deseja Continuar? Sim/Não")   
        