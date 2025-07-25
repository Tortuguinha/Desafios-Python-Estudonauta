# desafio084.py
# Gera palpites para a Mega Sena, sorteando 6 números entre 1 e 60 para cada jogo
import random

jogos = []
quantidade = int(input('Quantos jogos você quer gerar? '))

for i in range(quantidade):
    palpite = sorted(random.sample(range(1, 61), 6))
    jogos.append(palpite)

print('\nPalpites gerados:')
for idx, jogo in enumerate(jogos, 1):
    print(f'Jogo {idx}: {jogo}')
