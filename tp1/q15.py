def inicio():
    print("Caro Sr(a). Você é Frieren, uma maga lendária que sobreviveu à uma jornada épica com o herói Himmel.")
    print("Atualmente, após longos anos, você explora o mundo em busca de conhecimento e aventuras.")
    print("Você está andando pelo mundo, quando de repente, você encontra uma masmorra antiga.... O que você deseja fazer?")
    print("1 - Entrar na masmorra.")
    print("2 - Ignorar e ir comer uma torta numa cidade próxima.")
    
    escolha = input("Digite o número correspondente à sua escolha: ")
    
    if escolha == "1":
        entrar_masmorra()
    elif escolha == "2":
        comer_torta()
    else:
        print("Escolha inválida. Tente novamente.")
        inicio()

def entrar_masmorra():
    print("\nVocê entra na masmorra e, percebe que ela é mais escura do que você imaginava.")
    print("Logo à frente, você vê um grande baú de tesouro. O que você deseja fazer?")
    print("1 - Abrir o baú e pegar o tesouro!")
    print("2 - Ficar desconfiada... quem deixa um baú assim no meio de uma masmorra?")
    
    escolha = input("Digite o número correspondente à sua escolha: ")
    
    if escolha == "1":
        abrir_bau()
    elif escolha == "2":
        desconfiar_bau()
    else:
        print("Escolha inválida. Tente novamente.")
        entrar_masmorra()

def abrir_bau():
    print("\nVocê abre o baú... É um mímico! Ele tenta te morder! E agora?")
    print("1 - Usar magia de fogo e queimar esse baú falso.")
    print("2 - Chutar o Mimic e correr para longe.")
    
    escolha = input("Digite o número correspondente à sua escolha: ")
    
    if escolha == "1":
        magia_fogo()
    elif escolha == "2":
        chutar_e_correr()
    else:
        print("Escolha inválida. Tente novamente.")
        abrir_bau()

def desconfiar_bau():
    print("\nVocê olha bem para o baú. Algo está errado...")
    print("Você lança uma pequena magia, e o baú ganha dentes! É um mímico!")
    print("1 - Derrotar o mímico com um feitiço rápido.")
    print("2 - Sair da masmorra rindo e se perguntando quem ainda cai nessas armadilhas.")
    
    escolha = input("Digite o número correspondente à sua escolha: ")
    
    if escolha == "1":
        derrotar_mimico()
    elif escolha == "2":
        fugir_rindo()
    else:
        print("Escolha inválida. Tente novamente.")
        desconfiar_bau()

def magia_fogo():
    print("\nVocê lança uma magia! O mímico pega fogo e começa a desaparecer...")
    print("BVocê fica olhando fixamente para ele. Enfim, ele vira cinzas.")
    print("Fim da história. Hora de pegar o tesouro de verdade (se sobrou algo).")

def chutar_e_correr():
    print("\nVocê chuta o mímico com toda a sua força e sai correndo.")
    print("Você sobrevive, mas o tesouro ficou para trás.")
    print("Fim da história. Pelo menos você não foi mordida!")

def derrotar_mimico():
    print("\nCom um feitiço rápido e sem muito esforço, você derrota o mímico.")
    print("Ser uma maga lendária tem suas vantagens, afinal. O tesouro agora é seu.")
    print("Fim da história. Tesouro garantido, sem drama.")

def fugir_rindo():
    print("\nVocê sai da masmorra rindo, imaginando quantas pessoas já tentaram pegar aquele baú.")
    print("Afinal, você não precisa de tesouro. O verdadeiro tesouro são as memórias que fazemos pelo caminho (e as tortas).")
    print("Fim da história. A vida é muito curta para se preocupar com mímicos!")

def comer_torta():
    print("\nVocê decide que masmorras são chatas e vai para a cidade.")
    print("Lá, você encontra uma confeitaria e come a melhor torta de maçã da sua vida.")
    print("Fim da história. Afinal, quem precisa de tesouro quando se tem torta?")

inicio()