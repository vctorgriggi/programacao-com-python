lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [10, 20, 30, 40, 50, 60, 70, 80]

soma_listas = []

for i in range(len(lista1)):
    soma = lista1[i] + lista2[i]
    soma_listas.append(soma)

print("Caro usuário, a primeira lista é:", lista1)
print("A segunda lista é:", lista2)
print("Agora, a soma das listas é:", soma_listas)
