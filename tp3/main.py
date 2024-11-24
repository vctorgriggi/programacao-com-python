from datetime import datetime

print("Oi, usuário(a)! Bem vindo ao TP3. xD")

#%% Exercício 1
def concatenar_nome_sobrenome():
    nome = input("Digite com o nome: ").strip()
    sobrenome = input("Agora, digite com o sobrenome: ").strip()
    print(f"{nome} {sobrenome}")

#%% Exercício 2
def validar_nome_sobrenome():
    while True:
        entrada = input("Informe seu nome e sobrenome: ").strip()

        partes = entrada.split()

        if len(partes) >= 2 and all(len(parte) >= 2 for parte in partes):
            return partes
        else:
            print("Oops! O nome e sobrenome devem ter pelo menos 2 caracteres. Tente novamente.")

#%% Exercício 3 - Obs: Aqui, optei por utilizar o método de validação do exercício 2
def exibir_sobrenome_nome(partes):
    nome = partes[0]
    sobrenome = " ".join(partes[1:])
    print(f"{sobrenome.upper()}, {nome}")

#%% Exercício 4
def data_em_inteiros():
    data = input("Informe uma data no formato dd/mm/aaaa: ").strip()

    try:
        dia, mes, ano = map(int, data.split("/"))
        print(f"Dia: {dia}, Mês: {mes}, Ano: {ano}")
    except ValueError:
        print("Oops! A data deve estar no formato dd/mm/aaaa e conter apenas números.")

#%% Exercício 5
def validar_data():
    data = input("Informe uma data no formato dd/mm/aaaa: ").strip()

    try:
        datetime.strptime(data, "%d/%m/%Y")
        print("Show, data válida!")
    except ValueError:
        print("Eita! Data inválida. Tente novamente.")

#%% Exercício 6
def data_em_texto():
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]

    data = input("Informe uma data no formato dd/mm/aaaa: ").strip()

    try:
        dia, mes, ano = map(int, data.split("/"))

        if 1 <= mes <= 12:
            nome_mes = meses[mes - 1]
            print(f"{dia:02d} de {nome_mes} de {ano}")
        else:
            print("Oops! Mês inválido. Tente novamente.")

    except ValueError:
        print("Oops! A data deve estar no formato dd/mm/aaaa e conter apenas números.")

#%% Exercício 7
def verificar_palindromo():
    palavra = input("Informe uma uma palavra: ").strip().lower()

    if palavra == palavra[::-1]:
        print(f"Você descobriu um palíndromo! '{palavra}' é um palíndromo.")
    else:
        print(f"Hummm... '{palavra}' não é um palíndromo. Tente novamente.")

#%% Exercício 8
def contar_vogais():
    frase = input("Informe uma uma frase: ").strip().lower()

    vogais = "aeiou"

    total = sum(1 for letra in frase if letra in vogais)

    print(f"Você sabia que a frase possui {total} vogais?")

#%% Exercício 9
def formatar_numero_telefone():
    while True:
        telefone = input("Informe seu número de telefone (somente números), por favor? ").strip()

        if telefone.isdigit() and len(telefone) == 11:
            print(f"Show! Formatei seu número. Veja: ({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}")
            break
        else:
            print("Oops! O número de telefone deve conter 11 dígitos. Tente novamente.")

#%% Exercício 10
def dia_da_semana():
    while True:
        try:
            numero = int(input("Informe um número entre 1 e 7: ").strip())

            dias = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", 
                    "Quinta-feira", "Sexta-feira", "Sábado"]
            
            if 1 <= numero <= 7:
                print(f"Show! O dia da semana correspondente ao número {numero} é {dias[numero - 1]}.")
                break
            else:
                print("Oops! O número deve estar entre 1 e 7. Tente novamente.")
        except ValueError:
            print("Eita! Parece que você digitou algo errado... Tente novamente.")

#%% Exercício 11
def formatar_cpf():
    while True:
        cpf = input("Informe seu número de CPF (somente números), por favor? ").strip()

        if cpf.isdigit() and len(cpf) == 11:
            print(f"Show! Formatei seu CPF. Veja: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")
            break
        else:
            print("Oops! O CPF deve conter 11 dígitos. Tente novamente.")

#%% Exercício 12
def inverter_frase_com_for():
    frase = input("Informe uma frase! Seja criativo.: ").strip()

    invertida = ""

    for i in range(len(frase) - 1, -1, -1):
        invertida += frase[i]

    print(f"Inverti a frase para você: {invertida}")

#%% Exercício 13
def inverter_frase_com_slicing():
    frase = input("Informe uma frase! Seja criativo.: ").strip()
    print(f"Inverti a frase para você: {frase[::-1]}")

#%% Exercício 14
def cinco_primeiros_ultimos():
    frase = input("Informe uma frase! Seja criativo.: ").strip()

    cinco_primeiros = frase[:5]
    cinco_ultimos = frase[-5:]

    print(f"Bacana! A título de curiosidade, os cinco primeiros caracteres são: {cinco_primeiros}")
    print(f"E os cinco últimos são: {cinco_ultimos}")

#%% Exercício 15
def substituir_ponto_virgula():
    entrada = "1;Maria;1000".strip()
    saida = entrada.replace(";", ",")
    print(f"Hummm... Me deram a frase '{entrada}' e eu substituí o ';' por ',': '{saida}'")

#%% Exercício 16
def calculo_media():
    try:
        num1 = float(input("Informe o primeiro número: ").strip())
        num2 = float(input("Informe o segundo número: ").strip())

        media = (num1 + num2) / 2

        print(f"Você sabia que a média entre {num1} e {num2} é {media:.2f}?")
    except ValueError:
        print("Eita! Parece que você digitou algo errado... Tente novamente.")

#%% Menu
def menu():
    opcoes = {
        1: ("Concatenar Nome e Sobrenome", concatenar_nome_sobrenome),
        2: ("Validação de Nome e Sobrenome com Split", validar_nome_sobrenome),
        3: ("Exibir Sobrenome, Nome", lambda: exibir_sobrenome_nome(validar_nome_sobrenome())),
        4: ("Data em Formato Inteiro", data_em_inteiros),
        5: ("Validação de Data", validar_data),
        6: ("Formato 'dia de mês de ano'", data_em_texto),
        7: ("Verificar Palíndromo", verificar_palindromo),
        8: ("Contagem de Vogais", contar_vogais),
        9: ("Formatar Número de Telefone", formatar_numero_telefone),
        10: ("Dia da Semana", dia_da_semana),
        11: ("Formatar CPF", formatar_cpf),
        12: ("Inverter Frase com For", inverter_frase_com_for),
        13: ("Inverter Frase com Slicing", inverter_frase_com_slicing),
        14: ("Cinco Primeiros e Últimos Caracteres", cinco_primeiros_ultimos),
        15: ("Substituir ';' por ','", substituir_ponto_virgula),
        16: ("Cálculo de Média com f-strings", calculo_media),
    }

    while True:
        print("\nPor favor, escolha uma questão para visualizar!")
        for num, (descricao, _) in opcoes.items():
            print(f"{num} - {descricao}")
        print("0 - Sair")

        try:
            escolha = int(input("\nDigite o número correspondente à opção desejada: ").strip())
            if escolha == 0:
                print("Até mais! :)")
                break

            elif escolha in opcoes:
                opcoes[escolha][1]()

            else:
                print("Oops! Opção inválida. Tente novamente.")

        except ValueError:
            print("Eita! Parece que você digitou algo errado... Tente novamente.")

#%%
if __name__ == "__main__":
    menu()
