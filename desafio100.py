def notas(*n, situacao=False):
    """
    Calcula estatísticas de uma série de notas.

    Parâmetros:
    - *n: uma ou mais notas dos alunos (valores numéricos).
    - situacao (opcional): valor booleano que, se for True, adiciona a situação da turma.

    Retorno:
    - Um dicionário com:
        - quantidade: total de notas fornecidas
        - maior: a maior nota
        - menor: a menor nota
        - media: a média das notas (com 2 casas decimais)
        - situacao (opcional): avaliação da média como 'Boa', 'Razoável' ou 'Ruim'
    """
    resultado = {}
    resultado['quantidade'] = len(n)
    resultado['maior'] = max(n)
    resultado['menor'] = min(n)
    media = sum(n) / len(n)
    resultado['media'] = round(media, 2)  # arredondando a média

    if situacao:
        if media >= 7:
            resultado['situacao'] = 'Boa'
        elif media >= 5:
            resultado['situacao'] = 'Razoável'
        else:
            resultado['situacao'] = 'Ruim'
    
    return resultado


# Programa principal
notas_alunos = []

print("Digite as notas dos alunos. Digite 'sair' para encerrar.")
while True:
    entrada = input("Nota: ").strip()
    if entrada.lower() == 'sair':
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas_alunos.append(nota)
        else:
            print("⚠️ A nota deve estar entre 0 e 10.")
    except ValueError:
        print("⚠️ Entrada inválida. Digite um número válido ou 'sair'.")

if len(notas_alunos) > 0:
    incluir_situacao = input("Deseja incluir a situação da turma? [S/N] ").strip().upper()
    mostrar_situacao = incluir_situacao == 'S'

    resultado = notas(*notas_alunos, situacao=mostrar_situacao)

    print("\n📊 Resultado:")
    for chave, valor in resultado.items():
        print(f"{chave.capitalize()}: {valor}")
else:
    print("Nenhuma nota foi inserida.")
