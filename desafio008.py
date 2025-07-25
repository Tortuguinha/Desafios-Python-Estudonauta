
# desafio008.py
# Solicita o valor em reais e a cotação do dólar, mostra quanto pode comprar
real = float(input('Quanto de dinheiro você tem na carteira? R$'))  # Lê o valor em reais
cotacaoDolar = float(input('Quanto está a cotação do dolar? U$'))   # Lê a cotação do dólar
# Calcula e exibe o valor em dólares
print('Com R${:.2f} você pode comprar U${:.2f}!' .format(real, (real / cotacaoDolar)))