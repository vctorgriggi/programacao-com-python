import random

numero_secreto = random.randint(1, 100)

print("Oi! Que tal... brincarmos de adivinhação?")
print("Eu evou pensar em um número entre 1 e 100. Você tem que adivinhar, combinado?")

tentativas = 0

while True:
    try:
        tentativas += 1
        palpite = int(input("Qual é o seu palpite? "))
        
        if palpite < 1 or palpite > 100:
            print("Eita! Por favor, insira um número entre 1 e 100, como eu lhe falei...")
            continue
        if palpite == numero_secreto:
            print("Parabéns! Você acertou em", tentativas, "tentativas. Você é bom nisso! :)")
            break
        elif palpite < numero_secreto:
            print("Humm, o número que eu pensei é maior que o seu palpite.")
        else:
            print("Humm, O número que eu pensei é menor que o seu palpite.")
        
    except ValueError:
        print("Oops! Isso não é um número. Tente novamente.")
        continue