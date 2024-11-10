def eh_par(numero):
    return numero % 2 == 0

lista = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]

pares = []
impares = []

for numero in lista:
    if eh_par(numero):
        pares.append(numero)

    else:
        impares.append(numero)

print("Caro usuário, a lista de números é:", lista)
print("Dito isto, temos:")
print("Pares:", pares)
print("Ímpares:", impares)