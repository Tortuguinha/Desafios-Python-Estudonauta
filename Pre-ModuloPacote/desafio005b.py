
# desafio005b.py
# Solicita três notas e seus respectivos pesos, calcula e mostra a média ponderada
n1 = float(input('Digite a primeira nota de 0 a 10: '))  # Lê a primeira nota
p1 = int(input('Digite o peso dessa nota: '))             # Lê o peso da primeira nota
n2 = float(input('Digite a segunda nota de 0 a 10: '))   # Lê a segunda nota
p2 = int(input('Digite o peso dessa nota: '))             # Lê o peso da segunda nota
n3 = float(input('Digite a terceira nota de 0 a 10: '))  # Lê a terceira nota
p3 = int(input('Digite o peso dessa nota: '))             # Lê o peso da terceira nota

# Calcula a soma das notas ponderadas
nSoma = (n1 * p1) + (n2 * p2) + (n3 * p3)
# Calcula a soma dos pesos
pSoma = p1 + p2 + p3

# Exibe a média ponderada
print('A média ponderada das notas é: {:.2f}' .format(nSoma / pSoma))