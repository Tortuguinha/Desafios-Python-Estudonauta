
# desafio025.py
# Jogo de adivinhação: usuário tenta acertar número sorteado
import random

num1 = int(input('Em que número estou pensando de 0 a 10? '))  # Usuário tenta adivinhar
num2 = random.randint(0, 10)  # Número sorteado pelo computador

# Verifica se acertou
if num1 == num2:
    print('Parabens eu estava pensando nesse numero!')
else:
    print('Voce errou, eu estava pensando no numero {} e não {}' .format(num2, num1))