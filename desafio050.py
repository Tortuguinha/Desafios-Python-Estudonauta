
# desafio050.py
# Verifica se um número informado é primo
num = int(input('Digite um numero para ver se é primo: '))  # Lê o número
total = 0
for c in range (1, num + 1):  # Percorre de 1 até o número
    if num %  c == 0:
        print('\033[33m', end=' ')  # Marca divisores
        total += 1
    else:
        print('\033[31m', end=' ')  # Marca não divisores
    print(c, end= ' ')
print('\n')
# Exibe quantidade de divisores
print(f'\33[mO numero {num} foi divisível por {total} vezes')
# Verifica se é primo
if total > 2:
    print(f'O numero {num} não é primo!')
else:
    print(f'O numero {num} é primo!')