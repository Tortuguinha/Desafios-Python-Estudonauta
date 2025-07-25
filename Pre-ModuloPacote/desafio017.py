
# desafio017.py
# Solicita nomes de alunos e sorteia um deles
import random

aluno1 = str(input('Digite o nome do primeiro aluno: '))  # Lê nome do aluno 1
aluno2 = str(input('Digite o nome do segundo aluno: '))   # Lê nome do aluno 2
aluno3 = str(input('Digite o nome do terceiro aluno: '))  # Lê nome do aluno 3
aluno4 = str(input('Digite o nome do quarto aluno: '))    # Lê nome do aluno 4

# Cria lista com os nomes
lista = [aluno1, aluno2, aluno3, aluno4]

# Sorteia um aluno da lista
print('O aluno escolhido foi: {}' .format(random.choice(lista)))