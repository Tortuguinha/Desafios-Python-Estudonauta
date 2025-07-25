# desafio059.py
# Solicita um número ao usuário e verifica se é primo
num = int(input('Digite um número inteiro: '))  # Lê o número inteiro

# Conta quantos divisores o número possui
divisores = 0
for i in range(1, num + 1):
    if num % i == 0:
        divisores += 1

# Se tiver apenas dois divisores, é primo
if divisores == 2:
    print(f'{num} é um número primo!')
else:
    print(f'{num} não é um número primo.')
print(20 * '=')
print('10 temos de uma PA')
print(20 * '=')

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
c = 1

while c < 11:
    print(termo)
    termo = termo + razao
    c += 1