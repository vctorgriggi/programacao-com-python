def calculo_fatorial(n):
    fatorial = 1

    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

while True:
    print("Caro usuário, digite um número inteiro positivo (ou 0 para sair).")
    numero = int(input("Digite um número: "))

    if numero == 0:
        print("Encerrando! Até mais!")
        break

    if numero > 0:
        resultado = calculo_fatorial(numero)
        print(f"Fatorial de {numero}: {resultado}")

    else:
        print("Oops! Por favor, insira um número inteiro positivo.")
