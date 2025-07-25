# desafio061.py
# Solicita um número ao usuário e calcula o fatorial
num = int(input('Digite um número inteiro: '))  # Lê o número inteiro

# Inicializa o fatorial e multiplica pelo próximo número
fatorial = 1
for i in range(1, num + 1):
    fatorial *= i

print(f'O fatorial de {num} é {fatorial}')
import time
antecessor = 0
sucessor = 1
print(22 * '-')
print('Sequência de Fibonacci')
print(22 * '-')
num = int(input('Digite quantos termos você quer mostrar: '))

contador = 0
while contador < num:
    print(f'{antecessor}', end=' → ')
    proximo = antecessor + sucessor
    antecessor = sucessor
    sucessor = proximo
    contador += 1
    time.sleep(0.5)

print('FIM')
