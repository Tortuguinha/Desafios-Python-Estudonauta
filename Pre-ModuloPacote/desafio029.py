
# desafio029.py
# Verifica se um ano é bissexto
from datetime import date
ano = int(input('Que ano quer analizar? Colo que 0 para o ano atual'))  # Lê o ano

# Se o usuário digitar 0, pega o ano atual
if ano == 0:
    ano = date.today().year
# Verifica se é bissexto
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO' .format(ano))
else:
    print('O ano {} NÃO É BISSEXTO' .format(ano))