
# desafio037.py
# Calcula a média do aluno e informa situação
nota1 = float(input('Digite a primeira nota do aluno: '))  # Lê a primeira nota
nota2 = float(input('Digite a segunda nota do aluno: '))   # Lê a segunda nota

media = (nota2 + nota1) / 2  # Calcula a média

# Verifica situação do aluno
if media >= 7:
    print('Parabens o aluno passou com media {}!' .format(media))
elif 7 > media >= 4:
    print('O aluno está de recuperação com media {}!' .format(media))
else:
    print('Infelizmente o aluno está reprovado com media {}!' .format(media))