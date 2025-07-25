
# desafio012.py
# Solicita temperatura em Celsius e converte para Fahrenheit e Kelvin
C = float(input('Quantos graus Celcius está fazendo? °C'))  # Lê a temperatura em Celsius

# Converte para Fahrenheit
F = (C * 9/5) + 32
# Converte para Kelvin
K = C + 273.15

# Exibe as conversões
print('A temperatura de {}ºC corresponde a {}ºF!' .format(C, F))
print('A temperatura de {}ºC corresponde a {}ºK!' .format(C, K))