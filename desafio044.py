
# desafio044.py
# Mostra todos os números pares e ímpares até um valor informado
num = int(input('Digite o numero maximo: para seleção de pares: '))  # Lê o valor máximo
# Exibe pares
for a in range(1,num + 1):
    if a % 2 ==0:
        print(a)
# Exibe ímpares
for b in range(1, num + 1):
    if b % 2 == 1:
        print(b)