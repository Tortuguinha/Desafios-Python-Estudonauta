# desafio062.py
# Calcula a soma dos dígitos de um número
num = int(input('Digite um número inteiro: '))  # Lê o número inteiro

soma = 0  # Inicializa a soma dos dígitos
for digito in str(num):
    soma += int(digito)  # Soma cada dígito

print(f'A soma dos dígitos de {num} é {soma}')
print('Digite números inteiros (digite 999 para parar):')

numero = 0
soma = 0
contador = 0

while numero != 999:
    numero = int(input('Número: '))
    if numero != 999:
        soma += numero
        contador += 1

print('\nPrograma encerrado.')
print(f'Você digitou {contador} números.')
print(f'A soma entre eles é {soma}.')
