
# desafio048.py
# Soma números pares e ímpares informados pelo usuário
somaPar = 0
somaImpar = 0
for a in range(1, 7):  # Solicita 6 números
    num = int(input('Digite um numero a ser somado: '))
    if num % 2 == 0:
        somaPar = somaPar + num  # Soma pares
    if num % 2 == 1:
        somaImpar = somaImpar + num  # Soma ímpares
# Exibe os resultados
print(f'A soma de todos os numeros pares é {somaPar}')
print(f'A soma de todos os numeros impares é {somaImpar}')