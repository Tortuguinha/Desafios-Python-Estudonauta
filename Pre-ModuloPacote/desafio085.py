# desafio085.py
# Lê nome e duas notas de vários alunos, mostra boletim com média e permite consultar notas individuais

alunos = []

while True:
    nome = input('Nome do aluno: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    alunos.append([nome, [nota1, nota2], (nota1 + nota2) / 2])
    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

print('\nBoletim:')
print(f'{"Nº":<4}{"Nome":<15}{"Média":>6}')
print('-' * 27)
for i, aluno in enumerate(alunos):
    print(f'{i:<4}{aluno[0]:<15}{aluno[2]:>6.1f}')

while True:
    entrada = input('\nMostrar notas de qual aluno? (sair interrompe): ')
    if entrada.lower() == 'sair':
        break
    if entrada.isdigit():
        opcao = int(entrada)
        if 0 <= opcao < len(alunos):
            print(f'Notas de {alunos[opcao][0]}: {alunos[opcao][1]}')
        else:
            print('Aluno não encontrado.')
    else:
        print('Digite um número válido ou "sair" para interromper.')