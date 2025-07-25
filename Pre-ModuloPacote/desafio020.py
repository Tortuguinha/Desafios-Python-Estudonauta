
# desafio020.py
# Solicita um número e mostra unidade, dezena, centena e milhar
num = int(input('Informe um número: '))  # Lê o número

# Calcula cada casa do número
u = num // 1 % 10      # Unidade
d = num // 10 % 10     # Dezena
c = num // 100 % 10    # Centena
m = num // 1000 % 10   # Milhar

# Exibe cada casa
print('analisando o número {}' .format(num))
print('Unidade: {}' .format(u))
print('Dezena: {}' .format(d))
print('Centena: {}' .format(c))
print('Milhar: {}' .format(m))