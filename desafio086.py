alunos = {}

while True:
    nome = input("Nome do aluno (ou 'sair' para finalizar): ").strip()
    if nome.lower() == 'sair':
        break

    media = float(input(f"Média de {nome}: "))

    if media >= 7:
        situacao = 'Aprovado'
    elif media >= 5:
        situacao = 'Recuperação'
    else:
        situacao = 'Reprovado'

    # Armazena os dados no dicionário principal
    alunos[nome] = {
        'media': media,
        'situacao': situacao
    }

# Exibe o conteúdo do dicionário
print("\n=== RESULTADO FINAL ===")
for nome, dados in alunos.items():
    print(f"Nome: {nome}, Média: {dados['media']}, Situação: {dados['situacao']}")
