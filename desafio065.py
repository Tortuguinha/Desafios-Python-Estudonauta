import random

vitorias = 0

print('🕹️ Bem-vindo ao jogo do PAR ou ÍMPAR!\n')

while True:
    jogador = int(input('Digite um número: '))
    escolha = input('Par ou Ímpar? [P/I]: ').strip().upper()

    while escolha not in ['P', 'I']:
        escolha = input('Escolha inválida. Digite apenas [P] para Par ou [I] para Ímpar: ').strip().upper()

    computador = random.randint(0, 10)
    total = jogador + computador
    resultado = 'P' if total % 2 == 0 else 'I'

    print(f'\nVocê jogou {jogador} e o computador {computador}. Total = {total}')
    print('⚖️ Resultado: PAR' if resultado == 'P' else '⚖️ Resultado: ÍMPAR')

    if escolha == resultado:
        print('✅ Você VENCEU!\n')
        vitorias += 1
    else:
        print('❌ Você PERDEU!\n')
        break

print(f'🏁 Fim de jogo! Você teve {vitorias} vitória(s) consecutiva(s).')
