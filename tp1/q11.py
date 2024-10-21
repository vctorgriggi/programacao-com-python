import random

def lancar_dados(numero_de_dados):
    resultados = []
    
    for _ in range(numero_de_dados):
        resultado = random.randint(1, 6)
        resultados.append(resultado)
    return resultados

print("Oi! Que tal lançarmos alguns dados?")
numero_de_dados = int(input("Quantos dados você quer lançar? "))

resultados = lancar_dados(numero_de_dados)

print("Show! Os resultados dos seus lançamentos foram:", resultados)
