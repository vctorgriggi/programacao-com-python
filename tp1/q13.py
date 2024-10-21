import string

def considerada_palindromo(frase):
    texto_tratado = frase.replace(" ", "").lower()
    texto_tratado = texto_tratado.translate(str.maketrans('', '', string.punctuation))
    return texto_tratado == texto_tratado[::-1]

print("Oi! Vamos verificar se uma frase é um palíndromo?")
frase = input("Digite uma frase ou um texto! Escreva algo bonito. :) ")

if considerada_palindromo(frase):
    print("Show! A frase que você digitou é um palíndromo.")
else:
    print("A frase que você digitou não é um palíndromo.")