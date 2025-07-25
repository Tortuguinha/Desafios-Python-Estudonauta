diferenca = 0

# desafio036.py
# Calcula a idade e informa sobre o alistamento militar
from datetime import date
nascimento = int(input('Digite o ano em que voce nasceu: '))  # Lê o ano de nascimento
ano = date.today().year  # Ano atual
idade = ano - nascimento  # Calcula idade
diferenca = 0

# Verifica situação do alistamento
if idade == 18:
    print('Voce tem {} anos, deve se alistar imediatamente!' .format(idade))
elif idade < 18:
    diferenca = 18 - idade
    print('Voce tem apenas {} anos. ainda faltam {} anos para se alistar!' .format(idade, diferenca))
elif idade > 18:
    diferenca = idade - 18
    print('Voce tem {} anos e deveria ter se alistado a {} anos' .format(idade, diferenca))