
# desafio024.py
# Solicita o nome completo e mostra o primeiro e último nome
n = str(input('Digite seu nome completo: ')).strip()  # Lê o nome completo
nome = n.split()  # Separa o nome em partes
print('Muito Prazer!')
# Exibe o primeiro nome
print('Seu primeiro nome é {}' .format(nome[0]))
# Exibe o último nome
print('Seu ultimo nome é {}' .format(nome[len(nome) - 1]))