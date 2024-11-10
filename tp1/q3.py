def juntar_nomes(nome1, nome2):
    metade1 = nome1[:len(nome1)//2]
    metade2 = nome2[len(nome2)//2:]

    return metade1 + metade2

print("Oi! Vamos fazer algumas... operações de combinação?")
nome1 = input("Por favor, digite o primeiro nome: ")
nome2 = input("Agora, digite o segundo nome: ")

nome_combinado = juntar_nomes(nome1, nome2)

print(f"Show! O nome combinado é... {nome_combinado}!")