def classificar_palavras(palavras):
    curtas = []
    longas = []

    for palavra in palavras:
        if len(palavra) < 5:
            curtas.append(palavra)
        else:
            longas.append(palavra)

    return curtas, longas

print("Oi! Vamos classificar algumas palavras?")
palavras = input("Vamos lá, digite um texto. Pode ser uma poesia! ").split()

curtas, longas = classificar_palavras(palavras)

print("Show! As palavras curtas são:", curtas)
print("E as palavras longas são:", longas)