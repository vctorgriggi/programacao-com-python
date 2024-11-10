print("Caro usuário, digite uma lista de números inteiros. Quando terminar, digite 0 para finalizar.")

def ler_lista():
    lista = []

    while True:
        numero = int(input("Por favor, digite um número: "))
        
        if numero == 0:
            break

        lista.append(numero)

    return lista

def exibir_invertido(lista):
    print("Show! Agora, a lista de trás para frente é:")
    
    for i in range(len(lista) - 1, -1, -1):
        print(lista[i])

lista_numeros = ler_lista()
exibir_invertido(lista_numeros)
