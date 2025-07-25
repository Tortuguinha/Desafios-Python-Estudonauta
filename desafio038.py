
# desafio038.py
# Classifica nadador conforme idade
from datetime import date
nascimento = int(input('Digite o ano de nascimento do nadador: '))  # Lê ano de nascimento
ano = date.today().year  # Ano atual

idade = ano - nascimento  # Calcula idade

# Classifica conforme faixa etária
if idade <= 9:
    print('O atleta tem apenas {} anos.\n'
          'É um nadador mirim!' .format(idade))
elif idade <= 14:
    print('O atleta tem apenas {} anos.\n'
          'É um nadador infatil!' .format(idade))
elif idade <= 19:
    print('O atleta tem apenas {} anos.\n'
          'É um nadador junior!' .format(idade))
elif idade <= 25:
    print('O atleta tem apenas {} anos.\n'
          'É um nadador senior!' .format(idade))
else:
    print('O atleta tem {} anos\n'
          'É um atleta master!' .format(idade))