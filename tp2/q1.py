vogais = 'aeiouAEIOU'
qtde_vogais = 0

while True:
    print("Caro usuário, digite um caractere ou '.' para sair.")
    caractere = input("Digite um caractere: ")

    if caractere == '.':
        break

    if caractere in vogais:
        qtde_vogais += 1

print("Ok! O número de vogais é igual a:", qtde_vogais)