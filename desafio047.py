
# desafio047.py
# Exibe a tabuada de um número informado pelo usuário
num = int(input('Digite um numero para ver sua tabuada: '))  # Lê o número
for a in range(1, 11):  # Percorre de 1 a 10
    print(f'{num} x {a} = {num * a}')  # Exibe o resultado da multiplicação