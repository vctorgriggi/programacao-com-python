import random

personagens = ["Yuji Itadori", "Megumi Fushiguro", "Nobara Kugisaki", "Satoru Gojo", "Ryomen Sukuna"]
locais = ["o colégio de Jujutsu", "um cemitério", "uma escola", "uma floresta assombrada", "um templo antigo", "a casa da vovó"]
acoes = ["lutou", "usou uma técnica especial", "fugiu", "fez uma piada", "protegeu um amigo", "cansou e sentou para descansar no meio da batalha"]

personagem = random.choice(personagens)
local = random.choice(locais)
acao = random.choice(acoes)

print(f"Em um belo dia, {personagem} estava em {local} e {acao}.")