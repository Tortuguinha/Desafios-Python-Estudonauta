import random
from time import sleep
from operator import itemgetter

# Coletando os nomes dos jogadores (agora 5)
jogadores = {}
for i in range(1, 6):  # de 1 até 5 (inclusive)
    nome = input(f"Digite o nome do Jogador {i}: ")
    jogadores[nome] = random.randint(1, 6)

# Mostrando os valores sorteados
print("\nValores sorteados:")
for jogador, valor in jogadores.items():
    print(f"{jogador} tirou {valor} no dado.")
    sleep(0.5)

# Ordenando o dicionário em ordem decrescente
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

# Exibindo o ranking com empates
print("\nRanking dos jogadores:")
posicao = 1
contador = 1
anterior = None
ranking_completo = []

for jogador, valor in ranking:
    if valor != anterior:
        posicao = contador
    print(f"{posicao}º lugar: {jogador} com {valor}")
    ranking_completo.append((posicao, jogador, valor))
    anterior = valor
    contador += 1
    sleep(0.5)

# Identificando vencedores (1º lugar)
primeiro_valor = ranking_completo[0][2]
vencedores = [j for p, j, v in ranking_completo if v == primeiro_valor]
print(f"\nVencedor{'es' if len(vencedores) > 1 else ''}: {', '.join(vencedores)} com {primeiro_valor} ponto(s)!")

# Identificando perdedores (última posição)
ultimo_valor = ranking_completo[-1][2]
perdedores = [j for p, j, v in ranking_completo if v == ultimo_valor]
print(f"Perdedor{'es' if len(perdedores) > 1 else ''}: {', '.join(perdedores)} com {ultimo_valor} ponto(s)!")

# Segundo colocado (se houver)
segundos = [j for p, j, v in ranking_completo if p == 2]
if segundos:
    print(f"Segundo colocado{'s' if len(segundos) > 1 else ''}: {', '.join(segundos)}")

# Terceiro colocado (se houver)
terceiros = [j for p, j, v in ranking_completo if p == 3]
if terceiros:
    print(f"Terceiro colocado{'s' if len(terceiros) > 1 else ''}: {', '.join(terceiros)}")

# Quarto colocado (se houver)
quartos = [j for p, j, v in ranking_completo if p == 4]
if quartos:
    print(f"Quarto colocado{'s' if len(quartos) > 1 else ''}: {', '.join(quartos)}")
