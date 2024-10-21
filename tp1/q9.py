def calculo_desconto(valor_compra):
    if valor_compra > 500:
        desconto = 0.25
    elif valor_compra > 200:
        desconto = 0.15
    elif valor_compra > 100:
        desconto = 0.10
    else:
        desconto = 0.0

    valor_desconto = valor_compra * desconto
    valor_final = valor_compra - valor_desconto
    return valor_desconto, valor_final

print("Olá! Que tal fazermos umas comprinhas?")
valor_compra = float(input("Quanto você gastou? "))

valor_desconto, valor_final = calculo_desconto(valor_compra)

print(f"Com base no valor da sua compra, você ganhou um desconto de R${valor_desconto:.2f}!")
print(f"Então... O valor final da sua compra é R${valor_final:.2f}. :)")