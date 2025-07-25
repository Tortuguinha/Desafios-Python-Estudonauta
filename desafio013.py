
# desafio013.py
# Solicita dias e km de aluguel de carro, calcula o valor total
dias = int(input('Por quantos dias o carro foi alugado? '))      # Lê quantidade de dias
distancia = float(input('Quantos quilometros ele percorreu?'))  # Lê distância percorrida

# Calcula o preço pelo tempo e pela distância
precoDia = dias * 60
precoDistancia = distancia * 0.15

# Exibe o valor total do aluguel
print('O total de aluguel a se pagar é de R${:.2f}!' .format(precoDistancia + precoDia))