def cadastro():
    """
    Lê o nome e as notas de um aluno e retorna esses valores.
    """
    nome = input("Caro usuário, entre com o nome do aluno (ou 'FIM' para encerrar): ")

    if nome.upper() == "FIM":
        return None, None, None
    
    nota1 = float(input("Por favor, entre com a nota 1: "))
    nota2 = float(input("Agora, entre com a nota 2: "))
    
    return nome, nota1, nota2

def calculo_media_aluno(nota1, nota2):
    """
    Calcula a média de um aluno com base em suas duas notas.

    Args:
        nota1 (float): Primeira nota do aluno.
        nota2 (float): Segunda nota do aluno.

    Returns:
        float: Média do aluno
    """
    media = (nota1 + nota2) / 2
    return round(media, 1)

def calculo_media_turma(medias):
    """
    Calcula a média geral da turma com base nas médias dos alunos.

    Args:
        medias (list): Lista de médias dos alunos.

    Returns:
        float: Média geral da turma
    """
    if not medias:
        return 0
    
    media_turma = sum(medias) / len(medias)

    return round(media_turma, 1)

medias_turma = []

while True:
    nome, nota1, nota2 = cadastro()
    
    if nome is None:
        break
    
    media_aluno = calculo_media_aluno(nota1, nota2)
    medias_turma.append(media_aluno)
    
    print(f"O aluno {nome} obteve média {media_aluno}")
    if media_aluno >= 6:
        print("Show! Aluno aprovado!")
    else:
        print("Ops! Aluno em prova final...")

media_geral_turma = calculo_media_turma(medias_turma)
print(f"Curiosidade: a média geral da turma foi {media_geral_turma}")
