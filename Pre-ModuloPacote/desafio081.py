# desafio081.py
# Cadastro de pessoas com nome e peso, mostrando estatísticas ao final

pessoas = []  # Lista para armazenar os dados
maior_peso = menor_peso = 0

while True:
    nome = input('Nome: ').strip()
    peso = float(input('Peso: '))
    pessoas.append([nome, peso])
    if len(pessoas) == 1:
        maior_peso = menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    if continuar not in ['S', 'SIM', 'SS', 's', 'ss', 'sim']:
        break

print(f'\nTotal de pessoas cadastradas: {len(pessoas)}')
print(f'Maior peso cadastrado: {maior_peso} kg')
print('Pessoas mais pesadas:', end=' ')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'[{p[0]}]', end=' ')
print(f'\nMenor peso cadastrado: {menor_peso} kg')
print('Pessoas mais leves:', end=' ')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'[{p[0]}]', end=' ')
print()
