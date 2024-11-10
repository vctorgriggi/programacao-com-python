lista = [20, 10, 30, 40, 60, 50, 70, 90, 80, 100]

def buscar_elemento(lista, numero):
    for i in range(len(lista)):
        if lista[i] == numero:
            return i
        
    return -1

print("Caro usuário, digite um número inteiro para eu buscar em uma lista.")
numero = int(input("Por favor, digite um número: "))

posicao = buscar_elemento(lista, numero)

if posicao != -1:
    print(f"Show! O número {numero} foi encontrado na posição {posicao}.")

else:
    print(f"Poxa, o número {numero} não foi encontrado na lista.")
