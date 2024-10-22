votos1 = 0
votos2 = 0
votos3 = 0

print("Oi! Que tal votarmos em um candidato?")
print("Os candidatos são:")
print("1 - Yuji Itadori")
print("2 - Nobara Kugisaki")
print("3 - Satoru Gojo")

continuar = True

while continuar:
    try:
        voto = int(input("Em quem você quer votar? "))

        if voto == 1:
            votos1 += 1
        elif voto == 2:
            votos2 += 1
        elif voto == 3:
            votos3 += 1
        else:
            print("Voto inválido. Tente novamente.")
            continue

        continuar = input("Deseja continuar votando? (s/n) ").lower()
        if continuar != "s":
            continuar = False

    except ValueError:
        print("Voto inválido. Tente novamente.")
        continue

print("A votação acabou! Aqui estão os resultados:")
print("Yuji Itadori:", votos1, "votos")
print("Nobara Kugisaki:", votos2, "votos")
print("Satoru Gojo:", votos3, "votos")