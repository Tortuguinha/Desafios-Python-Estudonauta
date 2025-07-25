
# desafio018.py
# Solicita nomes de alunos e sorteia a ordem de apresentação
import random

n1 = str(input('Primeiro aluno:'))   # Lê nome do aluno 1
n2 = str(input('Segundo aluno: '))   # Lê nome do aluno 2
n3 = str(input('Terceiro aluno: '))  # Lê nome do aluno 3
n4 = str(input('Quarto aluno: '))    # Lê nome do aluno 4

# Cria lista com os nomes
lista = [n1, n2, n3, n4]
# Embaralha a lista
random.shuffle(lista)

# Exibe a ordem sorteada
print('A ordem de apresentação será: ')
print(lista)