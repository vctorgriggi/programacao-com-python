while True:
    numero = int(input("Caro usuário, digite um número inteiro: "))

    if numero >= 0:
        break 

    print("Oops! Número inválido. Tente novamente.")

print("Show! O número digitado foi:", numero)
