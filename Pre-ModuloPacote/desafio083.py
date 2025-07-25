# desafio083.py
# Cria uma matriz 3x3 preenchida pelo usuário e exibe formatada

matriz = []
for linha in range(3):
    matriz.append([])
    for coluna in range(3):
        valor = int(input(f'Digite o valor para [{linha},{coluna}]: '))
        matriz[linha].append(valor)

print('\nMatriz 3x3:')
for linha in matriz:
    for valor in linha:
        print(f'{valor:^5}', end='')  # Centraliza o valor em 5 espaços
    print()

# Calcula a soma dos valores pares e ímpares
pares = 0
impares = 0
for linha in matriz:
    for valor in linha:
        if valor % 2 == 0:
            pares += valor
        else:
            impares += valor

print(f'\nSoma dos valores pares: {pares}')
print(f'Soma dos valores ímpares: {impares}')

# Soma das colunas
for col in range(3):
    soma_col = sum(matriz[linha][col] for linha in range(3))
    print(f'Soma da coluna {col+1}: {soma_col}')

# Soma das linhas
for idx, linha in enumerate(matriz):
    soma_linha = sum(linha)
    print(f'Soma da linha {idx+1}: {soma_linha}')
