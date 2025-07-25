tempo = int(input('Digite o numero de onde deve começar a gontagem regressiva: '))
for a in range (tempo, -1, -1):
    print(a)
    sleep(1)
print('BOOM!')

# desafio043.py
# Faz uma contagem regressiva a partir de um número informado
from time import sleep

tempo = int(input('Digite o numero de onde deve começar a gontagem regressiva: '))  # Lê o número inicial
for a in range (tempo, -1, -1):  # Conta de tempo até zero
    print(a)
    sleep(1)  # Aguarda 1 segundo
print('BOOM!')  # Finaliza a contagem