lista = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]

menor = lista[0]
maior = lista[0]
soma = 0

for numero in lista:
    if numero < menor:
        menor = numero

    if numero > maior:
        maior = numero

    soma += numero

media = soma / len(lista)

print("Caro usuário, a lista fornecida é:", lista)
print("Nela, temos alguns números. Por exemplo:")
print("O de menor valor:", menor)
print("O de maior valor:", maior)
print("A soma dos elementos:", soma)
print("E, por fim, a média dos elementos:", media)
