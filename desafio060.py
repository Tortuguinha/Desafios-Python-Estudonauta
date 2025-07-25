print(20 * '=')
print('10 TERMOS DE UMA PA')
print(20 * '=')

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
total = 10
cont = 0
total_geral = 0

while True:
    while cont < total:
        print(f'{termo}', end=' → ')
        termo += razao
        cont += 1
        total_geral += 1
    print('PAUSA')
    mais = int(input('Deseja mostrar mais quantos termos? (0 para sair): '))
    if mais == 0:
        break
    total += mais

print(f'\nFIM da progressão 👏')
print(f'Foram exibidos {total_geral} termos ao todo.')
