lista = [10, 20, 30, 40, 50, 60, 70, 80]

print("Caro usuário, a lista original é:", lista)
print("Agora, a lista de trás para frente é:")

for i in range(len(lista) - 1, -1, -1):
    print(lista[i])
