
# desafio042.py
# Jogo de Pedra, Papel e Tesoura contra o computador
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')  # Opções do jogo
computador = randint(0, 2)  # Escolha do computador
# Exibe opções para o jogador
print('Suas opções:\n'
      '[0] PEDRA\n'
      '[1] PAPEL\n'
      '[2] TESOURA ')
jogador = int(input('Qual a sua jogada? '))  # Escolha do jogador

# Mostra escolhas
print(f'Voce escolheu {itens[jogador]}\n'
      f'O computador escolheu {itens[computador]}')

# Verifica resultado do jogo
if jogador == 0:
    if computador == 0:
        print('O jogo deu empate!')
    elif computador == 1:
        print('O computador venceu')
    else:
        print('O jogador venceu!')
elif jogador == 1:
    if computador == 0:
        print('O jogador venceu!')
    elif computador == 1:
        print('O jogo deu empate!')
    else:
        print('O computador venceu!')
elif jogador == 2:
    if computador == 0:
        print('O Computador venceu!')
    elif computador == 1:
        print('O jogador venceu!')
    else:
        print('O jogo deu empate!')
else:
    print('Jogada invalida!')