#A vista – 10% de desconto, caso o valor da venda seja maior que 500 15%, caso seja maior que 1000, 20% de desconto;
print("Bem vindo a SummerVeron")
nome = input("Qual seu nome? ")


#Perguntar ao usuário se as compras são a vista ou a prazo
print("Pagamentos a vista possuem descontos de acordo com o valor da compra!")
valorCompra = float(input(f"{nome}, qual valor das suas compras? "))
formaPagamento = int(input("Qual a forma de pagamento 1-Vista 2-Prazo"))
numeroParcelas = int(input("Qual numero de parcelas? "))

#pagamento a vista
#verificar valor da compra
if valorCompra < 500 and formaPagamento == 1:
    valorcomDesconto = valorCompra - (valorCompra * 0.10)
    print(f"{nome}, o valor total da sua compra é {valorcomDesconto:.2f}, com o desconto")
elif valorCompra <1000 and formaPagamento == 1:
    valorcomDesconto = valorCompra - (valorCompra * 0.15)
    print(f"{nome}, o valor total da sua compra é {valorcomDesconto:.2f}, com desconto")
elif valorCompra > 1000 and formaPagamento == 1:
    valorcomDesconto = valorCompra - (valorCompra * 0.20)
    print(f"{nome}, o valor total da sua compra é {valorcomDesconto:.2f}, com desconto")

#pagamento parcelado
if valorCompra < 800  and numeroParcelas > 5 and formaPagamento == 2:
    print("Número de parcelas inválidas!")
elif numeroParcelas > 18:
    print("Número de parcelas inválidas!")
elif numeroParcelas <= 10:
    valorParcelado = valorCompra/numeroParcelas
    print(f"Suas compra ficou o total de {valorCompra}, dividido {numeroParcelas} parcelas de R${valorParcelado:.2f}")
elif numeroParcelas == 11:
    juros = valorCompra * 0.05
elif numeroParcelas == 12:
    juros = valorCompra * 0.065
elif numeroParcelas == 13:
    juros = valorCompra * 0.07
elif numeroParcelas == 14:
    juros = valorCompra * 0.09
elif numeroParcelas == 15:
    juros = valorCompra * 0.095
elif numeroParcelas == 16:
    juros = valorCompra * 0.10
elif numeroParcelas == 17:
    juros = valorCompra * 0.113
elif numeroParcelas == 18:
    juros = valorCompra * 0.12
else:
    print("Numero parcelas inválidas!")

print(f"Suas compra ficou o total de {valorCompra}, dividido {numeroParcelas} parcelas de {valorCompra/numeroParcelas+juros:.2f}")
