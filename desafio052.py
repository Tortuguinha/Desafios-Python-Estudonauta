
# desafio052.py
# Conta quantas pessoas são maiores e menores de idade
from datetime import date
hoje = date.today().year  # Ano atual
contadorMaior = 0
contadorMenor = 0

# Loop para ler o ano de nascimento de 7 pessoas
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    if hoje - ano > 18:
        contadorMaior += 1  # Conta maiores de idade
    else:
        contadorMenor += 1  # Conta menores de idade
# Exibe os resultados
print(f'Existem {contadorMaior} pessoa(s) maior(es) de idade')
print(f'Existem {contadorMenor} pessoa(s) menor(es) de idade')