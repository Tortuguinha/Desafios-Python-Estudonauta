
# desafio049.py
# Exibe os 10 primeiros termos de uma PA
print(20 * '=')
print('10 termos de uma PA')
print(20 * '=')

termo = int(input('Digite o primeiro termo: '))  # Lê o primeiro termo
razao = int(input('Digite a razão: '))           # Lê a razão

for a in range(termo, termo + 10):  # Gera 10 termos
    print(termo)  # Exibe o termo atual
    termo = termo + razao  # Calcula o próximo termo