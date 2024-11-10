def gerar_pa(primeiro, segundo, termos):
    razao = segundo - primeiro 
    pa = [primeiro + i * razao for i in range(termos)]
    return pa

print("Caro usuário, veja a sequência em PA a seguir:")
primeiro = int(input("Informe o primeiro número da PA: "))
segundo = int(input("Agora, informe o segundo número da PA: "))
termos = int(input("Ok, agora informe a quantidade de termos da PA: "))

sequencia_pa = gerar_pa(primeiro, segundo, termos)

print("Com os dados informados, a sequência em PA é:", sequencia_pa)
