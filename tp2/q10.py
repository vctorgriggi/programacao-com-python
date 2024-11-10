print("Caro usuário, digite uma lista de números inteiros. Quando terminar, digite 0 para finalizar.")

def ler_lista():
    lista = []

    while True:
        numero = int(input("Por favor, digite um número: "))

        if numero == 0:
            break

        lista.append(numero)

    return lista

def maiores_ou_iguais_a_media(lista):
    if len(lista) == 0:
        print("Ooops! A lista está vazia.")
        return

    media = sum(lista) / len(lista)
    
    print(f"Com base nos números fornecidos, a média é {media}.")
    print("E os números maiores ou iguais à média são:")

    for numero in lista:
        if numero >= media:
            print(numero)

lista_numeros = ler_lista()
maiores_ou_iguais_a_media(lista_numeros)
