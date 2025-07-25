# desafio082.py
# Lê sete valores numéricos, separa pares e ímpares, e exibe em ordem crescente

numeros = [[], []]  # Lista: [pares, ímpares]

for i in range(7):
    valor = int(input(f'Digite o {i+1}º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

print(f'\nValores pares em ordem crescente: {sorted(numeros[0])}')
print(f'Valores ímpares em ordem crescente: {sorted(numeros[1])}')
