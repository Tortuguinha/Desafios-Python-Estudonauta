
# desafio030.py
# Solicita três números e mostra o maior e o menor
num1 = int(input('Digite um numero inteiro:'))  # Lê o primeiro número
num2 = int(input('Digite outro numero inteiro: '))  # Lê o segundo número
num3 = int(input('Digite outro numero inteiro: '))  # Lê o terceiro número

# Inicializa menor e maior
menor = num1
maior = num1

# Verifica o menor número
if num2 < menor and num2 < num3:
    menor = num2
if num3 < menor and num3 < num2:
    menor = num3
# Verifica o maior número
if num2 > maior and num2 > num3:
    maior = num2
if num3 > maior and num3 > num2:
    maior = num3
# Exibe os resultados
print('Menor numero é {}' .format(menor))
print('Maior numero é {}' .format(maior))