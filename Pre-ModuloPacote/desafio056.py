
# desafio056.py
# Jogo de adivinhação: computador escolhe número e usuário tenta acertar
from random import randint
# Variáveis
computador = randint(0,10)  # Número sorteado pelo computador
contador = 0

# Mensagem inicial
print('Sou seu computador...\n'
      'Acabei de pensar em um número entre 0 e 10.\n'
      'Será que consegue adivinhar?')
jogador = int(input('Qual é seu palpite? '))  # Palpite do usuário

# Loop até acertar
while jogador != computador:
    if jogador < computador:
        jogador = int(input('Mais... tente mais uma vez. '))
        contador += 1
    elif jogador > computador:
        jogador = int(input('Menos... tente mais uma vez.'))
        contador += 1
contador += 1  # Conta a tentativa correta
# Exibe resultado
print(f'Acertou com {contador} tentativas.')